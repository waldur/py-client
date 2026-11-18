from enum import Enum


class GroupEnum(str, Enum):
    ALL_USERS = "all_users"
    AUTHENTICATED_USERS = "authenticated_users"

    def __str__(self) -> str:
        return str(self.value)
