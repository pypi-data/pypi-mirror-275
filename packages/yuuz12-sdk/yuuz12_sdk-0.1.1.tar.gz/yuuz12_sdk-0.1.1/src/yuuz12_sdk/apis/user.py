import httpx

from ._api import Yuuz12Api


class User(Yuuz12Api):
    def __init__(self, client: httpx.AsyncClient):
        super().__init__(
            client=client,
            nodes=["user"],
            key_name="user"
        )


class UserCheck(Yuuz12Api):
    def __init__(self, client: httpx.AsyncClient):
        super().__init__(
            client=client,
            nodes=["user", "check"],
            key_name="user_check"
        )


__all__ = [
    'User',
    "UserCheck"
]
