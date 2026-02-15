from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import uuid
import httpx

app = FastAPI()

# Global state for jobs
jobs: Dict[str, Any] = {}

# Worker registry matching docker-compose service names
WORKERS = [
    "http://worker1:80",
    "http://worker2:80",
    "http://worker3:80",
    "http://worker4:80",
    "http://worker5:80"
]

class JobRequest(BaseModel):
    app_name: str
    data_path: str
    map_partitions: int
    reduce_partitions: int

@app.get("/healthcheck")
def healthcheck():
    return {"status": "up"}

@app.post("/jobs")
async def create_job(req: JobRequest):
    job_id = str(uuid.uuid4())
    
    # Setup Mappers using modulo distribution
    mappers = []
    for i in range(req.map_partitions):
        worker_url = WORKERS[i % len(WORKERS)]
        worker_label = worker_url.replace("http://", "")
        if ":" not in worker_label:
            worker_label += ":80"
        mappers.append({"worker": worker_label, "status": "in-progress", "partition": i})
    
    # Setup Reducers (initially idle)
    reducers = [{"worker": None, "status": "idle", "partition": i} 
                for i in range(req.reduce_partitions)]

    job_data = {
        "job_id": job_id,
        "app_name": req.app_name,
        "data_path": req.data_path,
        "map_partitions": req.map_partitions,
        "reduce_partitions": req.reduce_partitions,
        "mappers": mappers,
        "reducers": reducers,
        "status": "in-progress"
    }
    jobs[job_id] = job_data

    # Dispatch Map tasks to workers
    async with httpx.AsyncClient() as client:
        for mapper in mappers:
            worker_endpoint = f"http://{mapper['worker']}/map"
            map_task_body = {
                "job_id": job_id,
                "app_name": req.app_name,
                "data_path": req.data_path,
                "map_partition": mapper["partition"],
                "reduce_partitions": req.reduce_partitions
            }
            try:
                await client.post(worker_endpoint, json=map_task_body)
            except Exception as e:
                print(f"Error contacting {worker_endpoint}: {e}")

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
    mapper = next((m for m in job["mappers"] if m["partition"] == partition), None)
    
    if not mapper:
         raise HTTPException(status_code=404, detail="Partition not found")
         
    if mapper["status"] == "completed":
        raise HTTPException(status_code=409, detail="Task already completed")
        
    mapper["status"] = "completed"
    #when all the mapping is completed we start with the reduce
    if all(m["status"] == "completed" for m in job["mappers"]):
        await start_reduce_phase(job_id)
        
    return {"message": "Status updated"}

@app.post("/jobs/{job_id}/reduce/{partition}/completed")
async def reduce_completed(job_id: str, partition: int):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    
    job = jobs[job_id]
    reducer = next((r for r in job["reducers"] if r["partition"] == partition), None) 
    
    if not reducer:
        raise HTTPException(status_code=404, detail="Partition not found")
        
    if reducer["status"] == "completed":
        raise HTTPException(status_code=409, detail="Task already completed")
        
    reducer["status"] = "completed"

    # When all reduce tasks are completed we mark the job as completed
    if all(r["status"] == "completed" for r in job["reducers"]):
        job["status"] = "completed"
        
    return {"message": "Status updated"}

async def start_reduce_phase(job_id: str):
    job = jobs[job_id]
    async with httpx.AsyncClient() as client:
        for reducer_meta in job["reducers"]:
            worker_idx = reducer_meta["partition"] % len(WORKERS) 
            worker_url = WORKERS[worker_idx]
            
            reducer_meta["worker"] = worker_url.replace("http://", "") 
            reducer_meta["status"] = "in-progress"
            
            intermediate_urls = []  
            for mapper in job["mappers"]: 
                url = (f"http://{mapper['worker']}/map-output?"
                       f"job_id={job_id}&map_partition={mapper['partition']}&"
                       f"reduce_partition={reducer_meta['partition']}")
                intermediate_urls.append(url)
            
            reduce_req = {
                "job_id": job_id,
                "app_name": job["app_name"],
                "reduce_partition": reducer_meta["partition"],
                "intermediate_partitions": intermediate_urls
            }
            
            try:
                await client.post(f"{worker_url}/reduce", json=reduce_req)
            except Exception as e:
                print(f"Failed to start reduce on {worker_url}: {e}")