from abc import ABC, abstractproperty

from .feeds import AbstractFeeds
from .subscriptions import AbstractSubscriptions
from .users import AbstractUsers


class AbstractDb(ABC):
    @abstractproperty
    def feeds(self) -> AbstractFeeds: pass

    @abstractproperty
    def subscriptions(self) -> AbstractSubscriptions: pass

    @abstractproperty
    def users(self) -> AbstractUsers: pass
