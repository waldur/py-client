from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedKeycloakUserGroupMembershipRequest")


@_attrs_define
class PatchedKeycloakUserGroupMembershipRequest:
    """
    Attributes:
        username (Union[Unset, str]): Keycloak user username
        email (Union[Unset, str]): User's email for notifications
        group (Union[Unset, str]):
    """

    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    group: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        email = self.email

        group = self.group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        group = d.pop("group", UNSET)

        patched_keycloak_user_group_membership_request = cls(
            username=username,
            email=email,
            group=group,
        )

        patched_keycloak_user_group_membership_request.additional_properties = d
        return patched_keycloak_user_group_membership_request

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
