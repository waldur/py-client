import json
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_stack_fixed_ip_request import OpenStackFixedIpRequest


T = TypeVar("T", bound="OpenStackPortRequest")


@_attrs_define
class OpenStackPortRequest:
    """
    Attributes:
        name (str):
        description (Union[Unset, str]):
        fixed_ips (Union[Unset, list['OpenStackFixedIpRequest']]):
        mac_address (Union[Unset, str]):
        network (Union[None, Unset, str]):
    """

    name: str
    description: Union[Unset, str] = UNSET
    fixed_ips: Union[Unset, list["OpenStackFixedIpRequest"]] = UNSET
    mac_address: Union[Unset, str] = UNSET
    network: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        fixed_ips: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fixed_ips, Unset):
            fixed_ips = []
            for fixed_ips_item_data in self.fixed_ips:
                fixed_ips_item = fixed_ips_item_data.to_dict()
                fixed_ips.append(fixed_ips_item)

        mac_address = self.mac_address

        network: Union[None, Unset, str]
        if isinstance(self.network, Unset):
            network = UNSET
        else:
            network = self.network

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if fixed_ips is not UNSET:
            field_dict["fixed_ips"] = fixed_ips
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        fixed_ips: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.fixed_ips, Unset):
            _temp_fixed_ips = []
            for fixed_ips_item_data in self.fixed_ips:
                fixed_ips_item = fixed_ips_item_data.to_dict()
                _temp_fixed_ips.append(fixed_ips_item)
            fixed_ips = (None, json.dumps(_temp_fixed_ips).encode(), "application/json")

        mac_address = (
            self.mac_address
            if isinstance(self.mac_address, Unset)
            else (None, str(self.mac_address).encode(), "text/plain")
        )

        network: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.network, Unset):
            network = UNSET
        elif isinstance(self.network, str):
            network = (None, str(self.network).encode(), "text/plain")
        else:
            network = (None, str(self.network).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if fixed_ips is not UNSET:
            field_dict["fixed_ips"] = fixed_ips
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.open_stack_fixed_ip_request import OpenStackFixedIpRequest

        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        fixed_ips = []
        _fixed_ips = d.pop("fixed_ips", UNSET)
        for fixed_ips_item_data in _fixed_ips or []:
            fixed_ips_item = OpenStackFixedIpRequest.from_dict(fixed_ips_item_data)

            fixed_ips.append(fixed_ips_item)

        mac_address = d.pop("mac_address", UNSET)

        def _parse_network(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        network = _parse_network(d.pop("network", UNSET))

        open_stack_port_request = cls(
            name=name,
            description=description,
            fixed_ips=fixed_ips,
            mac_address=mac_address,
            network=network,
        )

        open_stack_port_request.additional_properties = d
        return open_stack_port_request

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
