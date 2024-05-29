import httpx
from ._api import Yuuz12Api


class Cave(Yuuz12Api):
    def __init__(self, client: httpx.AsyncClient):
        super().__init__(
            client=client,
            nodes=["cave"],
            key_name="cave"
        )


__all__ = [
    "Cave"
]
