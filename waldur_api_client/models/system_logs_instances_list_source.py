from enum import Enum


class SystemLogsInstancesListSource(str, Enum):
    API = "api"
    BEAT = "beat"
    WORKER = "worker"

    def __str__(self) -> str:
        return str(self.value)
