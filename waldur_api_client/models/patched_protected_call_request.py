from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedProtectedCallRequest")


@_attrs_define
class PatchedProtectedCallRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        backend_id (Union[Unset, str]):
        external_url (Union[None, Unset, str]):
        created_by (Union[None, Unset, str]):
        reference_code (Union[Unset, str]):
        default_project_role (Union[Unset, UUID]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    backend_id: Union[Unset, str] = UNSET
    external_url: Union[None, Unset, str] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    reference_code: Union[Unset, str] = UNSET
    default_project_role: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        backend_id = self.backend_id

        external_url: Union[None, Unset, str]
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        reference_code = self.reference_code

        default_project_role: Union[Unset, str] = UNSET
        if not isinstance(self.default_project_role, Unset):
            default_project_role = str(self.default_project_role)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if reference_code is not UNSET:
            field_dict["reference_code"] = reference_code
        if default_project_role is not UNSET:
            field_dict["default_project_role"] = default_project_role

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        backend_id = (
            self.backend_id
            if isinstance(self.backend_id, Unset)
            else (None, str(self.backend_id).encode(), "text/plain")
        )

        external_url: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.external_url, Unset):
            external_url = UNSET
        elif isinstance(self.external_url, str):
            external_url = (None, str(self.external_url).encode(), "text/plain")
        else:
            external_url = (None, str(self.external_url).encode(), "text/plain")

        created_by: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, str):
            created_by = (None, str(self.created_by).encode(), "text/plain")
        else:
            created_by = (None, str(self.created_by).encode(), "text/plain")

        reference_code = (
            self.reference_code
            if isinstance(self.reference_code, Unset)
            else (None, str(self.reference_code).encode(), "text/plain")
        )

        default_project_role: Union[Unset, bytes] = UNSET
        if not isinstance(self.default_project_role, Unset):
            default_project_role = str(self.default_project_role)

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if reference_code is not UNSET:
            field_dict["reference_code"] = reference_code
        if default_project_role is not UNSET:
            field_dict["default_project_role"] = default_project_role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        backend_id = d.pop("backend_id", UNSET)

        def _parse_external_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        reference_code = d.pop("reference_code", UNSET)

        _default_project_role = d.pop("default_project_role", UNSET)
        default_project_role: Union[Unset, UUID]
        if isinstance(_default_project_role, Unset):
            default_project_role = UNSET
        else:
            default_project_role = UUID(_default_project_role)

        patched_protected_call_request = cls(
            name=name,
            description=description,
            backend_id=backend_id,
            external_url=external_url,
            created_by=created_by,
            reference_code=reference_code,
            default_project_role=default_project_role,
        )

        patched_protected_call_request.additional_properties = d
        return patched_protected_call_request

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
