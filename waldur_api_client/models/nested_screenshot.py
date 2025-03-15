import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NestedScreenshot")


@_attrs_define
class NestedScreenshot:
    """
    Attributes:
        name (str):
        uuid (UUID):
        image (str):
        thumbnail (Union[None, str]):
        created (datetime.datetime):
        description (Union[Unset, str]):
    """

    name: str
    uuid: UUID
    image: str
    thumbnail: Union[None, str]
    created: datetime.datetime
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        uuid = str(self.uuid)

        image = self.image

        thumbnail: Union[None, str]
        thumbnail = self.thumbnail

        created = self.created.isoformat()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uuid": uuid,
                "image": image,
                "thumbnail": thumbnail,
                "created": created,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        uuid = UUID(d.pop("uuid"))

        image = d.pop("image")

        def _parse_thumbnail(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        thumbnail = _parse_thumbnail(d.pop("thumbnail"))

        created = isoparse(d.pop("created"))

        description = d.pop("description", UNSET)

        nested_screenshot = cls(
            name=name,
            uuid=uuid,
            image=image,
            thumbnail=thumbnail,
            created=created,
            description=description,
        )

        nested_screenshot.additional_properties = d
        return nested_screenshot

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
