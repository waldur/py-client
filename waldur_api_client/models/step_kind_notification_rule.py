from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StepKindNotificationRule")


@_attrs_define
class StepKindNotificationRule:
    """
    Attributes:
        trigger (str):
        recipient (str):
        days_before (Union[None, int]):
    """

    trigger: str
    recipient: str
    days_before: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger = self.trigger

        recipient = self.recipient

        days_before: Union[None, int]
        days_before = self.days_before

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trigger": trigger,
                "recipient": recipient,
                "days_before": days_before,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trigger = d.pop("trigger")

        recipient = d.pop("recipient")

        def _parse_days_before(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        days_before = _parse_days_before(d.pop("days_before"))

        step_kind_notification_rule = cls(
            trigger=trigger,
            recipient=recipient,
            days_before=days_before,
        )

        step_kind_notification_rule.additional_properties = d
        return step_kind_notification_rule

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
