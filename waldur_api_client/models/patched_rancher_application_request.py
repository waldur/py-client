from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_rancher_application_request_answers import PatchedRancherApplicationRequestAnswers


T = TypeVar("T", bound="PatchedRancherApplicationRequest")


@_attrs_define
class PatchedRancherApplicationRequest:
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
        template (Union[Unset, str]):
        rancher_project (Union[Unset, str]):
        namespace (Union[Unset, str]):
        namespace_name (Union[Unset, str]):
        version (Union[Unset, str]):
        answers (Union[Unset, PatchedRancherApplicationRequestAnswers]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    service_settings: Union[Unset, str] = UNSET
    project: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    error_traceback: Union[Unset, str] = UNSET
    backend_id: Union[Unset, str] = UNSET
    runtime_state: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    rancher_project: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    namespace_name: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    answers: Union[Unset, "PatchedRancherApplicationRequestAnswers"] = UNSET
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

        template = self.template

        rancher_project = self.rancher_project

        namespace = self.namespace

        namespace_name = self.namespace_name

        version = self.version

        answers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.answers, Unset):
            answers = self.answers.to_dict()

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
        if template is not UNSET:
            field_dict["template"] = template
        if rancher_project is not UNSET:
            field_dict["rancher_project"] = rancher_project
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if namespace_name is not UNSET:
            field_dict["namespace_name"] = namespace_name
        if version is not UNSET:
            field_dict["version"] = version
        if answers is not UNSET:
            field_dict["answers"] = answers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patched_rancher_application_request_answers import PatchedRancherApplicationRequestAnswers

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        service_settings = d.pop("service_settings", UNSET)

        project = d.pop("project", UNSET)

        error_message = d.pop("error_message", UNSET)

        error_traceback = d.pop("error_traceback", UNSET)

        backend_id = d.pop("backend_id", UNSET)

        runtime_state = d.pop("runtime_state", UNSET)

        template = d.pop("template", UNSET)

        rancher_project = d.pop("rancher_project", UNSET)

        namespace = d.pop("namespace", UNSET)

        namespace_name = d.pop("namespace_name", UNSET)

        version = d.pop("version", UNSET)

        _answers = d.pop("answers", UNSET)
        answers: Union[Unset, PatchedRancherApplicationRequestAnswers]
        if isinstance(_answers, Unset):
            answers = UNSET
        else:
            answers = PatchedRancherApplicationRequestAnswers.from_dict(_answers)

        patched_rancher_application_request = cls(
            name=name,
            description=description,
            service_settings=service_settings,
            project=project,
            error_message=error_message,
            error_traceback=error_traceback,
            backend_id=backend_id,
            runtime_state=runtime_state,
            template=template,
            rancher_project=rancher_project,
            namespace=namespace,
            namespace_name=namespace_name,
            version=version,
            answers=answers,
        )

        patched_rancher_application_request.additional_properties = d
        return patched_rancher_application_request

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
