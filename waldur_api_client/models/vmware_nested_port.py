from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VmwareNestedPort")


@_attrs_define
class VmwareNestedPort:
    """
    Attributes:
        url (str):
        uuid (UUID):
        name (str):
        mac_address (str):
        network (str):
    """

    url: str
    uuid: UUID
    name: str
    mac_address: str
    network: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        name = self.name

        mac_address = self.mac_address

        network = self.network

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "mac_address": mac_address,
                "network": network,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        mac_address = d.pop("mac_address")

        network = d.pop("network")

        vmware_nested_port = cls(
            url=url,
            uuid=uuid,
            name=name,
            mac_address=mac_address,
            network=network,
        )

        vmware_nested_port.additional_properties = d
        return vmware_nested_port

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
