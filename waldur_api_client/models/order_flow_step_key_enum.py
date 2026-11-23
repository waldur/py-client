from enum import Enum


class OrderFlowStepKeyEnum(str, Enum):
    CONSUMER_REVIEW = "consumer_review"
    DONE = "done"
    EXECUTION = "execution"
    PLACED = "placed"
    PROJECT_START = "project_start"
    PROVIDER_REVIEW = "provider_review"
    START_DATE = "start_date"

    def __str__(self) -> str:
        return str(self.value)
