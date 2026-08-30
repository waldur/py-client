from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recipient_enum import RecipientEnum
from ..models.trigger_enum import TriggerEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedCallWorkflowStepNotificationRuleRequest")


@_attrs_define
class PatchedCallWorkflowStepNotificationRuleRequest:
    """
    Attributes:
        workflow_step (Union[Unset, UUID]):
        trigger (Union[Unset, TriggerEnum]):
        recipient (Union[Unset, RecipientEnum]):
        days_before (Union[None, Unset, int]): Only for deadline_approaching: how many days before the step's deadline
            the reminder is sent.
        is_enabled (Union[Unset, bool]):
    """

    workflow_step: Union[Unset, UUID] = UNSET
    trigger: Union[Unset, TriggerEnum] = UNSET
    recipient: Union[Unset, RecipientEnum] = UNSET
    days_before: Union[None, Unset, int] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_step: Union[Unset, str] = UNSET
        if not isinstance(self.workflow_step, Unset):
            workflow_step = str(self.workflow_step)

        trigger: Union[Unset, str] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        recipient: Union[Unset, str] = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.value

        days_before: Union[None, Unset, int]
        if isinstance(self.days_before, Unset):
            days_before = UNSET
        else:
            days_before = self.days_before

        is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow_step is not UNSET:
            field_dict["workflow_step"] = workflow_step
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if days_before is not UNSET:
            field_dict["days_before"] = days_before
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _workflow_step = d.pop("workflow_step", UNSET)
        workflow_step: Union[Unset, UUID]
        if isinstance(_workflow_step, Unset):
            workflow_step = UNSET
        else:
            workflow_step = UUID(_workflow_step)

        _trigger = d.pop("trigger", UNSET)
        trigger: Union[Unset, TriggerEnum]
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = TriggerEnum(_trigger)

        _recipient = d.pop("recipient", UNSET)
        recipient: Union[Unset, RecipientEnum]
        if isinstance(_recipient, Unset):
            recipient = UNSET
        else:
            recipient = RecipientEnum(_recipient)

        def _parse_days_before(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        days_before = _parse_days_before(d.pop("days_before", UNSET))

        is_enabled = d.pop("is_enabled", UNSET)

        patched_call_workflow_step_notification_rule_request = cls(
            workflow_step=workflow_step,
            trigger=trigger,
            recipient=recipient,
            days_before=days_before,
            is_enabled=is_enabled,
        )

        patched_call_workflow_step_notification_rule_request.additional_properties = d
        return patched_call_workflow_step_notification_rule_request

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
