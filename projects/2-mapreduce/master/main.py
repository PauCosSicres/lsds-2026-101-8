from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uuid
import httpx
import asyncio

app = FastAPI()

jobs: Dict[str, Any] = {}

WORKERS = [
    "http://worker1:80",
    "http://worker2:80",
    "http://worker3:80",
    "http://worker4:80",
    "http://worker5:80",
]

alive_workers = set(WORKERS)
dead_workers = set()

worker_busy: Dict[str, bool] = {w: False for w in WORKERS}
task_queue: asyncio.Queue = asyncio.Queue()

class JobRequest(BaseModel):
    app_name: str
    data_path: str
    map_partitions: int
    reduce_partitions: int

@app.get("/healthcheck")
def healthcheck():
    return {"status": "up"}

@app.on_event("startup")
async def startup():
    asyncio.create_task(worker_monitor_loop())
    asyncio.create_task(dispatcher_loop())

async def worker_monitor_loop():
    global alive_workers, dead_workers
    while True:
        async with httpx.AsyncClient(timeout=2.0) as client:
            for worker in WORKERS:
                try:
                    await client.get(f"{worker}/healthcheck")
                    if worker in dead_workers:
                        dead_workers.remove(worker)
                        alive_workers.add(worker)
                except:
                    if worker in alive_workers:
                        alive_workers.remove(worker)
                        dead_workers.add(worker)
                        await reassign_tasks(worker)
        await asyncio.sleep(30)

def get_free_worker() -> Optional[str]:
    for w in sorted(alive_workers):
        if not worker_busy[w]:
            return w
    return None

async def dispatcher_loop():
    while True:
        task = await task_queue.get()
        while True:
            worker = get_free_worker()
            if worker:
                break
            await asyncio.sleep(0.2)
        await send_task_to_worker(worker, task)

async def send_task_to_worker(worker, task):
    worker_busy[worker] = True
    async with httpx.AsyncClient(timeout=20.0) as client:
        try:
            if task["type"] == "map":
                await client.post(f"{worker}/map", json=task["body"])
            else:
                await client.post(f"{worker}/reduce", json=task["body"])
        except:
            worker_busy[worker] = False

@app.post("/jobs")
async def create_job(req: JobRequest):
    if not alive_workers:
        raise HTTPException(status_code=503, detail="No alive workers available")

    job_id = str(uuid.uuid4())

    alive_list = sorted(list(alive_workers))

    mappers = []
    for i in range(req.map_partitions):
        worker_url = alive_list[i % len(alive_list)]
        worker_label = worker_url.replace("http://", "")
        mappers.append({"worker": worker_label, "status": "in-progress", "partition": i})

    reducers = [{"worker": None, "status": "idle", "partition": i} for i in range(req.reduce_partitions)]

    job_data = {
        "job_id": job_id,
        "app_name": req.app_name,
        "data_path": req.data_path,
        "map_partitions": req.map_partitions,
        "reduce_partitions": req.reduce_partitions,
        "mappers": mappers,
        "reducers": reducers,
        "status": "mapping",
    }

    jobs[job_id] = job_data

    for mapper in mappers:
        await task_queue.put({
            "type": "map",
            "body": {
                "job_id": job_id,
                "app_name": req.app_name,
                "data_path": req.data_path,
                "map_partition": mapper["partition"],
                "reduce_partitions": req.reduce_partitions,
            },
        })

    return job_data

@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    return jobs[job_id]

@app.post("/jobs/{job_id}/map/{partition}/completed")
async def map_completed(job_id: str, partition: int):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    job = jobs[job_id]

    worker_label = None
    for m in job["mappers"]:
        if m["partition"] == partition:
            m["status"] = "completed"
            worker_label = m["worker"]
            break

    if worker_label:
        worker_busy[f"http://{worker_label}"] = False

    if job["status"] == "mapping" and all(m["status"] == "completed" for m in job["mappers"]):
        job["status"] = "reducing"
        await start_reduce_phase(job_id)

    return {"message": "Status updated"}

@app.post("/jobs/{job_id}/reduce/{partition}/completed")
async def reduce_completed(job_id: str, partition: int):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    job = jobs[job_id]

    worker_label = None
    for r in job["reducers"]:
        if r["partition"] == partition:
            r["status"] = "completed"
            worker_label = r["worker"]
            break

    if worker_label:
        worker_busy[f"http://{worker_label}"] = False

    if all(r["status"] == "completed" for r in job["reducers"]):
        job["status"] = "completed"

    return {"message": "Status updated"}

async def start_reduce_phase(job_id: str):
    job = jobs[job_id]

    for reducer_meta in job["reducers"]:
        urls = []
        for mapper in job["mappers"]:
            urls.append(
                f"http://{mapper['worker']}/map-output?"
                f"job_id={job_id}&map_partition={mapper['partition']}&partition={reducer_meta['partition']}"
            )

        await task_queue.put({
            "type": "reduce",
            "body": {
                "job_id": job_id,
                "app_name": job["app_name"],
                "reduce_partition": reducer_meta["partition"],
                "intermediate_partitions": urls,
            },
        })

async def reassign_tasks(dead_worker: str):
    dead_label = dead_worker.replace("http://", "")

    for job in jobs.values():
        if job["status"] == "completed":
            continue

        for mapper in job["mappers"]:
            if mapper["worker"] == dead_label and mapper["status"] == "in-progress":
                new_worker = get_free_worker()
                if not new_worker:
                    continue

                mapper["worker"] = new_worker.replace("http://", "")

                await task_queue.put({
                    "type": "map",
                    "body": {
                        "job_id": job["job_id"],
                        "app_name": job["app_name"],
                        "data_path": job["data_path"],
                        "map_partition": mapper["partition"],
                        "reduce_partitions": job["reduce_partitions"],
                    },
                })

        for reducer in job["reducers"]:
            if reducer["worker"] == dead_label and reducer["status"] == "in-progress":
                new_worker = get_free_worker()
                if not new_worker:
                    continue

                reducer["worker"] = new_worker.replace("http://", "")

                urls = []
                for mapper in job["mappers"]:
                    urls.append(
                        f"http://{mapper['worker']}/map-output?"
                        f"job_id={job['job_id']}&map_partition={mapper['partition']}&partition={reducer['partition']}"
                    )

                await task_queue.put({
                    "type": "reduce",
                    "body": {
                        "job_id": job["job_id"],
                        "app_name": job["app_name"],
                        "reduce_partition": reducer["partition"],
                        "intermediate_partitions": urls,
                    },
                })
