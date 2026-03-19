import os
import json
import asyncio
import httpx
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
os.makedirs("/data", exist_ok=True)

BROKER_ID = int(os.getenv("BROKER_ID", 1))
LEADER_BROKER_ID = int(os.getenv("LEADER_BROKER_ID", 1))

# KRaft (metadata log)
class KRaft:
    def __init__(self):
        self.log_path = "metadata/__cluster_metadata.log"
        os.makedirs("metadata", exist_ok=True)

        if not os.path.exists(self.log_path):
            open(self.log_path, "w").close()

        self.records = self._load_metadata_log()

    def _load_metadata_log(self):
        records = []

        with open(self.log_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue

                offset, epoch, action, body = line.strip().split(" ", 3)

                records.append({
                    "offset": int(offset),
                    "epoch": int(epoch),
                    "action": action,
                    "body": json.loads(body)
                })

        return records

    def append_to_metadata_log(self, action, body):
        offset = len(self.records)
        epoch = 0  # fixed for 4.1
        line = f"{offset} {epoch} {action} {json.dumps(body)}\n"
        with open(self.log_path, "a") as f:
            f.write(line)

        self.records.append({
            "offset": offset,
            "epoch": epoch,
            "action": action,
            "body": body
        })

kraft = KRaft()


# MODELS
class CreateTopicRequest(BaseModel):
    topic_name: str
    partition_count: int

class ProduceRequest(BaseModel):
    topic_partition: str
    key: str | None = None
    payload: str
    acks: str

class ConsumeRequest(BaseModel):
    topic_partition: str
    last_offset: int
    max_batch_size: int
    follower_broker_id: str | None = None


# HELPERS
def topic_exists(topic_name):
    topics = set()

    for r in kraft.records:
        if r["action"] == "create-topic":
            topics.add(r["body"]["topic_name"])
        elif r["action"] == "delete-topic":
            topics.discard(r["body"]["topic_name"])

    return topic_name in topics

def get_partition_path(topic_partition: str):
    return f"/data/{topic_partition}/partition.log"

# ENDPOINTS
@app.get("/healthcheck")
def healthcheck():
    return {
        "status": "up",
        "broker_id": BROKER_ID,
        "leader_broker_id": LEADER_BROKER_ID
    }

@app.post("/admin/v1/topics", status_code=201)
def create_topic(req: CreateTopicRequest):

    # not leader
    if BROKER_ID != LEADER_BROKER_ID:
        raise HTTPException(
            status_code=421,
            detail=f"leader is {LEADER_BROKER_ID}, can't accept"
        )
    # invalid name
    if "-" in req.topic_name:
        raise HTTPException(status_code=400, detail="invalid topic name")

    # already exists
    if topic_exists(req.topic_name):
        raise HTTPException(
            status_code=409,
            detail=f"topic {req.topic_name} already exists"
        )
    # create partitions
    partitions = [
        {
            "id": f"{req.topic_name}-{i}",
            "replica_brokers": ["1", "2", "3", "4", "5"]
        }
        for i in range(1, req.partition_count + 1)
    ]
    # persist to metadata log (KEY PART)
    kraft.append_to_metadata_log(
        "create-topic",
        {
            "topic_name": req.topic_name,
            "partitions": partitions
        }
    )
    return {
        "topic_name": req.topic_name,
        "partitions": partitions
    }

@app.get("/admin/v1/topics")
def list_topics():
    if BROKER_ID != LEADER_BROKER_ID:
        raise HTTPException(
            status_code=421,
            detail=f"leader is {LEADER_BROKER_ID}, can't accept"
        )
    topics = {}

    #REPLAY LOG
    for r in kraft.records:
        if r["action"] == "create-topic":
            topics[r["body"]["topic_name"]] = r["body"]
        elif r["action"] == "delete-topic":
            topics.pop(r["body"]["topic_name"], None)
    return {
        "topics": list(topics.values())
    }

@app.delete("/admin/v1/topics/{topic_name}", status_code=204)
def delete_topic(topic_name: str):
    if BROKER_ID != LEADER_BROKER_ID:
        raise HTTPException(
            status_code=421,
            detail=f"leader is {LEADER_BROKER_ID}, can't accept"
        )
    #topic doesn't exist
    if not topic_exists(topic_name):
        raise HTTPException(
            status_code=404,
            detail=f"topic {topic_name} not found"
        )
    #append delete event to log
    kraft.append_to_metadata_log(
        "delete-topic",
        {
            "topic_name": topic_name
        }
    )
    return


@app.post("/data/v1/produce", status_code=204)
async def produce(request: ProduceRequest):
    if BROKER_ID != LEADER_BROKER_ID:
        raise HTTPException(status_code=421, detail="Not the leader")

    dir_path = f"/data/{request.topic_partition}"
    os.makedirs(dir_path, exist_ok=True) 
    
    log_path = get_partition_path(request.topic_partition)
    
    offset = 0
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            offset = len(f.readlines())

    with open(log_path, "a") as f:
        f.write(f"{offset} {request.key} {request.payload}\n")

    return {"offset": offset}

@app.post("/data/v1/consume")
def consume(req: ConsumeRequest):
    if BROKER_ID != LEADER_BROKER_ID:
        raise HTTPException(status_code=421, detail="Not the leader")

    log_path = get_partition_path(req.topic_partition)

    # Instead of 404, return empty records if file doesn't exist yet
    if not os.path.exists(log_path):
        return {"last_offset": req.last_offset, "records": []}

    with open(log_path, "r") as f:
        lines = f.readlines()

    # Determine start index
    start = 0 if req.last_offset == -1 else req.last_offset + 1
    batch = lines[start : start + req.max_batch_size]
    
    records = []
    new_last_offset = req.last_offset

    for line in batch:
        line = line.strip()
        if not line: continue
        
        parts = line.split(" ", 2)
        if len(parts) < 3: continue
        
        off, key, pay = parts
        records.append({
            "offset": int(off),
            "key": key,
            "payload": pay
        })
        new_last_offset = int(off)

    return {
        "last_offset": new_last_offset,
        "records": records
    }

BROKERS = [
    "1@broker1:8000",
    "2@broker2:8000",
    "3@broker3:8000",
    "4@broker4:8000",
    "5@broker5:8000",
]

replication_offsets = {}

async def background_loop():
    while True:
        if BROKER_ID != LEADER_BROKER_ID:
            try:
                async with httpx.AsyncClient() as client:

                    # get topics from leader
                    res = await client.get(
                        f"http://broker1:8000/admin/v1/topics"
                    )
                    topics = res.json()["topics"]

                    for topic in topics:
                        for partition in topic["partitions"]:
                            tp = partition["id"]

                            last_offset = replication_offsets.get(tp, -1)

                            # fetch new messages
                            res = await client.post(
                                f"http://broker1:8000/data/v1/consume",
                                json={
                                    "topic_partition": tp,
                                    "last_offset": last_offset,
                                    "max_batch_size": 100
                                }
                            )

                            data = res.json()
                            records = data["records"]

                            if not records:
                                continue

                            # write locally
                            dir_path = f"data/{tp}"
                            os.makedirs(dir_path, exist_ok=True)
                            log_path = get_partition_path(tp)

                            with open(log_path, "a") as f:
                                for r in records:
                                    f.write(
                                        f"{r['offset']} {r['key']} {r['payload']}\n"
                                    )

                            # update offset
                            replication_offsets[tp] = data["last_offset"]

            except Exception as e:
                logging.error(f"Replication error: {e}")

        await asyncio.sleep(1)

@app.on_event("startup")
async def start_background():
    asyncio.create_task(background_loop())

