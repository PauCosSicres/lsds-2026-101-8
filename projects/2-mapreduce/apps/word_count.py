from typing import Optional
import time

def map(key: str, value: str):
    time.sleep(5)  # for 2.2.7

    words = value.replace(",", " ").replace(".", "").replace(":", "").split()
    for word in words:
        yield word.lower(), 1


def reduce(key: str, values: list) -> str:
    return str(len(values))


def partitioner(key: str, partition_count: int) -> str:
    hash_value = 0
    for char in key:
        hash_value = (hash_value * 16777619 + ord(char)) % partition_count
    return str(hash_value)

