from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.proposal_review import ProposalReview
    from ..models.proposal_workflow_step_instance import ProposalWorkflowStepInstance
    from ..models.step_contribution_with_answers import StepContributionWithAnswers


T = TypeVar("T", bound="StepInput")


@_attrs_define
class StepInput:
    """
    Attributes:
        step (ProposalWorkflowStepInstance):
        contributions (list['StepContributionWithAnswers']): The step's contributions with their answers.
        reviews (list['ProposalReview']): The submitted reviews of a step collecting reviews; for the applicant without
            private comments, and without the reviewer unless the call reveals reviewers to applicants.
    """

    step: "ProposalWorkflowStepInstance"
    contributions: list["StepContributionWithAnswers"]
    reviews: list["ProposalReview"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step.to_dict()

        contributions = []
        for contributions_item_data in self.contributions:
            contributions_item = contributions_item_data.to_dict()
            contributions.append(contributions_item)

        reviews = []
        for reviews_item_data in self.reviews:
            reviews_item = reviews_item_data.to_dict()
            reviews.append(reviews_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
                "contributions": contributions,
                "reviews": reviews,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_review import ProposalReview
        from ..models.proposal_workflow_step_instance import ProposalWorkflowStepInstance
        from ..models.step_contribution_with_answers import StepContributionWithAnswers

        d = dict(src_dict)
        step = ProposalWorkflowStepInstance.from_dict(d.pop("step"))

        contributions = []
        _contributions = d.pop("contributions")
        for contributions_item_data in _contributions:
            contributions_item = StepContributionWithAnswers.from_dict(contributions_item_data)

            contributions.append(contributions_item)

        reviews = []
        _reviews = d.pop("reviews")
        for reviews_item_data in _reviews:
            reviews_item = ProposalReview.from_dict(reviews_item_data)

            reviews.append(reviews_item)

        step_input = cls(
            step=step,
            contributions=contributions,
            reviews=reviews,
        )

        step_input.additional_properties = d
        return step_input

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
