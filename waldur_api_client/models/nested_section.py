from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_attribute import NestedAttribute


T = TypeVar("T", bound="NestedSection")


@_attrs_define
class NestedSection:
    """
    Attributes:
        key (str):
        title (str):
        attributes (list['NestedAttribute']):
        is_standalone (Union[Unset, bool]): Whether section is rendered as a separate tab.
    """

    key: str
    title: str
    attributes: list["NestedAttribute"]
    is_standalone: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        title = self.title

        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        is_standalone = self.is_standalone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "title": title,
                "attributes": attributes,
            }
        )
        if is_standalone is not UNSET:
            field_dict["is_standalone"] = is_standalone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_attribute import NestedAttribute

        d = dict(src_dict)
        key = d.pop("key")

        title = d.pop("title")

        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = NestedAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        is_standalone = d.pop("is_standalone", UNSET)

        nested_section = cls(
            key=key,
            title=title,
            attributes=attributes,
            is_standalone=is_standalone,
        )

        nested_section.additional_properties = d
        return nested_section

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
