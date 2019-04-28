import graphene

from . import feed, subscription, user


class Query(feed.Query, subscription.Query, user.Query, graphene.ObjectType):
    node = graphene.relay.Node.Field()
