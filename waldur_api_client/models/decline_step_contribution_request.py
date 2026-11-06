from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeclineStepContributionRequest")


@_attrs_define
class DeclineStepContributionRequest:
    """
    Attributes:
        contribution_uuid (UUID):
        comment (Union[Unset, str]):  Default: ''.
    """

    contribution_uuid: UUID
    comment: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contribution_uuid = str(self.contribution_uuid)

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contribution_uuid": contribution_uuid,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contribution_uuid = UUID(d.pop("contribution_uuid"))

        comment = d.pop("comment", UNSET)

        decline_step_contribution_request = cls(
            contribution_uuid=contribution_uuid,
            comment=comment,
        )

        decline_step_contribution_request.additional_properties = d
        return decline_step_contribution_request

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
