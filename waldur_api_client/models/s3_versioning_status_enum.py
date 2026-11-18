from enum import Enum


class S3VersioningStatusEnum(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    SUSPENDED = "Suspended"

    def __str__(self) -> str:
        return str(self.value)
