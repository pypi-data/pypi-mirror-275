from dataclasses import dataclass, field


@dataclass
class UserModel:
    qq: str
    id: str
    name: str
    kook_id: str
    telegram_name: str
    osu_name: str
    osu_mode: str
    favorability: str
    coin: str
    check_in_time_last: str
    check_number: str
    check_rank: str
    status: str
    group: str
    registered_time: str
    registered_timestamp: str
    item: dict[str, int]
    check_continuous_number: int

    fst_mail: str = field(default="")
    qqguild_id: str = field(default="")
    badge: dict[str, list] = field(default_factory=dict)


__all__ = [
    "UserModel",
]
