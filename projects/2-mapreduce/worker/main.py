from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from importlib import import_module, reload
from typing import List
import sys, os, httpx

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"status": "up"}

sys.path.append("/apps")


class MapRequest(BaseModel):
    job_id: str
    app_name: str
    data_path: str
    map_partition: int
    reduce_partitions: int


def load_app(app_name):
    if app_name in sys.modules:
        module = reload(sys.modules[app_name])
    else:
        module = import_module(app_name)

    return (
        getattr(module, "map"),
        getattr(module, "reduce"),
        getattr(module, "partitioner"),
    )


@app.post("/map")
def map(req: MapRequest, background_task: BackgroundTasks):
    background_task.add_task(run_map_task, req)
    return {"status": "in-progress"}


def run_map_task(req: MapRequest):
    try:
        data_path = req.data_path
        data_path = data_path.replace("./data/", "/data/")
        file_path = f"{data_path}/{req.map_partition}"

        if not os.path.exists(file_path):
            raise Exception(f"File not found: {file_path}")

        with open(file_path, "r") as f:
            content = f.read()

        map_function, _, partition_function = load_app(req.app_name)

        mappings = map_function(str(req.map_partition), content)

        output_dir = f"/outputs/{req.job_id}/{req.map_partition}"

        # 🔥 LIMPIAR OUTPUT ANTIGUO
        if os.path.exists(output_dir):
            for f_name in os.listdir(output_dir):
                os.remove(os.path.join(output_dir, f_name))
        else:
            os.makedirs(output_dir, exist_ok=True)

        for key, value in mappings:
            reducer = partition_function(key, req.reduce_partitions)
            reducer_file = f"{output_dir}/{reducer}"
            with open(reducer_file, "a") as out:
                out.write(f"{key} {value}\n")

        httpx.post(
            f"http://master:8000/jobs/{req.job_id}/map/{req.map_partition}/completed",
            timeout=30
        )

    except Exception as e:
        print("MAP ERROR:", e)



@app.get("/map-output")
def map_output(job_id: str, map_partition: int, partition: int):
    output_path = f"/outputs/{job_id}/{map_partition}/{partition}"

    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Output not found")

    result = {}

    with open(output_path, "r") as f:
        for line in f:
            key, value = line.strip().split(" ", 1)
            result.setdefault(key, []).append(value)

    return result



class ReduceRequest(BaseModel):
    job_id: str
    app_name: str
    reduce_partition: int
    intermediate_partitions: List[str]


@app.post("/reduce")
def reduce(req: ReduceRequest, background_task: BackgroundTasks):
    background_task.add_task(run_reduce_task, req)
    return {"status": "in-progress"}


def run_reduce_task(req: ReduceRequest):
    try:
        _, reduce_function, _ = load_app(req.app_name)

        merged = {}

        for url in req.intermediate_partitions:
            r = httpx.get(url, timeout=30)
            if r.status_code != 200:
                continue

            data = r.json()
            for key, values in data.items():
                merged.setdefault(key, []).extend(values)

        results_dir = f"/results/{req.job_id}"
        os.makedirs(results_dir, exist_ok=True)
        result_file = f"{results_dir}/{req.reduce_partition}"

        with open(result_file, "w") as f:
            for key, values in merged.items():
                reduced_value = reduce_function(key, values)
                if reduced_value is not None:
                    f.write(f"{key} {reduced_value}\n")

        httpx.post(
            f"http://master:8000/jobs/{req.job_id}/reduce/{req.reduce_partition}/completed",
            timeout=30
        )

    except Exception as e:
        print("REDUCE ERROR:", e)
