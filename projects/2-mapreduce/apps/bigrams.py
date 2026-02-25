import re

def map(key: str, value: str):
    words = re.findall(r"[a-zA-Z']+", value.lower())

    for i in range(len(words) - 1):
        yield f"{words[i]} {words[i+1]}", "1"


def reduce(key: str, values: list) -> str:
    total = len(values)
    if total > 1:
        return str(total)
    return None


def partitioner(key: str, partition_count: int) -> int:
    return hash(key) % partition_count
