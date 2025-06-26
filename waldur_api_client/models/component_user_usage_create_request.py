from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentUserUsageCreateRequest")


@_attrs_define
class ComponentUserUsageCreateRequest:
    """
    Attributes:
        username (str):
        usage (Union[Unset, str]):
        user (Union[Unset, str]):
    """

    username: str
    usage: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        usage = self.usage

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        usage = d.pop("usage", UNSET)

        user = d.pop("user", UNSET)

        component_user_usage_create_request = cls(
            username=username,
            usage=usage,
            user=user,
        )

        component_user_usage_create_request.additional_properties = d
        return component_user_usage_create_request

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
