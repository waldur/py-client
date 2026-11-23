from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrderFlowStepStat")


@_attrs_define
class OrderFlowStepStat:
    """
    Attributes:
        step (str):
        samples (int):
        median_seconds (Union[None, float]):
    """

    step: str
    samples: int
    median_seconds: Union[None, float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step

        samples = self.samples

        median_seconds: Union[None, float]
        median_seconds = self.median_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
                "samples": samples,
                "median_seconds": median_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        step = d.pop("step")

        samples = d.pop("samples")

        def _parse_median_seconds(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        median_seconds = _parse_median_seconds(d.pop("median_seconds"))

        order_flow_step_stat = cls(
            step=step,
            samples=samples,
            median_seconds=median_seconds,
        )

        order_flow_step_stat.additional_properties = d
        return order_flow_step_stat

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
