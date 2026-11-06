import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenRoundWorkflowStepRequest")


@_attrs_define
class OpenRoundWorkflowStepRequest:
    """
    Attributes:
        step_uuid (Union[Unset, UUID]): UUID of the round step. Either this or step.
        step (Union[Unset, str]): Key of the round step. Either this or step_uuid.
        due_at (Union[None, Unset, datetime.datetime]): When the step is due in this round; left as it is when omitted.
        force (Union[Unset, bool]): Open the step although some proposals of the round have not reached it yet; they
            join it as they arrive. Default: False.
        reason (Union[Unset, str]): Why the step is opened early. Required with force. Default: ''.
    """

    step_uuid: Union[Unset, UUID] = UNSET
    step: Union[Unset, str] = UNSET
    due_at: Union[None, Unset, datetime.datetime] = UNSET
    force: Union[Unset, bool] = False
    reason: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.step_uuid, Unset):
            step_uuid = str(self.step_uuid)

        step = self.step

        due_at: Union[None, Unset, str]
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        force = self.force

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if step_uuid is not UNSET:
            field_dict["step_uuid"] = step_uuid
        if step is not UNSET:
            field_dict["step"] = step
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if force is not UNSET:
            field_dict["force"] = force
        if reason is not UNSET:
            field_dict["reason"] = reason

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

        def _parse_due_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = isoparse(data)

                return due_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        due_at = _parse_due_at(d.pop("due_at", UNSET))

        force = d.pop("force", UNSET)

        reason = d.pop("reason", UNSET)

        open_round_workflow_step_request = cls(
            step_uuid=step_uuid,
            step=step,
            due_at=due_at,
            force=force,
            reason=reason,
        )

        open_round_workflow_step_request.additional_properties = d
        return open_round_workflow_step_request

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
