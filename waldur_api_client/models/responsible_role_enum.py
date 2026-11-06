from enum import Enum


class ResponsibleRoleEnum(str, Enum):
    APPLICANT = "applicant"
    CALL_MANAGER = "call_manager"
    OFFERING_MANAGER = "offering_manager"
    PANEL_CHAIR = "panel_chair"
    PANEL_MEMBER = "panel_member"
    PROPOSAL_ROLE = "proposal_role"
    REVIEWER = "reviewer"

    def __str__(self) -> str:
        return str(self.value)
