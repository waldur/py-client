from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metric_breakdown_item_value_type_0 import MetricBreakdownItemValueType0


T = TypeVar("T", bound="MetricBreakdownItem")


@_attrs_define
class MetricBreakdownItem:
    """
    Attributes:
        value (Union['MetricBreakdownItemValueType0', None]):
        figure (Union[None, float]):
    """

    value: Union["MetricBreakdownItemValueType0", None]
    figure: Union[None, float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.metric_breakdown_item_value_type_0 import MetricBreakdownItemValueType0

        value: Union[None, dict[str, Any]]
        if isinstance(self.value, MetricBreakdownItemValueType0):
            value = self.value.to_dict()
        else:
            value = self.value

        figure: Union[None, float]
        figure = self.figure

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "figure": figure,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_breakdown_item_value_type_0 import MetricBreakdownItemValueType0

        d = dict(src_dict)

        def _parse_value(data: object) -> Union["MetricBreakdownItemValueType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = MetricBreakdownItemValueType0.from_dict(data)

                return value_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MetricBreakdownItemValueType0", None], data)

        value = _parse_value(d.pop("value"))

        def _parse_figure(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        figure = _parse_figure(d.pop("figure"))

        metric_breakdown_item = cls(
            value=value,
            figure=figure,
        )

        metric_breakdown_item.additional_properties = d
        return metric_breakdown_item

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
