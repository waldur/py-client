import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.broadcast_message_state_enum import BroadcastMessageStateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="BroadcastMessage")


@_attrs_define
class BroadcastMessage:
    """
    Attributes:
        uuid (UUID):
        created (datetime.datetime):
        subject (str):
        body (str):
        query (Any):
        author_full_name (str):
        emails (Any):
        state (BroadcastMessageStateEnum):
        send_at (Union[None, Unset, datetime.date]):
    """

    uuid: UUID
    created: datetime.datetime
    subject: str
    body: str
    query: Any
    author_full_name: str
    emails: Any
    state: BroadcastMessageStateEnum
    send_at: Union[None, Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        created = self.created.isoformat()

        subject = self.subject

        body = self.body

        query = self.query

        author_full_name = self.author_full_name

        emails = self.emails

        state = self.state.value

        send_at: Union[None, Unset, str]
        if isinstance(self.send_at, Unset):
            send_at = UNSET
        elif isinstance(self.send_at, datetime.date):
            send_at = self.send_at.isoformat()
        else:
            send_at = self.send_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "created": created,
                "subject": subject,
                "body": body,
                "query": query,
                "author_full_name": author_full_name,
                "emails": emails,
                "state": state,
            }
        )
        if send_at is not UNSET:
            field_dict["send_at"] = send_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        subject = d.pop("subject")

        body = d.pop("body")

        query = d.pop("query")

        author_full_name = d.pop("author_full_name")

        emails = d.pop("emails")

        state = BroadcastMessageStateEnum(d.pop("state"))

        def _parse_send_at(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                send_at_type_0 = isoparse(data).date()

                return send_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        send_at = _parse_send_at(d.pop("send_at", UNSET))

        broadcast_message = cls(
            uuid=uuid,
            created=created,
            subject=subject,
            body=body,
            query=query,
            author_full_name=author_full_name,
            emails=emails,
            state=state,
            send_at=send_at,
        )

        broadcast_message.additional_properties = d
        return broadcast_message

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
