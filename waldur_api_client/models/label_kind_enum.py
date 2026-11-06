from enum import Enum


class LabelKindEnum(str, Enum):
    AWAITING_RESPONSE = "awaiting_response"
    CONFIGURED = "configured"
    DECISION = "decision"
    INTERNAL_CHECK = "internal_check"
    STEP_NAME = "step_name"

    def __str__(self) -> str:
        return str(self.value)
