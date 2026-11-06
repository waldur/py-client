from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.step_contribution import StepContribution


T = TypeVar("T", bound="SubmitStepContributionResponse")


@_attrs_define
class SubmitStepContributionResponse:
    """
    Attributes:
        detail (str):
        contribution (StepContribution):
        step_completed (bool):
        proposal_state (str):
    """

    detail: str
    contribution: "StepContribution"
    step_completed: bool
    proposal_state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        contribution = self.contribution.to_dict()

        step_completed = self.step_completed

        proposal_state = self.proposal_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
                "contribution": contribution,
                "step_completed": step_completed,
                "proposal_state": proposal_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_contribution import StepContribution

        d = dict(src_dict)
        detail = d.pop("detail")

        contribution = StepContribution.from_dict(d.pop("contribution"))

        step_completed = d.pop("step_completed")

        proposal_state = d.pop("proposal_state")

        submit_step_contribution_response = cls(
            detail=detail,
            contribution=contribution,
            step_completed=step_completed,
            proposal_state=proposal_state,
        )

        submit_step_contribution_response.additional_properties = d
        return submit_step_contribution_response

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
