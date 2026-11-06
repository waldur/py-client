from enum import Enum


class ProposalRunPhaseEnum(str, Enum):
    CLOSING = "closing"
    EXTENSION = "extension"

    def __str__(self) -> str:
        return str(self.value)
