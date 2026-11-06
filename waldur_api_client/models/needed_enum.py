from enum import Enum


class NeededEnum(str, Enum):
    ACCEPT_AWARD = "accept_award"
    ACCEPT_DELEGATION = "accept_delegation"
    ADVANCE = "advance"
    ANSWER_ASSIGNMENT = "answer_assignment"
    ANSWER_INVITATION = "answer_invitation"
    ANSWER_OFFERING_REQUEST = "answer_offering_request"
    ASSIGN = "assign"
    COMPLETE = "complete"
    COMPLETE_ROUND_STEP = "complete_round_step"
    CONFIRM_NO_COI = "confirm_no_coi"
    CONTRIBUTE = "contribute"
    DECIDE = "decide"
    OPEN_ROUND_STEP = "open_round_step"
    RELEASE_REPORT = "release_report"
    RESPOND = "respond"
    REVIEW = "review"
    SUBMIT_CHANGES = "submit_changes"
    WRITE_ROUND_REPORT = "write_round_report"

    def __str__(self) -> str:
        return str(self.value)
