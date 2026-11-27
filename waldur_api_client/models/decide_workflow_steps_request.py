from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.outcome_enum import OutcomeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="DecideWorkflowStepsRequest")


@_attrs_define
class DecideWorkflowStepsRequest:
    """
    Attributes:
        call_step_uuid (UUID): UUID of the call step to decide: a decision step that is neither the allocation decision
            nor completed once per round.
        outcome (OutcomeEnum):
        proposal_uuids (list[UUID]): The proposals of the call to decide the step for.
        outcome_reason (Union[Unset, str]): Explanation for the outcome, recorded on each proposal. Default: ''.
        dry_run (Union[Unset, bool]): Check every proposal as the run would, and write nothing: the result tells which
            would be decided and why the others would be refused. Default: False.
    """

    call_step_uuid: UUID
    outcome: OutcomeEnum
    proposal_uuids: list[UUID]
    outcome_reason: Union[Unset, str] = ""
    dry_run: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_step_uuid = str(self.call_step_uuid)

        outcome = self.outcome.value

        proposal_uuids = []
        for proposal_uuids_item_data in self.proposal_uuids:
            proposal_uuids_item = str(proposal_uuids_item_data)
            proposal_uuids.append(proposal_uuids_item)

        outcome_reason = self.outcome_reason

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "call_step_uuid": call_step_uuid,
                "outcome": outcome,
                "proposal_uuids": proposal_uuids,
            }
        )
        if outcome_reason is not UNSET:
            field_dict["outcome_reason"] = outcome_reason
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        call_step_uuid = UUID(d.pop("call_step_uuid"))

        outcome = OutcomeEnum(d.pop("outcome"))

        proposal_uuids = []
        _proposal_uuids = d.pop("proposal_uuids")
        for proposal_uuids_item_data in _proposal_uuids:
            proposal_uuids_item = UUID(proposal_uuids_item_data)

            proposal_uuids.append(proposal_uuids_item)

        outcome_reason = d.pop("outcome_reason", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        decide_workflow_steps_request = cls(
            call_step_uuid=call_step_uuid,
            outcome=outcome,
            proposal_uuids=proposal_uuids,
            outcome_reason=outcome_reason,
            dry_run=dry_run,
        )

        decide_workflow_steps_request.additional_properties = d
        return decide_workflow_steps_request

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
