import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.spending_limit_period_enum import SpendingLimitPeriodEnum

T = TypeVar("T", bound="SpendingLimitUsage")


@_attrs_define
class SpendingLimitUsage:
    """
    Attributes:
        component_type (str):
        period (SpendingLimitPeriodEnum):
        limit (float):
        used (float): Usage reported in the current period.
        resets_at (datetime.datetime): When the current period ends and its usage starts from zero.
        reached (bool):
    """

    component_type: str
    period: SpendingLimitPeriodEnum
    limit: float
    used: float
    resets_at: datetime.datetime
    reached: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_type = self.component_type

        period = self.period.value

        limit = self.limit

        used = self.used

        resets_at = self.resets_at.isoformat()

        reached = self.reached

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_type": component_type,
                "period": period,
                "limit": limit,
                "used": used,
                "resets_at": resets_at,
                "reached": reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_type = d.pop("component_type")

        period = SpendingLimitPeriodEnum(d.pop("period"))

        limit = d.pop("limit")

        used = d.pop("used")

        resets_at = isoparse(d.pop("resets_at"))

        reached = d.pop("reached")

        spending_limit_usage = cls(
            component_type=component_type,
            period=period,
            limit=limit,
            used=used,
            resets_at=resets_at,
            reached=reached,
        )

        spending_limit_usage.additional_properties = d
        return spending_limit_usage

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
