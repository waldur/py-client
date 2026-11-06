import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.assignment_batch_status import AssignmentBatchStatus
from ..models.proposal_reviewer_suggestion_status import ProposalReviewerSuggestionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reviewer_suggestion_entry import ReviewerSuggestionEntry
    from ..models.suggested_reviewer_conflict import SuggestedReviewerConflict


T = TypeVar("T", bound="SuggestedReviewer")


@_attrs_define
class SuggestedReviewer:
    """
    Attributes:
        key (str): Identifies the suggested person within the proposal.
        email (str): The person's address, for staff, support and those overseeing the call; for anyone else only an
            address an evaluator typed, blank for a user they picked.
        status (ProposalReviewerSuggestionStatus):
        suggestions (list['ReviewerSuggestionEntry']):
        suggestion_uuids (list[UUID]):
        conflicts (list['SuggestedReviewerConflict']):
        has_conflict (bool): A conflict of interest stands between the person and the proposal.
        is_applicant_excluded (bool): The applicant asked for the person not to review the proposal.
        holds_evaluator_role (bool):
        is_on_applicant_team (bool):
        already_in_pool (bool):
        suggested_user_uuid (Union[None, UUID, Unset]):
        suggested_user_name (Union[None, Unset, str]):
        pool_entry_uuid (Union[None, UUID, Unset]):
        invitation_expires_at (Union[None, Unset, datetime.datetime]):
        assignment_batch_status (Union[AssignmentBatchStatus, None, Unset]): Where the latest assignment of the person
            to the proposal stands; draft until the call manager sends its batch.
    """

    key: str
    email: str
    status: ProposalReviewerSuggestionStatus
    suggestions: list["ReviewerSuggestionEntry"]
    suggestion_uuids: list[UUID]
    conflicts: list["SuggestedReviewerConflict"]
    has_conflict: bool
    is_applicant_excluded: bool
    holds_evaluator_role: bool
    is_on_applicant_team: bool
    already_in_pool: bool
    suggested_user_uuid: Union[None, UUID, Unset] = UNSET
    suggested_user_name: Union[None, Unset, str] = UNSET
    pool_entry_uuid: Union[None, UUID, Unset] = UNSET
    invitation_expires_at: Union[None, Unset, datetime.datetime] = UNSET
    assignment_batch_status: Union[AssignmentBatchStatus, None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        email = self.email

        status = self.status.value

        suggestions = []
        for suggestions_item_data in self.suggestions:
            suggestions_item = suggestions_item_data.to_dict()
            suggestions.append(suggestions_item)

        suggestion_uuids = []
        for suggestion_uuids_item_data in self.suggestion_uuids:
            suggestion_uuids_item = str(suggestion_uuids_item_data)
            suggestion_uuids.append(suggestion_uuids_item)

        conflicts = []
        for conflicts_item_data in self.conflicts:
            conflicts_item = conflicts_item_data.to_dict()
            conflicts.append(conflicts_item)

        has_conflict = self.has_conflict

        is_applicant_excluded = self.is_applicant_excluded

        holds_evaluator_role = self.holds_evaluator_role

        is_on_applicant_team = self.is_on_applicant_team

        already_in_pool = self.already_in_pool

        suggested_user_uuid: Union[None, Unset, str]
        if isinstance(self.suggested_user_uuid, Unset):
            suggested_user_uuid = UNSET
        elif isinstance(self.suggested_user_uuid, UUID):
            suggested_user_uuid = str(self.suggested_user_uuid)
        else:
            suggested_user_uuid = self.suggested_user_uuid

        suggested_user_name: Union[None, Unset, str]
        if isinstance(self.suggested_user_name, Unset):
            suggested_user_name = UNSET
        else:
            suggested_user_name = self.suggested_user_name

        pool_entry_uuid: Union[None, Unset, str]
        if isinstance(self.pool_entry_uuid, Unset):
            pool_entry_uuid = UNSET
        elif isinstance(self.pool_entry_uuid, UUID):
            pool_entry_uuid = str(self.pool_entry_uuid)
        else:
            pool_entry_uuid = self.pool_entry_uuid

        invitation_expires_at: Union[None, Unset, str]
        if isinstance(self.invitation_expires_at, Unset):
            invitation_expires_at = UNSET
        elif isinstance(self.invitation_expires_at, datetime.datetime):
            invitation_expires_at = self.invitation_expires_at.isoformat()
        else:
            invitation_expires_at = self.invitation_expires_at

        assignment_batch_status: Union[None, Unset, str]
        if isinstance(self.assignment_batch_status, Unset):
            assignment_batch_status = UNSET
        elif isinstance(self.assignment_batch_status, AssignmentBatchStatus):
            assignment_batch_status = self.assignment_batch_status.value
        else:
            assignment_batch_status = self.assignment_batch_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "email": email,
                "status": status,
                "suggestions": suggestions,
                "suggestion_uuids": suggestion_uuids,
                "conflicts": conflicts,
                "has_conflict": has_conflict,
                "is_applicant_excluded": is_applicant_excluded,
                "holds_evaluator_role": holds_evaluator_role,
                "is_on_applicant_team": is_on_applicant_team,
                "already_in_pool": already_in_pool,
            }
        )
        if suggested_user_uuid is not UNSET:
            field_dict["suggested_user_uuid"] = suggested_user_uuid
        if suggested_user_name is not UNSET:
            field_dict["suggested_user_name"] = suggested_user_name
        if pool_entry_uuid is not UNSET:
            field_dict["pool_entry_uuid"] = pool_entry_uuid
        if invitation_expires_at is not UNSET:
            field_dict["invitation_expires_at"] = invitation_expires_at
        if assignment_batch_status is not UNSET:
            field_dict["assignment_batch_status"] = assignment_batch_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reviewer_suggestion_entry import ReviewerSuggestionEntry
        from ..models.suggested_reviewer_conflict import SuggestedReviewerConflict

        d = dict(src_dict)
        key = d.pop("key")

        email = d.pop("email")

        status = ProposalReviewerSuggestionStatus(d.pop("status"))

        suggestions = []
        _suggestions = d.pop("suggestions")
        for suggestions_item_data in _suggestions:
            suggestions_item = ReviewerSuggestionEntry.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        suggestion_uuids = []
        _suggestion_uuids = d.pop("suggestion_uuids")
        for suggestion_uuids_item_data in _suggestion_uuids:
            suggestion_uuids_item = UUID(suggestion_uuids_item_data)

            suggestion_uuids.append(suggestion_uuids_item)

        conflicts = []
        _conflicts = d.pop("conflicts")
        for conflicts_item_data in _conflicts:
            conflicts_item = SuggestedReviewerConflict.from_dict(conflicts_item_data)

            conflicts.append(conflicts_item)

        has_conflict = d.pop("has_conflict")

        is_applicant_excluded = d.pop("is_applicant_excluded")

        holds_evaluator_role = d.pop("holds_evaluator_role")

        is_on_applicant_team = d.pop("is_on_applicant_team")

        already_in_pool = d.pop("already_in_pool")

        def _parse_suggested_user_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suggested_user_uuid_type_0 = UUID(data)

                return suggested_user_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        suggested_user_uuid = _parse_suggested_user_uuid(d.pop("suggested_user_uuid", UNSET))

        def _parse_suggested_user_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suggested_user_name = _parse_suggested_user_name(d.pop("suggested_user_name", UNSET))

        def _parse_pool_entry_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pool_entry_uuid_type_0 = UUID(data)

                return pool_entry_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        pool_entry_uuid = _parse_pool_entry_uuid(d.pop("pool_entry_uuid", UNSET))

        def _parse_invitation_expires_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invitation_expires_at_type_0 = isoparse(data)

                return invitation_expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        invitation_expires_at = _parse_invitation_expires_at(d.pop("invitation_expires_at", UNSET))

        def _parse_assignment_batch_status(data: object) -> Union[AssignmentBatchStatus, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assignment_batch_status_type_0 = AssignmentBatchStatus(data)

                return assignment_batch_status_type_0
            except:  # noqa: E722
                pass
            return cast(Union[AssignmentBatchStatus, None, Unset], data)

        assignment_batch_status = _parse_assignment_batch_status(d.pop("assignment_batch_status", UNSET))

        suggested_reviewer = cls(
            key=key,
            email=email,
            status=status,
            suggestions=suggestions,
            suggestion_uuids=suggestion_uuids,
            conflicts=conflicts,
            has_conflict=has_conflict,
            is_applicant_excluded=is_applicant_excluded,
            holds_evaluator_role=holds_evaluator_role,
            is_on_applicant_team=is_on_applicant_team,
            already_in_pool=already_in_pool,
            suggested_user_uuid=suggested_user_uuid,
            suggested_user_name=suggested_user_name,
            pool_entry_uuid=pool_entry_uuid,
            invitation_expires_at=invitation_expires_at,
            assignment_batch_status=assignment_batch_status,
        )

        suggested_reviewer.additional_properties = d
        return suggested_reviewer

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
