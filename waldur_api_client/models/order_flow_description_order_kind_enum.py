from enum import Enum


class OrderFlowDescriptionOrderKindEnum(str, Enum):
    AUTO_TERMINATE = "auto_terminate"
    CREATE = "create"
    RENEW = "renew"
    RESTORE = "restore"
    SWITCH_PLAN = "switch_plan"
    TERMINATE = "terminate"
    UPDATE_LIMITS = "update_limits"
    UPDATE_OPTIONS = "update_options"

    def __str__(self) -> str:
        return str(self.value)
