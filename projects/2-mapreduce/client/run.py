import sys
import time
import httpx

MASTER = "http://localhost:8000"


def create_job(data, maps, reduces, app):
    r = httpx.post(f"{MASTER}/jobs", json={
        "data_path": data,
        "map_partitions": int(maps),
        "reduce_partitions": int(reduces),
        "app_name": app
    })

    response = r.json()

    if "job_id" not in response:
        print("Server response:", response)
        raise Exception("Job creation failed")

    return response["job_id"]


def job_status(job_id):
    r = httpx.get(f"{MASTER}/jobs/{job_id}")
    return r.json()


def main():
    data = sys.argv[1]
    maps = sys.argv[2]
    reduces = sys.argv[3]
    app = sys.argv[4]

    job_id = create_job("./data/"+data, maps, reduces, app)
    print(f"job_id: {job_id}")

    last_message = ""

    while True:
        job = job_status(job_id)

        if job["status"] == "completed":
            print("completed")
            break

        # mapping progress
        mappers_done = sum(1 for m in job["mappers"] if m["status"] == "completed")
        mappers_total = len(job["mappers"])

        if mappers_done < mappers_total:
            phase = "mapping"
            done = mappers_done
            total = mappers_total
        else:
            # reducing progress
            reducers_done = sum(1 for r in job["reducers"] if r["status"] == "completed")
            reducers_total = len(job["reducers"])
            phase = "reducing"
            done = reducers_done
            total = reducers_total

        message = f"in-progress - {phase} ({done}/{total} partitions done)"

        if message != last_message:
            print(message)
            last_message = message

        time.sleep(0.25)


if __name__ == "__main__":
    main()
