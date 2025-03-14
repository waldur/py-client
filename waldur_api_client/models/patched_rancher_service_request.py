import json
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rancher_nested_workload_request import RancherNestedWorkloadRequest


T = TypeVar("T", bound="PatchedRancherServiceRequest")


@_attrs_define
class PatchedRancherServiceRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        service_settings (Union[Unset, str]):
        project (Union[Unset, str]):
        error_message (Union[Unset, str]):
        error_traceback (Union[Unset, str]):
        backend_id (Union[Unset, str]):
        runtime_state (Union[Unset, str]):
        namespace (Union[Unset, str]):
        cluster_ip (Union[None, Unset, str]):
        selector (Union[Unset, Any]):
        target_workloads (Union[Unset, list['RancherNestedWorkloadRequest']]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    service_settings: Union[Unset, str] = UNSET
    project: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    error_traceback: Union[Unset, str] = UNSET
    backend_id: Union[Unset, str] = UNSET
    runtime_state: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    cluster_ip: Union[None, Unset, str] = UNSET
    selector: Union[Unset, Any] = UNSET
    target_workloads: Union[Unset, list["RancherNestedWorkloadRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        service_settings = self.service_settings

        project = self.project

        error_message = self.error_message

        error_traceback = self.error_traceback

        backend_id = self.backend_id

        runtime_state = self.runtime_state

        namespace = self.namespace

        cluster_ip: Union[None, Unset, str]
        if isinstance(self.cluster_ip, Unset):
            cluster_ip = UNSET
        else:
            cluster_ip = self.cluster_ip

        selector = self.selector

        target_workloads: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.target_workloads, Unset):
            target_workloads = []
            for target_workloads_item_data in self.target_workloads:
                target_workloads_item = target_workloads_item_data.to_dict()
                target_workloads.append(target_workloads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if service_settings is not UNSET:
            field_dict["service_settings"] = service_settings
        if project is not UNSET:
            field_dict["project"] = project
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if error_traceback is not UNSET:
            field_dict["error_traceback"] = error_traceback
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if runtime_state is not UNSET:
            field_dict["runtime_state"] = runtime_state
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if cluster_ip is not UNSET:
            field_dict["cluster_ip"] = cluster_ip
        if selector is not UNSET:
            field_dict["selector"] = selector
        if target_workloads is not UNSET:
            field_dict["target_workloads"] = target_workloads

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        service_settings = (
            self.service_settings
            if isinstance(self.service_settings, Unset)
            else (None, str(self.service_settings).encode(), "text/plain")
        )

        project = self.project if isinstance(self.project, Unset) else (None, str(self.project).encode(), "text/plain")

        error_message = (
            self.error_message
            if isinstance(self.error_message, Unset)
            else (None, str(self.error_message).encode(), "text/plain")
        )

        error_traceback = (
            self.error_traceback
            if isinstance(self.error_traceback, Unset)
            else (None, str(self.error_traceback).encode(), "text/plain")
        )

        backend_id = (
            self.backend_id
            if isinstance(self.backend_id, Unset)
            else (None, str(self.backend_id).encode(), "text/plain")
        )

        runtime_state = (
            self.runtime_state
            if isinstance(self.runtime_state, Unset)
            else (None, str(self.runtime_state).encode(), "text/plain")
        )

        namespace = (
            self.namespace if isinstance(self.namespace, Unset) else (None, str(self.namespace).encode(), "text/plain")
        )

        cluster_ip: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.cluster_ip, Unset):
            cluster_ip = UNSET
        elif isinstance(self.cluster_ip, str):
            cluster_ip = (None, str(self.cluster_ip).encode(), "text/plain")
        else:
            cluster_ip = (None, str(self.cluster_ip).encode(), "text/plain")

        selector = (
            self.selector if isinstance(self.selector, Unset) else (None, str(self.selector).encode(), "text/plain")
        )

        target_workloads: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.target_workloads, Unset):
            _temp_target_workloads = []
            for target_workloads_item_data in self.target_workloads:
                target_workloads_item = target_workloads_item_data.to_dict()
                _temp_target_workloads.append(target_workloads_item)
            target_workloads = (None, json.dumps(_temp_target_workloads).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if service_settings is not UNSET:
            field_dict["service_settings"] = service_settings
        if project is not UNSET:
            field_dict["project"] = project
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if error_traceback is not UNSET:
            field_dict["error_traceback"] = error_traceback
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if runtime_state is not UNSET:
            field_dict["runtime_state"] = runtime_state
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if cluster_ip is not UNSET:
            field_dict["cluster_ip"] = cluster_ip
        if selector is not UNSET:
            field_dict["selector"] = selector
        if target_workloads is not UNSET:
            field_dict["target_workloads"] = target_workloads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.rancher_nested_workload_request import RancherNestedWorkloadRequest

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        service_settings = d.pop("service_settings", UNSET)

        project = d.pop("project", UNSET)

        error_message = d.pop("error_message", UNSET)

        error_traceback = d.pop("error_traceback", UNSET)

        backend_id = d.pop("backend_id", UNSET)

        runtime_state = d.pop("runtime_state", UNSET)

        namespace = d.pop("namespace", UNSET)

        def _parse_cluster_ip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cluster_ip = _parse_cluster_ip(d.pop("cluster_ip", UNSET))

        selector = d.pop("selector", UNSET)

        target_workloads = []
        _target_workloads = d.pop("target_workloads", UNSET)
        for target_workloads_item_data in _target_workloads or []:
            target_workloads_item = RancherNestedWorkloadRequest.from_dict(target_workloads_item_data)

            target_workloads.append(target_workloads_item)

        patched_rancher_service_request = cls(
            name=name,
            description=description,
            service_settings=service_settings,
            project=project,
            error_message=error_message,
            error_traceback=error_traceback,
            backend_id=backend_id,
            runtime_state=runtime_state,
            namespace=namespace,
            cluster_ip=cluster_ip,
            selector=selector,
            target_workloads=target_workloads,
        )

        patched_rancher_service_request.additional_properties = d
        return patched_rancher_service_request

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
