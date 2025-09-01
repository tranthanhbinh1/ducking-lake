from datetime import datetime


def parse_timestamp(v):
    if isinstance(v, str):
        v = v.rstrip("Z")
        return datetime.fromisoformat(v)
    return v
