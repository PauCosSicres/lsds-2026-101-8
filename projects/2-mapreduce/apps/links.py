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


def map(key: str, value: str) -> Iterable[Tuple[str, str]]:
    for line in value.splitlines():
        if not line.strip():
            continue
        agent = extract_agent(line)
        yield agent, "1"


def reduce(key: str, values: List[str]) -> str:
    total = sum(int(v) for v in values)
    return str(total)


def partitioner(key: str, partition_count: int) -> int:
    return hash(key) % partition_count
