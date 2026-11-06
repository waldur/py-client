import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="WorkflowProgressRoundStep")


@_attrs_define
class WorkflowProgressRoundStep:
    """
    Attributes:
        round_ (str):
        name (str):
        opened (bool): Whether the call's managers opened the step for the round.
        due_at (Union[None, datetime.datetime]):
        overdue (bool): Past its due date in the round with proposals still at it.
        waiting (int): The round's proposals at the step.
        completed (int):
        reports (int): Round reports of the step.
        reports_submitted (int):
    """

    round_: str
    name: str
    opened: bool
    due_at: Union[None, datetime.datetime]
    overdue: bool
    waiting: int
    completed: int
    reports: int
    reports_submitted: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        round_ = self.round_

        name = self.name

        opened = self.opened

        due_at: Union[None, str]
        if isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        overdue = self.overdue

        waiting = self.waiting

        completed = self.completed

        reports = self.reports

        reports_submitted = self.reports_submitted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "round": round_,
                "name": name,
                "opened": opened,
                "due_at": due_at,
                "overdue": overdue,
                "waiting": waiting,
                "completed": completed,
                "reports": reports,
                "reports_submitted": reports_submitted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        round_ = d.pop("round")

        name = d.pop("name")

        opened = d.pop("opened")

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

        overdue = d.pop("overdue")

        waiting = d.pop("waiting")

        completed = d.pop("completed")

        reports = d.pop("reports")

        reports_submitted = d.pop("reports_submitted")

        workflow_progress_round_step = cls(
            round_=round_,
            name=name,
            opened=opened,
            due_at=due_at,
            overdue=overdue,
            waiting=waiting,
            completed=completed,
            reports=reports,
            reports_submitted=reports_submitted,
        )

        workflow_progress_round_step.additional_properties = d
        return workflow_progress_round_step

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
