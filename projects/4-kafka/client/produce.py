import argparse
import httpx
import sys

DEFAULT_BROKERS = "1@localhost:8001,2@localhost:8002,3@localhost:8003,4@localhost:8004,5@localhost:8005"

def parse_brokers(brokers_str):
    brokers = []
    for b in brokers_str.split(","):
        broker_id, addr = b.split("@")
        brokers.append((broker_id, addr))
    return brokers

def produce_message(brokers, topic_partition, key, payload):
    # Data payload sent to the broker
    data = {
        "topic_partition": topic_partition,
        "key": key,
        "payload": payload,
        "acks": "all" 
    }

    # Go through the brokers to find the leader
    for _, addr in brokers:
        url = f"http://{addr}/data/v1/produce"
        try:
            r = httpx.post(url, json=data, timeout=5)
            
            if r.status_code == 200 or r.status_code == 204:
                print("> OK")
                return True
            if r.status_code == 421: # Not the leader, try next broker
                continue
            
            print(f"Error: {r.text}")
            return False
        except Exception:
            continue
            
    print("Error: No broker accepted the request")
    return False

def main():
    parser = argparse.ArgumentParser(description="Produce Client")
    parser.add_argument("topic_partition", help="Example: mytopic-0")
    
    args = parser.parse_args()
    brokers = parse_brokers(DEFAULT_BROKERS)

    try:
        while True:
            line = sys.stdin.readline()
            if not line: 
                break
            
            line = line.strip()
            if not line: # Exit on empty line per README
                sys.exit(0)

            # Split "key message" into key and payload
            parts = line.split(" ", 1) 
            if len(parts) < 2:
                print("Invalid format. Use: <key> <message>")
                continue
            
            key, payload = parts
            
            if not produce_message(brokers, args.topic_partition, key, payload):
                sys.exit(1)

    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()