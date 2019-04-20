from typing import NamedTuple

import graphene

from reader_server.backends.memory import Db


class Context(NamedTuple):
    db: Db


class ResolveInfo(graphene.ResolveInfo):
    context: Context
