from typing import Dict

from .users import User


class Connection:
    def __init__(self) -> None:
        self.users: Dict[str, User] = {}
