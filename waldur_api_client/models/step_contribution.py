import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.step_contribution_status import StepContributionStatus

if TYPE_CHECKING:
    from ..models.contribution_delegation_candidate import ContributionDelegationCandidate


T = TypeVar("T", bound="StepContribution")


@_attrs_define
class StepContribution:
    """
    Attributes:
        uuid (UUID):
        proposal_step_uuid (UUID):
        call_step_uuid (UUID):
        step_name (str):
        is_per_offering (bool):
        requested_offering_uuid (Union[None, UUID]):
        offering_uuid (Union[None, UUID]):
        offering_name (Union[None, str]):
        contributor_uuid (Union[None, UUID]):
        contributor_full_name (Union[None, str]):
        is_lead (bool):
        status (StepContributionStatus):
        outcome (str):
        conditions (str):
        comment (str):
        review_uuid (Union[None, UUID]):
        due_at (Union[None, datetime.datetime]):
        submitted_at (Union[None, datetime.datetime]):
        can_fill (bool):
        checklist_completed (bool):
        unanswered_required_count (int):
        delegate_uuid (Union[None, UUID]): Who the slot is handed to, while they may take it over; hidden from whoever
            may not know who contributed.
        delegate_full_name (Union[None, str]):
        delegated_at (Union[None, datetime.datetime]):
        can_delegate (bool): Whether the caller may hand the slot to someone, or take it back.
        can_accept (bool): Whether the slot is handed to the caller, who has yet to accept it.
        coi_declaration_text (str): The conflict-of-interest declaration taking the slot over asks of the caller, while
            it is handed to them; otherwise the one its delegate confirmed. Empty for the platform's standard declaration,
            or when none is asked for.
        delegation_candidates (list['ContributionDelegationCandidate']): Who the caller may hand the slot to, when they
            may hand it on; empty otherwise.
    """

    uuid: UUID
    proposal_step_uuid: UUID
    call_step_uuid: UUID
    step_name: str
    is_per_offering: bool
    requested_offering_uuid: Union[None, UUID]
    offering_uuid: Union[None, UUID]
    offering_name: Union[None, str]
    contributor_uuid: Union[None, UUID]
    contributor_full_name: Union[None, str]
    is_lead: bool
    status: StepContributionStatus
    outcome: str
    conditions: str
    comment: str
    review_uuid: Union[None, UUID]
    due_at: Union[None, datetime.datetime]
    submitted_at: Union[None, datetime.datetime]
    can_fill: bool
    checklist_completed: bool
    unanswered_required_count: int
    delegate_uuid: Union[None, UUID]
    delegate_full_name: Union[None, str]
    delegated_at: Union[None, datetime.datetime]
    can_delegate: bool
    can_accept: bool
    coi_declaration_text: str
    delegation_candidates: list["ContributionDelegationCandidate"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        proposal_step_uuid = str(self.proposal_step_uuid)

        call_step_uuid = str(self.call_step_uuid)

        step_name = self.step_name

        is_per_offering = self.is_per_offering

        requested_offering_uuid: Union[None, str]
        if isinstance(self.requested_offering_uuid, UUID):
            requested_offering_uuid = str(self.requested_offering_uuid)
        else:
            requested_offering_uuid = self.requested_offering_uuid

        offering_uuid: Union[None, str]
        if isinstance(self.offering_uuid, UUID):
            offering_uuid = str(self.offering_uuid)
        else:
            offering_uuid = self.offering_uuid

        offering_name: Union[None, str]
        offering_name = self.offering_name

        contributor_uuid: Union[None, str]
        if isinstance(self.contributor_uuid, UUID):
            contributor_uuid = str(self.contributor_uuid)
        else:
            contributor_uuid = self.contributor_uuid

        contributor_full_name: Union[None, str]
        contributor_full_name = self.contributor_full_name

        is_lead = self.is_lead

        status = self.status.value

        outcome = self.outcome

        conditions = self.conditions

        comment = self.comment

        review_uuid: Union[None, str]
        if isinstance(self.review_uuid, UUID):
            review_uuid = str(self.review_uuid)
        else:
            review_uuid = self.review_uuid

        due_at: Union[None, str]
        if isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        submitted_at: Union[None, str]
        if isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        can_fill = self.can_fill

        checklist_completed = self.checklist_completed

        unanswered_required_count = self.unanswered_required_count

        delegate_uuid: Union[None, str]
        if isinstance(self.delegate_uuid, UUID):
            delegate_uuid = str(self.delegate_uuid)
        else:
            delegate_uuid = self.delegate_uuid

        delegate_full_name: Union[None, str]
        delegate_full_name = self.delegate_full_name

        delegated_at: Union[None, str]
        if isinstance(self.delegated_at, datetime.datetime):
            delegated_at = self.delegated_at.isoformat()
        else:
            delegated_at = self.delegated_at

        can_delegate = self.can_delegate

        can_accept = self.can_accept

        coi_declaration_text = self.coi_declaration_text

        delegation_candidates = []
        for delegation_candidates_item_data in self.delegation_candidates:
            delegation_candidates_item = delegation_candidates_item_data.to_dict()
            delegation_candidates.append(delegation_candidates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "proposal_step_uuid": proposal_step_uuid,
                "call_step_uuid": call_step_uuid,
                "step_name": step_name,
                "is_per_offering": is_per_offering,
                "requested_offering_uuid": requested_offering_uuid,
                "offering_uuid": offering_uuid,
                "offering_name": offering_name,
                "contributor_uuid": contributor_uuid,
                "contributor_full_name": contributor_full_name,
                "is_lead": is_lead,
                "status": status,
                "outcome": outcome,
                "conditions": conditions,
                "comment": comment,
                "review_uuid": review_uuid,
                "due_at": due_at,
                "submitted_at": submitted_at,
                "can_fill": can_fill,
                "checklist_completed": checklist_completed,
                "unanswered_required_count": unanswered_required_count,
                "delegate_uuid": delegate_uuid,
                "delegate_full_name": delegate_full_name,
                "delegated_at": delegated_at,
                "can_delegate": can_delegate,
                "can_accept": can_accept,
                "coi_declaration_text": coi_declaration_text,
                "delegation_candidates": delegation_candidates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contribution_delegation_candidate import ContributionDelegationCandidate

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        proposal_step_uuid = UUID(d.pop("proposal_step_uuid"))

        call_step_uuid = UUID(d.pop("call_step_uuid"))

        step_name = d.pop("step_name")

        is_per_offering = d.pop("is_per_offering")

        def _parse_requested_offering_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                requested_offering_uuid_type_0 = UUID(data)

                return requested_offering_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        requested_offering_uuid = _parse_requested_offering_uuid(d.pop("requested_offering_uuid"))

        def _parse_offering_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                offering_uuid_type_0 = UUID(data)

                return offering_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        offering_uuid = _parse_offering_uuid(d.pop("offering_uuid"))

        def _parse_offering_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        offering_name = _parse_offering_name(d.pop("offering_name"))

        def _parse_contributor_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contributor_uuid_type_0 = UUID(data)

                return contributor_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        contributor_uuid = _parse_contributor_uuid(d.pop("contributor_uuid"))

        def _parse_contributor_full_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        contributor_full_name = _parse_contributor_full_name(d.pop("contributor_full_name"))

        is_lead = d.pop("is_lead")

        status = StepContributionStatus(d.pop("status"))

        outcome = d.pop("outcome")

        conditions = d.pop("conditions")

        comment = d.pop("comment")

        def _parse_review_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                review_uuid_type_0 = UUID(data)

                return review_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        review_uuid = _parse_review_uuid(d.pop("review_uuid"))

        def _parse_due_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = isoparse(data)

                return due_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        due_at = _parse_due_at(d.pop("due_at"))

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

        can_fill = d.pop("can_fill")

        checklist_completed = d.pop("checklist_completed")

        unanswered_required_count = d.pop("unanswered_required_count")

        def _parse_delegate_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegate_uuid_type_0 = UUID(data)

                return delegate_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        delegate_uuid = _parse_delegate_uuid(d.pop("delegate_uuid"))

        def _parse_delegate_full_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        delegate_full_name = _parse_delegate_full_name(d.pop("delegate_full_name"))

        def _parse_delegated_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegated_at_type_0 = isoparse(data)

                return delegated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        delegated_at = _parse_delegated_at(d.pop("delegated_at"))

        can_delegate = d.pop("can_delegate")

        can_accept = d.pop("can_accept")

        coi_declaration_text = d.pop("coi_declaration_text")

        delegation_candidates = []
        _delegation_candidates = d.pop("delegation_candidates")
        for delegation_candidates_item_data in _delegation_candidates:
            delegation_candidates_item = ContributionDelegationCandidate.from_dict(delegation_candidates_item_data)

            delegation_candidates.append(delegation_candidates_item)

        step_contribution = cls(
            uuid=uuid,
            proposal_step_uuid=proposal_step_uuid,
            call_step_uuid=call_step_uuid,
            step_name=step_name,
            is_per_offering=is_per_offering,
            requested_offering_uuid=requested_offering_uuid,
            offering_uuid=offering_uuid,
            offering_name=offering_name,
            contributor_uuid=contributor_uuid,
            contributor_full_name=contributor_full_name,
            is_lead=is_lead,
            status=status,
            outcome=outcome,
            conditions=conditions,
            comment=comment,
            review_uuid=review_uuid,
            due_at=due_at,
            submitted_at=submitted_at,
            can_fill=can_fill,
            checklist_completed=checklist_completed,
            unanswered_required_count=unanswered_required_count,
            delegate_uuid=delegate_uuid,
            delegate_full_name=delegate_full_name,
            delegated_at=delegated_at,
            can_delegate=can_delegate,
            can_accept=can_accept,
            coi_declaration_text=coi_declaration_text,
            delegation_candidates=delegation_candidates,
        )

        step_contribution.additional_properties = d
        return step_contribution

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
