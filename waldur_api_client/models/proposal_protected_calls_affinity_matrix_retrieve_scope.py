from enum import Enum


class ProposalProtectedCallsAffinityMatrixRetrieveScope(str, Enum):
    ALL = "all"
    POOL = "pool"
    SUGGESTIONS = "suggestions"

    def __str__(self) -> str:
        return str(self.value)
