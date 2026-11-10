from enum import Enum


class DemoPresetLoadJobStateEnum(str, Enum):
    DONE = "done"
    ERRED = "erred"
    PENDING = "pending"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
