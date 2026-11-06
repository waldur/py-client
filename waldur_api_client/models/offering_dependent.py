from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OfferingDependent")


@_attrs_define
class OfferingDependent:
    """
    Attributes:
        summary (str):
        blocks (bool): The change is refused, except for staff.
        blocks_staff (bool): The change is refused for staff too.
    """

    summary: str
    blocks: bool
    blocks_staff: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary

        blocks = self.blocks

        blocks_staff = self.blocks_staff

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
                "blocks": blocks,
                "blocks_staff": blocks_staff,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        summary = d.pop("summary")

        blocks = d.pop("blocks")

        blocks_staff = d.pop("blocks_staff")

        offering_dependent = cls(
            summary=summary,
            blocks=blocks,
            blocks_staff=blocks_staff,
        )

        offering_dependent.additional_properties = d
        return offering_dependent

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
