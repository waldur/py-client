from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedCallNotificationOverrideRequest")


@_attrs_define
class PatchedCallNotificationOverrideRequest:
    """
    Attributes:
        mail_type (Union[Unset, str]):
        variant (Union[Unset, str]):
        subject (Union[Unset, str]):
        body_text (Union[Unset, str]):
        body_html (Union[Unset, str]):
        enabled (Union[Unset, bool]):
    """

    mail_type: Union[Unset, str] = UNSET
    variant: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    body_text: Union[Unset, str] = UNSET
    body_html: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mail_type = self.mail_type

        variant = self.variant

        subject = self.subject

        body_text = self.body_text

        body_html = self.body_html

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mail_type is not UNSET:
            field_dict["mail_type"] = mail_type
        if variant is not UNSET:
            field_dict["variant"] = variant
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body_text is not UNSET:
            field_dict["body_text"] = body_text
        if body_html is not UNSET:
            field_dict["body_html"] = body_html
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mail_type = d.pop("mail_type", UNSET)

        variant = d.pop("variant", UNSET)

        subject = d.pop("subject", UNSET)

        body_text = d.pop("body_text", UNSET)

        body_html = d.pop("body_html", UNSET)

        enabled = d.pop("enabled", UNSET)

        patched_call_notification_override_request = cls(
            mail_type=mail_type,
            variant=variant,
            subject=subject,
            body_text=body_text,
            body_html=body_html,
            enabled=enabled,
        )

        patched_call_notification_override_request.additional_properties = d
        return patched_call_notification_override_request

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
