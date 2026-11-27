from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DecidableWorkflowStepsRequestRequest")


@_attrs_define
class DecidableWorkflowStepsRequestRequest:
    """
    Attributes:
        proposal_uuids (list[UUID]): The selected proposals of the call.
    """

    proposal_uuids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_uuids = []
        for proposal_uuids_item_data in self.proposal_uuids:
            proposal_uuids_item = str(proposal_uuids_item_data)
            proposal_uuids.append(proposal_uuids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposal_uuids": proposal_uuids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        proposal_uuids = []
        _proposal_uuids = d.pop("proposal_uuids")
        for proposal_uuids_item_data in _proposal_uuids:
            proposal_uuids_item = UUID(proposal_uuids_item_data)

            proposal_uuids.append(proposal_uuids_item)

        decidable_workflow_steps_request_request = cls(
            proposal_uuids=proposal_uuids,
        )

        decidable_workflow_steps_request_request.additional_properties = d
        return decidable_workflow_steps_request_request

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
