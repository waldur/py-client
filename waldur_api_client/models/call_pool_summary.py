from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallPoolSummary")


@_attrs_define
class CallPoolSummary:
    """
    Attributes:
        component_type (str):
        offered_total (float):
        round_name (Union[None, Unset, str]):
    """

    component_type: str
    offered_total: float
    round_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_type = self.component_type

        offered_total = self.offered_total

        round_name: Union[None, Unset, str]
        if isinstance(self.round_name, Unset):
            round_name = UNSET
        else:
            round_name = self.round_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_type": component_type,
                "offered_total": offered_total,
            }
        )
        if round_name is not UNSET:
            field_dict["round_name"] = round_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_type = d.pop("component_type")

        offered_total = d.pop("offered_total")

        def _parse_round_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_name = _parse_round_name(d.pop("round_name", UNSET))

        call_pool_summary = cls(
            component_type=component_type,
            offered_total=offered_total,
            round_name=round_name,
        )

        call_pool_summary.additional_properties = d
        return call_pool_summary

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
