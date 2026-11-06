from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.scenario_coverage_untried_outcomes import ScenarioCoverageUntriedOutcomes


T = TypeVar("T", bound="ScenarioCoverage")


@_attrs_define
class ScenarioCoverage:
    """
    Attributes:
        steps (int):
        exercised (list[str]):
        unexercised (list[str]):
        untried_outcomes (ScenarioCoverageUntriedOutcomes):
    """

    steps: int
    exercised: list[str]
    unexercised: list[str]
    untried_outcomes: "ScenarioCoverageUntriedOutcomes"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        steps = self.steps

        exercised = self.exercised

        unexercised = self.unexercised

        untried_outcomes = self.untried_outcomes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "steps": steps,
                "exercised": exercised,
                "unexercised": unexercised,
                "untried_outcomes": untried_outcomes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scenario_coverage_untried_outcomes import ScenarioCoverageUntriedOutcomes

        d = dict(src_dict)
        steps = d.pop("steps")

        exercised = cast(list[str], d.pop("exercised"))

        unexercised = cast(list[str], d.pop("unexercised"))

        untried_outcomes = ScenarioCoverageUntriedOutcomes.from_dict(d.pop("untried_outcomes"))

        scenario_coverage = cls(
            steps=steps,
            exercised=exercised,
            unexercised=unexercised,
            untried_outcomes=untried_outcomes,
        )

        scenario_coverage.additional_properties = d
        return scenario_coverage

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
