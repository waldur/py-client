from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.budget_report_pool import BudgetReportPool
    from ..models.budget_report_totals import BudgetReportTotals


T = TypeVar("T", bound="BudgetReport")


@_attrs_define
class BudgetReport:
    """
    Attributes:
        totals (BudgetReportTotals):
        pools (list['BudgetReportPool']):
    """

    totals: "BudgetReportTotals"
    pools: list["BudgetReportPool"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        totals = self.totals.to_dict()

        pools = []
        for pools_item_data in self.pools:
            pools_item = pools_item_data.to_dict()
            pools.append(pools_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totals": totals,
                "pools": pools,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_report_pool import BudgetReportPool
        from ..models.budget_report_totals import BudgetReportTotals

        d = dict(src_dict)
        totals = BudgetReportTotals.from_dict(d.pop("totals"))

        pools = []
        _pools = d.pop("pools")
        for pools_item_data in _pools:
            pools_item = BudgetReportPool.from_dict(pools_item_data)

            pools.append(pools_item)

        budget_report = cls(
            totals=totals,
            pools=pools,
        )

        budget_report.additional_properties = d
        return budget_report

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
