from abc import ABC, abstractproperty

from . import feeds, users


AbstractFeeds = feeds.AbstractFeeds
AbstractUsers = users.AbstractUsers


class AbstractDb(ABC):
    @abstractproperty
    def feeds(self) -> AbstractFeeds: pass

    @abstractproperty
    def users(self) -> AbstractUsers: pass
