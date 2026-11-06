from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowReportCallStep")


@_attrs_define
class WorkflowReportCallStep:
    """
    Attributes:
        total (int): Step instances counted.
        pending (int): Not started yet.
        waiting (int): Proposals at the step now.
        overdue (int): Of those waiting, the ones past the step's deadline.
        completed (int):
        completed_late (int): Completed after the step's deadline.
        skipped (int):
        expired (int):
        withdrawn (int):
        median_days (Union[None, float]): Median days from start to completion.
        p90_days (Union[None, float]): 90th percentile of the days from start to completion.
        call_uuid (UUID):
        call_name (str):
        call_slug (str):
        organisation_uuid (UUID): The call's call managing organization.
        organisation_name (str): The name of the call managing organization's customer.
        name (str): The step's name in this call.
        enabled (bool):
        planned_days (Union[None, int]):
    """

    total: int
    pending: int
    waiting: int
    overdue: int
    completed: int
    completed_late: int
    skipped: int
    expired: int
    withdrawn: int
    median_days: Union[None, float]
    p90_days: Union[None, float]
    call_uuid: UUID
    call_name: str
    call_slug: str
    organisation_uuid: UUID
    organisation_name: str
    name: str
    enabled: bool
    planned_days: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        pending = self.pending

        waiting = self.waiting

        overdue = self.overdue

        completed = self.completed

        completed_late = self.completed_late

        skipped = self.skipped

        expired = self.expired

        withdrawn = self.withdrawn

        median_days: Union[None, float]
        median_days = self.median_days

        p90_days: Union[None, float]
        p90_days = self.p90_days

        call_uuid = str(self.call_uuid)

        call_name = self.call_name

        call_slug = self.call_slug

        organisation_uuid = str(self.organisation_uuid)

        organisation_name = self.organisation_name

        name = self.name

        enabled = self.enabled

        planned_days: Union[None, int]
        planned_days = self.planned_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "pending": pending,
                "waiting": waiting,
                "overdue": overdue,
                "completed": completed,
                "completed_late": completed_late,
                "skipped": skipped,
                "expired": expired,
                "withdrawn": withdrawn,
                "median_days": median_days,
                "p90_days": p90_days,
                "call_uuid": call_uuid,
                "call_name": call_name,
                "call_slug": call_slug,
                "organisation_uuid": organisation_uuid,
                "organisation_name": organisation_name,
                "name": name,
                "enabled": enabled,
                "planned_days": planned_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        pending = d.pop("pending")

        waiting = d.pop("waiting")

        overdue = d.pop("overdue")

        completed = d.pop("completed")

        completed_late = d.pop("completed_late")

        skipped = d.pop("skipped")

        expired = d.pop("expired")

        withdrawn = d.pop("withdrawn")

        def _parse_median_days(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        median_days = _parse_median_days(d.pop("median_days"))

        def _parse_p90_days(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        p90_days = _parse_p90_days(d.pop("p90_days"))

        call_uuid = UUID(d.pop("call_uuid"))

        call_name = d.pop("call_name")

        call_slug = d.pop("call_slug")

        organisation_uuid = UUID(d.pop("organisation_uuid"))

        organisation_name = d.pop("organisation_name")

        name = d.pop("name")

        enabled = d.pop("enabled")

        def _parse_planned_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        planned_days = _parse_planned_days(d.pop("planned_days"))

        workflow_report_call_step = cls(
            total=total,
            pending=pending,
            waiting=waiting,
            overdue=overdue,
            completed=completed,
            completed_late=completed_late,
            skipped=skipped,
            expired=expired,
            withdrawn=withdrawn,
            median_days=median_days,
            p90_days=p90_days,
            call_uuid=call_uuid,
            call_name=call_name,
            call_slug=call_slug,
            organisation_uuid=organisation_uuid,
            organisation_name=organisation_name,
            name=name,
            enabled=enabled,
            planned_days=planned_days,
        )

        workflow_report_call_step.additional_properties = d
        return workflow_report_call_step

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
