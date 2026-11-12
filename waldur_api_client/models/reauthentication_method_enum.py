from enum import Enum


class ReauthenticationMethodEnum(str, Enum):
    PASSKEY = "passkey"
    PASSWORD = "password"

    def __str__(self) -> str:
        return str(self.value)
