import json
import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

SETTINGS_PATH = Path("/code/settings.json")
CHECKPOINT_PATH = Path("/code/checkpoint.json")
JOURNAL_PATH = Path("/code/journal")

fs_metadata = {}


def load_initial_state(): 
    global fs_metadata
    if CHECKPOINT_PATH.exists():
        with open(CHECKPOINT_PATH, "r") as f:
            fs_metadata = json.load(f)
    else:
        fs_metadata = {}

    if JOURNAL_PATH.exists() and JOURNAL_PATH.is_file():
        with open(JOURNAL_PATH, "r") as f:
            for line in f:
                line = line.strip()
                if not line: continue
                
                parts = line.split(" ", 1)
                if len(parts) < 2: continue
                action, data = parts[0], json.loads(parts[1])
                
                if action == "ADD_FILE":
                    fs_metadata[data["file_name"]] = data
                elif action == "ADD_BLOCK":
                    fs_metadata[data["file_name"]]["blocks"].append(data["block"])
                elif action == "DELETE_FILE":
                    fs_metadata.pop(data["file_name"], None)

        with open(CHECKPOINT_PATH, "w") as f:
            json.dump(fs_metadata, f, indent=4)
        open(JOURNAL_PATH, 'w').close() 

load_initial_state()

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
    if not request.file_name or request.file_name.strip() == "":
        raise HTTPException(status_code=400, detail="File name cannot be empty")
    
    if request.file_name in fs_metadata:
        raise HTTPException(status_code=409, detail="File already exists")

    with open(SETTINGS_PATH) as f:
        settings = json.load(f)

    new_file = {
        "file_name": request.file_name,
        "block_size_bytes": settings["block_size_bytes"],
        "blocks": []
    }
    
    fs_metadata[request.file_name] = new_file
    with open(JOURNAL_PATH, "a") as f:
        f.write(f"ADD_FILE {json.dumps(new_file)}\n")
    
    return new_file

@app.get("/files/{filename}")
def get_file_metadata(filename: str):
    if filename not in fs_metadata:
        raise HTTPException(status_code=404, detail="File not found")
    return fs_metadata[filename]

@app.post("/files/{filename}/blocks")
def add_block(filename: str):
    if filename not in fs_metadata:
        raise HTTPException(status_code=404, detail="File not found")

    with open(SETTINGS_PATH) as f:
        settings = json.load(f)

    datanodes = settings["datanodes"]
    rep_factor = settings["replication_factor"]
    block_num = len(fs_metadata[filename]["blocks"])
    
    first_node_idx = block_num % len(datanodes)
    replicas = [str(datanodes[(first_node_idx + i) % len(datanodes)]["id"]) for i in range(rep_factor)]

    new_block = {"number": block_num, "replicas": replicas}
    
    fs_metadata[filename]["blocks"].append(new_block)
    log_entry = {"file_name": filename, "block": new_block}
    with open(JOURNAL_PATH, "a") as f:
        f.write(f"ADD_BLOCK {json.dumps(log_entry)}\n")
        
    return fs_metadata[filename]

@app.delete("/files/{filename}", status_code=204)
def delete_file(filename: str):
    if filename not in fs_metadata:
        raise HTTPException(status_code=404, detail="File not found")
    
    fs_metadata.pop(filename)
    with open(JOURNAL_PATH, "a") as f:
        f.write(f"DELETE_FILE {json.dumps({'file_name': filename})}\n")