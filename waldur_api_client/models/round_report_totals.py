from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RoundReportTotals")


@_attrs_define
class RoundReportTotals:
    """
    Attributes:
        rounds (int):
        published (int): Rounds whose results are published, after a cut-off.
        late (int):
        median_days_cutoff_to_published (Union[None, float]):
    """

    rounds: int
    published: int
    late: int
    median_days_cutoff_to_published: Union[None, float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rounds = self.rounds

        published = self.published

        late = self.late

        median_days_cutoff_to_published: Union[None, float]
        median_days_cutoff_to_published = self.median_days_cutoff_to_published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rounds": rounds,
                "published": published,
                "late": late,
                "median_days_cutoff_to_published": median_days_cutoff_to_published,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rounds = d.pop("rounds")

        published = d.pop("published")

        late = d.pop("late")

        def _parse_median_days_cutoff_to_published(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        median_days_cutoff_to_published = _parse_median_days_cutoff_to_published(
            d.pop("median_days_cutoff_to_published")
        )

        round_report_totals = cls(
            rounds=rounds,
            published=published,
            late=late,
            median_days_cutoff_to_published=median_days_cutoff_to_published,
        )

        round_report_totals.additional_properties = d
        return round_report_totals

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
