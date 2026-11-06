from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reviewer_report_row import ReviewerReportRow
    from ..models.reviewer_report_totals import ReviewerReportTotals


T = TypeVar("T", bound="ReviewerReport")


@_attrs_define
class ReviewerReport:
    """
    Attributes:
        totals (ReviewerReportTotals):
        reviewers (list['ReviewerReportRow']): Busiest first: by reviews assigned.
    """

    totals: "ReviewerReportTotals"
    reviewers: list["ReviewerReportRow"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        totals = self.totals.to_dict()

        reviewers = []
        for reviewers_item_data in self.reviewers:
            reviewers_item = reviewers_item_data.to_dict()
            reviewers.append(reviewers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totals": totals,
                "reviewers": reviewers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reviewer_report_row import ReviewerReportRow
        from ..models.reviewer_report_totals import ReviewerReportTotals

        d = dict(src_dict)
        totals = ReviewerReportTotals.from_dict(d.pop("totals"))

        reviewers = []
        _reviewers = d.pop("reviewers")
        for reviewers_item_data in _reviewers:
            reviewers_item = ReviewerReportRow.from_dict(reviewers_item_data)

            reviewers.append(reviewers_item)

        reviewer_report = cls(
            totals=totals,
            reviewers=reviewers,
        )

        reviewer_report.additional_properties = d
        return reviewer_report

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
