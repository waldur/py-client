import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.proposal_review_state_enum import ProposalReviewStateEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proposal_review_criteria_scores import ProposalReviewCriteriaScores
    from ..models.review_criterion import ReviewCriterion


T = TypeVar("T", bound="ProposalReview")


@_attrs_define
class ProposalReview:
    """
    Attributes:
        url (str):
        uuid (UUID):
        proposal (str):
        proposal_name (str):
        proposal_uuid (UUID):
        proposal_slug (str):
        reviewer_email (str):
        reviewer_organization (str):
        reviewer_image (str):
        state (ProposalReviewStateEnum):
        review_end_date (Union[None, datetime.datetime]): When the review is due, or None when nothing sets a deadline.

            The deadline of the step the review contributes to. A review whose
            step has none -- not started yet, or with no duration -- falls back
            to the round's review duration from its creation, as before steps had
            deadlines. A review created by accepting an assignment is also due no
            earlier than its assignment batch's deadline, so extending the batch
            deadline moves the deadline of the reviews accepted from it.
        criteria (list['ReviewCriterion']): The criteria of the step the review is given in, each rated 1-5 in
            criteria_scores and weighted in the summary_score. Empty when the step has none, and the review is then rated by
            its summary_score alone.
        round_uuid (UUID):
        round_name (str):
        round_slug (str):
        round_cutoff_time (Union[None, datetime.datetime]): When submission closes. Empty: the round stays open until a
            call manager closes it.
        round_start_time (datetime.datetime):
        call_name (str):
        call_uuid (UUID):
        call_slug (str):
        call_managing_organisation_uuid (UUID):
        coi_confirmed (bool): Reviewer confirmed absence of conflict of interest with this proposal.
        coi_confirmed_at (Union[None, datetime.datetime]):
        coi_confirmation_required (bool):
        coi_declaration_text (str): The conflict-of-interest declaration the reviewer confirms: as confirmed once they
            did, else as worded now. Empty for the platform's standard declaration.
        submitted_at (Union[None, datetime.datetime]): When the reviewer submitted the review. Empty while it is not
            submitted, and for reviews submitted before this was recorded.
        created (datetime.datetime):
        modified (datetime.datetime):
        reviewer (Union[Unset, str]):
        reviewer_full_name (Union[Unset, str]):
        reviewer_uuid (Union[Unset, UUID]):
        anonymous_reviewer_name (Union[None, Unset, str]): Generate an anonymous reviewer identifier like 'Reviewer 1',
            'Reviewer 2'.
            Returns None if the review is not associated with a proposal.
        summary_score (Union[Unset, int]): The review's overall score, 1-5 (0 until rated). When the step has criteria,
            it is their weighted average.
        criteria_scores (Union[Unset, ProposalReviewCriteriaScores]): Score per criterion, 1-5, keyed by criterion UUID.
            Writing it replaces the scores, and summary_score becomes their weighted average, rounded half up.
        summary_public_comment (Union[Unset, str]):
        summary_private_comment (Union[Unset, str]):
        comment_project_title (Union[None, Unset, str]):
        comment_project_summary (Union[None, Unset, str]):
        comment_project_description (Union[None, Unset, str]):
        comment_project_supporting_documentation (Union[None, Unset, str]):
        comment_resource_requests (Union[None, Unset, str]):
        comment_team (Union[None, Unset, str]):
    """

    url: str
    uuid: UUID
    proposal: str
    proposal_name: str
    proposal_uuid: UUID
    proposal_slug: str
    reviewer_email: str
    reviewer_organization: str
    reviewer_image: str
    state: ProposalReviewStateEnum
    review_end_date: Union[None, datetime.datetime]
    criteria: list["ReviewCriterion"]
    round_uuid: UUID
    round_name: str
    round_slug: str
    round_cutoff_time: Union[None, datetime.datetime]
    round_start_time: datetime.datetime
    call_name: str
    call_uuid: UUID
    call_slug: str
    call_managing_organisation_uuid: UUID
    coi_confirmed: bool
    coi_confirmed_at: Union[None, datetime.datetime]
    coi_confirmation_required: bool
    coi_declaration_text: str
    submitted_at: Union[None, datetime.datetime]
    created: datetime.datetime
    modified: datetime.datetime
    reviewer: Union[Unset, str] = UNSET
    reviewer_full_name: Union[Unset, str] = UNSET
    reviewer_uuid: Union[Unset, UUID] = UNSET
    anonymous_reviewer_name: Union[None, Unset, str] = UNSET
    summary_score: Union[Unset, int] = UNSET
    criteria_scores: Union[Unset, "ProposalReviewCriteriaScores"] = UNSET
    summary_public_comment: Union[Unset, str] = UNSET
    summary_private_comment: Union[Unset, str] = UNSET
    comment_project_title: Union[None, Unset, str] = UNSET
    comment_project_summary: Union[None, Unset, str] = UNSET
    comment_project_description: Union[None, Unset, str] = UNSET
    comment_project_supporting_documentation: Union[None, Unset, str] = UNSET
    comment_resource_requests: Union[None, Unset, str] = UNSET
    comment_team: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        proposal = self.proposal

        proposal_name = self.proposal_name

        proposal_uuid = str(self.proposal_uuid)

        proposal_slug = self.proposal_slug

        reviewer_email = self.reviewer_email

        reviewer_organization = self.reviewer_organization

        reviewer_image = self.reviewer_image

        state = self.state.value

        review_end_date: Union[None, str]
        if isinstance(self.review_end_date, datetime.datetime):
            review_end_date = self.review_end_date.isoformat()
        else:
            review_end_date = self.review_end_date

        criteria = []
        for criteria_item_data in self.criteria:
            criteria_item = criteria_item_data.to_dict()
            criteria.append(criteria_item)

        round_uuid = str(self.round_uuid)

        round_name = self.round_name

        round_slug = self.round_slug

        round_cutoff_time: Union[None, str]
        if isinstance(self.round_cutoff_time, datetime.datetime):
            round_cutoff_time = self.round_cutoff_time.isoformat()
        else:
            round_cutoff_time = self.round_cutoff_time

        round_start_time = self.round_start_time.isoformat()

        call_name = self.call_name

        call_uuid = str(self.call_uuid)

        call_slug = self.call_slug

        call_managing_organisation_uuid = str(self.call_managing_organisation_uuid)

        coi_confirmed = self.coi_confirmed

        coi_confirmed_at: Union[None, str]
        if isinstance(self.coi_confirmed_at, datetime.datetime):
            coi_confirmed_at = self.coi_confirmed_at.isoformat()
        else:
            coi_confirmed_at = self.coi_confirmed_at

        coi_confirmation_required = self.coi_confirmation_required

        coi_declaration_text = self.coi_declaration_text

        submitted_at: Union[None, str]
        if isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        reviewer = self.reviewer

        reviewer_full_name = self.reviewer_full_name

        reviewer_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.reviewer_uuid, Unset):
            reviewer_uuid = str(self.reviewer_uuid)

        anonymous_reviewer_name: Union[None, Unset, str]
        if isinstance(self.anonymous_reviewer_name, Unset):
            anonymous_reviewer_name = UNSET
        else:
            anonymous_reviewer_name = self.anonymous_reviewer_name

        summary_score = self.summary_score

        criteria_scores: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.criteria_scores, Unset):
            criteria_scores = self.criteria_scores.to_dict()

        summary_public_comment = self.summary_public_comment

        summary_private_comment = self.summary_private_comment

        comment_project_title: Union[None, Unset, str]
        if isinstance(self.comment_project_title, Unset):
            comment_project_title = UNSET
        else:
            comment_project_title = self.comment_project_title

        comment_project_summary: Union[None, Unset, str]
        if isinstance(self.comment_project_summary, Unset):
            comment_project_summary = UNSET
        else:
            comment_project_summary = self.comment_project_summary

        comment_project_description: Union[None, Unset, str]
        if isinstance(self.comment_project_description, Unset):
            comment_project_description = UNSET
        else:
            comment_project_description = self.comment_project_description

        comment_project_supporting_documentation: Union[None, Unset, str]
        if isinstance(self.comment_project_supporting_documentation, Unset):
            comment_project_supporting_documentation = UNSET
        else:
            comment_project_supporting_documentation = self.comment_project_supporting_documentation

        comment_resource_requests: Union[None, Unset, str]
        if isinstance(self.comment_resource_requests, Unset):
            comment_resource_requests = UNSET
        else:
            comment_resource_requests = self.comment_resource_requests

        comment_team: Union[None, Unset, str]
        if isinstance(self.comment_team, Unset):
            comment_team = UNSET
        else:
            comment_team = self.comment_team

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "proposal": proposal,
                "proposal_name": proposal_name,
                "proposal_uuid": proposal_uuid,
                "proposal_slug": proposal_slug,
                "reviewer_email": reviewer_email,
                "reviewer_organization": reviewer_organization,
                "reviewer_image": reviewer_image,
                "state": state,
                "review_end_date": review_end_date,
                "criteria": criteria,
                "round_uuid": round_uuid,
                "round_name": round_name,
                "round_slug": round_slug,
                "round_cutoff_time": round_cutoff_time,
                "round_start_time": round_start_time,
                "call_name": call_name,
                "call_uuid": call_uuid,
                "call_slug": call_slug,
                "call_managing_organisation_uuid": call_managing_organisation_uuid,
                "coi_confirmed": coi_confirmed,
                "coi_confirmed_at": coi_confirmed_at,
                "coi_confirmation_required": coi_confirmation_required,
                "coi_declaration_text": coi_declaration_text,
                "submitted_at": submitted_at,
                "created": created,
                "modified": modified,
            }
        )
        if reviewer is not UNSET:
            field_dict["reviewer"] = reviewer
        if reviewer_full_name is not UNSET:
            field_dict["reviewer_full_name"] = reviewer_full_name
        if reviewer_uuid is not UNSET:
            field_dict["reviewer_uuid"] = reviewer_uuid
        if anonymous_reviewer_name is not UNSET:
            field_dict["anonymous_reviewer_name"] = anonymous_reviewer_name
        if summary_score is not UNSET:
            field_dict["summary_score"] = summary_score
        if criteria_scores is not UNSET:
            field_dict["criteria_scores"] = criteria_scores
        if summary_public_comment is not UNSET:
            field_dict["summary_public_comment"] = summary_public_comment
        if summary_private_comment is not UNSET:
            field_dict["summary_private_comment"] = summary_private_comment
        if comment_project_title is not UNSET:
            field_dict["comment_project_title"] = comment_project_title
        if comment_project_summary is not UNSET:
            field_dict["comment_project_summary"] = comment_project_summary
        if comment_project_description is not UNSET:
            field_dict["comment_project_description"] = comment_project_description
        if comment_project_supporting_documentation is not UNSET:
            field_dict["comment_project_supporting_documentation"] = comment_project_supporting_documentation
        if comment_resource_requests is not UNSET:
            field_dict["comment_resource_requests"] = comment_resource_requests
        if comment_team is not UNSET:
            field_dict["comment_team"] = comment_team

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_review_criteria_scores import ProposalReviewCriteriaScores
        from ..models.review_criterion import ReviewCriterion

        d = dict(src_dict)
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        proposal = d.pop("proposal")

        proposal_name = d.pop("proposal_name")

        proposal_uuid = UUID(d.pop("proposal_uuid"))

        proposal_slug = d.pop("proposal_slug")

        reviewer_email = d.pop("reviewer_email")

        reviewer_organization = d.pop("reviewer_organization")

        reviewer_image = d.pop("reviewer_image")

        state = ProposalReviewStateEnum(d.pop("state"))

        def _parse_review_end_date(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                review_end_date_type_0 = isoparse(data)

                return review_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        review_end_date = _parse_review_end_date(d.pop("review_end_date"))

        criteria = []
        _criteria = d.pop("criteria")
        for criteria_item_data in _criteria:
            criteria_item = ReviewCriterion.from_dict(criteria_item_data)

            criteria.append(criteria_item)

        round_uuid = UUID(d.pop("round_uuid"))

        round_name = d.pop("round_name")

        round_slug = d.pop("round_slug")

        def _parse_round_cutoff_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_cutoff_time_type_0 = isoparse(data)

                return round_cutoff_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        round_cutoff_time = _parse_round_cutoff_time(d.pop("round_cutoff_time"))

        round_start_time = isoparse(d.pop("round_start_time"))

        call_name = d.pop("call_name")

        call_uuid = UUID(d.pop("call_uuid"))

        call_slug = d.pop("call_slug")

        call_managing_organisation_uuid = UUID(d.pop("call_managing_organisation_uuid"))

        coi_confirmed = d.pop("coi_confirmed")

        def _parse_coi_confirmed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                coi_confirmed_at_type_0 = isoparse(data)

                return coi_confirmed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        coi_confirmed_at = _parse_coi_confirmed_at(d.pop("coi_confirmed_at"))

        coi_confirmation_required = d.pop("coi_confirmation_required")

        coi_declaration_text = d.pop("coi_declaration_text")

        def _parse_submitted_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = isoparse(data)

                return submitted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        reviewer = d.pop("reviewer", UNSET)

        reviewer_full_name = d.pop("reviewer_full_name", UNSET)

        _reviewer_uuid = d.pop("reviewer_uuid", UNSET)
        reviewer_uuid: Union[Unset, UUID]
        if isinstance(_reviewer_uuid, Unset):
            reviewer_uuid = UNSET
        else:
            reviewer_uuid = UUID(_reviewer_uuid)

        def _parse_anonymous_reviewer_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        anonymous_reviewer_name = _parse_anonymous_reviewer_name(d.pop("anonymous_reviewer_name", UNSET))

        summary_score = d.pop("summary_score", UNSET)

        _criteria_scores = d.pop("criteria_scores", UNSET)
        criteria_scores: Union[Unset, ProposalReviewCriteriaScores]
        if isinstance(_criteria_scores, Unset):
            criteria_scores = UNSET
        else:
            criteria_scores = ProposalReviewCriteriaScores.from_dict(_criteria_scores)

        summary_public_comment = d.pop("summary_public_comment", UNSET)

        summary_private_comment = d.pop("summary_private_comment", UNSET)

        def _parse_comment_project_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment_project_title = _parse_comment_project_title(d.pop("comment_project_title", UNSET))

        def _parse_comment_project_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment_project_summary = _parse_comment_project_summary(d.pop("comment_project_summary", UNSET))

        def _parse_comment_project_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment_project_description = _parse_comment_project_description(d.pop("comment_project_description", UNSET))

        def _parse_comment_project_supporting_documentation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment_project_supporting_documentation = _parse_comment_project_supporting_documentation(
            d.pop("comment_project_supporting_documentation", UNSET)
        )

        def _parse_comment_resource_requests(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment_resource_requests = _parse_comment_resource_requests(d.pop("comment_resource_requests", UNSET))

        def _parse_comment_team(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment_team = _parse_comment_team(d.pop("comment_team", UNSET))

        proposal_review = cls(
            url=url,
            uuid=uuid,
            proposal=proposal,
            proposal_name=proposal_name,
            proposal_uuid=proposal_uuid,
            proposal_slug=proposal_slug,
            reviewer_email=reviewer_email,
            reviewer_organization=reviewer_organization,
            reviewer_image=reviewer_image,
            state=state,
            review_end_date=review_end_date,
            criteria=criteria,
            round_uuid=round_uuid,
            round_name=round_name,
            round_slug=round_slug,
            round_cutoff_time=round_cutoff_time,
            round_start_time=round_start_time,
            call_name=call_name,
            call_uuid=call_uuid,
            call_slug=call_slug,
            call_managing_organisation_uuid=call_managing_organisation_uuid,
            coi_confirmed=coi_confirmed,
            coi_confirmed_at=coi_confirmed_at,
            coi_confirmation_required=coi_confirmation_required,
            coi_declaration_text=coi_declaration_text,
            submitted_at=submitted_at,
            created=created,
            modified=modified,
            reviewer=reviewer,
            reviewer_full_name=reviewer_full_name,
            reviewer_uuid=reviewer_uuid,
            anonymous_reviewer_name=anonymous_reviewer_name,
            summary_score=summary_score,
            criteria_scores=criteria_scores,
            summary_public_comment=summary_public_comment,
            summary_private_comment=summary_private_comment,
            comment_project_title=comment_project_title,
            comment_project_summary=comment_project_summary,
            comment_project_description=comment_project_description,
            comment_project_supporting_documentation=comment_project_supporting_documentation,
            comment_resource_requests=comment_resource_requests,
            comment_team=comment_team,
        )

        proposal_review.additional_properties = d
        return proposal_review

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
