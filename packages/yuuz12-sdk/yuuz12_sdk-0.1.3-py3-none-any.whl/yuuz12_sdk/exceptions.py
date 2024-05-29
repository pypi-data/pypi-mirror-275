"""https://doc.yuuz12.top/web/#/5/23"""


class Yuuz12ApiException(Exception):
    def __init__(self, msg: str = "接口正常响应", code: int = 200):
        self.msg = msg
        self.code = code

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"[{self.code}] {self.msg}"


class InsufficientPermissionException(Yuuz12ApiException):
    def __init__(self):
        super().__init__("用户权限不足", 300)


class InsufficientItemException(Yuuz12ApiException):
    def __init__(self):
        super().__init__("货币好感或道具不足", 301)


class ExistenceStatusException(Yuuz12ApiException):
    def __init__(self):
        super().__init__("参数指定数据不存在或已存在", 302)


class WrongParameterException(Yuuz12ApiException):
    def __init__(self):
        super().__init__("参数错误接口拒绝响应", 400)


class ApiConnectionError(Yuuz12ApiException):
    def __init__(self):
        super().__init__("与参数指定目标连接时发生错误", 401)


class FatalError(Yuuz12ApiException):
    def __init__(self):
        super().__init__("接口发生严重错误无法响应", 500)


__all__ = [
    "InsufficientPermissionException",
    "InsufficientItemException",
    "ExistenceStatusException",
    "WrongParameterException",
    "ApiConnectionError",
    "FatalError",
]
