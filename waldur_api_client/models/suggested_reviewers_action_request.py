from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SuggestedReviewersActionRequest")


@_attrs_define
class SuggestedReviewersActionRequest:
    """
    Attributes:
        suggestion_uuids (list[UUID]): Suggestions naming the people to act on; every suggestion of each person for the
            proposal is acted on.
    """

    suggestion_uuids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suggestion_uuids = []
        for suggestion_uuids_item_data in self.suggestion_uuids:
            suggestion_uuids_item = str(suggestion_uuids_item_data)
            suggestion_uuids.append(suggestion_uuids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "suggestion_uuids": suggestion_uuids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        suggestion_uuids = []
        _suggestion_uuids = d.pop("suggestion_uuids")
        for suggestion_uuids_item_data in _suggestion_uuids:
            suggestion_uuids_item = UUID(suggestion_uuids_item_data)

            suggestion_uuids.append(suggestion_uuids_item)

        suggested_reviewers_action_request = cls(
            suggestion_uuids=suggestion_uuids,
        )

        suggested_reviewers_action_request.additional_properties = d
        return suggested_reviewers_action_request

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
