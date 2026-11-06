from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MyTaskSummary")


@_attrs_define
class MyTaskSummary:
    """
    Attributes:
        total (int): Every open task.
        overdue (int): Tasks past their deadline.
        due_soon (int): Tasks due within due_soon_days, not yet past their deadline.
        due_soon_days (int): How many days ahead a deadline counts as due soon.
    """

    total: int
    overdue: int
    due_soon: int
    due_soon_days: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        overdue = self.overdue

        due_soon = self.due_soon

        due_soon_days = self.due_soon_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "overdue": overdue,
                "due_soon": due_soon,
                "due_soon_days": due_soon_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        overdue = d.pop("overdue")

        due_soon = d.pop("due_soon")

        due_soon_days = d.pop("due_soon_days")

        my_task_summary = cls(
            total=total,
            overdue=overdue,
            due_soon=due_soon,
            due_soon_days=due_soon_days,
        )

        my_task_summary.additional_properties = d
        return my_task_summary

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
