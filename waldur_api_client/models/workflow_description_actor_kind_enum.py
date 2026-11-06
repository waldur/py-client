from enum import Enum


class WorkflowDescriptionActorKindEnum(str, Enum):
    APPLICANT = "applicant"
    CALL_MANAGER = "call_manager"
    OFFERING_TEAM = "offering_team"
    PANEL_CHAIR = "panel_chair"
    PANEL_MEMBER = "panel_member"
    PROPOSAL_ROLE = "proposal_role"
    PROPOSAL_ROLE_LEAD = "proposal_role_lead"
    REVIEWER = "reviewer"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
