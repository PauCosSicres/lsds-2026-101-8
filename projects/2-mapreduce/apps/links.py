from typing import Iterable, Tuple, List

def extract_agent(line: str) -> str:
    parts = line.split('"')
    if len(parts) < 6:
        return "unknown"
    agent = parts[5].lower()

    if "chrome" in agent:
        return "chrome"
    if "firefox" in agent:
        return "firefox"
    if "mozilla" in agent:
        return "mozilla"
    if "postman" in agent:
        return "postman"
    if "curl" in agent:
        return "curl"
    return "other"


def map(key: str, value: str) -> Iterable[Tuple[str, int]]:
    for line in value.splitlines():
        agent = extract_agent(line)
        yield agent, 1


def reduce(key: str, values: List[str]) -> str:
    return str(len(values))


def partitioner(key: str, partition_count: int) -> str:
    h = 0
    for c in key:
        h = (h * 31 + ord(c)) % partition_count
    return str(h)
