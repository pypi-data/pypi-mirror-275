from ._api import Yuuz12Api
import httpx


class MinecraftPing(Yuuz12Api):
    def __init__(self, client: httpx.AsyncClient):
        super().__init__(
            client=client,
            nodes=["minecraft"],
            key_name="minecraft_ping"
        )


class MinecraftServer(Yuuz12Api):
    def __init__(self, client: httpx.AsyncClient):
        super().__init__(
            client=client,
            nodes=["minecraft", "server"],
            key_name="minecraft_server"
        )


class MinecraftBlacklist(Yuuz12Api):
    def __init__(self, client: httpx.AsyncClient):
        super().__init__(
            client=client,
            nodes=["minecraft", "blacklist"],
            key_name="minecraft_blacklist"
        )


__all__ = [
    "MinecraftPing",
    "MinecraftServer",
    "MinecraftBlacklist"
]
