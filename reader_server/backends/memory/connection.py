from typing import Dict

from .feeds import Feed
from .users import User


class Connection:
    def __init__(self) -> None:
        self.feeds: Dict[str, Feed] = {}
        self.users: Dict[str, User] = {}
