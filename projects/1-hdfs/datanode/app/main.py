from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import httpx

app = FastAPI()

STORAGE_PATH = Path("/code/storage")

@app.get("/healthcheck")
def healthcheck():
    return {"status": "up"}

@app.put("/files/{filename}/blocks/{block_number}")
def write_block(filename: str,block_number: int,file: UploadFile,pipeline: str = None ):
    file_dir = STORAGE_PATH / filename
    file_dir.mkdir(parents=True, exist_ok=True)

    block_path = file_dir / str(block_number)

    data = file.file.read()
    with open(block_path, "wb") as f:
        f.write(data)

    # send block to next datanode if pipeline exists
    if pipeline:
        datanodes = pipeline.split(",")
        next_dn = datanodes[0]
        remaining_pipeline = ",".join(datanodes[1:])

        url = f"http://datanode{next_dn}:80/files/{filename}/blocks/{block_number}"

        params = {}
        if remaining_pipeline:
            params["pipeline"] = remaining_pipeline

        with httpx.Client() as client:
            response = client.put(
                url,
                params=params,
                files={"file": data}
            )

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Pipeline forwarding failed")

    return {"status": "stored"}

@app.get("/files/{filename}/blocks/{block_number}")
def read_block(filename: str, block_number: int):
    block_path = STORAGE_PATH / filename / str(block_number)

    if not block_path.exists():
        raise HTTPException(status_code=404, detail="Block not found")

    return FileResponse(block_path)
