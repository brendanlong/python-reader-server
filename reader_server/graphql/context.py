from typing import Optional, NamedTuple

import aiohttp
import graphene

from reader_server.backends.memory import Db
from reader_server.types import User


class Context(NamedTuple):
    db: Db
    session: aiohttp.ClientSession
    user: Optional[User] = None


class ResolveInfo(graphene.ResolveInfo):
    context: Context
