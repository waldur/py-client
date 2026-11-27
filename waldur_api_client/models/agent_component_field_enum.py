from enum import Enum


class AgentComponentFieldEnum(str, Enum):
    ACCOUNTING_TYPE = "accounting_type"
    LABEL = "label"
    LIMIT = "limit"
    MEASURED_UNIT = "measured_unit"
    UNIT_FACTOR = "unit_factor"

    def __str__(self) -> str:
        return str(self.value)
