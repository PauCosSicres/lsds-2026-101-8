def map(key: str, value: str):
    words = value.replace(",", " ").replace(".", "").replace(":", "").split()

    for w in words:
        w = w.lower()
        if len(w) > 3 and w.startswith("t"):
            yield "total", 1


def reduce(key: str, values: list) -> str:
    return str(sum(int(v) for v in values))


def partitioner(key: str, partition_count: int) -> str:
    return str(hash(key) % partition_count)
