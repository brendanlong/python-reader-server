from typing import Iterable

import graphene
from graphene import relay

from .context import ResolveInfo
from reader_server.types import User


class UserObj(graphene.ObjectType):
    class Meta:
        interfaces = (relay.Node,)

    email = graphene.NonNull(graphene.String)

    @classmethod
    async def get_node(cls, info: ResolveInfo, id: str) -> User:
        return await info.context.db.users.by_id(id)

    def resolve_id(user: User, info: ResolveInfo) -> str:
        return user.id

    def resolve_email(user: User, info: ResolveInfo) -> str:
        return user.email


class UserConnection(relay.Connection):
    class Meta:
        node = UserObj


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()

    users = relay.ConnectionField(UserConnection)

    async def resolve_users(self, info: ResolveInfo) -> Iterable[User]:
        return await info.context.db.users.all()


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.NonNull(graphene.String)
        password = graphene.NonNull(graphene.String)

    user = graphene.Field(lambda: UserObj)

    async def mutate(self, info: ResolveInfo, email: str,
                     password: str) -> "CreateUser":
        user = await info.context.db.users.create(email, password)
        return CreateUser(user)


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
