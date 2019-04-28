from reader_server.backends.interface import AbstractDb
from .connection import Connection
from .feeds import Feeds
from .users import Users


class Db(AbstractDb):
    def __init__(self) -> None:
        self._conn = Connection()
        self._users = Users(self._conn)
        self._feeds = Feeds(self._conn)

    @property
    def feeds(self) -> Feeds:
        return self._feeds

    @property
    def users(self) -> Users:
        return self._users
