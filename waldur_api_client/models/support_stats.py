from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SupportStats")


@_attrs_define
class SupportStats:
    """
    Attributes:
        open_issues_count (int):
        closed_this_month_count (int):
        recent_broadcasts_count (int):
    """

    open_issues_count: int
    closed_this_month_count: int
    recent_broadcasts_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_issues_count = self.open_issues_count

        closed_this_month_count = self.closed_this_month_count

        recent_broadcasts_count = self.recent_broadcasts_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "open_issues_count": open_issues_count,
                "closed_this_month_count": closed_this_month_count,
                "recent_broadcasts_count": recent_broadcasts_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_issues_count = d.pop("open_issues_count")

        closed_this_month_count = d.pop("closed_this_month_count")

        recent_broadcasts_count = d.pop("recent_broadcasts_count")

        support_stats = cls(
            open_issues_count=open_issues_count,
            closed_this_month_count=closed_this_month_count,
            recent_broadcasts_count=recent_broadcasts_count,
        )

        support_stats.additional_properties = d
        return support_stats

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
