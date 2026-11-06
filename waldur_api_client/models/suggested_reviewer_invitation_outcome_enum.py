from enum import Enum


class SuggestedReviewerInvitationOutcomeEnum(str, Enum):
    INVITED = "invited"
    LINKED = "linked"
    REFUSED = "refused"
    RESENT = "resent"

    def __str__(self) -> str:
        return str(self.value)
