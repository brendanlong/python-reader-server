from typing import List, Optional
from uuid import uuid4

from reader_server.backends.interface import AbstractUsers
from reader_server.types import User
if __name__ == "MYPY":
    from .connection import Connection


class Users(AbstractUsers):
    def __init__(self, conn: "Connection") -> None:
        self.conn = conn

    async def by_id(self, id: str) -> Optional[User]:
        return self.conn.users.get(id)

    async def by_email(self, email: str) -> Optional[User]:
        for user in self.conn.users.values():
            if user.email == email.lower():
                return user
        return None

    async def create(self, email: str, password: str) -> User:
        user = User(id=str(uuid4()), email=email.lower())
        assert user.id not in self.conn.users
        self.conn.users[user.id] = user
        return user

    async def all(self) -> List[User]:
        return list(self.conn.users.values())
