import httpx
from ._api import Yuuz12Api


class Statistics(Yuuz12Api):
    def __init__(self, client: httpx.AsyncClient):
        super().__init__(
            client=client,
            nodes=["statistics"],
            key_name="statistics"
        )


__all__ = [
    "Statistics"
]
