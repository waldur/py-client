import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="WorkflowTimelineStep")


@_attrs_define
class WorkflowTimelineStep:
    """
    Attributes:
        key (str):
        name (str):
        stage (int):
        status (str):
        outcome (Union[None, str]):
        planned_days (Union[None, int]):
        started_at (Union[None, datetime.datetime]):
        completed_at (Union[None, datetime.datetime]):
        deadline (Union[None, datetime.datetime]):
        overdue (bool): Past its deadline now, or completed after it.
        completed_by_name (Union[None, str]):
        sent_notifications (list[str]): Keys of the mail the step's rules sent, without time: what went out before sends
            were logged as events.
    """

    key: str
    name: str
    stage: int
    status: str
    outcome: Union[None, str]
    planned_days: Union[None, int]
    started_at: Union[None, datetime.datetime]
    completed_at: Union[None, datetime.datetime]
    deadline: Union[None, datetime.datetime]
    overdue: bool
    completed_by_name: Union[None, str]
    sent_notifications: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        stage = self.stage

        status = self.status

        outcome: Union[None, str]
        outcome = self.outcome

        planned_days: Union[None, int]
        planned_days = self.planned_days

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

        deadline: Union[None, str]
        if isinstance(self.deadline, datetime.datetime):
            deadline = self.deadline.isoformat()
        else:
            deadline = self.deadline

        overdue = self.overdue

        completed_by_name: Union[None, str]
        completed_by_name = self.completed_by_name

        sent_notifications = self.sent_notifications

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "stage": stage,
                "status": status,
                "outcome": outcome,
                "planned_days": planned_days,
                "started_at": started_at,
                "completed_at": completed_at,
                "deadline": deadline,
                "overdue": overdue,
                "completed_by_name": completed_by_name,
                "sent_notifications": sent_notifications,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        stage = d.pop("stage")

        status = d.pop("status")

        def _parse_outcome(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        outcome = _parse_outcome(d.pop("outcome"))

        def _parse_planned_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        planned_days = _parse_planned_days(d.pop("planned_days"))

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

        def _parse_deadline(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deadline_type_0 = isoparse(data)

                return deadline_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        deadline = _parse_deadline(d.pop("deadline"))

        overdue = d.pop("overdue")

        def _parse_completed_by_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        completed_by_name = _parse_completed_by_name(d.pop("completed_by_name"))

        sent_notifications = cast(list[str], d.pop("sent_notifications"))

        workflow_timeline_step = cls(
            key=key,
            name=name,
            stage=stage,
            status=status,
            outcome=outcome,
            planned_days=planned_days,
            started_at=started_at,
            completed_at=completed_at,
            deadline=deadline,
            overdue=overdue,
            completed_by_name=completed_by_name,
            sent_notifications=sent_notifications,
        )

        workflow_timeline_step.additional_properties = d
        return workflow_timeline_step

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
