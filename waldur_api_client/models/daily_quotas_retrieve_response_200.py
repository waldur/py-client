from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DailyQuotasRetrieveResponse200")


@_attrs_define
class DailyQuotasRetrieveResponse200:
    """ """

    additional_properties: dict[str, list[int]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        daily_quotas_retrieve_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = cast(list[int], prop_dict)

            additional_properties[prop_name] = additional_property

        daily_quotas_retrieve_response_200.additional_properties = additional_properties
        return daily_quotas_retrieve_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[int]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[int]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
