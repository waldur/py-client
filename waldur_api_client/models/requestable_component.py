from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RequestableComponent")


@_attrs_define
class RequestableComponent:
    """
    Attributes:
        type_ (str):
        name (str):
        measured_unit (str):
        limit_period (str):
        unit_factor (int):
        min_value (Union[None, float]):
        max_value (Union[None, float]):
        limit_decimal_places (int):
    """

    type_: str
    name: str
    measured_unit: str
    limit_period: str
    unit_factor: int
    min_value: Union[None, float]
    max_value: Union[None, float]
    limit_decimal_places: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        measured_unit = self.measured_unit

        limit_period = self.limit_period

        unit_factor = self.unit_factor

        min_value: Union[None, float]
        min_value = self.min_value

        max_value: Union[None, float]
        max_value = self.max_value

        limit_decimal_places = self.limit_decimal_places

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "measured_unit": measured_unit,
                "limit_period": limit_period,
                "unit_factor": unit_factor,
                "min_value": min_value,
                "max_value": max_value,
                "limit_decimal_places": limit_decimal_places,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        measured_unit = d.pop("measured_unit")

        limit_period = d.pop("limit_period")

        unit_factor = d.pop("unit_factor")

        def _parse_min_value(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        min_value = _parse_min_value(d.pop("min_value"))

        def _parse_max_value(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        max_value = _parse_max_value(d.pop("max_value"))

        limit_decimal_places = d.pop("limit_decimal_places")

        requestable_component = cls(
            type_=type_,
            name=name,
            measured_unit=measured_unit,
            limit_period=limit_period,
            unit_factor=unit_factor,
            min_value=min_value,
            max_value=max_value,
            limit_decimal_places=limit_decimal_places,
        )

        requestable_component.additional_properties = d
        return requestable_component

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
