from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SectionCreateRequest")


@_attrs_define
class SectionCreateRequest:
    """
    Attributes:
        title (str):
        category (str):
        key (Union[Unset, str]):
        is_standalone (Union[Unset, bool]): Whether section is rendered as a separate tab.
    """

    title: str
    category: str
    key: Union[Unset, str] = UNSET
    is_standalone: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        category = self.category

        key = self.key

        is_standalone = self.is_standalone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "category": category,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if is_standalone is not UNSET:
            field_dict["is_standalone"] = is_standalone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        category = d.pop("category")

        key = d.pop("key", UNSET)

        is_standalone = d.pop("is_standalone", UNSET)

        section_create_request = cls(
            title=title,
            category=category,
            key=key,
            is_standalone=is_standalone,
        )

        section_create_request.additional_properties = d
        return section_create_request

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
