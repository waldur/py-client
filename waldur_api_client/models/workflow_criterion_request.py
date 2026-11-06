from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowCriterionRequest")


@_attrs_define
class WorkflowCriterionRequest:
    """
    Attributes:
        name (str):
        order (Union[Unset, int]):
        weight (Union[Unset, int]): The criterion's weight in a review's overall score, relative to the other criteria
            of the step.
    """

    name: str
    order: Union[Unset, int] = UNSET
    weight: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        order = self.order

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        order = d.pop("order", UNSET)

        weight = d.pop("weight", UNSET)

        workflow_criterion_request = cls(
            name=name,
            order=order,
            weight=weight,
        )

        workflow_criterion_request.additional_properties = d
        return workflow_criterion_request

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
