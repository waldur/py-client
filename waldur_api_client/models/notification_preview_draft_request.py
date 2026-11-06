from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recipient_enum import RecipientEnum
from ..models.trigger_enum import TriggerEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationPreviewDraftRequest")


@_attrs_define
class NotificationPreviewDraftRequest:
    """
    Attributes:
        subject (str):
        body_text (str):
        step (Union[Unset, str]):
        trigger (Union[Unset, TriggerEnum]):
        recipient (Union[Unset, RecipientEnum]):
        days_before (Union[Unset, int]):
        mail_type (Union[Unset, str]):
        variant (Union[Unset, str]):
        body_html (Union[Unset, str]):  Default: ''.
    """

    subject: str
    body_text: str
    step: Union[Unset, str] = UNSET
    trigger: Union[Unset, TriggerEnum] = UNSET
    recipient: Union[Unset, RecipientEnum] = UNSET
    days_before: Union[Unset, int] = UNSET
    mail_type: Union[Unset, str] = UNSET
    variant: Union[Unset, str] = UNSET
    body_html: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject = self.subject

        body_text = self.body_text

        step = self.step

        trigger: Union[Unset, str] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        recipient: Union[Unset, str] = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.value

        days_before = self.days_before

        mail_type = self.mail_type

        variant = self.variant

        body_html = self.body_html

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject": subject,
                "body_text": body_text,
            }
        )
        if step is not UNSET:
            field_dict["step"] = step
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if days_before is not UNSET:
            field_dict["days_before"] = days_before
        if mail_type is not UNSET:
            field_dict["mail_type"] = mail_type
        if variant is not UNSET:
            field_dict["variant"] = variant
        if body_html is not UNSET:
            field_dict["body_html"] = body_html

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subject = d.pop("subject")

        body_text = d.pop("body_text")

        step = d.pop("step", UNSET)

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

        days_before = d.pop("days_before", UNSET)

        mail_type = d.pop("mail_type", UNSET)

        variant = d.pop("variant", UNSET)

        body_html = d.pop("body_html", UNSET)

        notification_preview_draft_request = cls(
            subject=subject,
            body_text=body_text,
            step=step,
            trigger=trigger,
            recipient=recipient,
            days_before=days_before,
            mail_type=mail_type,
            variant=variant,
            body_html=body_html,
        )

        notification_preview_draft_request.additional_properties = d
        return notification_preview_draft_request

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
