from enum import Enum


class PublicMaintenanceAnnouncementTypeEnum(str, Enum):
    DANGER = "danger"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
