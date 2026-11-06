from enum import Enum


class RecipientEnum(str, Enum):
    ALL_POOL_REVIEWERS = "all_pool_reviewers"
    APPLICANT = "applicant"
    ASSIGNED_REVIEWERS = "assigned_reviewers"
    CALL_MANAGERS = "call_managers"
    OFFERING_TEAMS = "offering_teams"
    PANEL_CHAIR = "panel_chair"
    PROPOSAL_ROLE = "proposal_role"
    PROPOSAL_ROLE_LEAD = "proposal_role_lead"
    RESPONSIBLE_ROLE = "responsible_role"

    def __str__(self) -> str:
        return str(self.value)
