from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DecidableWorkflowStep")


@_attrs_define
class DecidableWorkflowStep:
    """
    Attributes:
        call_step_uuid (UUID):
        step_name (str):
        allowed_outcomes (list[str]):
        proposal_uuids (list[UUID]): The selected proposals standing on the step.
    """

    call_step_uuid: UUID
    step_name: str
    allowed_outcomes: list[str]
    proposal_uuids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_step_uuid = str(self.call_step_uuid)

        step_name = self.step_name

        allowed_outcomes = self.allowed_outcomes

        proposal_uuids = []
        for proposal_uuids_item_data in self.proposal_uuids:
            proposal_uuids_item = str(proposal_uuids_item_data)
            proposal_uuids.append(proposal_uuids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "call_step_uuid": call_step_uuid,
                "step_name": step_name,
                "allowed_outcomes": allowed_outcomes,
                "proposal_uuids": proposal_uuids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        call_step_uuid = UUID(d.pop("call_step_uuid"))

        step_name = d.pop("step_name")

        allowed_outcomes = cast(list[str], d.pop("allowed_outcomes"))

        proposal_uuids = []
        _proposal_uuids = d.pop("proposal_uuids")
        for proposal_uuids_item_data in _proposal_uuids:
            proposal_uuids_item = UUID(proposal_uuids_item_data)

            proposal_uuids.append(proposal_uuids_item)

        decidable_workflow_step = cls(
            call_step_uuid=call_step_uuid,
            step_name=step_name,
            allowed_outcomes=allowed_outcomes,
            proposal_uuids=proposal_uuids,
        )

        decidable_workflow_step.additional_properties = d
        return decidable_workflow_step

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
