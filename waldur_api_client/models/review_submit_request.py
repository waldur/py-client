from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.review_submit_request_criteria_scores import ReviewSubmitRequestCriteriaScores


T = TypeVar("T", bound="ReviewSubmitRequest")


@_attrs_define
class ReviewSubmitRequest:
    """
    Attributes:
        summary_score (Union[Unset, int]): The review's overall score, 1-5 (0 until rated). When the step has criteria,
            it is their weighted average.
        criteria_scores (Union[Unset, ReviewSubmitRequestCriteriaScores]): Score per criterion, keyed by criterion UUID;
            the review's saved scores when left out. Every criterion of the step must be scored.
        summary_public_comment (Union[Unset, str]):
        summary_private_comment (Union[Unset, str]):
        coi_confirmed (Union[Unset, bool]): Reviewer confirmed absence of conflict of interest with this proposal.
    """

    summary_score: Union[Unset, int] = UNSET
    criteria_scores: Union[Unset, "ReviewSubmitRequestCriteriaScores"] = UNSET
    summary_public_comment: Union[Unset, str] = UNSET
    summary_private_comment: Union[Unset, str] = UNSET
    coi_confirmed: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary_score = self.summary_score

        criteria_scores: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.criteria_scores, Unset):
            criteria_scores = self.criteria_scores.to_dict()

        summary_public_comment = self.summary_public_comment

        summary_private_comment = self.summary_private_comment

        coi_confirmed = self.coi_confirmed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary_score is not UNSET:
            field_dict["summary_score"] = summary_score
        if criteria_scores is not UNSET:
            field_dict["criteria_scores"] = criteria_scores
        if summary_public_comment is not UNSET:
            field_dict["summary_public_comment"] = summary_public_comment
        if summary_private_comment is not UNSET:
            field_dict["summary_private_comment"] = summary_private_comment
        if coi_confirmed is not UNSET:
            field_dict["coi_confirmed"] = coi_confirmed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_submit_request_criteria_scores import ReviewSubmitRequestCriteriaScores

        d = dict(src_dict)
        summary_score = d.pop("summary_score", UNSET)

        _criteria_scores = d.pop("criteria_scores", UNSET)
        criteria_scores: Union[Unset, ReviewSubmitRequestCriteriaScores]
        if isinstance(_criteria_scores, Unset):
            criteria_scores = UNSET
        else:
            criteria_scores = ReviewSubmitRequestCriteriaScores.from_dict(_criteria_scores)

        summary_public_comment = d.pop("summary_public_comment", UNSET)

        summary_private_comment = d.pop("summary_private_comment", UNSET)

        coi_confirmed = d.pop("coi_confirmed", UNSET)

        review_submit_request = cls(
            summary_score=summary_score,
            criteria_scores=criteria_scores,
            summary_public_comment=summary_public_comment,
            summary_private_comment=summary_private_comment,
            coi_confirmed=coi_confirmed,
        )

        review_submit_request.additional_properties = d
        return review_submit_request

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
