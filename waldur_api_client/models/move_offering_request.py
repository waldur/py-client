from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MoveOfferingRequest")


@_attrs_define
class MoveOfferingRequest:
    """
    Attributes:
        customer (str):
        preserve_permissions (bool):
    """

    customer: str
    preserve_permissions: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer = self.customer

        preserve_permissions = self.preserve_permissions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer": customer,
                "preserve_permissions": preserve_permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer = d.pop("customer")

        preserve_permissions = d.pop("preserve_permissions")

        move_offering_request = cls(
            customer=customer,
            preserve_permissions=preserve_permissions,
        )

        move_offering_request.additional_properties = d
        return move_offering_request

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
