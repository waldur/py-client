from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProposalReviewerSuggestionWithdrawRequest")


@_attrs_define
class ProposalReviewerSuggestionWithdrawRequest:
    """
    Attributes:
        suggestion_uuid (UUID):
    """

    suggestion_uuid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suggestion_uuid = str(self.suggestion_uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "suggestion_uuid": suggestion_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        suggestion_uuid = UUID(d.pop("suggestion_uuid"))

        proposal_reviewer_suggestion_withdraw_request = cls(
            suggestion_uuid=suggestion_uuid,
        )

        proposal_reviewer_suggestion_withdraw_request.additional_properties = d
        return proposal_reviewer_suggestion_withdraw_request

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
