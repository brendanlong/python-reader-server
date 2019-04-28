from typing import List, Optional
from uuid import uuid4

from reader_server.backends.interface import AbstractFeeds
from reader_server.types import Feed
if __name__ == "MYPY":
    from .connection import Connection


class Feeds(AbstractFeeds):
    def __init__(self, conn: "Connection") -> None:
        self.conn = conn

    async def by_id(self, id: str) -> Optional[Feed]:
        return self.conn.feeds.get(id)

    async def by_url(self, url: str) -> Optional[Feed]:
        for feed in self.conn.feeds.values():
            if feed.url == url.lower():
                return feed
        return None

    async def upsert(self, url: str, title: Optional[str]) -> Feed:
        existing_feed = await self.by_url(url)
        if existing_feed is None:
            id = str(uuid4())
        else:
            id = existing_feed.id
        feed = Feed(id=id, url=url, title=title)
        self.conn.feeds[feed.id] = feed
        return feed

    async def all(self) -> List[Feed]:
        return list(self.conn.feeds.values())
