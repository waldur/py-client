from enum import Enum


class ConflictsOfInterestListSeverity(str, Enum):
    APPARENT = "apparent"
    POTENTIAL = "potential"
    REAL = "real"

    def __str__(self) -> str:
        return str(self.value)
