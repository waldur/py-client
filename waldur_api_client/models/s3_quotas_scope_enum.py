from enum import Enum


class S3QuotasScopeEnum(str, Enum):
    ACCOUNT = "account"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
