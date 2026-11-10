from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.set_resource_spending_limits_spending_limits import SetResourceSpendingLimitsSpendingLimits


T = TypeVar("T", bound="SetResourceSpendingLimits")


@_attrs_define
class SetResourceSpendingLimits:
    """
    Attributes:
        spending_limits (SetResourceSpendingLimitsSpendingLimits): The resource's spending limits, replacing the current
            ones: {component_type: {period: amount}}. A missing or null period clears that limit; an empty object clears
            them all.
    """

    spending_limits: "SetResourceSpendingLimitsSpendingLimits"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spending_limits = self.spending_limits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spending_limits": spending_limits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.set_resource_spending_limits_spending_limits import SetResourceSpendingLimitsSpendingLimits

        d = dict(src_dict)
        spending_limits = SetResourceSpendingLimitsSpendingLimits.from_dict(d.pop("spending_limits"))

        set_resource_spending_limits = cls(
            spending_limits=spending_limits,
        )

        set_resource_spending_limits.additional_properties = d
        return set_resource_spending_limits

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
