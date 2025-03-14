import json
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_stack_nested_floating_ip_request import OpenStackNestedFloatingIPRequest
    from ..models.open_stack_nested_port_request import OpenStackNestedPortRequest


T = TypeVar("T", bound="OpenStackBackupRestorationRequest")


@_attrs_define
class OpenStackBackupRestorationRequest:
    """
    Attributes:
        flavor (str):
        name (Union[Unset, str]): New instance name. Leave blank to use source instance name.
        floating_ips (Union[Unset, list['OpenStackNestedFloatingIPRequest']]):
        ports (Union[Unset, list['OpenStackNestedPortRequest']]):
    """

    flavor: str
    name: Union[Unset, str] = UNSET
    floating_ips: Union[Unset, list["OpenStackNestedFloatingIPRequest"]] = UNSET
    ports: Union[Unset, list["OpenStackNestedPortRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flavor = self.flavor

        name = self.name

        floating_ips: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.floating_ips, Unset):
            floating_ips = []
            for floating_ips_item_data in self.floating_ips:
                floating_ips_item = floating_ips_item_data.to_dict()
                floating_ips.append(floating_ips_item)

        ports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "flavor": flavor,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if floating_ips is not UNSET:
            field_dict["floating_ips"] = floating_ips
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        flavor = (None, str(self.flavor).encode(), "text/plain")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        floating_ips: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.floating_ips, Unset):
            _temp_floating_ips = []
            for floating_ips_item_data in self.floating_ips:
                floating_ips_item = floating_ips_item_data.to_dict()
                _temp_floating_ips.append(floating_ips_item)
            floating_ips = (None, json.dumps(_temp_floating_ips).encode(), "application/json")

        ports: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.ports, Unset):
            _temp_ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                _temp_ports.append(ports_item)
            ports = (None, json.dumps(_temp_ports).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "flavor": flavor,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if floating_ips is not UNSET:
            field_dict["floating_ips"] = floating_ips
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.open_stack_nested_floating_ip_request import OpenStackNestedFloatingIPRequest
        from ..models.open_stack_nested_port_request import OpenStackNestedPortRequest

        d = src_dict.copy()
        flavor = d.pop("flavor")

        name = d.pop("name", UNSET)

        floating_ips = []
        _floating_ips = d.pop("floating_ips", UNSET)
        for floating_ips_item_data in _floating_ips or []:
            floating_ips_item = OpenStackNestedFloatingIPRequest.from_dict(floating_ips_item_data)

            floating_ips.append(floating_ips_item)

        ports = []
        _ports = d.pop("ports", UNSET)
        for ports_item_data in _ports or []:
            ports_item = OpenStackNestedPortRequest.from_dict(ports_item_data)

            ports.append(ports_item)

        open_stack_backup_restoration_request = cls(
            flavor=flavor,
            name=name,
            floating_ips=floating_ips,
            ports=ports,
        )

        open_stack_backup_restoration_request.additional_properties = d
        return open_stack_backup_restoration_request

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
