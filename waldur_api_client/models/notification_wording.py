from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NotificationWording")


@_attrs_define
class NotificationWording:
    """
    Attributes:
        subject (str):
        body_text (str):
        body_html (str):
    """

    subject: str
    body_text: str
    body_html: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject = self.subject

        body_text = self.body_text

        body_html = self.body_html

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject": subject,
                "body_text": body_text,
                "body_html": body_html,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subject = d.pop("subject")

        body_text = d.pop("body_text")

        body_html = d.pop("body_html")

        notification_wording = cls(
            subject=subject,
            body_text=body_text,
            body_html=body_html,
        )

        notification_wording.additional_properties = d
        return notification_wording

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
