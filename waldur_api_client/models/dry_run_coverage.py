from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dry_run_coverage_contribution_outcomes import DryRunCoverageContributionOutcomes
    from ..models.dry_run_coverage_outcomes import DryRunCoverageOutcomes


T = TypeVar("T", bound="DryRunCoverage")


@_attrs_define
class DryRunCoverage:
    """
    Attributes:
        steps (list[str]):
        exercised (list[str]):
        outcomes (DryRunCoverageOutcomes):
        contribution_outcomes (DryRunCoverageContributionOutcomes):
    """

    steps: list[str]
    exercised: list[str]
    outcomes: "DryRunCoverageOutcomes"
    contribution_outcomes: "DryRunCoverageContributionOutcomes"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        steps = self.steps

        exercised = self.exercised

        outcomes = self.outcomes.to_dict()

        contribution_outcomes = self.contribution_outcomes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "steps": steps,
                "exercised": exercised,
                "outcomes": outcomes,
                "contribution_outcomes": contribution_outcomes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dry_run_coverage_contribution_outcomes import DryRunCoverageContributionOutcomes
        from ..models.dry_run_coverage_outcomes import DryRunCoverageOutcomes

        d = dict(src_dict)
        steps = cast(list[str], d.pop("steps"))

        exercised = cast(list[str], d.pop("exercised"))

        outcomes = DryRunCoverageOutcomes.from_dict(d.pop("outcomes"))

        contribution_outcomes = DryRunCoverageContributionOutcomes.from_dict(d.pop("contribution_outcomes"))

        dry_run_coverage = cls(
            steps=steps,
            exercised=exercised,
            outcomes=outcomes,
            contribution_outcomes=contribution_outcomes,
        )

        dry_run_coverage.additional_properties = d
        return dry_run_coverage

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
