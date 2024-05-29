import httpx
from ._api import Yuuz12Api


class Prize(Yuuz12Api):
    def __init__(self, client: httpx.AsyncClient):
        super().__init__(
            client=client,
            nodes=["Prize"],
            key_name="Prize"
        )


__all__ = [
    "Prize"
]