from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvanceRoundWorkflowStepRequest")


@_attrs_define
class AdvanceRoundWorkflowStepRequest:
    """
    Attributes:
        step_uuid (Union[Unset, UUID]): UUID of the completed step to move on from. Either this or step.
        step (Union[Unset, str]): Key of the completed step to move on from. Either this or step_uuid.
    """

    step_uuid: Union[Unset, UUID] = UNSET
    step: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.step_uuid, Unset):
            step_uuid = str(self.step_uuid)

        step = self.step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if step_uuid is not UNSET:
            field_dict["step_uuid"] = step_uuid
        if step is not UNSET:
            field_dict["step"] = step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _step_uuid = d.pop("step_uuid", UNSET)
        step_uuid: Union[Unset, UUID]
        if isinstance(_step_uuid, Unset):
            step_uuid = UNSET
        else:
            step_uuid = UUID(_step_uuid)

        step = d.pop("step", UNSET)

        advance_round_workflow_step_request = cls(
            step_uuid=step_uuid,
            step=step,
        )

        advance_round_workflow_step_request.additional_properties = d
        return advance_round_workflow_step_request

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
