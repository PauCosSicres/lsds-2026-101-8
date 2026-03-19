import argparse
import httpx
import sys
import time

DEFAULT_BROKERS = "1@localhost:8001,2@localhost:8002,3@localhost:8003,4@localhost:8004,5@localhost:8005"

def parse_brokers(brokers_str):
    brokers = []
    for b in brokers_str.split(","):
        try:
            broker_id, addr = b.split("@")
            brokers.append((broker_id, addr))
        except ValueError:
            continue
    return brokers

def fetch_records(brokers, topic_partition, last_offset, max_batch_size):
    payload = {
        "topic_partition": topic_partition,
        "last_offset": last_offset,
        "max_batch_size": max_batch_size
    }

    for _, addr in brokers:
        url = f"http://{addr}/data/v1/consume"
        try:
            r = httpx.post(url, json=payload, timeout=5)
            if r.status_code == 200:
                return r.json()
            if r.status_code == 421: # Not the leader
                continue
        except Exception:
            continue
    return None

def main():
    parser = argparse.ArgumentParser(description="Consume Client")
    parser.add_argument("topic_partition", help="Example: mytopic-1")
    parser.add_argument("-s", "--size", type=int, default=10, help="Batch size")
    
    args = parser.parse_args()
    brokers = parse_brokers(DEFAULT_BROKERS)
    
    # Start at -1 se we fetch at the start
    current_offset = -1

    print(f"[*] Consuming from {args.topic_partition}...")

    try:
        while True:
            data = fetch_records(brokers, args.topic_partition, current_offset, args.size)
            
            if data and "records" in data:
                records = data["records"]
                for rec in records:
                    # Output format: [offset] [key] payload
                    print(f"[{rec['offset']}] [{rec['key']}] {rec['payload']}")
                
                # If we got new records, we move the pointer to the last one received
                if records:
                    current_offset = data["last_offset"]
            
            # Polling interval to keep things smooth
            time.sleep(0.5)

    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()