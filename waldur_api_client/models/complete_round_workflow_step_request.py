from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.outcome_enum import OutcomeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proposal_feedback_request import ProposalFeedbackRequest


T = TypeVar("T", bound="CompleteRoundWorkflowStepRequest")


@_attrs_define
class CompleteRoundWorkflowStepRequest:
    """
    Attributes:
        outcome (OutcomeEnum):
        step_uuid (Union[Unset, UUID]): UUID of the call step to complete. Either this or step.
        step (Union[Unset, str]): Key of the call step to complete. Either this or step_uuid.
        feedback (Union[Unset, list['ProposalFeedbackRequest']]): Feedback per proposal, stored as that proposal's
            outcome reason for the step. The applicant reads it only once the step's report is released.
    """

    outcome: OutcomeEnum
    step_uuid: Union[Unset, UUID] = UNSET
    step: Union[Unset, str] = UNSET
    feedback: Union[Unset, list["ProposalFeedbackRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outcome = self.outcome.value

        step_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.step_uuid, Unset):
            step_uuid = str(self.step_uuid)

        step = self.step

        feedback: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.feedback, Unset):
            feedback = []
            for feedback_item_data in self.feedback:
                feedback_item = feedback_item_data.to_dict()
                feedback.append(feedback_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outcome": outcome,
            }
        )
        if step_uuid is not UNSET:
            field_dict["step_uuid"] = step_uuid
        if step is not UNSET:
            field_dict["step"] = step
        if feedback is not UNSET:
            field_dict["feedback"] = feedback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_feedback_request import ProposalFeedbackRequest

        d = dict(src_dict)
        outcome = OutcomeEnum(d.pop("outcome"))

        _step_uuid = d.pop("step_uuid", UNSET)
        step_uuid: Union[Unset, UUID]
        if isinstance(_step_uuid, Unset):
            step_uuid = UNSET
        else:
            step_uuid = UUID(_step_uuid)

        step = d.pop("step", UNSET)

        feedback = []
        _feedback = d.pop("feedback", UNSET)
        for feedback_item_data in _feedback or []:
            feedback_item = ProposalFeedbackRequest.from_dict(feedback_item_data)

            feedback.append(feedback_item)

        complete_round_workflow_step_request = cls(
            outcome=outcome,
            step_uuid=step_uuid,
            step=step,
            feedback=feedback,
        )

        complete_round_workflow_step_request.additional_properties = d
        return complete_round_workflow_step_request

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
