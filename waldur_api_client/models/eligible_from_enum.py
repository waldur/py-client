from enum import Enum


class EligibleFromEnum(str, Enum):
    ANY_USER = "any_user"
    CALL_ROLEMANAGER = "call_role:manager"
    CALL_ROLEPANEL_MEMBER = "call_role:panel_member"
    CALL_ROLEREVIEWER = "call_role:reviewer"
    PANELCHAIR = "panel:chair"
    PANELMEMBER = "panel:member"
    PROPOSAL_REVIEWERS = "proposal_reviewers"

    def __str__(self) -> str:
        return str(self.value)
