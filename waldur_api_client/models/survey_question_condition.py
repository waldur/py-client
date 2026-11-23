from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checklist_operators import ChecklistOperators

T = TypeVar("T", bound="SurveyQuestionCondition")


@_attrs_define
class SurveyQuestionCondition:
    """
    Attributes:
        depends_on (str): Key of the question it depends on.
        operator (ChecklistOperators):
        required_answer_value (Any): For a select question, option keys instead of option UUIDs.
    """

    depends_on: str
    operator: ChecklistOperators
    required_answer_value: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        depends_on = self.depends_on

        operator = self.operator.value

        required_answer_value = self.required_answer_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "depends_on": depends_on,
                "operator": operator,
                "required_answer_value": required_answer_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        depends_on = d.pop("depends_on")

        operator = ChecklistOperators(d.pop("operator"))

        required_answer_value = d.pop("required_answer_value")

        survey_question_condition = cls(
            depends_on=depends_on,
            operator=operator,
            required_answer_value=required_answer_value,
        )

        survey_question_condition.additional_properties = d
        return survey_question_condition

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
