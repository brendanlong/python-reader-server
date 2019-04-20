from abc import ABC, abstractproperty

from .users import AbstractUsers


class AbstractDb(ABC):
    @abstractproperty
    def users(self) -> AbstractUsers: pass
