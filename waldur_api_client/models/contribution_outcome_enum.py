from enum import Enum


class ContributionOutcomeEnum(str, Enum):
    ACCEPTED = "accepted"
    CONDITIONALLY_ACCEPTED = "conditionally_accepted"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
