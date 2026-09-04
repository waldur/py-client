import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.event_consumer_scope_output import EventConsumerScopeOutput


T = TypeVar("T", bound="EventConsumer")


@_attrs_define
class EventConsumer:
    """
    Attributes:
        uuid (UUID):
        object_types (list[str]):
        scopes (list['EventConsumerScopeOutput']):
        is_global (bool):
        rmq_username (str): RabbitMQ username (UUID hex) for the consumer queue.
        queue_created (bool):
        user_uuid (UUID):
        user_username (str): Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters
        user_full_name (str):
        created (datetime.datetime):
        modified (datetime.datetime):
    """

    uuid: UUID
    object_types: list[str]
    scopes: list["EventConsumerScopeOutput"]
    is_global: bool
    rmq_username: str
    queue_created: bool
    user_uuid: UUID
    user_username: str
    user_full_name: str
    created: datetime.datetime
    modified: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        object_types = self.object_types

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.to_dict()
            scopes.append(scopes_item)

        is_global = self.is_global

        rmq_username = self.rmq_username

        queue_created = self.queue_created

        user_uuid = str(self.user_uuid)

        user_username = self.user_username

        user_full_name = self.user_full_name

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "object_types": object_types,
                "scopes": scopes,
                "is_global": is_global,
                "rmq_username": rmq_username,
                "queue_created": queue_created,
                "user_uuid": user_uuid,
                "user_username": user_username,
                "user_full_name": user_full_name,
                "created": created,
                "modified": modified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_consumer_scope_output import EventConsumerScopeOutput

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        object_types = cast(list[str], d.pop("object_types"))

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = EventConsumerScopeOutput.from_dict(scopes_item_data)

            scopes.append(scopes_item)

        is_global = d.pop("is_global")

        rmq_username = d.pop("rmq_username")

        queue_created = d.pop("queue_created")

        user_uuid = UUID(d.pop("user_uuid"))

        user_username = d.pop("user_username")

        user_full_name = d.pop("user_full_name")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        event_consumer = cls(
            uuid=uuid,
            object_types=object_types,
            scopes=scopes,
            is_global=is_global,
            rmq_username=rmq_username,
            queue_created=queue_created,
            user_uuid=user_uuid,
            user_username=user_username,
            user_full_name=user_full_name,
            created=created,
            modified=modified,
        )

        event_consumer.additional_properties = d
        return event_consumer

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
