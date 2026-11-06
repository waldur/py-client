from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reviewer_standing_enum import ReviewerStandingEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReviewerStandingRequest")


@_attrs_define
class ReviewerStandingRequest:
    """
    Attributes:
        standing (ReviewerStandingEnum):
        reason (Union[Unset, str]):
    """

    standing: ReviewerStandingEnum
    reason: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        standing = self.standing.value

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "standing": standing,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        standing = ReviewerStandingEnum(d.pop("standing"))

        reason = d.pop("reason", UNSET)

        reviewer_standing_request = cls(
            standing=standing,
            reason=reason,
        )

        reviewer_standing_request.additional_properties = d
        return reviewer_standing_request

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
