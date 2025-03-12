from enum import Enum


class ScopeTypeEnum(str, Enum):
    CLUSTER = "cluster"
    GLOBAL = "global"
    PROJECT = "project"

    def __str__(self) -> str:
        return str(self.value)
