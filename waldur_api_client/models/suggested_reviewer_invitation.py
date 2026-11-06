from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.suggested_reviewer_invitation_outcome_enum import SuggestedReviewerInvitationOutcomeEnum

if TYPE_CHECKING:
    from ..models.suggested_reviewer import SuggestedReviewer


T = TypeVar("T", bound="SuggestedReviewerInvitation")


@_attrs_define
class SuggestedReviewerInvitation:
    """
    Attributes:
        candidate (SuggestedReviewer):
        outcome (SuggestedReviewerInvitationOutcomeEnum):
        invited (bool): Whether an invitation e-mail is sent: invited or resent.
        detail (str):
    """

    candidate: "SuggestedReviewer"
    outcome: SuggestedReviewerInvitationOutcomeEnum
    invited: bool
    detail: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        candidate = self.candidate.to_dict()

        outcome = self.outcome.value

        invited = self.invited

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "candidate": candidate,
                "outcome": outcome,
                "invited": invited,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.suggested_reviewer import SuggestedReviewer

        d = dict(src_dict)
        candidate = SuggestedReviewer.from_dict(d.pop("candidate"))

        outcome = SuggestedReviewerInvitationOutcomeEnum(d.pop("outcome"))

        invited = d.pop("invited")

        detail = d.pop("detail")

        suggested_reviewer_invitation = cls(
            candidate=candidate,
            outcome=outcome,
            invited=invited,
            detail=detail,
        )

        suggested_reviewer_invitation.additional_properties = d
        return suggested_reviewer_invitation

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
