import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="PortfolioReportMonth")


@_attrs_define
class PortfolioReportMonth:
    """
    Attributes:
        month (datetime.date): The first day of the month.
        submitted (int):
        accepted (int): Of the proposals submitted that month, those accepted.
    """

    month: datetime.date
    submitted: int
    accepted: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month.isoformat()

        submitted = self.submitted

        accepted = self.accepted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
                "submitted": submitted,
                "accepted": accepted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = isoparse(d.pop("month")).date()

        submitted = d.pop("submitted")

        accepted = d.pop("accepted")

        portfolio_report_month = cls(
            month=month,
            submitted=submitted,
            accepted=accepted,
        )

        portfolio_report_month.additional_properties = d
        return portfolio_report_month

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
