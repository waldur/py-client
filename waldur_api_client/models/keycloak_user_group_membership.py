import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.keycloak_user_group_membership_state import KeycloakUserGroupMembershipState
from ..models.rancher_catalog_scope_type import RancherCatalogScopeType

T = TypeVar("T", bound="KeycloakUserGroupMembership")


@_attrs_define
class KeycloakUserGroupMembership:
    """
    Attributes:
        uuid (UUID):
        url (str):
        username (str): Keycloak user username
        email (str): User's email for notifications
        group (str):
        group_name (str):
        group_role (str):
        group_scope_type (RancherCatalogScopeType):
        state (KeycloakUserGroupMembershipState):
        created (datetime.datetime):
        modified (datetime.datetime):
        last_checked (datetime.datetime):
        error_message (str):
        error_traceback (str):
    """

    uuid: UUID
    url: str
    username: str
    email: str
    group: str
    group_name: str
    group_role: str
    group_scope_type: RancherCatalogScopeType
    state: KeycloakUserGroupMembershipState
    created: datetime.datetime
    modified: datetime.datetime
    last_checked: datetime.datetime
    error_message: str
    error_traceback: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        url = self.url

        username = self.username

        email = self.email

        group = self.group

        group_name = self.group_name

        group_role = self.group_role

        group_scope_type = self.group_scope_type.value

        state = self.state.value

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        last_checked = self.last_checked.isoformat()

        error_message = self.error_message

        error_traceback = self.error_traceback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "url": url,
                "username": username,
                "email": email,
                "group": group,
                "group_name": group_name,
                "group_role": group_role,
                "group_scope_type": group_scope_type,
                "state": state,
                "created": created,
                "modified": modified,
                "last_checked": last_checked,
                "error_message": error_message,
                "error_traceback": error_traceback,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        url = d.pop("url")

        username = d.pop("username")

        email = d.pop("email")

        group = d.pop("group")

        group_name = d.pop("group_name")

        group_role = d.pop("group_role")

        group_scope_type = RancherCatalogScopeType(d.pop("group_scope_type"))

        state = KeycloakUserGroupMembershipState(d.pop("state"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        last_checked = isoparse(d.pop("last_checked"))

        error_message = d.pop("error_message")

        error_traceback = d.pop("error_traceback")

        keycloak_user_group_membership = cls(
            uuid=uuid,
            url=url,
            username=username,
            email=email,
            group=group,
            group_name=group_name,
            group_role=group_role,
            group_scope_type=group_scope_type,
            state=state,
            created=created,
            modified=modified,
            last_checked=last_checked,
            error_message=error_message,
            error_traceback=error_traceback,
        )

        keycloak_user_group_membership.additional_properties = d
        return keycloak_user_group_membership

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
