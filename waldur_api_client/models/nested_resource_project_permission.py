import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NestedResourceProjectPermission")


@_attrs_define
class NestedResourceProjectPermission:
    """
    Attributes:
        url (Union[Unset, str]):
        uuid (Union[Unset, str]):
        name (Union[Unset, str]):
        role_name (Union[Unset, str]):
        role_uuid (Union[Unset, UUID]):
        expiration_time (Union[None, Unset, datetime.datetime]):
    """

    url: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    role_name: Union[Unset, str] = UNSET
    role_uuid: Union[Unset, UUID] = UNSET
    expiration_time: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = self.uuid

        name = self.name

        role_name = self.role_name

        role_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.role_uuid, Unset):
            role_uuid = str(self.role_uuid)

        expiration_time: Union[None, Unset, str]
        if isinstance(self.expiration_time, Unset):
            expiration_time = UNSET
        elif isinstance(self.expiration_time, datetime.datetime):
            expiration_time = self.expiration_time.isoformat()
        else:
            expiration_time = self.expiration_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if role_name is not UNSET:
            field_dict["role_name"] = role_name
        if role_uuid is not UNSET:
            field_dict["role_uuid"] = role_uuid
        if expiration_time is not UNSET:
            field_dict["expiration_time"] = expiration_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        role_name = d.pop("role_name", UNSET)

        _role_uuid = d.pop("role_uuid", UNSET)
        role_uuid: Union[Unset, UUID]
        if isinstance(_role_uuid, Unset):
            role_uuid = UNSET
        else:
            role_uuid = UUID(_role_uuid)

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

        nested_resource_project_permission = cls(
            url=url,
            uuid=uuid,
            name=name,
            role_name=role_name,
            role_uuid=role_uuid,
            expiration_time=expiration_time,
        )

        nested_resource_project_permission.additional_properties = d
        return nested_resource_project_permission

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
