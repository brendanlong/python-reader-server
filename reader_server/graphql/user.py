from typing import Iterable, Optional

import graphene
from graphene import relay

from .context import ResolveInfo
from reader_server.types import User
from .scalars import Email


class UserObj(graphene.ObjectType):
    class Meta:
        interfaces = (relay.Node,)

    email = graphene.Field(Email, required=True)

    @classmethod
    async def get_node(cls, info: ResolveInfo, id: str) -> User:
        user = await info.context.db.users.by_id(id)
        return cls(user.id, user.email)

    def resolve_id(user: User, info: ResolveInfo) -> str:
        return user.id

    def resolve_email(user: User, info: ResolveInfo) -> str:
        return user.email


class UserConnection(relay.Connection):
    class Meta:
        node = UserObj


class Query(graphene.ObjectType):
    users = relay.ConnectionField(UserConnection)

    async def resolve_users(
        self,
        info: ResolveInfo,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None
    ) -> Iterable[User]:
        return await info.context.db.users.all()


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.NonNull(Email)
        password = graphene.NonNull(graphene.String)

    user = graphene.Field(lambda: UserObj)

    async def mutate(self, info: ResolveInfo, email: str,
                     password: str) -> "CreateUser":
        user = await info.context.db.users.create(email, password)
        return CreateUser(UserObj(user.id, user.email))


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
