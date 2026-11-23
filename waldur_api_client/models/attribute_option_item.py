from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttributeOptionItem")


@_attrs_define
class AttributeOptionItem:
    """
    Attributes:
        uuid (UUID):
        title (str):
        is_default (bool):
        key (Union[Unset, str]):
    """

    uuid: UUID
    title: str
    is_default: bool
    key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        title = self.title

        is_default = self.is_default

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "title": title,
                "is_default": is_default,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        title = d.pop("title")

        is_default = d.pop("is_default")

        key = d.pop("key", UNSET)

        attribute_option_item = cls(
            uuid=uuid,
            title=title,
            is_default=is_default,
            key=key,
        )

        attribute_option_item.additional_properties = d
        return attribute_option_item

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
