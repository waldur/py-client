from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompleteWorkflowStepResponse")


@_attrs_define
class CompleteWorkflowStepResponse:
    """
    Attributes:
        detail (str):
        proposal_state (Union[Unset, str]): New proposal state when the workflow terminates.
        next_step (Union[Unset, str]): Key of the step that just became active.
        next_step_uuid (Union[Unset, UUID]): UUID of the call step that just became active.
    """

    detail: str
    proposal_state: Union[Unset, str] = UNSET
    next_step: Union[Unset, str] = UNSET
    next_step_uuid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        proposal_state = self.proposal_state

        next_step = self.next_step

        next_step_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.next_step_uuid, Unset):
            next_step_uuid = str(self.next_step_uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
            }
        )
        if proposal_state is not UNSET:
            field_dict["proposal_state"] = proposal_state
        if next_step is not UNSET:
            field_dict["next_step"] = next_step
        if next_step_uuid is not UNSET:
            field_dict["next_step_uuid"] = next_step_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        detail = d.pop("detail")

        proposal_state = d.pop("proposal_state", UNSET)

        next_step = d.pop("next_step", UNSET)

        _next_step_uuid = d.pop("next_step_uuid", UNSET)
        next_step_uuid: Union[Unset, UUID]
        if isinstance(_next_step_uuid, Unset):
            next_step_uuid = UNSET
        else:
            next_step_uuid = UUID(_next_step_uuid)

        complete_workflow_step_response = cls(
            detail=detail,
            proposal_state=proposal_state,
            next_step=next_step,
            next_step_uuid=next_step_uuid,
        )

        complete_workflow_step_response.additional_properties = d
        return complete_workflow_step_response

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
