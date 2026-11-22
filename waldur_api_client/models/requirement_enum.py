from enum import Enum


class RequirementEnum(str, Enum):
    OPTIONAL = "optional"
    REQUIRED = "required"
    REQUIRED_WITH_PARENT = "required_with_parent"

    def __str__(self) -> str:
        return str(self.value)
