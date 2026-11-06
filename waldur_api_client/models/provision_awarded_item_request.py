from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProvisionAwardedItemRequest")


@_attrs_define
class ProvisionAwardedItemRequest:
    """
    Attributes:
        awarded_resource_uuid (UUID): The awarded item to order again.
    """

    awarded_resource_uuid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        awarded_resource_uuid = str(self.awarded_resource_uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "awarded_resource_uuid": awarded_resource_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        awarded_resource_uuid = UUID(d.pop("awarded_resource_uuid"))

        provision_awarded_item_request = cls(
            awarded_resource_uuid=awarded_resource_uuid,
        )

        provision_awarded_item_request.additional_properties = d
        return provision_awarded_item_request

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
