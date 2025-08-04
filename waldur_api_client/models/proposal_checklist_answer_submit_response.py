from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.proposal_checklist_completion import ProposalChecklistCompletion


T = TypeVar("T", bound="ProposalChecklistAnswerSubmitResponse")


@_attrs_define
class ProposalChecklistAnswerSubmitResponse:
    """
    Attributes:
        detail (str):
        completion (ProposalChecklistCompletion):
    """

    detail: str
    completion: "ProposalChecklistCompletion"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        completion = self.completion.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
                "completion": completion,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_checklist_completion import ProposalChecklistCompletion

        d = dict(src_dict)
        detail = d.pop("detail")

        completion = ProposalChecklistCompletion.from_dict(d.pop("completion"))

        proposal_checklist_answer_submit_response = cls(
            detail=detail,
            completion=completion,
        )

        proposal_checklist_answer_submit_response.additional_properties = d
        return proposal_checklist_answer_submit_response

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
