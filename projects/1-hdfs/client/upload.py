import sys
import httpx
from pathlib import Path

NAMENODE = "http://localhost:8000"

def main():
    local_path = Path(sys.argv[1])
    filename = sys.argv[2]


    # read local file
    data = local_path.read_bytes()

    # 1. create file metadata (and get block size)
    resp = httpx.post(
        f"{NAMENODE}/files",
        json={"file_name": filename}
    )
    resp.raise_for_status()

    file_meta = resp.json()
    block_size = file_meta["block_size_bytes"]

    # 2. split file into blocks
    blocks = [
        data[i:i + block_size]
        for i in range(0, len(data), block_size)
    ]

    # 3. upload each block
    for block_number, block_data in enumerate(blocks):
        # create block metadata
        resp = httpx.post(
            f"{NAMENODE}/files/{filename}/blocks"
        )
        resp.raise_for_status()

        block_meta = resp.json()["blocks"][-1]
        replicas = block_meta["replicas"]

        first_dn = replicas[0]
        pipeline = ",".join(replicas[1:])

        url = f"http://localhost:800{first_dn}/files/{filename}/blocks/{block_number}"

        params = {}
        if pipeline:
            params["pipeline"] = pipeline

        httpx.put(
            url,
            params=params,
            files={"file": block_data}
        )

if __name__ == "__main__":
    main()
