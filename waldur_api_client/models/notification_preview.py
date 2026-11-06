from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_preview_source_enum import NotificationPreviewSourceEnum

T = TypeVar("T", bound="NotificationPreview")


@_attrs_define
class NotificationPreview:
    """
    Attributes:
        key (str):
        mail_type (str):
        variant (str):
        label (str):
        audience (str):
        notification (str):
        enabled (bool): Whether the portal sends this notification at all.
        source (NotificationPreviewSourceEnum):
        step (Union[None, str]):
        trigger (Union[None, str]):
        recipient (Union[None, str]):
        subject (str):
        text (str):
        html (str):
    """

    key: str
    mail_type: str
    variant: str
    label: str
    audience: str
    notification: str
    enabled: bool
    source: NotificationPreviewSourceEnum
    step: Union[None, str]
    trigger: Union[None, str]
    recipient: Union[None, str]
    subject: str
    text: str
    html: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        mail_type = self.mail_type

        variant = self.variant

        label = self.label

        audience = self.audience

        notification = self.notification

        enabled = self.enabled

        source = self.source.value

        step: Union[None, str]
        step = self.step

        trigger: Union[None, str]
        trigger = self.trigger

        recipient: Union[None, str]
        recipient = self.recipient

        subject = self.subject

        text = self.text

        html = self.html

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "mail_type": mail_type,
                "variant": variant,
                "label": label,
                "audience": audience,
                "notification": notification,
                "enabled": enabled,
                "source": source,
                "step": step,
                "trigger": trigger,
                "recipient": recipient,
                "subject": subject,
                "text": text,
                "html": html,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        mail_type = d.pop("mail_type")

        variant = d.pop("variant")

        label = d.pop("label")

        audience = d.pop("audience")

        notification = d.pop("notification")

        enabled = d.pop("enabled")

        source = NotificationPreviewSourceEnum(d.pop("source"))

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

        def _parse_recipient(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        recipient = _parse_recipient(d.pop("recipient"))

        subject = d.pop("subject")

        text = d.pop("text")

        html = d.pop("html")

        notification_preview = cls(
            key=key,
            mail_type=mail_type,
            variant=variant,
            label=label,
            audience=audience,
            notification=notification,
            enabled=enabled,
            source=source,
            step=step,
            trigger=trigger,
            recipient=recipient,
            subject=subject,
            text=text,
            html=html,
        )

        notification_preview.additional_properties = d
        return notification_preview

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
