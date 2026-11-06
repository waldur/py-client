from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_report_call_step import WorkflowReportCallStep


T = TypeVar("T", bound="WorkflowReportStep")


@_attrs_define
class WorkflowReportStep:
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
        key (str):
        name (str):
        phase (str):
        calls (list['WorkflowReportCallStep']): The step in each call that has it.
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
    key: str
    name: str
    phase: str
    calls: list["WorkflowReportCallStep"]
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

        key = self.key

        name = self.name

        phase = self.phase

        calls = []
        for calls_item_data in self.calls:
            calls_item = calls_item_data.to_dict()
            calls.append(calls_item)

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
                "key": key,
                "name": name,
                "phase": phase,
                "calls": calls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_report_call_step import WorkflowReportCallStep

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

        key = d.pop("key")

        name = d.pop("name")

        phase = d.pop("phase")

        calls = []
        _calls = d.pop("calls")
        for calls_item_data in _calls:
            calls_item = WorkflowReportCallStep.from_dict(calls_item_data)

            calls.append(calls_item)

        workflow_report_step = cls(
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
            key=key,
            name=name,
            phase=phase,
            calls=calls,
        )

        workflow_report_step.additional_properties = d
        return workflow_report_step

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
