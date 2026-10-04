from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.matrix_external_login_method_enum import MatrixExternalLoginMethodEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatrixCredentials")


@_attrs_define
class MatrixCredentials:
    """
    Attributes:
        method (MatrixExternalLoginMethodEnum):
        homeserver_url (str):
        matrix_user_id (str):
        password (Union[Unset, str]):
    """

    method: MatrixExternalLoginMethodEnum
    homeserver_url: str
    matrix_user_id: str
    password: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        homeserver_url = self.homeserver_url

        matrix_user_id = self.matrix_user_id

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "homeserver_url": homeserver_url,
                "matrix_user_id": matrix_user_id,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = MatrixExternalLoginMethodEnum(d.pop("method"))

        homeserver_url = d.pop("homeserver_url")

        matrix_user_id = d.pop("matrix_user_id")

        password = d.pop("password", UNSET)

        matrix_credentials = cls(
            method=method,
            homeserver_url=homeserver_url,
            matrix_user_id=matrix_user_id,
            password=password,
        )

        matrix_credentials.additional_properties = d
        return matrix_credentials

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
