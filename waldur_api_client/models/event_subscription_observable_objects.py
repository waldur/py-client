from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EventSubscriptionObservableObjects")


@_attrs_define
class EventSubscriptionObservableObjects:
    """List of objects to observe. Each item must have 'object_type' (one of: order, user_role, resource, offering_user,
    importable_resources, service_account, course_account, resource_periodic_limits) and optionally 'object_id'
    (integer). Example: [{"object_type": "resource"}, {"object_type": "order", "object_id": 123}]

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_subscription_observable_objects = cls()

        event_subscription_observable_objects.additional_properties = d
        return event_subscription_observable_objects

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
