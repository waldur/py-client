from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenStackPortFloatingIp")


@_attrs_define
class OpenStackPortFloatingIp:
    """
    Attributes:
        uuid (Union[Unset, UUID]):
        address (Union[None, Unset, str]): The public IPv4 address of the floating IP
        external_address (Union[None, Unset, str]): Optional address that maps to floating IP's address in external
            networks
    """

    uuid: Union[Unset, UUID] = UNSET
    address: Union[None, Unset, str] = UNSET
    external_address: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: Union[Unset, str] = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        external_address: Union[None, Unset, str]
        if isinstance(self.external_address, Unset):
            external_address = UNSET
        else:
            external_address = self.external_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if address is not UNSET:
            field_dict["address"] = address
        if external_address is not UNSET:
            field_dict["external_address"] = external_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: Union[Unset, UUID]
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_external_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_address = _parse_external_address(d.pop("external_address", UNSET))

        open_stack_port_floating_ip = cls(
            uuid=uuid,
            address=address,
            external_address=external_address,
        )

        open_stack_port_floating_ip.additional_properties = d
        return open_stack_port_floating_ip

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
