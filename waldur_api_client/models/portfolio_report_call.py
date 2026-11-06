from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.portfolio_report_round import PortfolioReportRound


T = TypeVar("T", bound="PortfolioReportCall")


@_attrs_define
class PortfolioReportCall:
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
        call_uuid (UUID):
        call_name (str):
        call_slug (str):
        organisation_uuid (UUID): The call's call managing organization.
        organisation_name (str): The name of the call managing organization's customer.
        call_state (str):
        rounds (list['PortfolioReportRound']):
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
    call_uuid: UUID
    call_name: str
    call_slug: str
    organisation_uuid: UUID
    organisation_name: str
    call_state: str
    rounds: list["PortfolioReportRound"]
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

        call_uuid = str(self.call_uuid)

        call_name = self.call_name

        call_slug = self.call_slug

        organisation_uuid = str(self.organisation_uuid)

        organisation_name = self.organisation_name

        call_state = self.call_state

        rounds = []
        for rounds_item_data in self.rounds:
            rounds_item = rounds_item_data.to_dict()
            rounds.append(rounds_item)

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
                "call_uuid": call_uuid,
                "call_name": call_name,
                "call_slug": call_slug,
                "organisation_uuid": organisation_uuid,
                "organisation_name": organisation_name,
                "call_state": call_state,
                "rounds": rounds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portfolio_report_round import PortfolioReportRound

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

        call_uuid = UUID(d.pop("call_uuid"))

        call_name = d.pop("call_name")

        call_slug = d.pop("call_slug")

        organisation_uuid = UUID(d.pop("organisation_uuid"))

        organisation_name = d.pop("organisation_name")

        call_state = d.pop("call_state")

        rounds = []
        _rounds = d.pop("rounds")
        for rounds_item_data in _rounds:
            rounds_item = PortfolioReportRound.from_dict(rounds_item_data)

            rounds.append(rounds_item)

        portfolio_report_call = cls(
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
            call_uuid=call_uuid,
            call_name=call_name,
            call_slug=call_slug,
            organisation_uuid=organisation_uuid,
            organisation_name=organisation_name,
            call_state=call_state,
            rounds=rounds,
        )

        portfolio_report_call.additional_properties = d
        return portfolio_report_call

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
