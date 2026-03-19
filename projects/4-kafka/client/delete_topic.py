import argparse, httpx, sys

DEFAULT_BROKERS = "1@localhost:8001,2@localhost:8002,3@localhost:8003,4@localhost:8004,5@localhost:8005"


def parse_brokers(brokers_str):
    brokers = []
    for b in brokers_str.split(","):
        broker_id, addr = b.split("@")
        brokers.append((broker_id, addr))
    return brokers


def delete_topic(brokers, topic_name):
    for _, addr in brokers:
        url = f"http://{addr}/admin/v1/topics/{topic_name}"

        try:
            r = httpx.delete(url, timeout=5)

            #success
            if r.status_code == 204:
                return 0

            #not leader, try next
            if r.status_code == 421:
                continue

            #other error
            print(r.text)
            return 1

        except Exception:
            continue

    print("No broker accepted the request")
    return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("topic_name")
    parser.add_argument("-b", default=DEFAULT_BROKERS)

    args = parser.parse_args()

    brokers = parse_brokers(args.b)

    exit_code = delete_topic(brokers, args.topic_name)
    sys.exit(exit_code)