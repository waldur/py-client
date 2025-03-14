from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.open_stack_fixed_ip import OpenStackFixedIp


T = TypeVar("T", bound="OpenStackNestedFloatingIP")


@_attrs_define
class OpenStackNestedFloatingIP:
    """
    Attributes:
        url (str):
        uuid (UUID):
        address (Union[None, str]):
        port_fixed_ips (list['OpenStackFixedIp']):
        port_mac_address (str):
        subnet (str):
        subnet_uuid (UUID):
        subnet_name (str):
        subnet_description (str):
        subnet_cidr (str):
    """

    url: str
    uuid: UUID
    address: Union[None, str]
    port_fixed_ips: list["OpenStackFixedIp"]
    port_mac_address: str
    subnet: str
    subnet_uuid: UUID
    subnet_name: str
    subnet_description: str
    subnet_cidr: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        address: Union[None, str]
        address = self.address

        port_fixed_ips = []
        for port_fixed_ips_item_data in self.port_fixed_ips:
            port_fixed_ips_item = port_fixed_ips_item_data.to_dict()
            port_fixed_ips.append(port_fixed_ips_item)

        port_mac_address = self.port_mac_address

        subnet = self.subnet

        subnet_uuid = str(self.subnet_uuid)

        subnet_name = self.subnet_name

        subnet_description = self.subnet_description

        subnet_cidr = self.subnet_cidr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "address": address,
                "port_fixed_ips": port_fixed_ips,
                "port_mac_address": port_mac_address,
                "subnet": subnet,
                "subnet_uuid": subnet_uuid,
                "subnet_name": subnet_name,
                "subnet_description": subnet_description,
                "subnet_cidr": subnet_cidr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.open_stack_fixed_ip import OpenStackFixedIp

        d = src_dict.copy()
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        def _parse_address(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        address = _parse_address(d.pop("address"))

        port_fixed_ips = []
        _port_fixed_ips = d.pop("port_fixed_ips")
        for port_fixed_ips_item_data in _port_fixed_ips:
            port_fixed_ips_item = OpenStackFixedIp.from_dict(port_fixed_ips_item_data)

            port_fixed_ips.append(port_fixed_ips_item)

        port_mac_address = d.pop("port_mac_address")

        subnet = d.pop("subnet")

        subnet_uuid = UUID(d.pop("subnet_uuid"))

        subnet_name = d.pop("subnet_name")

        subnet_description = d.pop("subnet_description")

        subnet_cidr = d.pop("subnet_cidr")

        open_stack_nested_floating_ip = cls(
            url=url,
            uuid=uuid,
            address=address,
            port_fixed_ips=port_fixed_ips,
            port_mac_address=port_mac_address,
            subnet=subnet,
            subnet_uuid=subnet_uuid,
            subnet_name=subnet_name,
            subnet_description=subnet_description,
            subnet_cidr=subnet_cidr,
        )

        open_stack_nested_floating_ip.additional_properties = d
        return open_stack_nested_floating_ip

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
