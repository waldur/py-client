from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RmqQueueStats")


@_attrs_define
class RmqQueueStats:
    """
    Attributes:
        name (str): Queue name (e.g., 'subscription_{uuid}_offering_{uuid}_{type}')
        messages (int): Total number of messages in the queue
        messages_ready (int): Number of messages ready for delivery
        messages_unacknowledged (int): Number of messages awaiting acknowledgement
        consumers (int): Number of active consumers for this queue
        subscription_uuid (Union[None, str]): Parsed subscription UUID from queue name
        offering_uuid (Union[None, str]): Parsed offering UUID from queue name
        object_type (Union[None, str]): Parsed object type from queue name (e.g., 'resource', 'order')
    """

    name: str
    messages: int
    messages_ready: int
    messages_unacknowledged: int
    consumers: int
    subscription_uuid: Union[None, str]
    offering_uuid: Union[None, str]
    object_type: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        messages = self.messages

        messages_ready = self.messages_ready

        messages_unacknowledged = self.messages_unacknowledged

        consumers = self.consumers

        subscription_uuid: Union[None, str]
        subscription_uuid = self.subscription_uuid

        offering_uuid: Union[None, str]
        offering_uuid = self.offering_uuid

        object_type: Union[None, str]
        object_type = self.object_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "messages": messages,
                "messages_ready": messages_ready,
                "messages_unacknowledged": messages_unacknowledged,
                "consumers": consumers,
                "subscription_uuid": subscription_uuid,
                "offering_uuid": offering_uuid,
                "object_type": object_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        messages = d.pop("messages")

        messages_ready = d.pop("messages_ready")

        messages_unacknowledged = d.pop("messages_unacknowledged")

        consumers = d.pop("consumers")

        def _parse_subscription_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        subscription_uuid = _parse_subscription_uuid(d.pop("subscription_uuid"))

        def _parse_offering_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        offering_uuid = _parse_offering_uuid(d.pop("offering_uuid"))

        def _parse_object_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        object_type = _parse_object_type(d.pop("object_type"))

        rmq_queue_stats = cls(
            name=name,
            messages=messages,
            messages_ready=messages_ready,
            messages_unacknowledged=messages_unacknowledged,
            consumers=consumers,
            subscription_uuid=subscription_uuid,
            offering_uuid=offering_uuid,
            object_type=object_type,
        )

        rmq_queue_stats.additional_properties = d
        return rmq_queue_stats

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
