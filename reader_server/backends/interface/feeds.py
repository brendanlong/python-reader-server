from abc import ABC, abstractmethod
from typing import List, Optional

from reader_server.types import Feed


class AbstractFeeds(ABC):
    @abstractmethod
    async def by_id(self, id: str) -> Optional[Feed]: pass

    @abstractmethod
    async def by_url(self, url: str) -> Optional[Feed]: pass

    @abstractmethod
    async def upsert(self, url: str, title: Optional[str]) -> Feed: pass

    @abstractmethod
    async def all(self) -> List[Feed]: pass
