from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RancherIngressRequest")


@_attrs_define
class RancherIngressRequest:
    """
    Attributes:
        name (str):
        service_settings (str):
        project (str):
        rancher_project (str):
        description (Union[Unset, str]):
        error_message (Union[Unset, str]):
        error_traceback (Union[Unset, str]):
        backend_id (Union[Unset, str]):
        runtime_state (Union[Unset, str]):
        namespace (Union[Unset, str]):
        rules (Union[Unset, Any]):
    """

    name: str
    service_settings: str
    project: str
    rancher_project: str
    description: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    error_traceback: Union[Unset, str] = UNSET
    backend_id: Union[Unset, str] = UNSET
    runtime_state: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    rules: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        service_settings = self.service_settings

        project = self.project

        rancher_project = self.rancher_project

        description = self.description

        error_message = self.error_message

        error_traceback = self.error_traceback

        backend_id = self.backend_id

        runtime_state = self.runtime_state

        namespace = self.namespace

        rules = self.rules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "service_settings": service_settings,
                "project": project,
                "rancher_project": rancher_project,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
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
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        service_settings = (None, str(self.service_settings).encode(), "text/plain")

        project = (None, str(self.project).encode(), "text/plain")

        rancher_project = (None, str(self.rancher_project).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

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

        rules = self.rules if isinstance(self.rules, Unset) else (None, str(self.rules).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
                "service_settings": service_settings,
                "project": project,
                "rancher_project": rancher_project,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
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
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        service_settings = d.pop("service_settings")

        project = d.pop("project")

        rancher_project = d.pop("rancher_project")

        description = d.pop("description", UNSET)

        error_message = d.pop("error_message", UNSET)

        error_traceback = d.pop("error_traceback", UNSET)

        backend_id = d.pop("backend_id", UNSET)

        runtime_state = d.pop("runtime_state", UNSET)

        namespace = d.pop("namespace", UNSET)

        rules = d.pop("rules", UNSET)

        rancher_ingress_request = cls(
            name=name,
            service_settings=service_settings,
            project=project,
            rancher_project=rancher_project,
            description=description,
            error_message=error_message,
            error_traceback=error_traceback,
            backend_id=backend_id,
            runtime_state=runtime_state,
            namespace=namespace,
            rules=rules,
        )

        rancher_ingress_request.additional_properties = d
        return rancher_ingress_request

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
