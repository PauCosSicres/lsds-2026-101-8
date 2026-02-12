from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import FileResponse
from pydantic import BaseModel
from importlib import import_module
import sys, os

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

    # create key -  value pairs of each file
    map_function, reduce_function, partition_function = load_app(req.app_name)
    mapings = map_function(str(req.map_partition), content)

    # create output directory
    output_dir = f"outputs/{req.job_id}/{req.map_partition}"
    os.makedirs(output_dir, exist_ok=True)

    for key, value in mapings:
        reductor = partition_function(key, req.reduce_partitions)
        reductor_dir = os.path.join(output_dir, f"{reductor}")
        with open(reductor_dir, "a") as append:
            append.write(f"{key} {value}\n")