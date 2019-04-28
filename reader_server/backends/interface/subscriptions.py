from abc import ABC, abstractmethod
from typing import AsyncIterable, Optional

from reader_server.types import Subscription


class AbstractSubscriptions(ABC):
    @abstractmethod
    async def by_id(self, id: str) -> Optional[Subscription]: pass

    @abstractmethod
    async def by_feed_id(self, feed_id: str) -> AsyncIterable[Subscription]: pass

    @abstractmethod
    async def by_user_id(self, user_id: str) -> AsyncIterable[Subscription]: pass

    @abstractmethod
    async def create(self, feed_id: str, user_id: str) -> Subscription: pass

    @abstractmethod
    async def all(self) -> AsyncIterable[Subscription]: pass
