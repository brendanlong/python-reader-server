from abc import ABC, abstractproperty

from . import feeds, subscriptions, users


AbstractFeeds = feeds.AbstractFeeds
AbstractSubscriptions = subscriptions.AbstractSubscriptions
AbstractUsers = users.AbstractUsers


class AbstractDb(ABC):
    @abstractproperty
    def feeds(self) -> AbstractFeeds: pass

    @abstractproperty
    def subscriptions(self) -> AbstractSubscriptions: pass

    @abstractproperty
    def users(self) -> AbstractUsers: pass
