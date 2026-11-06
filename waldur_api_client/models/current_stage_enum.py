from enum import Enum


class CurrentStageEnum(str, Enum):
    AWAITING_EVALUATION = "awaiting_evaluation"
    CALL_ARCHIVED = "call_archived"
    CALL_DRAFT = "call_draft"
    DECIDING = "deciding"
    EVALUATING = "evaluating"
    OPEN = "open"
    RESULTS_PUBLISHED = "results_published"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
