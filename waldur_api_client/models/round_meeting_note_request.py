from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="RoundMeetingNoteRequest")


@_attrs_define
class RoundMeetingNoteRequest:
    """
    Attributes:
        round_ (UUID):
        title (str):
        body (Union[Unset, str]):
        new_documents (Union[Unset, list[File]]): Files to attach to the note.
        removed_documents (Union[Unset, list[UUID]]): UUIDs of attached documents to remove.
    """

    round_: UUID
    title: str
    body: Union[Unset, str] = UNSET
    new_documents: Union[Unset, list[File]] = UNSET
    removed_documents: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        round_ = str(self.round_)

        title = self.title

        body = self.body

        new_documents: Union[Unset, list[types.FileTypes]] = UNSET
        if not isinstance(self.new_documents, Unset):
            new_documents = []
            for new_documents_item_data in self.new_documents:
                new_documents_item = new_documents_item_data.to_tuple()

                new_documents.append(new_documents_item)

        removed_documents: Union[Unset, list[str]] = UNSET
        if not isinstance(self.removed_documents, Unset):
            removed_documents = []
            for removed_documents_item_data in self.removed_documents:
                removed_documents_item = str(removed_documents_item_data)
                removed_documents.append(removed_documents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "round": round_,
                "title": title,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body
        if new_documents is not UNSET:
            field_dict["new_documents"] = new_documents
        if removed_documents is not UNSET:
            field_dict["removed_documents"] = removed_documents

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("round", (None, str(self.round_), "text/plain")))

        files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.body, Unset):
            files.append(("body", (None, str(self.body).encode(), "text/plain")))

        if not isinstance(self.new_documents, Unset):
            for new_documents_item_element in self.new_documents:
                files.append(("new_documents", new_documents_item_element.to_tuple()))

        if not isinstance(self.removed_documents, Unset):
            for removed_documents_item_element in self.removed_documents:
                files.append(("removed_documents", (None, str(removed_documents_item_element), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        round_ = UUID(d.pop("round"))

        title = d.pop("title")

        body = d.pop("body", UNSET)

        new_documents = []
        _new_documents = d.pop("new_documents", UNSET)
        for new_documents_item_data in _new_documents or []:
            new_documents_item = File(payload=BytesIO(new_documents_item_data))

            new_documents.append(new_documents_item)

        removed_documents = []
        _removed_documents = d.pop("removed_documents", UNSET)
        for removed_documents_item_data in _removed_documents or []:
            removed_documents_item = UUID(removed_documents_item_data)

            removed_documents.append(removed_documents_item)

        round_meeting_note_request = cls(
            round_=round_,
            title=title,
            body=body,
            new_documents=new_documents,
            removed_documents=removed_documents,
        )

        round_meeting_note_request.additional_properties = d
        return round_meeting_note_request

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
