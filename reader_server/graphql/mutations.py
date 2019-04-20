import graphene

from . import user


class Mutations(user.Mutations, graphene.ObjectType):
    pass
