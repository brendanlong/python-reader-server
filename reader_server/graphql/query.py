import graphene

from . import user


class Query(user.Query, graphene.ObjectType):
    node = graphene.relay.Node.Field()
