from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OfferingDemandPool")


@_attrs_define
class OfferingDemandPool:
    """
    Attributes:
        offered (float):
        awarded (float):
        remaining (float):
    """

    offered: float
    awarded: float
    remaining: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offered = self.offered

        awarded = self.awarded

        remaining = self.remaining

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offered": offered,
                "awarded": awarded,
                "remaining": remaining,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offered = d.pop("offered")

        awarded = d.pop("awarded")

        remaining = d.pop("remaining")

        offering_demand_pool = cls(
            offered=offered,
            awarded=awarded,
            remaining=remaining,
        )

        offering_demand_pool.additional_properties = d
        return offering_demand_pool

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
