from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_stack_allowed_address_pair import OpenStackAllowedAddressPair
    from ..models.open_stack_fixed_ip import OpenStackFixedIp


T = TypeVar("T", bound="OpenStackNestedPort")


@_attrs_define
class OpenStackNestedPort:
    """
    Attributes:
        fixed_ips (list['OpenStackFixedIp']):
        mac_address (str):
        subnet_uuid (UUID):
        subnet_name (str):
        subnet_description (str):
        subnet_cidr (str):
        allowed_address_pairs (list['OpenStackAllowedAddressPair']):
        device_id (Union[None, str]):
        device_owner (Union[None, str]):
        subnet (Union[None, Unset, str]):
    """

    fixed_ips: list["OpenStackFixedIp"]
    mac_address: str
    subnet_uuid: UUID
    subnet_name: str
    subnet_description: str
    subnet_cidr: str
    allowed_address_pairs: list["OpenStackAllowedAddressPair"]
    device_id: Union[None, str]
    device_owner: Union[None, str]
    subnet: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fixed_ips = []
        for fixed_ips_item_data in self.fixed_ips:
            fixed_ips_item = fixed_ips_item_data.to_dict()
            fixed_ips.append(fixed_ips_item)

        mac_address = self.mac_address

        subnet_uuid = str(self.subnet_uuid)

        subnet_name = self.subnet_name

        subnet_description = self.subnet_description

        subnet_cidr = self.subnet_cidr

        allowed_address_pairs = []
        for allowed_address_pairs_item_data in self.allowed_address_pairs:
            allowed_address_pairs_item = allowed_address_pairs_item_data.to_dict()
            allowed_address_pairs.append(allowed_address_pairs_item)

        device_id: Union[None, str]
        device_id = self.device_id

        device_owner: Union[None, str]
        device_owner = self.device_owner

        subnet: Union[None, Unset, str]
        if isinstance(self.subnet, Unset):
            subnet = UNSET
        else:
            subnet = self.subnet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fixed_ips": fixed_ips,
                "mac_address": mac_address,
                "subnet_uuid": subnet_uuid,
                "subnet_name": subnet_name,
                "subnet_description": subnet_description,
                "subnet_cidr": subnet_cidr,
                "allowed_address_pairs": allowed_address_pairs,
                "device_id": device_id,
                "device_owner": device_owner,
            }
        )
        if subnet is not UNSET:
            field_dict["subnet"] = subnet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_stack_allowed_address_pair import OpenStackAllowedAddressPair
        from ..models.open_stack_fixed_ip import OpenStackFixedIp

        d = dict(src_dict)
        fixed_ips = []
        _fixed_ips = d.pop("fixed_ips")
        for fixed_ips_item_data in _fixed_ips:
            fixed_ips_item = OpenStackFixedIp.from_dict(fixed_ips_item_data)

            fixed_ips.append(fixed_ips_item)

        mac_address = d.pop("mac_address")

        subnet_uuid = UUID(d.pop("subnet_uuid"))

        subnet_name = d.pop("subnet_name")

        subnet_description = d.pop("subnet_description")

        subnet_cidr = d.pop("subnet_cidr")

        allowed_address_pairs = []
        _allowed_address_pairs = d.pop("allowed_address_pairs")
        for allowed_address_pairs_item_data in _allowed_address_pairs:
            allowed_address_pairs_item = OpenStackAllowedAddressPair.from_dict(allowed_address_pairs_item_data)

            allowed_address_pairs.append(allowed_address_pairs_item)

        def _parse_device_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        device_id = _parse_device_id(d.pop("device_id"))

        def _parse_device_owner(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        device_owner = _parse_device_owner(d.pop("device_owner"))

        def _parse_subnet(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subnet = _parse_subnet(d.pop("subnet", UNSET))

        open_stack_nested_port = cls(
            fixed_ips=fixed_ips,
            mac_address=mac_address,
            subnet_uuid=subnet_uuid,
            subnet_name=subnet_name,
            subnet_description=subnet_description,
            subnet_cidr=subnet_cidr,
            allowed_address_pairs=allowed_address_pairs,
            device_id=device_id,
            device_owner=device_owner,
            subnet=subnet,
        )

        open_stack_nested_port.additional_properties = d
        return open_stack_nested_port

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
