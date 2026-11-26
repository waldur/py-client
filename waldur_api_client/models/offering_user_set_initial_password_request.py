from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferingUserSetInitialPasswordRequest")


@_attrs_define
class OfferingUserSetInitialPasswordRequest:
    """
    Attributes:
        password (str): The initial password of the user's account at the backend. It stops working once the user
            changes it there.
        username (Union[Unset, str]): The offering user's username the password was created for. When given, the
            password is refused if the offering user no longer has it, so a password for a replaced account is never stored.
    """

    password: str
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password")

        username = d.pop("username", UNSET)

        offering_user_set_initial_password_request = cls(
            password=password,
            username=username,
        )

        offering_user_set_initial_password_request.additional_properties = d
        return offering_user_set_initial_password_request

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
