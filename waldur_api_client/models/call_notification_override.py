import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallNotificationOverride")


@_attrs_define
class CallNotificationOverride:
    """
    Attributes:
        uuid (UUID):
        key (str):
        mail_type (str):
        subject (str):
        body_text (str):
        updated_by_name (Union[None, str]):
        modified (datetime.datetime):
        variant (Union[Unset, str]):
        body_html (Union[Unset, str]):
        enabled (Union[Unset, bool]):
    """

    uuid: UUID
    key: str
    mail_type: str
    subject: str
    body_text: str
    updated_by_name: Union[None, str]
    modified: datetime.datetime
    variant: Union[Unset, str] = UNSET
    body_html: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        key = self.key

        mail_type = self.mail_type

        subject = self.subject

        body_text = self.body_text

        updated_by_name: Union[None, str]
        updated_by_name = self.updated_by_name

        modified = self.modified.isoformat()

        variant = self.variant

        body_html = self.body_html

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "key": key,
                "mail_type": mail_type,
                "subject": subject,
                "body_text": body_text,
                "updated_by_name": updated_by_name,
                "modified": modified,
            }
        )
        if variant is not UNSET:
            field_dict["variant"] = variant
        if body_html is not UNSET:
            field_dict["body_html"] = body_html
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        key = d.pop("key")

        mail_type = d.pop("mail_type")

        subject = d.pop("subject")

        body_text = d.pop("body_text")

        def _parse_updated_by_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        updated_by_name = _parse_updated_by_name(d.pop("updated_by_name"))

        modified = isoparse(d.pop("modified"))

        variant = d.pop("variant", UNSET)

        body_html = d.pop("body_html", UNSET)

        enabled = d.pop("enabled", UNSET)

        call_notification_override = cls(
            uuid=uuid,
            key=key,
            mail_type=mail_type,
            subject=subject,
            body_text=body_text,
            updated_by_name=updated_by_name,
            modified=modified,
            variant=variant,
            body_html=body_html,
            enabled=enabled,
        )

        call_notification_override.additional_properties = d
        return call_notification_override

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
