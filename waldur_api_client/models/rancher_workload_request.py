from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RancherWorkloadRequest")


@_attrs_define
class RancherWorkloadRequest:
    """
    Attributes:
        name (str):
        scale (int):
        runtime_state (Union[Unset, str]):
        cluster (Union[None, Unset, str]):
        project (Union[None, Unset, str]):
        namespace (Union[None, Unset, str]):
    """

    name: str
    scale: int
    runtime_state: Union[Unset, str] = UNSET
    cluster: Union[None, Unset, str] = UNSET
    project: Union[None, Unset, str] = UNSET
    namespace: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scale = self.scale

        runtime_state = self.runtime_state

        cluster: Union[None, Unset, str]
        if isinstance(self.cluster, Unset):
            cluster = UNSET
        else:
            cluster = self.cluster

        project: Union[None, Unset, str]
        if isinstance(self.project, Unset):
            project = UNSET
        else:
            project = self.project

        namespace: Union[None, Unset, str]
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "scale": scale,
            }
        )
        if runtime_state is not UNSET:
            field_dict["runtime_state"] = runtime_state
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if project is not UNSET:
            field_dict["project"] = project
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        scale = (None, str(self.scale).encode(), "text/plain")

        runtime_state = (
            self.runtime_state
            if isinstance(self.runtime_state, Unset)
            else (None, str(self.runtime_state).encode(), "text/plain")
        )

        cluster: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.cluster, Unset):
            cluster = UNSET
        elif isinstance(self.cluster, str):
            cluster = (None, str(self.cluster).encode(), "text/plain")
        else:
            cluster = (None, str(self.cluster).encode(), "text/plain")

        project: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.project, Unset):
            project = UNSET
        elif isinstance(self.project, str):
            project = (None, str(self.project).encode(), "text/plain")
        else:
            project = (None, str(self.project).encode(), "text/plain")

        namespace: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.namespace, Unset):
            namespace = UNSET
        elif isinstance(self.namespace, str):
            namespace = (None, str(self.namespace).encode(), "text/plain")
        else:
            namespace = (None, str(self.namespace).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
                "scale": scale,
            }
        )
        if runtime_state is not UNSET:
            field_dict["runtime_state"] = runtime_state
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if project is not UNSET:
            field_dict["project"] = project
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        scale = d.pop("scale")

        runtime_state = d.pop("runtime_state", UNSET)

        def _parse_cluster(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cluster = _parse_cluster(d.pop("cluster", UNSET))

        def _parse_project(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        project = _parse_project(d.pop("project", UNSET))

        def _parse_namespace(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        rancher_workload_request = cls(
            name=name,
            scale=scale,
            runtime_state=runtime_state,
            cluster=cluster,
            project=project,
            namespace=namespace,
        )

        rancher_workload_request.additional_properties = d
        return rancher_workload_request

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
