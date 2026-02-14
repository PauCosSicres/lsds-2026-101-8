from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from importlib import import_module
from typing import List
import sys, os, httpx


app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    
    return {"status": "up"}

sys.path.append("/apps")

# json format like this
class MapRequest(BaseModel):
    job_id: str
    app_name: str
    data_path: str
    map_partition: int
    reduce_partitions: int

# get functions from word_count.py
def load_app(app_name):
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

    files = f"{req.data_path}/{req.map_partition}"

    with open(files, "r") as f:
        content = f.read()

    map_function, reduce_function, partition_function = load_app(req.app_name)
    # create key -  value pairs of each file
    mapings = map_function(str(req.map_partition), content)

    # create output directory
    output_dir = f"outputs/{req.job_id}/{req.map_partition}"
    os.makedirs(output_dir, exist_ok=True)

    for key, value in mapings:
        reductor = partition_function(key, req.reduce_partitions)
        reductor_dir = os.path.join(output_dir, f"{reductor}")
        with open(reductor_dir, "a") as append:
            append.write(f"{key} {value}\n")

@app.get("/map-output")
def map_output(job_id: str, map_partition: int, partition: int):
    
    output_path = f"outputs/{job_id}/{map_partition}/{partition}"
    
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Output path file not found")
    
    result = {}

    with open(output_path, "r") as f:
        for line in f:
            key, value = line.strip().split(" ", 1)
            if key not in result:
                result[key] = []
            result[key].append(value)            

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
    
    map_function, reduce_function, partition_function = load_app(req.app_name)
    
    # get intermediate outputs
    for url in req.intermediate_partitions:
        response = httpx.get(url)
        if response.status_code != 200:
            continue

        data = response.json()
        result = {}

        for key, values in data.items():
            if key not in result:
                result[key] = []
            result[key].extend(values)
    
    results_dir = f"/results/{req.job_id}"
    os.makedirs(results_dir, exist_ok=True)

    results_file = f"{results_dir}/{req.reduce_partition}"

    with open(results_file, "w") as f:
        for key, values in result.items():
            reduced_value = reduce_function(key, values)
            if reduced_value is not None:
                f.write(f"{key} {reduced_value}\n")
