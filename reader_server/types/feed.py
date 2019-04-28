from typing import NamedTuple, Optional


class Feed(NamedTuple):
    id: str
    url: str
    title: Optional[str]
