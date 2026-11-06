import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ReviewerReportRow")


@_attrs_define
class ReviewerReportRow:
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
        reviewer_uuid (Union[None, UUID]): Empty for a reviewer invited by email who has no account yet: the row is
            their address's invitations.
        reviewer_name (str):
        reviewer_email (str):
        is_active (Union[None, bool]): Empty without an account.
        median_response_days (Union[None, float]): Median days from an assignment batch being sent to the reviewer
            accepting or declining a proposal of it.
        median_turnaround_days (Union[None, float]): Median days from a review's creation to its submission, over the
            reviews whose submission time is recorded.
        mean_score (Union[None, float]): Mean overall score of the submitted reviews, 1-5.
        last_submitted_at (Union[None, datetime.datetime]):
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
    reviewer_uuid: Union[None, UUID]
    reviewer_name: str
    reviewer_email: str
    is_active: Union[None, bool]
    median_response_days: Union[None, float]
    median_turnaround_days: Union[None, float]
    mean_score: Union[None, float]
    last_submitted_at: Union[None, datetime.datetime]
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

        reviewer_uuid: Union[None, str]
        if isinstance(self.reviewer_uuid, UUID):
            reviewer_uuid = str(self.reviewer_uuid)
        else:
            reviewer_uuid = self.reviewer_uuid

        reviewer_name = self.reviewer_name

        reviewer_email = self.reviewer_email

        is_active: Union[None, bool]
        is_active = self.is_active

        median_response_days: Union[None, float]
        median_response_days = self.median_response_days

        median_turnaround_days: Union[None, float]
        median_turnaround_days = self.median_turnaround_days

        mean_score: Union[None, float]
        mean_score = self.mean_score

        last_submitted_at: Union[None, str]
        if isinstance(self.last_submitted_at, datetime.datetime):
            last_submitted_at = self.last_submitted_at.isoformat()
        else:
            last_submitted_at = self.last_submitted_at

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
                "reviewer_uuid": reviewer_uuid,
                "reviewer_name": reviewer_name,
                "reviewer_email": reviewer_email,
                "is_active": is_active,
                "median_response_days": median_response_days,
                "median_turnaround_days": median_turnaround_days,
                "mean_score": mean_score,
                "last_submitted_at": last_submitted_at,
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

        def _parse_reviewer_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewer_uuid_type_0 = UUID(data)

                return reviewer_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        reviewer_uuid = _parse_reviewer_uuid(d.pop("reviewer_uuid"))

        reviewer_name = d.pop("reviewer_name")

        reviewer_email = d.pop("reviewer_email")

        def _parse_is_active(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        is_active = _parse_is_active(d.pop("is_active"))

        def _parse_median_response_days(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        median_response_days = _parse_median_response_days(d.pop("median_response_days"))

        def _parse_median_turnaround_days(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        median_turnaround_days = _parse_median_turnaround_days(d.pop("median_turnaround_days"))

        def _parse_mean_score(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        mean_score = _parse_mean_score(d.pop("mean_score"))

        def _parse_last_submitted_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_submitted_at_type_0 = isoparse(data)

                return last_submitted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_submitted_at = _parse_last_submitted_at(d.pop("last_submitted_at"))

        reviewer_report_row = cls(
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
            reviewer_uuid=reviewer_uuid,
            reviewer_name=reviewer_name,
            reviewer_email=reviewer_email,
            is_active=is_active,
            median_response_days=median_response_days,
            median_turnaround_days=median_turnaround_days,
            mean_score=mean_score,
            last_submitted_at=last_submitted_at,
        )

        reviewer_report_row.additional_properties = d
        return reviewer_report_row

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
