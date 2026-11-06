from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AllocationPlanAward")


@_attrs_define
class AllocationPlanAward:
    """
    Attributes:
        offering_name (str):
        component_type (str):
        amount (float): What the award draws from the pools: a periodic amount counted once per period the item runs.
    """

    offering_name: str
    component_type: str
    amount: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offering_name = self.offering_name

        component_type = self.component_type

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offering_name": offering_name,
                "component_type": component_type,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offering_name = d.pop("offering_name")

        component_type = d.pop("component_type")

        amount = d.pop("amount")

        allocation_plan_award = cls(
            offering_name=offering_name,
            component_type=component_type,
            amount=amount,
        )

        allocation_plan_award.additional_properties = d
        return allocation_plan_award

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
