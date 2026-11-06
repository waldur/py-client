from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dry_run_audience import DryRunAudience


T = TypeVar("T", bound="DryRunMessage")


@_attrs_define
class DryRunMessage:
    """
    Attributes:
        index (int):
        action (Union[None, int]):
        day (int):
        trigger (str):
        notification (str):
        enabled (bool):
        step (Union[None, str]):
        step_name (Union[None, str]):
        audience (DryRunAudience):
        single_message (bool):
        subject (str):
        text (str):
        html (str):
    """

    index: int
    action: Union[None, int]
    day: int
    trigger: str
    notification: str
    enabled: bool
    step: Union[None, str]
    step_name: Union[None, str]
    audience: "DryRunAudience"
    single_message: bool
    subject: str
    text: str
    html: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        action: Union[None, int]
        action = self.action

        day = self.day

        trigger = self.trigger

        notification = self.notification

        enabled = self.enabled

        step: Union[None, str]
        step = self.step

        step_name: Union[None, str]
        step_name = self.step_name

        audience = self.audience.to_dict()

        single_message = self.single_message

        subject = self.subject

        text = self.text

        html = self.html

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "action": action,
                "day": day,
                "trigger": trigger,
                "notification": notification,
                "enabled": enabled,
                "step": step,
                "step_name": step_name,
                "audience": audience,
                "single_message": single_message,
                "subject": subject,
                "text": text,
                "html": html,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dry_run_audience import DryRunAudience

        d = dict(src_dict)
        index = d.pop("index")

        def _parse_action(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        action = _parse_action(d.pop("action"))

        day = d.pop("day")

        trigger = d.pop("trigger")

        notification = d.pop("notification")

        enabled = d.pop("enabled")

        def _parse_step(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        step = _parse_step(d.pop("step"))

        def _parse_step_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        step_name = _parse_step_name(d.pop("step_name"))

        audience = DryRunAudience.from_dict(d.pop("audience"))

        single_message = d.pop("single_message")

        subject = d.pop("subject")

        text = d.pop("text")

        html = d.pop("html")

        dry_run_message = cls(
            index=index,
            action=action,
            day=day,
            trigger=trigger,
            notification=notification,
            enabled=enabled,
            step=step,
            step_name=step_name,
            audience=audience,
            single_message=single_message,
            subject=subject,
            text=text,
            html=html,
        )

        dry_run_message.additional_properties = d
        return dry_run_message

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
