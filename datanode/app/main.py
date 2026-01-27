from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {
        "status": "up"
    }

from fastapi.responses import FileResponse
from fastapi import HTTPException
import os

@app.get("/files/{filename}/blocks/{block_number}")
def get_block(filename: str, block_number: int):
    block_path = f"/code/storage/{filename}/{block_number}"

    if not os.path.exists(block_path):
        raise HTTPException(status_code=404, detail="Block not found")

    return FileResponse(
        path=block_path,
        media_type="application/octet-stream",
        filename=str(block_number)
    )
