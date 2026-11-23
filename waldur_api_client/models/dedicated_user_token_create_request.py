import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DedicatedUserTokenCreateRequest")


@_attrs_define
class DedicatedUserTokenCreateRequest:
    """
    Attributes:
        template (str):
        target_type (str):
        target_uuid (UUID):
        name (str):
        expires_at (datetime.datetime):
        username (Union[Unset, str]): Of the new user; derived from the target when left out.
        features (Union[Unset, list[str]]): Keys of the template's optional features to add.
        allowed_networks (Union[Unset, list[str]]):
    """

    template: str
    target_type: str
    target_uuid: UUID
    name: str
    expires_at: datetime.datetime
    username: Union[Unset, str] = UNSET
    features: Union[Unset, list[str]] = UNSET
    allowed_networks: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template = self.template

        target_type = self.target_type

        target_uuid = str(self.target_uuid)

        name = self.name

        expires_at = self.expires_at.isoformat()

        username = self.username

        features: Union[Unset, list[str]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        allowed_networks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_networks, Unset):
            allowed_networks = self.allowed_networks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template": template,
                "target_type": target_type,
                "target_uuid": target_uuid,
                "name": name,
                "expires_at": expires_at,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if features is not UNSET:
            field_dict["features"] = features
        if allowed_networks is not UNSET:
            field_dict["allowed_networks"] = allowed_networks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template = d.pop("template")

        target_type = d.pop("target_type")

        target_uuid = UUID(d.pop("target_uuid"))

        name = d.pop("name")

        expires_at = isoparse(d.pop("expires_at"))

        username = d.pop("username", UNSET)

        features = cast(list[str], d.pop("features", UNSET))

        allowed_networks = cast(list[str], d.pop("allowed_networks", UNSET))

        dedicated_user_token_create_request = cls(
            template=template,
            target_type=target_type,
            target_uuid=target_uuid,
            name=name,
            expires_at=expires_at,
            username=username,
            features=features,
            allowed_networks=allowed_networks,
        )

        dedicated_user_token_create_request.additional_properties = d
        return dedicated_user_token_create_request

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
