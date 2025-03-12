from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.roles_enum import RolesEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_volume_request import DataVolumeRequest


T = TypeVar("T", bound="RancherNestedNodeRequest")


@_attrs_define
class RancherNestedNodeRequest:
    """
    Attributes:
        subnet (Union[None, str]):
        roles (list[RolesEnum]):
        flavor (Union[None, Unset, str]):
        system_volume_size (Union[Unset, int]):
        system_volume_type (Union[None, Unset, str]):
        data_volumes (Union[Unset, list['DataVolumeRequest']]):
        memory (Union[Unset, int]):
        cpu (Union[Unset, int]):
        error_traceback (Union[Unset, str]):
        backend_id (Union[Unset, str]):
        controlplane_role (Union[Unset, bool]):
    """

    subnet: Union[None, str]
    roles: list[RolesEnum]
    flavor: Union[None, Unset, str] = UNSET
    system_volume_size: Union[Unset, int] = UNSET
    system_volume_type: Union[None, Unset, str] = UNSET
    data_volumes: Union[Unset, list["DataVolumeRequest"]] = UNSET
    memory: Union[Unset, int] = UNSET
    cpu: Union[Unset, int] = UNSET
    error_traceback: Union[Unset, str] = UNSET
    backend_id: Union[Unset, str] = UNSET
    controlplane_role: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subnet: Union[None, str]
        subnet = self.subnet

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.value
            roles.append(roles_item)

        flavor: Union[None, Unset, str]
        if isinstance(self.flavor, Unset):
            flavor = UNSET
        else:
            flavor = self.flavor

        system_volume_size = self.system_volume_size

        system_volume_type: Union[None, Unset, str]
        if isinstance(self.system_volume_type, Unset):
            system_volume_type = UNSET
        else:
            system_volume_type = self.system_volume_type

        data_volumes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_volumes, Unset):
            data_volumes = []
            for data_volumes_item_data in self.data_volumes:
                data_volumes_item = data_volumes_item_data.to_dict()
                data_volumes.append(data_volumes_item)

        memory = self.memory

        cpu = self.cpu

        error_traceback = self.error_traceback

        backend_id = self.backend_id

        controlplane_role = self.controlplane_role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subnet": subnet,
                "roles": roles,
            }
        )
        if flavor is not UNSET:
            field_dict["flavor"] = flavor
        if system_volume_size is not UNSET:
            field_dict["system_volume_size"] = system_volume_size
        if system_volume_type is not UNSET:
            field_dict["system_volume_type"] = system_volume_type
        if data_volumes is not UNSET:
            field_dict["data_volumes"] = data_volumes
        if memory is not UNSET:
            field_dict["memory"] = memory
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if error_traceback is not UNSET:
            field_dict["error_traceback"] = error_traceback
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if controlplane_role is not UNSET:
            field_dict["controlplane_role"] = controlplane_role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_volume_request import DataVolumeRequest

        d = src_dict.copy()

        def _parse_subnet(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        subnet = _parse_subnet(d.pop("subnet"))

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = RolesEnum(roles_item_data)

            roles.append(roles_item)

        def _parse_flavor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        flavor = _parse_flavor(d.pop("flavor", UNSET))

        system_volume_size = d.pop("system_volume_size", UNSET)

        def _parse_system_volume_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        system_volume_type = _parse_system_volume_type(d.pop("system_volume_type", UNSET))

        data_volumes = []
        _data_volumes = d.pop("data_volumes", UNSET)
        for data_volumes_item_data in _data_volumes or []:
            data_volumes_item = DataVolumeRequest.from_dict(data_volumes_item_data)

            data_volumes.append(data_volumes_item)

        memory = d.pop("memory", UNSET)

        cpu = d.pop("cpu", UNSET)

        error_traceback = d.pop("error_traceback", UNSET)

        backend_id = d.pop("backend_id", UNSET)

        controlplane_role = d.pop("controlplane_role", UNSET)

        rancher_nested_node_request = cls(
            subnet=subnet,
            roles=roles,
            flavor=flavor,
            system_volume_size=system_volume_size,
            system_volume_type=system_volume_type,
            data_volumes=data_volumes,
            memory=memory,
            cpu=cpu,
            error_traceback=error_traceback,
            backend_id=backend_id,
            controlplane_role=controlplane_role,
        )

        rancher_nested_node_request.additional_properties = d
        return rancher_nested_node_request

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
