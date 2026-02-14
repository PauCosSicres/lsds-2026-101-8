from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/info")
def read_info():
    return {"studentId": 555, "universityName": "upf"}

class Operate(BaseModel):
    x: int
    y: int

@app.post("/sum")
def sum(sum: Operate):
    return {f"result: {sum.x + sum.y}"}

@app.post("/multiply/{int1}/{int2}")
def multiply(int1: int, int2: int):
    return {f"result: {int1 * int2}"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
