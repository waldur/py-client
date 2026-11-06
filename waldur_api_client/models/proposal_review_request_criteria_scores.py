from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProposalReviewRequestCriteriaScores")


@_attrs_define
class ProposalReviewRequestCriteriaScores:
    """Score per criterion, 1-5, keyed by criterion UUID. Writing it replaces the scores, and summary_score becomes their
    weighted average, rounded half up.

    """

    additional_properties: dict[str, Union[None, int]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        proposal_review_request_criteria_scores = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> Union[None, int]:
                if data is None:
                    return data
                return cast(Union[None, int], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        proposal_review_request_criteria_scores.additional_properties = additional_properties
        return proposal_review_request_criteria_scores

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union[None, int]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Union[None, int]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
