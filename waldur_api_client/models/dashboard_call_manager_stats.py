from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DashboardCallManagerStats")


@_attrs_define
class DashboardCallManagerStats:
    """
    Attributes:
        pending_assessments (int):
        active_calls (int):
        overdue_reviews (int):
    """

    pending_assessments: int
    active_calls: int
    overdue_reviews: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pending_assessments = self.pending_assessments

        active_calls = self.active_calls

        overdue_reviews = self.overdue_reviews

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pending_assessments": pending_assessments,
                "active_calls": active_calls,
                "overdue_reviews": overdue_reviews,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pending_assessments = d.pop("pending_assessments")

        active_calls = d.pop("active_calls")

        overdue_reviews = d.pop("overdue_reviews")

        dashboard_call_manager_stats = cls(
            pending_assessments=pending_assessments,
            active_calls=active_calls,
            overdue_reviews=overdue_reviews,
        )

        dashboard_call_manager_stats.additional_properties = d
        return dashboard_call_manager_stats

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
