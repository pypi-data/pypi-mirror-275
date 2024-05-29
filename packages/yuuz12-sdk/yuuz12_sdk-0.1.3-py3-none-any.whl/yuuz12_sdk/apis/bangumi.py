import httpx
from ._api import Yuuz12Api


class Bangumi(Yuuz12Api):
    def __init__(self, client: httpx.AsyncClient):
        super().__init__(
            client=client,
            nodes=["Bangumi"],
            key_name="Bangumi"
        )


__all__ = [
    "Bangumi"
]
