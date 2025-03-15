import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rancher_nested_node_request import RancherNestedNodeRequest


T = TypeVar("T", bound="RancherClusterRequest")


@_attrs_define
class RancherClusterRequest:
    """
    Attributes:
        name (str):
        service_settings (str):
        project (str):
        nodes (list['RancherNestedNodeRequest']):
        tenant (str):
        description (Union[Unset, str]):
        ssh_public_key (Union[Unset, str]):
        install_longhorn (Union[Unset, bool]): Longhorn is a distributed block storage deployed on top of Kubernetes
            cluster Default: False.
    """

    name: str
    service_settings: str
    project: str
    nodes: list["RancherNestedNodeRequest"]
    tenant: str
    description: Union[Unset, str] = UNSET
    ssh_public_key: Union[Unset, str] = UNSET
    install_longhorn: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        service_settings = self.service_settings

        project = self.project

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        tenant = self.tenant

        description = self.description

        ssh_public_key = self.ssh_public_key

        install_longhorn = self.install_longhorn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "service_settings": service_settings,
                "project": project,
                "nodes": nodes,
                "tenant": tenant,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if ssh_public_key is not UNSET:
            field_dict["ssh_public_key"] = ssh_public_key
        if install_longhorn is not UNSET:
            field_dict["install_longhorn"] = install_longhorn

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        service_settings = (None, str(self.service_settings).encode(), "text/plain")

        project = (None, str(self.project).encode(), "text/plain")

        _temp_nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            _temp_nodes.append(nodes_item)
        nodes = (None, json.dumps(_temp_nodes).encode(), "application/json")

        tenant = (None, str(self.tenant).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        ssh_public_key = (
            self.ssh_public_key
            if isinstance(self.ssh_public_key, Unset)
            else (None, str(self.ssh_public_key).encode(), "text/plain")
        )

        install_longhorn = (
            self.install_longhorn
            if isinstance(self.install_longhorn, Unset)
            else (None, str(self.install_longhorn).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
                "service_settings": service_settings,
                "project": project,
                "nodes": nodes,
                "tenant": tenant,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if ssh_public_key is not UNSET:
            field_dict["ssh_public_key"] = ssh_public_key
        if install_longhorn is not UNSET:
            field_dict["install_longhorn"] = install_longhorn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rancher_nested_node_request import RancherNestedNodeRequest

        d = dict(src_dict)
        name = d.pop("name")

        service_settings = d.pop("service_settings")

        project = d.pop("project")

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = RancherNestedNodeRequest.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        tenant = d.pop("tenant")

        description = d.pop("description", UNSET)

        ssh_public_key = d.pop("ssh_public_key", UNSET)

        install_longhorn = d.pop("install_longhorn", UNSET)

        rancher_cluster_request = cls(
            name=name,
            service_settings=service_settings,
            project=project,
            nodes=nodes,
            tenant=tenant,
            description=description,
            ssh_public_key=ssh_public_key,
            install_longhorn=install_longhorn,
        )

        rancher_cluster_request.additional_properties = d
        return rancher_cluster_request

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
