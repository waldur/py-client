from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenStackVolumeType")


@_attrs_define
class OpenStackVolumeType:
    """
    Attributes:
        url (str):
        uuid (UUID):
        name (str):
        settings (str):
        description (Union[Unset, str]):
        is_public (Union[Unset, bool]): Whether every project of the cloud may use the volume type. Cinder gives a
            private type only to the projects it is assigned to.
    """

    url: str
    uuid: UUID
    name: str
    settings: str
    description: Union[Unset, str] = UNSET
    is_public: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        name = self.name

        settings = self.settings

        description = self.description

        is_public = self.is_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "settings": settings,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_public is not UNSET:
            field_dict["is_public"] = is_public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        settings = d.pop("settings")

        description = d.pop("description", UNSET)

        is_public = d.pop("is_public", UNSET)

        open_stack_volume_type = cls(
            url=url,
            uuid=uuid,
            name=name,
            settings=settings,
            description=description,
            is_public=is_public,
        )

        open_stack_volume_type.additional_properties = d
        return open_stack_volume_type

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
