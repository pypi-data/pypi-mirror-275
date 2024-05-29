import httpx
from ._api import Yuuz12Api


class BaiduCensor(Yuuz12Api):
    def __init__(self, client: httpx.AsyncClient):
        super().__init__(
            client=client,
            nodes=["baidu", "img_censor"],
            key_name="baidu_imgcensor"
        )


__all__ = [
    "BaiduCensor"
]