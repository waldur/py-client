from enum import Enum


class TeamPartEnum(str, Enum):
    COMPLETES = "completes"
    CONTRIBUTES = "contributes"

    def __str__(self) -> str:
        return str(self.value)
