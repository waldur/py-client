from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rancher_keycloak_group_scope_type import RancherKeycloakGroupScopeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedKeycloakGroupRequest")


@_attrs_define
class PatchedKeycloakGroupRequest:
    """
    Attributes:
        scope_type (Union[Unset, RancherKeycloakGroupScopeType]):
        scope_uuid (Union[Unset, UUID]): UUID of the cluster or project
        role (Union[Unset, str]):
    """

    scope_type: Union[Unset, RancherKeycloakGroupScopeType] = UNSET
    scope_uuid: Union[Unset, UUID] = UNSET
    role: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope_type: Union[Unset, str] = UNSET
        if not isinstance(self.scope_type, Unset):
            scope_type = self.scope_type.value

        scope_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.scope_uuid, Unset):
            scope_uuid = str(self.scope_uuid)

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope_type is not UNSET:
            field_dict["scope_type"] = scope_type
        if scope_uuid is not UNSET:
            field_dict["scope_uuid"] = scope_uuid
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _scope_type = d.pop("scope_type", UNSET)
        scope_type: Union[Unset, RancherKeycloakGroupScopeType]
        if isinstance(_scope_type, Unset):
            scope_type = UNSET
        else:
            scope_type = RancherKeycloakGroupScopeType(_scope_type)

        _scope_uuid = d.pop("scope_uuid", UNSET)
        scope_uuid: Union[Unset, UUID]
        if isinstance(_scope_uuid, Unset):
            scope_uuid = UNSET
        else:
            scope_uuid = UUID(_scope_uuid)

        role = d.pop("role", UNSET)

        patched_keycloak_group_request = cls(
            scope_type=scope_type,
            scope_uuid=scope_uuid,
            role=role,
        )

        patched_keycloak_group_request.additional_properties = d
        return patched_keycloak_group_request

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
