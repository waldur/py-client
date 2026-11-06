from enum import Enum


class TargetEnum(str, Enum):
    ASSIGNMENTS = "assignments"
    EVALUATOR_ROLES = "evaluator_roles"
    INVITATIONS = "invitations"
    OFFERING_REQUESTS = "offering_requests"
    PROPOSAL = "proposal"
    REVIEW = "review"
    ROUND = "round"
    ROUND_REPORT = "round_report"

    def __str__(self) -> str:
        return str(self.value)
