from typing import Optional, NamedTuple

import graphene

from reader_server.backends.memory import Db
from reader_server.types import User


class Context(NamedTuple):
    db: Db
    user: Optional[User] = None


class ResolveInfo(graphene.ResolveInfo):
    context: Context
