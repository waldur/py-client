from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StepRunCondition")


@_attrs_define
class StepRunCondition:
    """
    Attributes:
        step (Union[Unset, str]): Key of the earlier step whose outcome or scores decide.
        outcomes (Union[Unset, list[str]]): Outcomes of that step, or of its contributions, on which this step runs;
            'expired' when it lapsed or was skipped.
        score_spread_above (Union[Unset, float]): In place of outcomes: the step runs only when the highest and the
            lowest score that step's contributions gave the proposal differ by more than this many points.
    """

    step: Union[Unset, str] = UNSET
    outcomes: Union[Unset, list[str]] = UNSET
    score_spread_above: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step

        outcomes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.outcomes, Unset):
            outcomes = self.outcomes

        score_spread_above = self.score_spread_above

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if step is not UNSET:
            field_dict["step"] = step
        if outcomes is not UNSET:
            field_dict["outcomes"] = outcomes
        if score_spread_above is not UNSET:
            field_dict["score_spread_above"] = score_spread_above

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        step = d.pop("step", UNSET)

        outcomes = cast(list[str], d.pop("outcomes", UNSET))

        score_spread_above = d.pop("score_spread_above", UNSET)

        step_run_condition = cls(
            step=step,
            outcomes=outcomes,
            score_spread_above=score_spread_above,
        )

        step_run_condition.additional_properties = d
        return step_run_condition

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
