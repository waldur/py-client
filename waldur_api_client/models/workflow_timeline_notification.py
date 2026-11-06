import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="WorkflowTimelineNotification")


@_attrs_define
class WorkflowTimelineNotification:
    """
    Attributes:
        created (datetime.datetime):
        step_key (Union[None, str]):
        step_name (Union[None, str]):
        template (str):
        trigger (str):
        audience (str): The role addressed; never an address.
        recipient_count (int):
        email_log_uuids (list[str]): The mails as sent, readable through the proposal's workflow-mails; empty for mail
            sent before they were kept.
    """

    created: datetime.datetime
    step_key: Union[None, str]
    step_name: Union[None, str]
    template: str
    trigger: str
    audience: str
    recipient_count: int
    email_log_uuids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created.isoformat()

        step_key: Union[None, str]
        step_key = self.step_key

        step_name: Union[None, str]
        step_name = self.step_name

        template = self.template

        trigger = self.trigger

        audience = self.audience

        recipient_count = self.recipient_count

        email_log_uuids = self.email_log_uuids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "step_key": step_key,
                "step_name": step_name,
                "template": template,
                "trigger": trigger,
                "audience": audience,
                "recipient_count": recipient_count,
                "email_log_uuids": email_log_uuids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = isoparse(d.pop("created"))

        def _parse_step_key(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        step_key = _parse_step_key(d.pop("step_key"))

        def _parse_step_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        step_name = _parse_step_name(d.pop("step_name"))

        template = d.pop("template")

        trigger = d.pop("trigger")

        audience = d.pop("audience")

        recipient_count = d.pop("recipient_count")

        email_log_uuids = cast(list[str], d.pop("email_log_uuids"))

        workflow_timeline_notification = cls(
            created=created,
            step_key=step_key,
            step_name=step_name,
            template=template,
            trigger=trigger,
            audience=audience,
            recipient_count=recipient_count,
            email_log_uuids=email_log_uuids,
        )

        workflow_timeline_notification.additional_properties = d
        return workflow_timeline_notification

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
