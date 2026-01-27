from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
blocks = {}

@app.get("/healthcheck")
def healthcheck():
    return {"status": "up"}

class Block(BaseModel):
    block_id: int
    data: str

@app.put("/block")
def put_block(block: Block):
    blocks[block.block_id] = block.data
    return {
        "message": "block stored",
        "block_id": block.block_id
    }
