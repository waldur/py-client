import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.bulk_step_decision_state_enum import BulkStepDecisionStateEnum

T = TypeVar("T", bound="BulkStepDecisionSummary")


@_attrs_define
class BulkStepDecisionSummary:
    """
    Attributes:
        uuid (Union[None, UUID]): Null for a preview decided within the request: nothing is recorded.
        dry_run (bool): A preview: nothing is decided, each result tells what would be.
        state (BulkStepDecisionStateEnum):
        call_uuid (UUID):
        call_name (str):
        call_step_uuid (Union[None, UUID]):
        step_name (str):
        outcome (str):
        outcome_reason (str):
        created_by_uuid (Union[None, UUID]):
        created_by_name (Union[None, str]):
        total (int):
        processed (int):
        decided_count (int):
        refused_count (int):
        created (Union[None, datetime.datetime]):
        modified (Union[None, datetime.datetime]): When the run last recorded a proposal.
        started_at (Union[None, datetime.datetime]):
        completed_at (Union[None, datetime.datetime]):
        error_message (str):
    """

    uuid: Union[None, UUID]
    dry_run: bool
    state: BulkStepDecisionStateEnum
    call_uuid: UUID
    call_name: str
    call_step_uuid: Union[None, UUID]
    step_name: str
    outcome: str
    outcome_reason: str
    created_by_uuid: Union[None, UUID]
    created_by_name: Union[None, str]
    total: int
    processed: int
    decided_count: int
    refused_count: int
    created: Union[None, datetime.datetime]
    modified: Union[None, datetime.datetime]
    started_at: Union[None, datetime.datetime]
    completed_at: Union[None, datetime.datetime]
    error_message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: Union[None, str]
        if isinstance(self.uuid, UUID):
            uuid = str(self.uuid)
        else:
            uuid = self.uuid

        dry_run = self.dry_run

        state = self.state.value

        call_uuid = str(self.call_uuid)

        call_name = self.call_name

        call_step_uuid: Union[None, str]
        if isinstance(self.call_step_uuid, UUID):
            call_step_uuid = str(self.call_step_uuid)
        else:
            call_step_uuid = self.call_step_uuid

        step_name = self.step_name

        outcome = self.outcome

        outcome_reason = self.outcome_reason

        created_by_uuid: Union[None, str]
        if isinstance(self.created_by_uuid, UUID):
            created_by_uuid = str(self.created_by_uuid)
        else:
            created_by_uuid = self.created_by_uuid

        created_by_name: Union[None, str]
        created_by_name = self.created_by_name

        total = self.total

        processed = self.processed

        decided_count = self.decided_count

        refused_count = self.refused_count

        created: Union[None, str]
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        modified: Union[None, str]
        if isinstance(self.modified, datetime.datetime):
            modified = self.modified.isoformat()
        else:
            modified = self.modified

        started_at: Union[None, str]
        if isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        completed_at: Union[None, str]
        if isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "dry_run": dry_run,
                "state": state,
                "call_uuid": call_uuid,
                "call_name": call_name,
                "call_step_uuid": call_step_uuid,
                "step_name": step_name,
                "outcome": outcome,
                "outcome_reason": outcome_reason,
                "created_by_uuid": created_by_uuid,
                "created_by_name": created_by_name,
                "total": total,
                "processed": processed,
                "decided_count": decided_count,
                "refused_count": refused_count,
                "created": created,
                "modified": modified,
                "started_at": started_at,
                "completed_at": completed_at,
                "error_message": error_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                uuid_type_0 = UUID(data)

                return uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        uuid = _parse_uuid(d.pop("uuid"))

        dry_run = d.pop("dry_run")

        state = BulkStepDecisionStateEnum(d.pop("state"))

        call_uuid = UUID(d.pop("call_uuid"))

        call_name = d.pop("call_name")

        def _parse_call_step_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                call_step_uuid_type_0 = UUID(data)

                return call_step_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        call_step_uuid = _parse_call_step_uuid(d.pop("call_step_uuid"))

        step_name = d.pop("step_name")

        outcome = d.pop("outcome")

        outcome_reason = d.pop("outcome_reason")

        def _parse_created_by_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_uuid_type_0 = UUID(data)

                return created_by_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        created_by_uuid = _parse_created_by_uuid(d.pop("created_by_uuid"))

        def _parse_created_by_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by_name = _parse_created_by_name(d.pop("created_by_name"))

        total = d.pop("total")

        processed = d.pop("processed")

        decided_count = d.pop("decided_count")

        refused_count = d.pop("refused_count")

        def _parse_created(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        created = _parse_created(d.pop("created"))

        def _parse_modified(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_type_0 = isoparse(data)

                return modified_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        modified = _parse_modified(d.pop("modified"))

        def _parse_started_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        started_at = _parse_started_at(d.pop("started_at"))

        def _parse_completed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        error_message = d.pop("error_message")

        bulk_step_decision_summary = cls(
            uuid=uuid,
            dry_run=dry_run,
            state=state,
            call_uuid=call_uuid,
            call_name=call_name,
            call_step_uuid=call_step_uuid,
            step_name=step_name,
            outcome=outcome,
            outcome_reason=outcome_reason,
            created_by_uuid=created_by_uuid,
            created_by_name=created_by_name,
            total=total,
            processed=processed,
            decided_count=decided_count,
            refused_count=refused_count,
            created=created,
            modified=modified,
            started_at=started_at,
            completed_at=completed_at,
            error_message=error_message,
        )

        bulk_step_decision_summary.additional_properties = d
        return bulk_step_decision_summary

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
