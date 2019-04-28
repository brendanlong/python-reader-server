from typing import AsyncIterable, Iterable, Optional
from uuid import uuid4

from reader_server.backends.interface import AbstractSubscriptions
from reader_server.types import Subscription
if __name__ == "MYPY":
    from .connection import Connection


class Subscriptions(AbstractSubscriptions):
    def __init__(self, conn: "Connection") -> None:
        self.conn = conn

    async def by_id(self, id: str) -> Optional[Subscription]:
        return self.conn.subscriptions.get(id)

    async def by_feed_id(self, feed_id: str) -> AsyncIterable[Subscription]:
        for subscription in self.conn.subscriptions.values():
            if subscription.feed_id == feed_id:
                yield subscription

    async def by_user_id(self, user_id: str) -> AsyncIterable[Subscription]:
        for subscription in self.conn.subscriptions.values():
            if subscription.user_id == user_id:
                yield subscription

    async def create(self, feed_id: str, user_id: str) -> Subscription:
        existing_subscription = None
        async for subscription in self.by_user_id(user_id):
            if subscription.feed_id == feed_id:
                existing_subscription = subscription
                break

        if existing_subscription is None:
            id = str(uuid4())
        else:
            id = existing_subscription.id
        subscription = Subscription(id=id, feed_id=feed_id, user_id=user_id)
        self.conn.subscriptions[subscription.id] = subscription
        return subscription

    async def all(self) -> AsyncIterable[Subscription]:
        for subscription in self.conn.subscriptions.values():
            yield subscription
