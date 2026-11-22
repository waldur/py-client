from enum import Enum


class RecipientsEnum(str, Enum):
    APPLICANT = "applicant"
    REVIEWERS = "reviewers"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
