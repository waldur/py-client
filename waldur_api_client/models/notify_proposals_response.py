from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.skipped_proposal import SkippedProposal


T = TypeVar("T", bound="NotifyProposalsResponse")


@_attrs_define
class NotifyProposalsResponse:
    """
    Attributes:
        proposals_notified (int):
        skipped_proposals (list['SkippedProposal']): Requested proposals that are not part of this call
    """

    proposals_notified: int
    skipped_proposals: list["SkippedProposal"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposals_notified = self.proposals_notified

        skipped_proposals = []
        for skipped_proposals_item_data in self.skipped_proposals:
            skipped_proposals_item = skipped_proposals_item_data.to_dict()
            skipped_proposals.append(skipped_proposals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposals_notified": proposals_notified,
                "skipped_proposals": skipped_proposals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.skipped_proposal import SkippedProposal

        d = dict(src_dict)
        proposals_notified = d.pop("proposals_notified")

        skipped_proposals = []
        _skipped_proposals = d.pop("skipped_proposals")
        for skipped_proposals_item_data in _skipped_proposals:
            skipped_proposals_item = SkippedProposal.from_dict(skipped_proposals_item_data)

            skipped_proposals.append(skipped_proposals_item)

        notify_proposals_response = cls(
            proposals_notified=proposals_notified,
            skipped_proposals=skipped_proposals,
        )

        notify_proposals_response.additional_properties = d
        return notify_proposals_response

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
