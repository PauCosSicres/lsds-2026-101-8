import httpx

NAMENODE = "http://localhost:8000"

def main():
    response = httpx.get(f"{NAMENODE}/datanodes")
    response.raise_for_status()
    datanodes = response.json()["datanodes"]

    for dn in datanodes:
        print(f"{dn['id']}@{dn['host']}:{dn['port']}")

if __name__ == "__main__":
    main()
