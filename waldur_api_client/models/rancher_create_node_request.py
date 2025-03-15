import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.roles_enum import RolesEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_volume_request import DataVolumeRequest


T = TypeVar("T", bound="RancherCreateNodeRequest")


@_attrs_define
class RancherCreateNodeRequest:
    """
    Attributes:
        cluster (str):
        roles (list[RolesEnum]):
        subnet (Union[None, str]):
        system_volume_size (Union[Unset, int]):
        system_volume_type (Union[None, Unset, str]):
        memory (Union[Unset, int]):
        cpu (Union[Unset, int]):
        flavor (Union[None, Unset, str]):
        data_volumes (Union[Unset, list['DataVolumeRequest']]):
        ssh_public_key (Union[Unset, str]):
    """

    cluster: str
    roles: list[RolesEnum]
    subnet: Union[None, str]
    system_volume_size: Union[Unset, int] = UNSET
    system_volume_type: Union[None, Unset, str] = UNSET
    memory: Union[Unset, int] = UNSET
    cpu: Union[Unset, int] = UNSET
    flavor: Union[None, Unset, str] = UNSET
    data_volumes: Union[Unset, list["DataVolumeRequest"]] = UNSET
    ssh_public_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.value
            roles.append(roles_item)

        subnet: Union[None, str]
        subnet = self.subnet

        system_volume_size = self.system_volume_size

        system_volume_type: Union[None, Unset, str]
        if isinstance(self.system_volume_type, Unset):
            system_volume_type = UNSET
        else:
            system_volume_type = self.system_volume_type

        memory = self.memory

        cpu = self.cpu

        flavor: Union[None, Unset, str]
        if isinstance(self.flavor, Unset):
            flavor = UNSET
        else:
            flavor = self.flavor

        data_volumes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_volumes, Unset):
            data_volumes = []
            for data_volumes_item_data in self.data_volumes:
                data_volumes_item = data_volumes_item_data.to_dict()
                data_volumes.append(data_volumes_item)

        ssh_public_key = self.ssh_public_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cluster": cluster,
                "roles": roles,
                "subnet": subnet,
            }
        )
        if system_volume_size is not UNSET:
            field_dict["system_volume_size"] = system_volume_size
        if system_volume_type is not UNSET:
            field_dict["system_volume_type"] = system_volume_type
        if memory is not UNSET:
            field_dict["memory"] = memory
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if flavor is not UNSET:
            field_dict["flavor"] = flavor
        if data_volumes is not UNSET:
            field_dict["data_volumes"] = data_volumes
        if ssh_public_key is not UNSET:
            field_dict["ssh_public_key"] = ssh_public_key

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        cluster = (None, str(self.cluster).encode(), "text/plain")

        _temp_roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.value
            _temp_roles.append(roles_item)
        roles = (None, json.dumps(_temp_roles).encode(), "application/json")

        subnet: tuple[None, bytes, str]

        if isinstance(self.subnet, str):
            subnet = (None, str(self.subnet).encode(), "text/plain")
        else:
            subnet = (None, str(self.subnet).encode(), "text/plain")

        system_volume_size = (
            self.system_volume_size
            if isinstance(self.system_volume_size, Unset)
            else (None, str(self.system_volume_size).encode(), "text/plain")
        )

        system_volume_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.system_volume_type, Unset):
            system_volume_type = UNSET
        elif isinstance(self.system_volume_type, str):
            system_volume_type = (None, str(self.system_volume_type).encode(), "text/plain")
        else:
            system_volume_type = (None, str(self.system_volume_type).encode(), "text/plain")

        memory = self.memory if isinstance(self.memory, Unset) else (None, str(self.memory).encode(), "text/plain")

        cpu = self.cpu if isinstance(self.cpu, Unset) else (None, str(self.cpu).encode(), "text/plain")

        flavor: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.flavor, Unset):
            flavor = UNSET
        elif isinstance(self.flavor, str):
            flavor = (None, str(self.flavor).encode(), "text/plain")
        else:
            flavor = (None, str(self.flavor).encode(), "text/plain")

        data_volumes: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.data_volumes, Unset):
            _temp_data_volumes = []
            for data_volumes_item_data in self.data_volumes:
                data_volumes_item = data_volumes_item_data.to_dict()
                _temp_data_volumes.append(data_volumes_item)
            data_volumes = (None, json.dumps(_temp_data_volumes).encode(), "application/json")

        ssh_public_key = (
            self.ssh_public_key
            if isinstance(self.ssh_public_key, Unset)
            else (None, str(self.ssh_public_key).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "cluster": cluster,
                "roles": roles,
                "subnet": subnet,
            }
        )
        if system_volume_size is not UNSET:
            field_dict["system_volume_size"] = system_volume_size
        if system_volume_type is not UNSET:
            field_dict["system_volume_type"] = system_volume_type
        if memory is not UNSET:
            field_dict["memory"] = memory
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if flavor is not UNSET:
            field_dict["flavor"] = flavor
        if data_volumes is not UNSET:
            field_dict["data_volumes"] = data_volumes
        if ssh_public_key is not UNSET:
            field_dict["ssh_public_key"] = ssh_public_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_volume_request import DataVolumeRequest

        d = dict(src_dict)
        cluster = d.pop("cluster")

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = RolesEnum(roles_item_data)

            roles.append(roles_item)

        def _parse_subnet(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        subnet = _parse_subnet(d.pop("subnet"))

        system_volume_size = d.pop("system_volume_size", UNSET)

        def _parse_system_volume_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        system_volume_type = _parse_system_volume_type(d.pop("system_volume_type", UNSET))

        memory = d.pop("memory", UNSET)

        cpu = d.pop("cpu", UNSET)

        def _parse_flavor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        flavor = _parse_flavor(d.pop("flavor", UNSET))

        data_volumes = []
        _data_volumes = d.pop("data_volumes", UNSET)
        for data_volumes_item_data in _data_volumes or []:
            data_volumes_item = DataVolumeRequest.from_dict(data_volumes_item_data)

            data_volumes.append(data_volumes_item)

        ssh_public_key = d.pop("ssh_public_key", UNSET)

        rancher_create_node_request = cls(
            cluster=cluster,
            roles=roles,
            subnet=subnet,
            system_volume_size=system_volume_size,
            system_volume_type=system_volume_type,
            memory=memory,
            cpu=cpu,
            flavor=flavor,
            data_volumes=data_volumes,
            ssh_public_key=ssh_public_key,
        )

        rancher_create_node_request.additional_properties = d
        return rancher_create_node_request

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
