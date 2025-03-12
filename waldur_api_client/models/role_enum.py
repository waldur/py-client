from enum import Enum


class RoleEnum(str, Enum):
    MEMBER = "member"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
