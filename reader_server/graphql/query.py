import graphene

from . import feed
from . import user


class Query(feed.Query, user.Query, graphene.ObjectType):
    node = graphene.relay.Node.Field()
