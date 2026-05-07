from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RejectWorkflowStepRequest")


@_attrs_define
class RejectWorkflowStepRequest:
    """
    Attributes:
        step_uuid (UUID): UUID of the workflow step instance the client believes is active. Used to detect concurrent
            step transitions.
        reason (str): Reason for rejecting the proposal at this step.
    """

    step_uuid: UUID
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step_uuid = str(self.step_uuid)

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step_uuid": step_uuid,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        step_uuid = UUID(d.pop("step_uuid"))

        reason = d.pop("reason")

        reject_workflow_step_request = cls(
            step_uuid=step_uuid,
            reason=reason,
        )

        reject_workflow_step_request.additional_properties = d
        return reject_workflow_step_request

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
