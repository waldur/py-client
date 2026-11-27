from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_step_decision_result_status_enum import BulkStepDecisionResultStatusEnum

T = TypeVar("T", bound="BulkStepDecisionResult")


@_attrs_define
class BulkStepDecisionResult:
    """
    Attributes:
        proposal_uuid (str): The proposal named, as hex.
        proposal_name (str): Empty for a proposal not found in the call, or one the run's user may not act on: of those
            only the id and the reason are told.
        status (BulkStepDecisionResultStatusEnum):
        detail (str): What deciding it did, or why it was refused.
        proposal_state (str):
        current_step_name (str): Where the proposal stands now.
    """

    proposal_uuid: str
    proposal_name: str
    status: BulkStepDecisionResultStatusEnum
    detail: str
    proposal_state: str
    current_step_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_uuid = self.proposal_uuid

        proposal_name = self.proposal_name

        status = self.status.value

        detail = self.detail

        proposal_state = self.proposal_state

        current_step_name = self.current_step_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposal_uuid": proposal_uuid,
                "proposal_name": proposal_name,
                "status": status,
                "detail": detail,
                "proposal_state": proposal_state,
                "current_step_name": current_step_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        proposal_uuid = d.pop("proposal_uuid")

        proposal_name = d.pop("proposal_name")

        status = BulkStepDecisionResultStatusEnum(d.pop("status"))

        detail = d.pop("detail")

        proposal_state = d.pop("proposal_state")

        current_step_name = d.pop("current_step_name")

        bulk_step_decision_result = cls(
            proposal_uuid=proposal_uuid,
            proposal_name=proposal_name,
            status=status,
            detail=detail,
            proposal_state=proposal_state,
            current_step_name=current_step_name,
        )

        bulk_step_decision_result.additional_properties = d
        return bulk_step_decision_result

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
