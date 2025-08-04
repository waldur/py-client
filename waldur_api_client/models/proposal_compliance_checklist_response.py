from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.proposal_checklist_completion import ProposalChecklistCompletion
    from ..models.proposal_checklist_question import ProposalChecklistQuestion
    from ..models.proposal_compliance_checklist_response_checklist import ProposalComplianceChecklistResponseChecklist


T = TypeVar("T", bound="ProposalComplianceChecklistResponse")


@_attrs_define
class ProposalComplianceChecklistResponse:
    """
    Attributes:
        checklist (ProposalComplianceChecklistResponseChecklist):
        completion (ProposalChecklistCompletion):
        questions (list['ProposalChecklistQuestion']):
    """

    checklist: "ProposalComplianceChecklistResponseChecklist"
    completion: "ProposalChecklistCompletion"
    questions: list["ProposalChecklistQuestion"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checklist = self.checklist.to_dict()

        completion = self.completion.to_dict()

        questions = []
        for questions_item_data in self.questions:
            questions_item = questions_item_data.to_dict()
            questions.append(questions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checklist": checklist,
                "completion": completion,
                "questions": questions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_checklist_completion import ProposalChecklistCompletion
        from ..models.proposal_checklist_question import ProposalChecklistQuestion
        from ..models.proposal_compliance_checklist_response_checklist import (
            ProposalComplianceChecklistResponseChecklist,
        )

        d = dict(src_dict)
        checklist = ProposalComplianceChecklistResponseChecklist.from_dict(d.pop("checklist"))

        completion = ProposalChecklistCompletion.from_dict(d.pop("completion"))

        questions = []
        _questions = d.pop("questions")
        for questions_item_data in _questions:
            questions_item = ProposalChecklistQuestion.from_dict(questions_item_data)

            questions.append(questions_item)

        proposal_compliance_checklist_response = cls(
            checklist=checklist,
            completion=completion,
            questions=questions,
        )

        proposal_compliance_checklist_response.additional_properties = d
        return proposal_compliance_checklist_response

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
