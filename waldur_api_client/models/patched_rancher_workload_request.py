from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRancherWorkloadRequest")


@_attrs_define
class PatchedRancherWorkloadRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        runtime_state (Union[Unset, str]):
        cluster (Union[None, Unset, str]):
        project (Union[None, Unset, str]):
        namespace (Union[None, Unset, str]):
        scale (Union[Unset, int]):
    """

    name: Union[Unset, str] = UNSET
    runtime_state: Union[Unset, str] = UNSET
    cluster: Union[None, Unset, str] = UNSET
    project: Union[None, Unset, str] = UNSET
    namespace: Union[None, Unset, str] = UNSET
    scale: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

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

        scale = self.scale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if runtime_state is not UNSET:
            field_dict["runtime_state"] = runtime_state
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if project is not UNSET:
            field_dict["project"] = project
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if scale is not UNSET:
            field_dict["scale"] = scale

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

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

        scale = self.scale if isinstance(self.scale, Unset) else (None, str(self.scale).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if runtime_state is not UNSET:
            field_dict["runtime_state"] = runtime_state
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if project is not UNSET:
            field_dict["project"] = project
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if scale is not UNSET:
            field_dict["scale"] = scale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

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

        scale = d.pop("scale", UNSET)

        patched_rancher_workload_request = cls(
            name=name,
            runtime_state=runtime_state,
            cluster=cluster,
            project=project,
            namespace=namespace,
            scale=scale,
        )

        patched_rancher_workload_request.additional_properties = d
        return patched_rancher_workload_request

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
