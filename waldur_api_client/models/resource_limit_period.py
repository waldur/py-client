from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResourceLimitPeriod")


@_attrs_define
class ResourceLimitPeriod:
    """
    Attributes:
        start (str):
        end (str):
        quantity (int):
        billing_periods (int):
        total (str):
    """

    start: str
    end: str
    quantity: int
    billing_periods: int
    total: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        quantity = self.quantity

        billing_periods = self.billing_periods

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "quantity": quantity,
                "billing_periods": billing_periods,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = d.pop("start")

        end = d.pop("end")

        quantity = d.pop("quantity")

        billing_periods = d.pop("billing_periods")

        total = d.pop("total")

        resource_limit_period = cls(
            start=start,
            end=end,
            quantity=quantity,
            billing_periods=billing_periods,
            total=total,
        )

        resource_limit_period.additional_properties = d
        return resource_limit_period

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
