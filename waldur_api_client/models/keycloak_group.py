import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rancher_keycloak_group_scope_type import RancherKeycloakGroupScopeType

T = TypeVar("T", bound="KeycloakGroup")


@_attrs_define
class KeycloakGroup:
    """
    Attributes:
        uuid (UUID):
        url (str):
        name (str):
        backend_id (str):
        scope_type (RancherKeycloakGroupScopeType):
        scope_uuid (UUID): UUID of the cluster or project
        scope_name (str): Get the name of the cluster or project
        role (str):
        created (datetime.datetime):
        modified (datetime.datetime):
    """

    uuid: UUID
    url: str
    name: str
    backend_id: str
    scope_type: RancherKeycloakGroupScopeType
    scope_uuid: UUID
    scope_name: str
    role: str
    created: datetime.datetime
    modified: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        url = self.url

        name = self.name

        backend_id = self.backend_id

        scope_type = self.scope_type.value

        scope_uuid = str(self.scope_uuid)

        scope_name = self.scope_name

        role = self.role

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "url": url,
                "name": name,
                "backend_id": backend_id,
                "scope_type": scope_type,
                "scope_uuid": scope_uuid,
                "scope_name": scope_name,
                "role": role,
                "created": created,
                "modified": modified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        url = d.pop("url")

        name = d.pop("name")

        backend_id = d.pop("backend_id")

        scope_type = RancherKeycloakGroupScopeType(d.pop("scope_type"))

        scope_uuid = UUID(d.pop("scope_uuid"))

        scope_name = d.pop("scope_name")

        role = d.pop("role")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        keycloak_group = cls(
            uuid=uuid,
            url=url,
            name=name,
            backend_id=backend_id,
            scope_type=scope_type,
            scope_uuid=scope_uuid,
            scope_name=scope_name,
            role=role,
            created=created,
            modified=modified,
        )

        keycloak_group.additional_properties = d
        return keycloak_group

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
