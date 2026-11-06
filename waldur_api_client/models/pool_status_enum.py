from enum import Enum


class PoolStatusEnum(str, Enum):
    ACCEPTED = "accepted"
    DECLINED = "declined"
    EXPIRED = "expired"
    INVITED = "invited"

    def __str__(self) -> str:
        return str(self.value)
