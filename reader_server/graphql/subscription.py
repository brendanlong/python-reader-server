from typing import Iterable, Optional

import aiohttp
import feedparser
import graphene
from graphene import relay

from .context import ResolveInfo
from .feed import FeedObj
from .user import UserObj
from reader_server.types import Subscription, User


class SubscriptionObj(graphene.ObjectType):
    class Meta:
        name = "Subscription"
        interfaces = (relay.Node,)

    id: str
    feed: str = graphene.Field(FeedObj, required=True)
    user: str = graphene.Field(UserObj, required=True)

    @classmethod
    async def get_node(cls, info: ResolveInfo, id: str) -> User:
        subscription = await info.context.db.subscriptions.by_id(id)
        return cls(subscription.id, subscription.feed_id, subscription.user_id)

    def resolve_id(subscription: Subscription, info: ResolveInfo) -> str:
        return subscription.id

    def resolve_feed(subscription: Subscription, info: ResolveInfo) -> str:
        return info.context.db.feeds.by_id(subscription.feed_id)

    def resolve_user(subscription: Subscription, info: ResolveInfo) -> str:
        return info.context.db.users.by_id(subscription.user_id)


class SubscriptionConnection(relay.Connection):
    class Meta:
        node = SubscriptionObj


class Query(graphene.ObjectType):
    subscriptions = relay.ConnectionField(SubscriptionConnection)

    async def resolve_subscription(
        self,
        info: ResolveInfo,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None
    ) -> Iterable[User]:
        return await info.context.db.subscriptions.all()


class CreateSubscription(graphene.Mutation):
    class Arguments:
        url = graphene.NonNull(graphene.String)

    subscription: SubscriptionObj = graphene.Field(
        SubscriptionObj, required=True)

    async def mutate(
        self,
        info: ResolveInfo,
        url: str
    ) -> "CreateSubscription":
        user = info.context.user
        assert user is not None
        session = info.context.session
        res = await session.get(url)
        text = await res.text()
        assert res.status == 200

        data = feedparser.parse(text)
        db = info.context.db
        feed = await db.feeds.upsert(url, data.feed.title)
        subscription = await db.subscriptions.create(feed.id, user.id)
        return CreateSubscription(subscription)


class Mutations(graphene.ObjectType):
    create_subscription = CreateSubscription.Field()
