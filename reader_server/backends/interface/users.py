from abc import ABC, abstractmethod
from typing import List, Optional

from reader_server.types import User


class AbstractUsers(ABC):
    @abstractmethod
    async def by_id(self, id: str) -> Optional[str]: pass

    @abstractmethod
    async def by_email(self, email: str) -> Optional[str]: pass

    @abstractmethod
    async def create(self, email: str, password: str) -> User: pass

    @abstractmethod
    async def all(self) -> List[User]: pass
