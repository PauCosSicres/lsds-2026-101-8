import re

def map(key: str, value: str):
    words = re.findall(r"[a-zA-Z']+", value.lower())

    for i in range(len(words) - 1):
        yield f"{words[i]} {words[i+1]}", 1


def reduce(key: str, values: list) -> str:
    return str(len(values))


def partitioner(key: str, partition_count: int) -> str:
    h = 0
    for c in key:
        h = (h * 31 + ord(c)) % partition_count
    return str(h)
