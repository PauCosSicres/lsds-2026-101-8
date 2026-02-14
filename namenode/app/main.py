from fastapi import FastAPI
import time
import asyncio
from collections import defaultdict, deque

app = FastAPI()

datanode_blocks = defaultdict(set)

block_locations = defaultdict(set)

last_heartbeat = {}

replication_queue = deque()

REPLICATION_FACTOR = 2
DATANODE_TIMEOUT = 90


@app.get("/healthcheck")
def healthcheck():
    return {"status": "up"}


@app.post("/block-report")
def block_report(report: dict):
    """
    report = {
        "datanode_id": 1,
        "blocks": [
            {"filename": "a.txt", "block_number": 0}
        ]
    }
    """

    datanode_id = report["datanode_id"]
    now = time.time()

    last_heartbeat[datanode_id] = now

    reported_blocks = {
        (b["filename"], b["block_number"]) for b in report["blocks"]
    }

    previous_blocks = datanode_blocks[datanode_id]

    removed_blocks = previous_blocks - reported_blocks
    for block in removed_blocks:
        block_locations[block].discard(datanode_id)
        if len(block_locations[block]) < REPLICATION_FACTOR:
            replication_queue.append(block)

    new_blocks = reported_blocks - previous_blocks
    for block in new_blocks:
        block_locations[block].add(datanode_id)

    datanode_blocks[datanode_id] = reported_blocks

    replicate = []

    if replication_queue:
        block = replication_queue[0]
        owners = block_locations[block]

        if datanode_id in owners:
            for target_dn in datanode_blocks.keys():
                if target_dn not in owners:
                    replicate.append({
                        "filename": block[0],
                        "block_number": block[1],
                        "target_datanode": target_dn
                    })
                    replication_queue.popleft()
                    break

    return {
        "replicate": replicate,
        "delete": []
    }


async def monitor_datanodes():
    while True:
        now = time.time()

        for dn, last in list(last_heartbeat.items()):
            if now - last > DATANODE_TIMEOUT:
                print(f"[namenode] datanode {dn} is DOWN")

                for block in datanode_blocks[dn]:
                    block_locations[block].discard(dn)
                    if len(block_locations[block]) < REPLICATION_FACTOR:
                        replication_queue.append(block)

                datanode_blocks.pop(dn, None)
                last_heartbeat.pop(dn, None)

        await asyncio.sleep(10)


@app.on_event("startup")
async def start_monitor():
    asyncio.create_task(monitor_datanodes())
