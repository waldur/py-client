from enum import Enum


class KeysHeadOItem(str, Enum):
    NAME = "name"
    VALUE_0 = "-name"

    def __str__(self) -> str:
        return str(self.value)
