import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Environments:

    redis_url: str
    redis_port: int
    public_dir: str


_environemnts: Optional[Environments] = None


def get_environments():
    global _environemnts
    if not _environemnts:
        _environemnts = Environments(
            redis_url=os.environ["REDIS_URL"],
            redis_port=os.environ["REDIS_PORT"],
            public_dir=os.environ["PUBLIC_DIR"],
        )

    return _environemnts
