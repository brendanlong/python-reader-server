from reader_server.backends.interface import AbstractDb
from .connection import Connection
from .users import Users


class Db(AbstractDb):
    def __init__(self) -> None:
        self._conn = Connection()
        self._users = Users(self._conn)

    @property
    def users(self) -> Users:
        return self._users
