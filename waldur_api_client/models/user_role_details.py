import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserRoleDetails")


@_attrs_define
class UserRoleDetails:
    """
    Attributes:
        uuid (UUID):
        created (datetime.datetime):
        role_name (str):
        role_uuid (UUID):
        user_email (str):
        user_full_name (str):
        user_username (str): Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters
        user_uuid (UUID):
        user_image (str):
        created_by_full_name (str):
        created_by_uuid (UUID):
        expiration_time (Union[None, Unset, datetime.datetime]):
    """

    uuid: UUID
    created: datetime.datetime
    role_name: str
    role_uuid: UUID
    user_email: str
    user_full_name: str
    user_username: str
    user_uuid: UUID
    user_image: str
    created_by_full_name: str
    created_by_uuid: UUID
    expiration_time: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        created = self.created.isoformat()

        role_name = self.role_name

        role_uuid = str(self.role_uuid)

        user_email = self.user_email

        user_full_name = self.user_full_name

        user_username = self.user_username

        user_uuid = str(self.user_uuid)

        user_image = self.user_image

        created_by_full_name = self.created_by_full_name

        created_by_uuid = str(self.created_by_uuid)

        expiration_time: Union[None, Unset, str]
        if isinstance(self.expiration_time, Unset):
            expiration_time = UNSET
        elif isinstance(self.expiration_time, datetime.datetime):
            expiration_time = self.expiration_time.isoformat()
        else:
            expiration_time = self.expiration_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "created": created,
                "role_name": role_name,
                "role_uuid": role_uuid,
                "user_email": user_email,
                "user_full_name": user_full_name,
                "user_username": user_username,
                "user_uuid": user_uuid,
                "user_image": user_image,
                "created_by_full_name": created_by_full_name,
                "created_by_uuid": created_by_uuid,
            }
        )
        if expiration_time is not UNSET:
            field_dict["expiration_time"] = expiration_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        role_name = d.pop("role_name")

        role_uuid = UUID(d.pop("role_uuid"))

        user_email = d.pop("user_email")

        user_full_name = d.pop("user_full_name")

        user_username = d.pop("user_username")

        user_uuid = UUID(d.pop("user_uuid"))

        user_image = d.pop("user_image")

        created_by_full_name = d.pop("created_by_full_name")

        created_by_uuid = UUID(d.pop("created_by_uuid"))

        def _parse_expiration_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_time_type_0 = isoparse(data)

                return expiration_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expiration_time = _parse_expiration_time(d.pop("expiration_time", UNSET))

        user_role_details = cls(
            uuid=uuid,
            created=created,
            role_name=role_name,
            role_uuid=role_uuid,
            user_email=user_email,
            user_full_name=user_full_name,
            user_username=user_username,
            user_uuid=user_uuid,
            user_image=user_image,
            created_by_full_name=created_by_full_name,
            created_by_uuid=created_by_uuid,
            expiration_time=expiration_time,
        )

        user_role_details.additional_properties = d
        return user_role_details

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
