from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_stack_nested_floating_ip_request import OpenStackNestedFloatingIPRequest
    from ..models.open_stack_nested_port_request import OpenStackNestedPortRequest


T = TypeVar("T", bound="OpenStackInstanceCreateOrderAttributes")


@_attrs_define
class OpenStackInstanceCreateOrderAttributes:
    """This mixin allows to specify list of fields to be rendered by serializer.
    It expects that request is available in serializer's context.

        Attributes:
            name (str):
            flavor (str):
            image (str):
            ports (list['OpenStackNestedPortRequest']):
            system_volume_size (int):
            description (Union[Unset, str]):
            floating_ips (Union[Unset, list['OpenStackNestedFloatingIPRequest']]):
            system_volume_type (Union[None, Unset, str]):
            data_volume_size (Union[Unset, int]):
            data_volume_type (Union[None, Unset, str]):
            ssh_public_key (Union[Unset, str]):
            user_data (Union[Unset, str]): Additional data that will be added to instance on provisioning
            availability_zone (Union[None, Unset, str]):
            connect_directly_to_external_network (Union[Unset, bool]):
    """

    name: str
    flavor: str
    image: str
    ports: list["OpenStackNestedPortRequest"]
    system_volume_size: int
    description: Union[Unset, str] = UNSET
    floating_ips: Union[Unset, list["OpenStackNestedFloatingIPRequest"]] = UNSET
    system_volume_type: Union[None, Unset, str] = UNSET
    data_volume_size: Union[Unset, int] = UNSET
    data_volume_type: Union[None, Unset, str] = UNSET
    ssh_public_key: Union[Unset, str] = UNSET
    user_data: Union[Unset, str] = UNSET
    availability_zone: Union[None, Unset, str] = UNSET
    connect_directly_to_external_network: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        flavor = self.flavor

        image = self.image

        ports = []
        for ports_item_data in self.ports:
            ports_item = ports_item_data.to_dict()
            ports.append(ports_item)

        system_volume_size = self.system_volume_size

        description = self.description

        floating_ips: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.floating_ips, Unset):
            floating_ips = []
            for floating_ips_item_data in self.floating_ips:
                floating_ips_item = floating_ips_item_data.to_dict()
                floating_ips.append(floating_ips_item)

        system_volume_type: Union[None, Unset, str]
        if isinstance(self.system_volume_type, Unset):
            system_volume_type = UNSET
        else:
            system_volume_type = self.system_volume_type

        data_volume_size = self.data_volume_size

        data_volume_type: Union[None, Unset, str]
        if isinstance(self.data_volume_type, Unset):
            data_volume_type = UNSET
        else:
            data_volume_type = self.data_volume_type

        ssh_public_key = self.ssh_public_key

        user_data = self.user_data

        availability_zone: Union[None, Unset, str]
        if isinstance(self.availability_zone, Unset):
            availability_zone = UNSET
        else:
            availability_zone = self.availability_zone

        connect_directly_to_external_network = self.connect_directly_to_external_network

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "flavor": flavor,
                "image": image,
                "ports": ports,
                "system_volume_size": system_volume_size,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if floating_ips is not UNSET:
            field_dict["floating_ips"] = floating_ips
        if system_volume_type is not UNSET:
            field_dict["system_volume_type"] = system_volume_type
        if data_volume_size is not UNSET:
            field_dict["data_volume_size"] = data_volume_size
        if data_volume_type is not UNSET:
            field_dict["data_volume_type"] = data_volume_type
        if ssh_public_key is not UNSET:
            field_dict["ssh_public_key"] = ssh_public_key
        if user_data is not UNSET:
            field_dict["user_data"] = user_data
        if availability_zone is not UNSET:
            field_dict["availability_zone"] = availability_zone
        if connect_directly_to_external_network is not UNSET:
            field_dict["connect_directly_to_external_network"] = connect_directly_to_external_network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_stack_nested_floating_ip_request import OpenStackNestedFloatingIPRequest
        from ..models.open_stack_nested_port_request import OpenStackNestedPortRequest

        d = dict(src_dict)
        name = d.pop("name")

        flavor = d.pop("flavor")

        image = d.pop("image")

        ports = []
        _ports = d.pop("ports")
        for ports_item_data in _ports:
            ports_item = OpenStackNestedPortRequest.from_dict(ports_item_data)

            ports.append(ports_item)

        system_volume_size = d.pop("system_volume_size")

        description = d.pop("description", UNSET)

        floating_ips = []
        _floating_ips = d.pop("floating_ips", UNSET)
        for floating_ips_item_data in _floating_ips or []:
            floating_ips_item = OpenStackNestedFloatingIPRequest.from_dict(floating_ips_item_data)

            floating_ips.append(floating_ips_item)

        def _parse_system_volume_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        system_volume_type = _parse_system_volume_type(d.pop("system_volume_type", UNSET))

        data_volume_size = d.pop("data_volume_size", UNSET)

        def _parse_data_volume_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        data_volume_type = _parse_data_volume_type(d.pop("data_volume_type", UNSET))

        ssh_public_key = d.pop("ssh_public_key", UNSET)

        user_data = d.pop("user_data", UNSET)

        def _parse_availability_zone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        availability_zone = _parse_availability_zone(d.pop("availability_zone", UNSET))

        connect_directly_to_external_network = d.pop("connect_directly_to_external_network", UNSET)

        open_stack_instance_create_order_attributes = cls(
            name=name,
            flavor=flavor,
            image=image,
            ports=ports,
            system_volume_size=system_volume_size,
            description=description,
            floating_ips=floating_ips,
            system_volume_type=system_volume_type,
            data_volume_size=data_volume_size,
            data_volume_type=data_volume_type,
            ssh_public_key=ssh_public_key,
            user_data=user_data,
            availability_zone=availability_zone,
            connect_directly_to_external_network=connect_directly_to_external_network,
        )

        open_stack_instance_create_order_attributes.additional_properties = d
        return open_stack_instance_create_order_attributes

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
