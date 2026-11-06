from enum import Enum


class RecipientsEnum(str, Enum):
    APPLICANT = "applicant"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
