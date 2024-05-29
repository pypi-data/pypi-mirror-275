from ._api import Yuuz12Api
import httpx


class Email(Yuuz12Api):
    def __init__(self, client: httpx.AsyncClient):
        super().__init__(
            client=client,
            nodes=["email"]
        )


__all__ = [
    "Email"
]
