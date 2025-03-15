import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Permission")


@_attrs_define
class Permission:
    """
    Attributes:
        user_uuid (UUID):
        user_name (str):
        user_slug (str):
        created (datetime.datetime):
        created_by_full_name (str):
        created_by_username (str):
        role_name (str):
        role_description (str):
        role_uuid (UUID):
        scope_type (str):
        scope_uuid (UUID):
        scope_name (str):
        customer_uuid (UUID):
        customer_name (str):
        expiration_time (Union[None, Unset, datetime.datetime]):
    """

    user_uuid: UUID
    user_name: str
    user_slug: str
    created: datetime.datetime
    created_by_full_name: str
    created_by_username: str
    role_name: str
    role_description: str
    role_uuid: UUID
    scope_type: str
    scope_uuid: UUID
    scope_name: str
    customer_uuid: UUID
    customer_name: str
    expiration_time: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_uuid = str(self.user_uuid)

        user_name = self.user_name

        user_slug = self.user_slug

        created = self.created.isoformat()

        created_by_full_name = self.created_by_full_name

        created_by_username = self.created_by_username

        role_name = self.role_name

        role_description = self.role_description

        role_uuid = str(self.role_uuid)

        scope_type = self.scope_type

        scope_uuid = str(self.scope_uuid)

        scope_name = self.scope_name

        customer_uuid = str(self.customer_uuid)

        customer_name = self.customer_name

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
                "user_uuid": user_uuid,
                "user_name": user_name,
                "user_slug": user_slug,
                "created": created,
                "created_by_full_name": created_by_full_name,
                "created_by_username": created_by_username,
                "role_name": role_name,
                "role_description": role_description,
                "role_uuid": role_uuid,
                "scope_type": scope_type,
                "scope_uuid": scope_uuid,
                "scope_name": scope_name,
                "customer_uuid": customer_uuid,
                "customer_name": customer_name,
            }
        )
        if expiration_time is not UNSET:
            field_dict["expiration_time"] = expiration_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_uuid = UUID(d.pop("user_uuid"))

        user_name = d.pop("user_name")

        user_slug = d.pop("user_slug")

        created = isoparse(d.pop("created"))

        created_by_full_name = d.pop("created_by_full_name")

        created_by_username = d.pop("created_by_username")

        role_name = d.pop("role_name")

        role_description = d.pop("role_description")

        role_uuid = UUID(d.pop("role_uuid"))

        scope_type = d.pop("scope_type")

        scope_uuid = UUID(d.pop("scope_uuid"))

        scope_name = d.pop("scope_name")

        customer_uuid = UUID(d.pop("customer_uuid"))

        customer_name = d.pop("customer_name")

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

        permission = cls(
            user_uuid=user_uuid,
            user_name=user_name,
            user_slug=user_slug,
            created=created,
            created_by_full_name=created_by_full_name,
            created_by_username=created_by_username,
            role_name=role_name,
            role_description=role_description,
            role_uuid=role_uuid,
            scope_type=scope_type,
            scope_uuid=scope_uuid,
            scope_name=scope_name,
            customer_uuid=customer_uuid,
            customer_name=customer_name,
            expiration_time=expiration_time,
        )

        permission.additional_properties = d
        return permission

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
