import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.message_role_enum import MessageRoleEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """
    Attributes:
        uuid (UUID):
        thread (UUID):
        role (MessageRoleEnum):
        content (str):
        sequence_index (int):
        created (datetime.datetime):
        replaces (Union[None, UUID, Unset]):
    """

    uuid: UUID
    thread: UUID
    role: MessageRoleEnum
    content: str
    sequence_index: int
    created: datetime.datetime
    replaces: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        thread = str(self.thread)

        role = self.role.value

        content = self.content

        sequence_index = self.sequence_index

        created = self.created.isoformat()

        replaces: Union[None, Unset, str]
        if isinstance(self.replaces, Unset):
            replaces = UNSET
        elif isinstance(self.replaces, UUID):
            replaces = str(self.replaces)
        else:
            replaces = self.replaces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "thread": thread,
                "role": role,
                "content": content,
                "sequence_index": sequence_index,
                "created": created,
            }
        )
        if replaces is not UNSET:
            field_dict["replaces"] = replaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        thread = UUID(d.pop("thread"))

        role = MessageRoleEnum(d.pop("role"))

        content = d.pop("content")

        sequence_index = d.pop("sequence_index")

        created = isoparse(d.pop("created"))

        def _parse_replaces(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                replaces_type_0 = UUID(data)

                return replaces_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        replaces = _parse_replaces(d.pop("replaces", UNSET))

        message = cls(
            uuid=uuid,
            thread=thread,
            role=role,
            content=content,
            sequence_index=sequence_index,
            created=created,
            replaces=replaces,
        )

        message.additional_properties = d
        return message

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
