import sys, httpx
from pathlib import Path

NAMENODE_URL = "http://localhost:8000"

def main():
    filename = sys.argv[1]
    output_path = Path(sys.argv[2])

    # get metadata
    meta = httpx.get(f"{NAMENODE_URL}/files/{filename}").json()
    blocks = meta["blocks"]

    with open(output_path, "wb") as out: # binary
        for block in blocks:
            block_number = block["number"]
            replica = block["replicas"][0]

            url = f"http://localhost:800{replica}/files/{filename}/blocks/{block_number}"
            resp = httpx.get(url)
            resp.raise_for_status()

            out.write(resp.content)

if __name__ == "__main__":
    main()
