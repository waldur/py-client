from enum import Enum


class CallStepKindEnum(str, Enum):
    APPLICANT_ACTION = "applicant_action"
    ASSESSMENT = "assessment"
    ASSIGNMENT = "assignment"
    DECISION = "decision"

    def __str__(self) -> str:
        return str(self.value)
