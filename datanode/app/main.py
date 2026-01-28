from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
import os
import asyncio
import httpx

app = FastAPI()

STORAGE_PATH = "/code/storage"
NAMENODE_URL = "http://namenode:80"


@app.get("/healthcheck")
def healthcheck():
    return {"status": "up"}


@app.get("/files/{filename}/blocks/{block_number}")
def get_block(filename: str, block_number: int):
    block_path = f"{STORAGE_PATH}/{filename}/{block_number}"

    if not os.path.exists(block_path):
        raise HTTPException(status_code=404, detail="Block not found")

    return FileResponse(
        path=block_path,
        media_type="application/octet-stream",
        filename=str(block_number),
    )


@app.put("/files/{filename}/blocks/{block_number}")
async def put_block(
    filename: str,
    block_number: int,
    request: Request,
    pipeline: str | None = None,
):
    data = await request.body()

    dir_path = f"{STORAGE_PATH}/{filename}"
    os.makedirs(dir_path, exist_ok=True)

    block_path = f"{dir_path}/{block_number}"
    with open(block_path, "wb") as f:
        f.write(data)

    if pipeline:
        pipeline_ids = [x.strip() for x in pipeline.split(",") if x.strip()]

        if pipeline_ids:
            next_dn = pipeline_ids[0]
            remaining = pipeline_ids[1:]

            url = f"http://datanode{next_dn}:80/files/{filename}/blocks/{block_number}"

            params = {}
            if remaining:
                params["pipeline"] = ",".join(remaining)

            async with httpx.AsyncClient() as client:
                await client.put(
                    url,
                    params=params,
                    content=data,
                    headers={"Content-Type": "application/octet-stream"},
                )

    return {
        "message": "block stored",
        "filename": filename,
        "block_number": block_number,
    }


def collect_blocks():
    blocks = []

    if not os.path.exists(STORAGE_PATH):
        return blocks

    for filename in os.listdir(STORAGE_PATH):
        file_dir = f"{STORAGE_PATH}/{filename}"
        if not os.path.isdir(file_dir):
            continue

        for block in os.listdir(file_dir):
            try:
                block_num = int(block)
            except ValueError:
                continue

            blocks.append({"filename": filename, "block_number": block_num})

    return blocks


async def send_block_report():
    datanode_id = int(os.environ.get("DATANODE_ID", "1"))

    report = {
        "datanode_id": datanode_id,
        "blocks": collect_blocks(),
    }

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(f"{NAMENODE_URL}/block-report", json=report)
            resp.raise_for_status()

        payload = resp.json()
        replications = payload.get("replicate", [])

        for r in replications:
            filename = r["filename"]
            block_number = r["block_number"]
            target_dn = r["target_datanode"]

            src_path = f"{STORAGE_PATH}/{filename}/{block_number}"
            if not os.path.exists(src_path):
                continue

            with open(src_path, "rb") as f:
                data = f.read()

            url = f"http://datanode{target_dn}:80/files/{filename}/blocks/{block_number}"

            async with httpx.AsyncClient() as client:
                await client.put(
                    url,
                    content=data,
                    headers={"Content-Type": "application/octet-stream"}
                )
    except Exception as e:
        print(f"[datanode {datanode_id}] block report failed: {e}")


async def block_report_loop():
    while True:
        await send_block_report()
        await asyncio.sleep(30)


@app.on_event("startup")
async def start_background_tasks():
    asyncio.create_task(block_report_loop())
