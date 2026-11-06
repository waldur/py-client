from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowDescriptionRunCondition")


@_attrs_define
class WorkflowDescriptionRunCondition:
    """
    Attributes:
        step (str):
        outcomes (list[str]): The outcomes of the step it runs on; empty on a score spread.
        score_spread_above (Union[None, float]): Runs only when the scores the step's contributions gave lie more than
            this many points apart; null on an outcome condition.
    """

    step: str
    outcomes: list[str]
    score_spread_above: Union[None, float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step

        outcomes = self.outcomes

        score_spread_above: Union[None, float]
        score_spread_above = self.score_spread_above

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
                "outcomes": outcomes,
                "score_spread_above": score_spread_above,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        step = d.pop("step")

        outcomes = cast(list[str], d.pop("outcomes"))

        def _parse_score_spread_above(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        score_spread_above = _parse_score_spread_above(d.pop("score_spread_above"))

        workflow_description_run_condition = cls(
            step=step,
            outcomes=outcomes,
            score_spread_above=score_spread_above,
        )

        workflow_description_run_condition.additional_properties = d
        return workflow_description_run_condition

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
