from enum import Enum


class SecretFormatEnum(str, Enum):
    COMMENT = "comment"
    ENV = "env"

    def __str__(self) -> str:
        return str(self.value)
