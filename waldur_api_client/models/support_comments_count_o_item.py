from enum import Enum


class SupportCommentsCountOItem(str, Enum):
    CREATED = "created"
    MODIFIED = "modified"
    VALUE_0 = "-created"
    VALUE_1 = "-modified"

    def __str__(self) -> str:
        return str(self.value)
