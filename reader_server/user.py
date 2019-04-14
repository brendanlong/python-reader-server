from typing import Any, Iterable

import graphene
from graphene import relay
from promise.dataloader import DataLoader


class User(graphene.ObjectType):
    class Meta:
        interfaces = (relay.Node,)

    email = graphene.String()

    @classmethod
    async def get_node(cls, info: Any, id: str) -> "User":
        users = await get_users([id])
        return next(iter(users))


async def get_users(ids: Iterable[str]) -> Iterable[User]:
    return []


class UserConnection(relay.Connection):
    class Meta:
        node = User


class UserLoader(DataLoader):
    async def batch_load_fn(self, keys: Iterable[str]) -> Iterable[User]:
        return await get_users(ids=keys)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()

    users = graphene.List(graphene.NonNull(User))

    async def resolve_users(_, info: Any) -> Iterable[User]:
        return await get_users([])
