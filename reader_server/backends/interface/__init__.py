from abc import ABC, abstractproperty

from . import users


AbstractUsers = users.AbstractUsers


class AbstractDb(ABC):
    @abstractproperty
    def users(self) -> AbstractUsers: pass
