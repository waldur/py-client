import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="RoundMeetingNoteDocument")


@_attrs_define
class RoundMeetingNoteDocument:
    """
    Attributes:
        uuid (UUID):
        file (str):
        name (str):
        created (datetime.datetime):
    """

    uuid: UUID
    file: str
    name: str
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        file = self.file

        name = self.name

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "file": file,
                "name": name,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        file = d.pop("file")

        name = d.pop("name")

        created = isoparse(d.pop("created"))

        round_meeting_note_document = cls(
            uuid=uuid,
            file=file,
            name=name,
            created=created,
        )

        round_meeting_note_document.additional_properties = d
        return round_meeting_note_document

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
