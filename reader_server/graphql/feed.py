from typing import Iterable, Optional

import graphene
from graphene import relay

from .context import ResolveInfo
from reader_server.types import Feed


class FeedType(graphene.ObjectType):
    class Meta:
        name = "Feed"
        interfaces = (relay.Node,)

    id: str
    url: str = graphene.Field(graphene.String, required=True)
    title: Optional[str] = graphene.Field(graphene.String)

    @classmethod
    async def get_node(cls, info: ResolveInfo, id: str) -> Feed:
        feed = await info.context.db.feeds.by_id(id)
        return cls(feed.id, feed.url, feed.title)

    def resolve_id(feed: Feed, info: ResolveInfo) -> str:
        return feed.id

    def resolve_url(feed: Feed, info: ResolveInfo) -> str:
        return feed.url

    def resolve_title(feed: Feed, info: ResolveInfo) -> Optional[str]:
        return feed.title


class FeedConnection(relay.Connection):
    class Meta:
        node = FeedType


class Query(graphene.ObjectType):
    feeds = relay.ConnectionField(FeedConnection)

    async def resolve_feeds(
        self,
        info: ResolveInfo,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None
    ) -> Iterable[Feed]:
        return await info.context.db.feeds.all()
