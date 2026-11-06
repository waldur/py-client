from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.portfolio_report_block import PortfolioReportBlock
    from ..models.portfolio_report_call import PortfolioReportCall
    from ..models.portfolio_report_month import PortfolioReportMonth


T = TypeVar("T", bound="PortfolioReport")


@_attrs_define
class PortfolioReport:
    """
    Attributes:
        totals (PortfolioReportBlock):
        calls (list['PortfolioReportCall']):
        months (list['PortfolioReportMonth']):
    """

    totals: "PortfolioReportBlock"
    calls: list["PortfolioReportCall"]
    months: list["PortfolioReportMonth"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        totals = self.totals.to_dict()

        calls = []
        for calls_item_data in self.calls:
            calls_item = calls_item_data.to_dict()
            calls.append(calls_item)

        months = []
        for months_item_data in self.months:
            months_item = months_item_data.to_dict()
            months.append(months_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totals": totals,
                "calls": calls,
                "months": months,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portfolio_report_block import PortfolioReportBlock
        from ..models.portfolio_report_call import PortfolioReportCall
        from ..models.portfolio_report_month import PortfolioReportMonth

        d = dict(src_dict)
        totals = PortfolioReportBlock.from_dict(d.pop("totals"))

        calls = []
        _calls = d.pop("calls")
        for calls_item_data in _calls:
            calls_item = PortfolioReportCall.from_dict(calls_item_data)

            calls.append(calls_item)

        months = []
        _months = d.pop("months")
        for months_item_data in _months:
            months_item = PortfolioReportMonth.from_dict(months_item_data)

            months.append(months_item)

        portfolio_report = cls(
            totals=totals,
            calls=calls,
            months=months,
        )

        portfolio_report.additional_properties = d
        return portfolio_report

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
