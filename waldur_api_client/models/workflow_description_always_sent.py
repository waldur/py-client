from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowDescriptionAlwaysSent")


@_attrs_define
class WorkflowDescriptionAlwaysSent:
    """
    Attributes:
        task (str):
        event (str):
        audience (list[str]):
        mail_types (list[str]): Keys of the mail types a call may word for this mail.
        customised (bool): Whether the call words one of them itself.
    """

    task: str
    event: str
    audience: list[str]
    mail_types: list[str]
    customised: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task = self.task

        event = self.event

        audience = self.audience

        mail_types = self.mail_types

        customised = self.customised

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task": task,
                "event": event,
                "audience": audience,
                "mail_types": mail_types,
                "customised": customised,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task = d.pop("task")

        event = d.pop("event")

        audience = cast(list[str], d.pop("audience"))

        mail_types = cast(list[str], d.pop("mail_types"))

        customised = d.pop("customised")

        workflow_description_always_sent = cls(
            task=task,
            event=event,
            audience=audience,
            mail_types=mail_types,
            customised=customised,
        )

        workflow_description_always_sent.additional_properties = d
        return workflow_description_always_sent

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
