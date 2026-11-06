from enum import Enum


class TriggerEnum(str, Enum):
    CHANGES_REQUESTED = "changes_requested"
    CHANGES_SUBMITTED = "changes_submitted"
    CONTRIBUTION_REOPENED = "contribution_reopened"
    CONTRIBUTION_SUBMITTED = "contribution_submitted"
    DEADLINE_APPROACHING = "deadline_approaching"
    STEP_COMPLETED = "step_completed"
    STEP_EXPIRED = "step_expired"
    STEP_REJECTED = "step_rejected"
    STEP_STARTED = "step_started"

    def __str__(self) -> str:
        return str(self.value)
