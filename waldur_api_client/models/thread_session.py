import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThreadSession")


@_attrs_define
class ThreadSession:
    """
    Attributes:
        uuid (Union[Unset, UUID]):
        name (Union[Unset, str]):
        chat_session (Union[Unset, UUID]):
        flags (Union[Unset, Any]):
        is_archived (Union[Unset, bool]):
        message_count (Union[Unset, int]):
        created (Union[Unset, datetime.datetime]):
    """

    uuid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    chat_session: Union[Unset, UUID] = UNSET
    flags: Union[Unset, Any] = UNSET
    is_archived: Union[Unset, bool] = UNSET
    message_count: Union[Unset, int] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: Union[Unset, str] = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        name = self.name

        chat_session: Union[Unset, str] = UNSET
        if not isinstance(self.chat_session, Unset):
            chat_session = str(self.chat_session)

        flags = self.flags

        is_archived = self.is_archived

        message_count = self.message_count

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if chat_session is not UNSET:
            field_dict["chat_session"] = chat_session
        if flags is not UNSET:
            field_dict["flags"] = flags
        if is_archived is not UNSET:
            field_dict["is_archived"] = is_archived
        if message_count is not UNSET:
            field_dict["message_count"] = message_count
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: Union[Unset, UUID]
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        name = d.pop("name", UNSET)

        _chat_session = d.pop("chat_session", UNSET)
        chat_session: Union[Unset, UUID]
        if isinstance(_chat_session, Unset):
            chat_session = UNSET
        else:
            chat_session = UUID(_chat_session)

        flags = d.pop("flags", UNSET)

        is_archived = d.pop("is_archived", UNSET)

        message_count = d.pop("message_count", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        thread_session = cls(
            uuid=uuid,
            name=name,
            chat_session=chat_session,
            flags=flags,
            is_archived=is_archived,
            message_count=message_count,
            created=created,
        )

        thread_session.additional_properties = d
        return thread_session

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
