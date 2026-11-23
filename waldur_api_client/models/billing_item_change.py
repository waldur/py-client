from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_item_change_change_enum import BillingItemChangeChangeEnum

T = TypeVar("T", bound="BillingItemChange")


@_attrs_define
class BillingItemChange:
    """
    Attributes:
        uuid (str):
        name (str):
        resource_name (str):
        change (BillingItemChangeChangeEnum):
        amount_before (str):
        amount_after (str):
    """

    uuid: str
    name: str
    resource_name: str
    change: BillingItemChangeChangeEnum
    amount_before: str
    amount_after: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        name = self.name

        resource_name = self.resource_name

        change = self.change.value

        amount_before = self.amount_before

        amount_after = self.amount_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "resource_name": resource_name,
                "change": change,
                "amount_before": amount_before,
                "amount_after": amount_after,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid")

        name = d.pop("name")

        resource_name = d.pop("resource_name")

        change = BillingItemChangeChangeEnum(d.pop("change"))

        amount_before = d.pop("amount_before")

        amount_after = d.pop("amount_after")

        billing_item_change = cls(
            uuid=uuid,
            name=name,
            resource_name=resource_name,
            change=change,
            amount_before=amount_before,
            amount_after=amount_after,
        )

        billing_item_change.additional_properties = d
        return billing_item_change

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
