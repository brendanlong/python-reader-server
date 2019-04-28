import graphene

from . import subscription, user


class Mutations(subscription.Mutations, user.Mutations, graphene.ObjectType):
    pass
