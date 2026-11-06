import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.proposal_run_state_enum import ProposalRunStateEnum
from ..models.workflow_phase_enum import WorkflowPhaseEnum

if TYPE_CHECKING:
    from ..models.proposal_run_applied_changes import ProposalRunAppliedChanges
    from ..models.proposal_run_granted_limits import ProposalRunGrantedLimits
    from ..models.proposal_run_requested_limits import ProposalRunRequestedLimits


T = TypeVar("T", bound="ProposalRun")


@_attrs_define
class ProposalRun:
    """
    Attributes:
        uuid (UUID):
        phase (WorkflowPhaseEnum):
        state (ProposalRunStateEnum):
        opened_at (datetime.datetime):
        opened_by_name (Union[None, str]):
        closed_at (Union[None, datetime.datetime]):
        requested_end_date (Union[None, datetime.date]): Extension: the end date the applicant asks for.
        requested_limits (ProposalRunRequestedLimits): Extension: the limits the applicant asks for, per resource.
        granted_end_date (Union[None, datetime.date]): Extension: the end date the decision grants.
        granted_limits (ProposalRunGrantedLimits): Extension: the limits the decision grants, per resource.
        granted_by_name (Union[None, str]): Extension: who set what the decision grants.
        applied_changes (ProposalRunAppliedChanges): Extension: what the approval changed -- the end date requests
            recorded and the orders created -- and what it left alone, and why.
        active_step_uuid (Union[None, UUID]): The run's step that is running now, if any.
        active_step_kind (Union[None, str]):
    """

    uuid: UUID
    phase: WorkflowPhaseEnum
    state: ProposalRunStateEnum
    opened_at: datetime.datetime
    opened_by_name: Union[None, str]
    closed_at: Union[None, datetime.datetime]
    requested_end_date: Union[None, datetime.date]
    requested_limits: "ProposalRunRequestedLimits"
    granted_end_date: Union[None, datetime.date]
    granted_limits: "ProposalRunGrantedLimits"
    granted_by_name: Union[None, str]
    applied_changes: "ProposalRunAppliedChanges"
    active_step_uuid: Union[None, UUID]
    active_step_kind: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        phase = self.phase.value

        state = self.state.value

        opened_at = self.opened_at.isoformat()

        opened_by_name: Union[None, str]
        opened_by_name = self.opened_by_name

        closed_at: Union[None, str]
        if isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        requested_end_date: Union[None, str]
        if isinstance(self.requested_end_date, datetime.date):
            requested_end_date = self.requested_end_date.isoformat()
        else:
            requested_end_date = self.requested_end_date

        requested_limits = self.requested_limits.to_dict()

        granted_end_date: Union[None, str]
        if isinstance(self.granted_end_date, datetime.date):
            granted_end_date = self.granted_end_date.isoformat()
        else:
            granted_end_date = self.granted_end_date

        granted_limits = self.granted_limits.to_dict()

        granted_by_name: Union[None, str]
        granted_by_name = self.granted_by_name

        applied_changes = self.applied_changes.to_dict()

        active_step_uuid: Union[None, str]
        if isinstance(self.active_step_uuid, UUID):
            active_step_uuid = str(self.active_step_uuid)
        else:
            active_step_uuid = self.active_step_uuid

        active_step_kind: Union[None, str]
        active_step_kind = self.active_step_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "phase": phase,
                "state": state,
                "opened_at": opened_at,
                "opened_by_name": opened_by_name,
                "closed_at": closed_at,
                "requested_end_date": requested_end_date,
                "requested_limits": requested_limits,
                "granted_end_date": granted_end_date,
                "granted_limits": granted_limits,
                "granted_by_name": granted_by_name,
                "applied_changes": applied_changes,
                "active_step_uuid": active_step_uuid,
                "active_step_kind": active_step_kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_run_applied_changes import ProposalRunAppliedChanges
        from ..models.proposal_run_granted_limits import ProposalRunGrantedLimits
        from ..models.proposal_run_requested_limits import ProposalRunRequestedLimits

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        phase = WorkflowPhaseEnum(d.pop("phase"))

        state = ProposalRunStateEnum(d.pop("state"))

        opened_at = isoparse(d.pop("opened_at"))

        def _parse_opened_by_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        opened_by_name = _parse_opened_by_name(d.pop("opened_by_name"))

        def _parse_closed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = isoparse(data)

                return closed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        closed_at = _parse_closed_at(d.pop("closed_at"))

        def _parse_requested_end_date(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                requested_end_date_type_0 = isoparse(data).date()

                return requested_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        requested_end_date = _parse_requested_end_date(d.pop("requested_end_date"))

        requested_limits = ProposalRunRequestedLimits.from_dict(d.pop("requested_limits"))

        def _parse_granted_end_date(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                granted_end_date_type_0 = isoparse(data).date()

                return granted_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        granted_end_date = _parse_granted_end_date(d.pop("granted_end_date"))

        granted_limits = ProposalRunGrantedLimits.from_dict(d.pop("granted_limits"))

        def _parse_granted_by_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        granted_by_name = _parse_granted_by_name(d.pop("granted_by_name"))

        applied_changes = ProposalRunAppliedChanges.from_dict(d.pop("applied_changes"))

        def _parse_active_step_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_step_uuid_type_0 = UUID(data)

                return active_step_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        active_step_uuid = _parse_active_step_uuid(d.pop("active_step_uuid"))

        def _parse_active_step_kind(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        active_step_kind = _parse_active_step_kind(d.pop("active_step_kind"))

        proposal_run = cls(
            uuid=uuid,
            phase=phase,
            state=state,
            opened_at=opened_at,
            opened_by_name=opened_by_name,
            closed_at=closed_at,
            requested_end_date=requested_end_date,
            requested_limits=requested_limits,
            granted_end_date=granted_end_date,
            granted_limits=granted_limits,
            granted_by_name=granted_by_name,
            applied_changes=applied_changes,
            active_step_uuid=active_step_uuid,
            active_step_kind=active_step_kind,
        )

        proposal_run.additional_properties = d
        return proposal_run

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
