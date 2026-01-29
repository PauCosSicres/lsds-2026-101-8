import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

SETTINGS_PATH = Path("/code/settings.json")
CHECKPOINT_PATH = Path("/code/checkpoint.json")

class FileRequest(BaseModel):
    file_name: str

@app.get("/healthcheck")
def healthcheck():
    return {"status": "up"}

@app.get("/datanodes")
def get_datanodes():
    with open(SETTINGS_PATH) as f:
        config = json.load(f)
    return {"datanodes": config["datanodes"]}

@app.post("/files")
def create_file(request: FileRequest):
    with open(CHECKPOINT_PATH, "r") as f:
        checkpoint = json.load(f)
    
    if request.file_name in checkpoint:
        raise HTTPException(status_code=409, detail="File already exists")

    with open(SETTINGS_PATH) as f:
        settings = json.load(f)
    new_file = {
        "file_name": request.file_name,
        "block_size_bytes": settings["block_size_bytes"],
        "blocks": []
    }
    
    checkpoint[request.file_name] = new_file
    with open(CHECKPOINT_PATH, "w") as f:
        json.dump(checkpoint, f, indent=4)
    
    return new_file

@app.get("/files/{filename}")
def get_file_metadata(filename: str):
    with open(CHECKPOINT_PATH) as f:
        checkpoint = json.load(f)
    
    if filename not in checkpoint:
        raise HTTPException(status_code=404, detail="File not found")
    
    return checkpoint[filename]

@app.post("/files/{filename}/blocks")
def add_block(filename: str):
    with open(CHECKPOINT_PATH, "r") as f:
        checkpoint = json.load(f)
    
    if filename not in checkpoint:
        raise HTTPException(status_code=404, detail="File not found")

    with open(SETTINGS_PATH) as f:
        settings = json.load(f)

    datanodes = settings["datanodes"]
    rep_factor = settings["replication_factor"]
    
    block_number = len(checkpoint[filename]["blocks"])
    
    first_node_index = block_number % len(datanodes)
    
    replicas = []
    for i in range(rep_factor):
        node_index = (first_node_index + i) % len(datanodes)
        replicas.append(datanodes[node_index]["id"])

    new_block = {
        "number": block_number,
        "replicas": replicas
    }
    
    checkpoint[filename]["blocks"].append(new_block)
    
    with open(CHECKPOINT_PATH, "w") as f:
        json.dump(checkpoint, f, indent=4)
        
    return checkpoint[filename]

@app.delete("/files/{filename}", status_code=204)
def delete_file(filename: str):
    with open(CHECKPOINT_PATH, "r") as f:
        checkpoint = json.load(f)
    
    if filename not in checkpoint:
        raise HTTPException(status_code=404, detail="File not found")
    
    del checkpoint[filename]
    
    with open(CHECKPOINT_PATH, "w") as f:
        json.dump(checkpoint, f, indent=4)