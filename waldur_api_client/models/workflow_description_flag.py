from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_description_flag_kind_enum import WorkflowDescriptionFlagKindEnum
from ..models.workflow_description_flag_severity_enum import WorkflowDescriptionFlagSeverityEnum

if TYPE_CHECKING:
    from ..models.workflow_description_ref import WorkflowDescriptionRef


T = TypeVar("T", bound="WorkflowDescriptionFlag")


@_attrs_define
class WorkflowDescriptionFlag:
    """
    Attributes:
        code (str):
        kind (WorkflowDescriptionFlagKindEnum):
        severity (WorkflowDescriptionFlagSeverityEnum):
        step (Union[None, str]):
        trigger (Union[None, str]):
        days_before (Union[None, int]): The flagged rule's lead time, for a deadline reminder.
        recipient (Union[None, str]):
        message (str):
        because (list['WorkflowDescriptionRef']):
    """

    code: str
    kind: WorkflowDescriptionFlagKindEnum
    severity: WorkflowDescriptionFlagSeverityEnum
    step: Union[None, str]
    trigger: Union[None, str]
    days_before: Union[None, int]
    recipient: Union[None, str]
    message: str
    because: list["WorkflowDescriptionRef"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        kind = self.kind.value

        severity = self.severity.value

        step: Union[None, str]
        step = self.step

        trigger: Union[None, str]
        trigger = self.trigger

        days_before: Union[None, int]
        days_before = self.days_before

        recipient: Union[None, str]
        recipient = self.recipient

        message = self.message

        because = []
        for because_item_data in self.because:
            because_item = because_item_data.to_dict()
            because.append(because_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "kind": kind,
                "severity": severity,
                "step": step,
                "trigger": trigger,
                "days_before": days_before,
                "recipient": recipient,
                "message": message,
                "because": because,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_description_ref import WorkflowDescriptionRef

        d = dict(src_dict)
        code = d.pop("code")

        kind = WorkflowDescriptionFlagKindEnum(d.pop("kind"))

        severity = WorkflowDescriptionFlagSeverityEnum(d.pop("severity"))

        def _parse_step(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        step = _parse_step(d.pop("step"))

        def _parse_trigger(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        trigger = _parse_trigger(d.pop("trigger"))

        def _parse_days_before(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        days_before = _parse_days_before(d.pop("days_before"))

        def _parse_recipient(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        recipient = _parse_recipient(d.pop("recipient"))

        message = d.pop("message")

        because = []
        _because = d.pop("because")
        for because_item_data in _because:
            because_item = WorkflowDescriptionRef.from_dict(because_item_data)

            because.append(because_item)

        workflow_description_flag = cls(
            code=code,
            kind=kind,
            severity=severity,
            step=step,
            trigger=trigger,
            days_before=days_before,
            recipient=recipient,
            message=message,
            because=because,
        )

        workflow_description_flag.additional_properties = d
        return workflow_description_flag

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
