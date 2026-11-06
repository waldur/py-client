import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="PortfolioReportRound")


@_attrs_define
class PortfolioReportRound:
    """
    Attributes:
        proposals (int): Proposals counted: those submitted within the dates when dates are given, else every proposal,
            drafts included.
        submitted (int): Proposals that left draft: they have a submission time.
        draft (int):
        awaiting_review (int): Submitted, not yet taken into evaluation.
        in_review (int):
        accepted (int):
        rejected (int):
        canceled (int): Withdrawn or canceled.
        decided (int): Accepted plus rejected.
        success_rate (Union[None, float]): Accepted out of decided, 0-1; empty while none is decided.
        scored_reviews (int): Submitted reviews with an overall score.
        mean_score (Union[None, float]): Mean overall score of the submitted reviews, 1-5.
        active_rounds (int): Rounds open for submissions now: within their submission window, of an active call.
        round_uuid (UUID):
        round_name (str):
        round_slug (str):
        start_time (datetime.datetime):
        cutoff_time (Union[None, datetime.datetime]):
    """

    proposals: int
    submitted: int
    draft: int
    awaiting_review: int
    in_review: int
    accepted: int
    rejected: int
    canceled: int
    decided: int
    success_rate: Union[None, float]
    scored_reviews: int
    mean_score: Union[None, float]
    active_rounds: int
    round_uuid: UUID
    round_name: str
    round_slug: str
    start_time: datetime.datetime
    cutoff_time: Union[None, datetime.datetime]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposals = self.proposals

        submitted = self.submitted

        draft = self.draft

        awaiting_review = self.awaiting_review

        in_review = self.in_review

        accepted = self.accepted

        rejected = self.rejected

        canceled = self.canceled

        decided = self.decided

        success_rate: Union[None, float]
        success_rate = self.success_rate

        scored_reviews = self.scored_reviews

        mean_score: Union[None, float]
        mean_score = self.mean_score

        active_rounds = self.active_rounds

        round_uuid = str(self.round_uuid)

        round_name = self.round_name

        round_slug = self.round_slug

        start_time = self.start_time.isoformat()

        cutoff_time: Union[None, str]
        if isinstance(self.cutoff_time, datetime.datetime):
            cutoff_time = self.cutoff_time.isoformat()
        else:
            cutoff_time = self.cutoff_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposals": proposals,
                "submitted": submitted,
                "draft": draft,
                "awaiting_review": awaiting_review,
                "in_review": in_review,
                "accepted": accepted,
                "rejected": rejected,
                "canceled": canceled,
                "decided": decided,
                "success_rate": success_rate,
                "scored_reviews": scored_reviews,
                "mean_score": mean_score,
                "active_rounds": active_rounds,
                "round_uuid": round_uuid,
                "round_name": round_name,
                "round_slug": round_slug,
                "start_time": start_time,
                "cutoff_time": cutoff_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        proposals = d.pop("proposals")

        submitted = d.pop("submitted")

        draft = d.pop("draft")

        awaiting_review = d.pop("awaiting_review")

        in_review = d.pop("in_review")

        accepted = d.pop("accepted")

        rejected = d.pop("rejected")

        canceled = d.pop("canceled")

        decided = d.pop("decided")

        def _parse_success_rate(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        success_rate = _parse_success_rate(d.pop("success_rate"))

        scored_reviews = d.pop("scored_reviews")

        def _parse_mean_score(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        mean_score = _parse_mean_score(d.pop("mean_score"))

        active_rounds = d.pop("active_rounds")

        round_uuid = UUID(d.pop("round_uuid"))

        round_name = d.pop("round_name")

        round_slug = d.pop("round_slug")

        start_time = isoparse(d.pop("start_time"))

        def _parse_cutoff_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cutoff_time_type_0 = isoparse(data)

                return cutoff_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        cutoff_time = _parse_cutoff_time(d.pop("cutoff_time"))

        portfolio_report_round = cls(
            proposals=proposals,
            submitted=submitted,
            draft=draft,
            awaiting_review=awaiting_review,
            in_review=in_review,
            accepted=accepted,
            rejected=rejected,
            canceled=canceled,
            decided=decided,
            success_rate=success_rate,
            scored_reviews=scored_reviews,
            mean_score=mean_score,
            active_rounds=active_rounds,
            round_uuid=round_uuid,
            round_name=round_name,
            round_slug=round_slug,
            start_time=start_time,
            cutoff_time=cutoff_time,
        )

        portfolio_report_round.additional_properties = d
        return portfolio_report_round

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
