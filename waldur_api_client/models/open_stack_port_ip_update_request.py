from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OpenStackPortIPUpdateRequest")


@_attrs_define
class OpenStackPortIPUpdateRequest:
    """
    Attributes:
        subnet (str):
        ip_address (str):
    """

    subnet: str
    ip_address: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subnet = self.subnet

        ip_address = self.ip_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subnet": subnet,
                "ip_address": ip_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subnet = d.pop("subnet")

        ip_address = d.pop("ip_address")

        open_stack_port_ip_update_request = cls(
            subnet=subnet,
            ip_address=ip_address,
        )

        open_stack_port_ip_update_request.additional_properties = d
        return open_stack_port_ip_update_request

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
