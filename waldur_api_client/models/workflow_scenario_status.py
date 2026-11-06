from enum import Enum


class WorkflowScenarioStatus(str, Enum):
    ERROR = "error"
    FAILED = "failed"
    PASSED = "passed"

    def __str__(self) -> str:
        return str(self.value)
