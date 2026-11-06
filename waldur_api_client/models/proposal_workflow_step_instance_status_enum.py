from enum import Enum


class ProposalWorkflowStepInstanceStatusEnum(str, Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    EXPIRED = "expired"
    PENDING = "pending"
    SKIPPED = "skipped"
    WITHDRAWN = "withdrawn"

    def __str__(self) -> str:
        return str(self.value)
