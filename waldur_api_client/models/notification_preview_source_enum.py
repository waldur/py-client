from enum import Enum


class NotificationPreviewSourceEnum(str, Enum):
    CALL = "call"
    DEFAULT = "default"
    PORTAL = "portal"

    def __str__(self) -> str:
        return str(self.value)
