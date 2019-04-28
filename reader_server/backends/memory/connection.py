from typing import Dict

from .feeds import Feed
from .subscriptions import Subscription
from .users import User


class Connection:
    def __init__(self) -> None:
        self.feeds: Dict[str, Feed] = {}
        self.subscriptions: Dict[str, Subscription] = {}
        self.users: Dict[str, User] = {}
