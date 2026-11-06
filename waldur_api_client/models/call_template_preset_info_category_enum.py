from enum import Enum


class CallTemplatePresetInfoCategoryEnum(str, Enum):
    GENERIC = "generic"
    PROGRAMME = "programme"

    def __str__(self) -> str:
        return str(self.value)
