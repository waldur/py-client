from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReviewerReportTotals")


@_attrs_define
class ReviewerReportTotals:
    """
    Attributes:
        invitations (int): Proposals sent to the reviewer in assignment batches; a draft batch's are not counted until
            it is sent. The sum of the invitations_* counts.
        invitations_accepted (int):
        invitations_declined (int):
        invitations_expired (int): Left unanswered until the batch's deadline.
        invitations_pending (int): Awaiting an answer, before the batch's deadline.
        invitations_withdrawn (int): Unanswered when the call team canceled the batch.
        invitations_coi_blocked (int): Blocked by a conflict of interest.
        invitations_reassigned (int): Given to another reviewer instead.
        reviews_assigned (int):
        reviews_submitted (int):
        reviews_in_progress (int): In review, with a score or a comment entered.
        reviews_not_started (int): In review, with nothing entered yet.
        reviews_declined (int):
        reviews_expired (int): Closed at their deadline without being submitted.
        reviews_withdrawn (int): Withdrawn when the reviewer joined the proposal's team.
        reviews_overdue (int): In review past their deadline.
        reviewers (int):
    """

    invitations: int
    invitations_accepted: int
    invitations_declined: int
    invitations_expired: int
    invitations_pending: int
    invitations_withdrawn: int
    invitations_coi_blocked: int
    invitations_reassigned: int
    reviews_assigned: int
    reviews_submitted: int
    reviews_in_progress: int
    reviews_not_started: int
    reviews_declined: int
    reviews_expired: int
    reviews_withdrawn: int
    reviews_overdue: int
    reviewers: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invitations = self.invitations

        invitations_accepted = self.invitations_accepted

        invitations_declined = self.invitations_declined

        invitations_expired = self.invitations_expired

        invitations_pending = self.invitations_pending

        invitations_withdrawn = self.invitations_withdrawn

        invitations_coi_blocked = self.invitations_coi_blocked

        invitations_reassigned = self.invitations_reassigned

        reviews_assigned = self.reviews_assigned

        reviews_submitted = self.reviews_submitted

        reviews_in_progress = self.reviews_in_progress

        reviews_not_started = self.reviews_not_started

        reviews_declined = self.reviews_declined

        reviews_expired = self.reviews_expired

        reviews_withdrawn = self.reviews_withdrawn

        reviews_overdue = self.reviews_overdue

        reviewers = self.reviewers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invitations": invitations,
                "invitations_accepted": invitations_accepted,
                "invitations_declined": invitations_declined,
                "invitations_expired": invitations_expired,
                "invitations_pending": invitations_pending,
                "invitations_withdrawn": invitations_withdrawn,
                "invitations_coi_blocked": invitations_coi_blocked,
                "invitations_reassigned": invitations_reassigned,
                "reviews_assigned": reviews_assigned,
                "reviews_submitted": reviews_submitted,
                "reviews_in_progress": reviews_in_progress,
                "reviews_not_started": reviews_not_started,
                "reviews_declined": reviews_declined,
                "reviews_expired": reviews_expired,
                "reviews_withdrawn": reviews_withdrawn,
                "reviews_overdue": reviews_overdue,
                "reviewers": reviewers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invitations = d.pop("invitations")

        invitations_accepted = d.pop("invitations_accepted")

        invitations_declined = d.pop("invitations_declined")

        invitations_expired = d.pop("invitations_expired")

        invitations_pending = d.pop("invitations_pending")

        invitations_withdrawn = d.pop("invitations_withdrawn")

        invitations_coi_blocked = d.pop("invitations_coi_blocked")

        invitations_reassigned = d.pop("invitations_reassigned")

        reviews_assigned = d.pop("reviews_assigned")

        reviews_submitted = d.pop("reviews_submitted")

        reviews_in_progress = d.pop("reviews_in_progress")

        reviews_not_started = d.pop("reviews_not_started")

        reviews_declined = d.pop("reviews_declined")

        reviews_expired = d.pop("reviews_expired")

        reviews_withdrawn = d.pop("reviews_withdrawn")

        reviews_overdue = d.pop("reviews_overdue")

        reviewers = d.pop("reviewers")

        reviewer_report_totals = cls(
            invitations=invitations,
            invitations_accepted=invitations_accepted,
            invitations_declined=invitations_declined,
            invitations_expired=invitations_expired,
            invitations_pending=invitations_pending,
            invitations_withdrawn=invitations_withdrawn,
            invitations_coi_blocked=invitations_coi_blocked,
            invitations_reassigned=invitations_reassigned,
            reviews_assigned=reviews_assigned,
            reviews_submitted=reviews_submitted,
            reviews_in_progress=reviews_in_progress,
            reviews_not_started=reviews_not_started,
            reviews_declined=reviews_declined,
            reviews_expired=reviews_expired,
            reviews_withdrawn=reviews_withdrawn,
            reviews_overdue=reviews_overdue,
            reviewers=reviewers,
        )

        reviewer_report_totals.additional_properties = d
        return reviewer_report_totals

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
