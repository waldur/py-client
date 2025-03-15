from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRancherIngressRequest")


@_attrs_define
class PatchedRancherIngressRequest:
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
        rancher_project (Union[Unset, str]):
        namespace (Union[Unset, str]):
        rules (Union[Unset, Any]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    service_settings: Union[Unset, str] = UNSET
    project: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    error_traceback: Union[Unset, str] = UNSET
    backend_id: Union[Unset, str] = UNSET
    runtime_state: Union[Unset, str] = UNSET
    rancher_project: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    rules: Union[Unset, Any] = UNSET
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

        rancher_project = self.rancher_project

        namespace = self.namespace

        rules = self.rules

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
        if rancher_project is not UNSET:
            field_dict["rancher_project"] = rancher_project
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if rules is not UNSET:
            field_dict["rules"] = rules

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

        rancher_project = (
            self.rancher_project
            if isinstance(self.rancher_project, Unset)
            else (None, str(self.rancher_project).encode(), "text/plain")
        )

        namespace = (
            self.namespace if isinstance(self.namespace, Unset) else (None, str(self.namespace).encode(), "text/plain")
        )

        rules = self.rules if isinstance(self.rules, Unset) else (None, str(self.rules).encode(), "text/plain")

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
        if rancher_project is not UNSET:
            field_dict["rancher_project"] = rancher_project
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        service_settings = d.pop("service_settings", UNSET)

        project = d.pop("project", UNSET)

        error_message = d.pop("error_message", UNSET)

        error_traceback = d.pop("error_traceback", UNSET)

        backend_id = d.pop("backend_id", UNSET)

        runtime_state = d.pop("runtime_state", UNSET)

        rancher_project = d.pop("rancher_project", UNSET)

        namespace = d.pop("namespace", UNSET)

        rules = d.pop("rules", UNSET)

        patched_rancher_ingress_request = cls(
            name=name,
            description=description,
            service_settings=service_settings,
            project=project,
            error_message=error_message,
            error_traceback=error_traceback,
            backend_id=backend_id,
            runtime_state=runtime_state,
            rancher_project=rancher_project,
            namespace=namespace,
            rules=rules,
        )

        patched_rancher_ingress_request.additional_properties = d
        return patched_rancher_ingress_request

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
