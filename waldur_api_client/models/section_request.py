from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SectionRequest")


@_attrs_define
class SectionRequest:
    """
    Attributes:
        key (str):
        title (str):
        category (str):
        is_standalone (Union[Unset, bool]): Whether section is rendered as a separate tab.
    """

    key: str
    title: str
    category: str
    is_standalone: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        title = self.title

        category = self.category

        is_standalone = self.is_standalone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "title": title,
                "category": category,
            }
        )
        if is_standalone is not UNSET:
            field_dict["is_standalone"] = is_standalone

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        key = (None, str(self.key).encode(), "text/plain")

        title = (None, str(self.title).encode(), "text/plain")

        category = (None, str(self.category).encode(), "text/plain")

        is_standalone = (
            self.is_standalone
            if isinstance(self.is_standalone, Unset)
            else (None, str(self.is_standalone).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "key": key,
                "title": title,
                "category": category,
            }
        )
        if is_standalone is not UNSET:
            field_dict["is_standalone"] = is_standalone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        title = d.pop("title")

        category = d.pop("category")

        is_standalone = d.pop("is_standalone", UNSET)

        section_request = cls(
            key=key,
            title=title,
            category=category,
            is_standalone=is_standalone,
        )

        section_request.additional_properties = d
        return section_request

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
