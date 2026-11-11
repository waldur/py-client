from enum import Enum


class ResourceApiKeyStatusOEnum(str, Enum):
    CREATED = "created"
    ESTIMATED_COST = "estimated_cost"
    ISSUED_AT = "issued_at"
    STATE = "state"
    VALUE_0 = "-created"
    VALUE_1 = "-estimated_cost"
    VALUE_2 = "-issued_at"
    VALUE_3 = "-state"

    def __str__(self) -> str:
        return str(self.value)
