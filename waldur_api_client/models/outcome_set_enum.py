from enum import Enum


class OutcomeSetEnum(str, Enum):
    ACCEPTANCE = "acceptance"
    APPROVAL = "approval"
    DONE = "done"
    ELIGIBILITY = "eligibility"
    FEASIBILITY = "feasibility"
    PER_OFFERING = "per_offering"
    REVIEWED = "reviewed"
    SUBMITTED = "submitted"

    def __str__(self) -> str:
        return str(self.value)
