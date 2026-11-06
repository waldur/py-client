from enum import Enum


class ViewEnum(str, Enum):
    APPLICANT = "applicant"
    CALL_TEAM = "call_team"
    OFFERING_TEAM = "offering_team"
    PARTICIPANT = "participant"

    def __str__(self) -> str:
        return str(self.value)
