from enum import Enum


class FeatureScopeEnum(str, Enum):
    DEPLOYMENT = "deployment"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
