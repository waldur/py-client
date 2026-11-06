from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_description_always_sent import WorkflowDescriptionAlwaysSent
    from ..models.workflow_description_flag import WorkflowDescriptionFlag


T = TypeVar("T", bound="WorkflowDescriptionNotifications")


@_attrs_define
class WorkflowDescriptionNotifications:
    """
    Attributes:
        flags (list['WorkflowDescriptionFlag']):
        always_sent (list['WorkflowDescriptionAlwaysSent']):
        customised (list[str]): Keys of the mail types the call words itself.
    """

    flags: list["WorkflowDescriptionFlag"]
    always_sent: list["WorkflowDescriptionAlwaysSent"]
    customised: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flags = []
        for flags_item_data in self.flags:
            flags_item = flags_item_data.to_dict()
            flags.append(flags_item)

        always_sent = []
        for always_sent_item_data in self.always_sent:
            always_sent_item = always_sent_item_data.to_dict()
            always_sent.append(always_sent_item)

        customised = self.customised

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "flags": flags,
                "always_sent": always_sent,
                "customised": customised,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_description_always_sent import WorkflowDescriptionAlwaysSent
        from ..models.workflow_description_flag import WorkflowDescriptionFlag

        d = dict(src_dict)
        flags = []
        _flags = d.pop("flags")
        for flags_item_data in _flags:
            flags_item = WorkflowDescriptionFlag.from_dict(flags_item_data)

            flags.append(flags_item)

        always_sent = []
        _always_sent = d.pop("always_sent")
        for always_sent_item_data in _always_sent:
            always_sent_item = WorkflowDescriptionAlwaysSent.from_dict(always_sent_item_data)

            always_sent.append(always_sent_item)

        customised = cast(list[str], d.pop("customised"))

        workflow_description_notifications = cls(
            flags=flags,
            always_sent=always_sent,
            customised=customised,
        )

        workflow_description_notifications.additional_properties = d
        return workflow_description_notifications

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
