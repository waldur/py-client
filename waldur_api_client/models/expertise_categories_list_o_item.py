from enum import Enum


class ExpertiseCategoriesListOItem(str, Enum):
    CODE = "code"
    LEVEL = "level"
    NAME = "name"
    VALUE_0 = "-code"
    VALUE_1 = "-level"
    VALUE_2 = "-name"

    def __str__(self) -> str:
        return str(self.value)
