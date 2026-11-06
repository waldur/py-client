from enum import Enum


class OutcomeEnum(str, Enum):
    ACCEPTED = "accepted"
    APPROVED = "approved"
    DECLINED = "declined"
    DONE = "done"
    ELIGIBLE = "eligible"
    EXPIRED = "expired"
    FEASIBLE = "feasible"
    INELIGIBLE = "ineligible"
    INFEASIBLE = "infeasible"
    NO_RESPONSE = "no_response"
    REJECTED = "rejected"
    REVIEWED = "reviewed"
    SUBMITTED = "submitted"

    def __str__(self) -> str:
        return str(self.value)
