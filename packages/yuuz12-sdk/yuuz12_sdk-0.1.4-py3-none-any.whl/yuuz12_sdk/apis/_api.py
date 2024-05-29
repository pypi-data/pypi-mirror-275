"""https://doc.yuuz12.top/web/#/5/"""
from json import JSONDecodeError

import httpx
import os
from dotenv import load_dotenv

from ..log import logger

load_dotenv()

API_VERSION = int(os.getenv("API_VERSION", default=2))
API_KEY_V1 = os.getenv("API_KEY_V1", default=None)
API_KEY_V2 = os.getenv("API_KEY_V2", default=None)


class Yuuz12Api:
    BASE_URL_BOT = "https://bot.miku.chat/api"
    BASE_URL_FST = "https://skin.fstmc.top/api"

    def __init__(self, client: httpx.AsyncClient, version: int = API_VERSION, nodes: list[str] = None, key_name: str = None):
        self._client = client

        self._version = version
        self._nodes: list[str] = nodes or []  # ['user'], ['user', 'check']
        self._base_url = f"{self.BASE_URL_BOT}/v{self._version}/{'/'.join(self._nodes)}"

        self._key_name: str = key_name
        self._response: httpx.Response = None
        self._raw_content: bytes = None
        self._raw_json: dict = {}
        self._raw_code: int = None
        self._raw_msg: str = None
        self._result_json: dict = {}

    def call_api(self, api_name: str):
        async def _(method: str = "GET", **kwargs) -> httpx.Response:
            """通用请求 API"""
            url = f"{self._base_url}/{api_name}"
            match self._version:
                case 1:
                    kwargs |= {"key": API_KEY_V1}
                case 2:
                    kwargs |= {"key": API_KEY_V2}

            match method:
                case "GET":
                    response = await self._client.get(url, params=kwargs, follow_redirects=True)
                case "POST":
                    response = await self._client.post(url, data=kwargs, follow_redirects=True)
                case _:
                    raise TypeError(f"Unsupported method {method} in API call")
            logger.info(f"API get: {response.url}")

            self._response = response
            self._raw_content = self.response.content
            try:
                self._raw_json = self._response.json()
                if self._raw_json:
                    self._result_json = self._raw_json[self._key_name]
                    self._raw_code = self._raw_json["code"]
                    self._raw_msg = self._raw_json["msg"]
            except (UnicodeDecodeError, KeyError, JSONDecodeError) as e:  # 无 json
                self._raw_json = {}
                self._result_json = {}
            return response
        return _

    def __getattr__(self, api_name: str):
        return self.call_api(api_name)

    @property
    def response(self) -> httpx.Response:
        return self._response

    @property
    def raw(self) -> bytes:
        return self._raw_content

    @property
    def raw_data(self) -> dict:
        return self._raw_json

    @property
    def raw_msg(self) -> str:
        return self._raw_msg

    @property
    def raw_code(self) -> int:
        return self._raw_code

    @property
    def data(self) -> dict:
        return self._result_json

    @property
    def error(self) -> bool:
        return self.raw_code != 200


__all__ = [
    "Yuuz12Api"
]
