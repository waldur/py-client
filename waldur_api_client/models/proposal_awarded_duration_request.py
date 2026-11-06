from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProposalAwardedDurationRequest")


@_attrs_define
class ProposalAwardedDurationRequest:
    """
    Attributes:
        awarded_duration_months (int): The project length the award grants, in months: one of the call's
            allowed_duration_months.
    """

    awarded_duration_months: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        awarded_duration_months = self.awarded_duration_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "awarded_duration_months": awarded_duration_months,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        awarded_duration_months = d.pop("awarded_duration_months")

        proposal_awarded_duration_request = cls(
            awarded_duration_months=awarded_duration_months,
        )

        proposal_awarded_duration_request.additional_properties = d
        return proposal_awarded_duration_request

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
