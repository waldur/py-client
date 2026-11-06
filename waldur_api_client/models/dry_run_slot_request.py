from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DryRunSlotRequest")


@_attrs_define
class DryRunSlotRequest:
    """
    Attributes:
        offering (Union[None, Unset, int]):
        slot (Union[None, Unset, int]):
    """

    offering: Union[None, Unset, int] = UNSET
    slot: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offering: Union[None, Unset, int]
        if isinstance(self.offering, Unset):
            offering = UNSET
        else:
            offering = self.offering

        slot: Union[None, Unset, int]
        if isinstance(self.slot, Unset):
            slot = UNSET
        else:
            slot = self.slot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offering is not UNSET:
            field_dict["offering"] = offering
        if slot is not UNSET:
            field_dict["slot"] = slot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_offering(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        offering = _parse_offering(d.pop("offering", UNSET))

        def _parse_slot(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        slot = _parse_slot(d.pop("slot", UNSET))

        dry_run_slot_request = cls(
            offering=offering,
            slot=slot,
        )

        dry_run_slot_request.additional_properties = d
        return dry_run_slot_request

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
