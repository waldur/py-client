from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DemoPresetPreviewOfferingGroup")


@_attrs_define
class DemoPresetPreviewOfferingGroup:
    """
    Attributes:
        type_ (str):
        category (str):
        names (list[str]):
    """

    type_: str
    category: str
    names: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        category = self.category

        names = self.names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "category": category,
                "names": names,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        category = d.pop("category")

        names = cast(list[str], d.pop("names"))

        demo_preset_preview_offering_group = cls(
            type_=type_,
            category=category,
            names=names,
        )

        demo_preset_preview_offering_group.additional_properties = d
        return demo_preset_preview_offering_group

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
