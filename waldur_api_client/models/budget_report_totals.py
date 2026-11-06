from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BudgetReportTotals")


@_attrs_define
class BudgetReportTotals:
    """
    Attributes:
        pools (int):
        pools_exhausted (int): Pools with nothing left to award.
    """

    pools: int
    pools_exhausted: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pools = self.pools

        pools_exhausted = self.pools_exhausted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pools": pools,
                "pools_exhausted": pools_exhausted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pools = d.pop("pools")

        pools_exhausted = d.pop("pools_exhausted")

        budget_report_totals = cls(
            pools=pools,
            pools_exhausted=pools_exhausted,
        )

        budget_report_totals.additional_properties = d
        return budget_report_totals

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
