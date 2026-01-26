from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SlurmPolicyCarryover")


@_attrs_define
class SlurmPolicyCarryover:
    """
    Attributes:
        previous_usage (float):
        days_elapsed (int):
        half_life (int):
        decay_factor (float):
        effective_usage (float):
        base_allocation (float):
        unused_carryover (float):
        total_allocation (float):
    """

    previous_usage: float
    days_elapsed: int
    half_life: int
    decay_factor: float
    effective_usage: float
    base_allocation: float
    unused_carryover: float
    total_allocation: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        previous_usage = self.previous_usage

        days_elapsed = self.days_elapsed

        half_life = self.half_life

        decay_factor = self.decay_factor

        effective_usage = self.effective_usage

        base_allocation = self.base_allocation

        unused_carryover = self.unused_carryover

        total_allocation = self.total_allocation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "previous_usage": previous_usage,
                "days_elapsed": days_elapsed,
                "half_life": half_life,
                "decay_factor": decay_factor,
                "effective_usage": effective_usage,
                "base_allocation": base_allocation,
                "unused_carryover": unused_carryover,
                "total_allocation": total_allocation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        previous_usage = d.pop("previous_usage")

        days_elapsed = d.pop("days_elapsed")

        half_life = d.pop("half_life")

        decay_factor = d.pop("decay_factor")

        effective_usage = d.pop("effective_usage")

        base_allocation = d.pop("base_allocation")

        unused_carryover = d.pop("unused_carryover")

        total_allocation = d.pop("total_allocation")

        slurm_policy_carryover = cls(
            previous_usage=previous_usage,
            days_elapsed=days_elapsed,
            half_life=half_life,
            decay_factor=decay_factor,
            effective_usage=effective_usage,
            base_allocation=base_allocation,
            unused_carryover=unused_carryover,
            total_allocation=total_allocation,
        )

        slurm_policy_carryover.additional_properties = d
        return slurm_policy_carryover

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
