from typing import Iterable

import graphene
from graphene import relay

from reader_server import types
from .context import ResolveInfo


class User(graphene.ObjectType):
    class Meta:
        interfaces = (relay.Node,)

    email = graphene.NonNull(graphene.String)

    @classmethod
    def from_db(cls, db_user: types.User) -> "User":
        return cls(id=db_user.id, email=db_user.email)

    @classmethod
    async def get_node(cls, info: ResolveInfo, id: str) -> "User":
        return await info.context.db.users.by_id(id)


class UserConnection(relay.Connection):
    class Meta:
        node = User


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()

    users = relay.ConnectionField(UserConnection)

    async def resolve_users(self, info: ResolveInfo) -> Iterable[User]:
        return await info.context.db.users.all()
