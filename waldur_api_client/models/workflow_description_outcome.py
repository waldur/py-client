from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.polarity_enum import PolarityEnum

T = TypeVar("T", bound="WorkflowDescriptionOutcome")


@_attrs_define
class WorkflowDescriptionOutcome:
    """
    Attributes:
        value (str):
        polarity (PolarityEnum):
    """

    value: str
    polarity: PolarityEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        polarity = self.polarity.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "polarity": polarity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        polarity = PolarityEnum(d.pop("polarity"))

        workflow_description_outcome = cls(
            value=value,
            polarity=polarity,
        )

        workflow_description_outcome.additional_properties = d
        return workflow_description_outcome

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
