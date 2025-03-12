from enum import Enum


class UserInvitationsListOItem(str, Enum):
    CREATED = "created"
    EMAIL = "email"
    STATE = "state"
    VALUE_0 = "-created"
    VALUE_1 = "-email"
    VALUE_2 = "-state"

    def __str__(self) -> str:
        return str(self.value)
