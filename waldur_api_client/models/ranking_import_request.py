from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="RankingImportRequest")


@_attrs_define
class RankingImportRequest:
    """
    Attributes:
        round_ (UUID):
        file (File): CSV with a header row: proposal_uuid or proposal_slug, rank, final_score, notes, and
            recommended:<requested offering uuid>:<component type> per recommended amount -- the columns the export writes.
        meeting_note (Union[None, UUID, Unset]): The round report to import the ranking of; empty for the round's
            overall ranking.
    """

    round_: UUID
    file: File
    meeting_note: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        round_ = str(self.round_)

        file = self.file.to_tuple()

        meeting_note: Union[None, Unset, str]
        if isinstance(self.meeting_note, Unset):
            meeting_note = UNSET
        elif isinstance(self.meeting_note, UUID):
            meeting_note = str(self.meeting_note)
        else:
            meeting_note = self.meeting_note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "round": round_,
                "file": file,
            }
        )
        if meeting_note is not UNSET:
            field_dict["meeting_note"] = meeting_note

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("round", (None, str(self.round_), "text/plain")))

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.meeting_note, Unset):
            if isinstance(self.meeting_note, UUID):
                files.append(("meeting_note", (None, str(self.meeting_note), "text/plain")))
            else:
                files.append(("meeting_note", (None, str(self.meeting_note).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        round_ = UUID(d.pop("round"))

        file = File(payload=BytesIO(d.pop("file")))

        def _parse_meeting_note(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                meeting_note_type_0 = UUID(data)

                return meeting_note_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        meeting_note = _parse_meeting_note(d.pop("meeting_note", UNSET))

        ranking_import_request = cls(
            round_=round_,
            file=file,
            meeting_note=meeting_note,
        )

        ranking_import_request.additional_properties = d
        return ranking_import_request

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
