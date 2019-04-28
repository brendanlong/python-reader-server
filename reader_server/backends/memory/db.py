from reader_server.backends.interface import AbstractDb
from .connection import Connection
from .feeds import Feeds
from .subscriptions import Subscriptions
from .users import Users


class Db(AbstractDb):
    def __init__(self) -> None:
        self._conn = Connection()
        self._feeds = Feeds(self._conn)
        self._subscriptions = Subscriptions(self._conn)
        self._users = Users(self._conn)

    @property
    def feeds(self) -> Feeds:
        return self._feeds

    @property
    def subscriptions(self) -> Subscriptions:
        return self._subscriptions

    @property
    def users(self) -> Users:
        return self._users
