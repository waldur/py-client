import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.round_meeting_note_document import RoundMeetingNoteDocument
    from ..models.round_report_proposal import RoundReportProposal


T = TypeVar("T", bound="RoundMeetingNote")


@_attrs_define
class RoundMeetingNote:
    """
    Attributes:
        uuid (UUID):
        round_ (UUID):
        round_uuid (UUID):
        round_name (str):
        call_uuid (UUID):
        call_name (str):
        title (str):
        author_name (Union[None, str]):
        author_uuid (Union[None, UUID]):
        call_step_uuid (Union[None, UUID]): The round step a round report is for; null for a free note.
        call_step_name (Union[None, str]):
        is_report (bool):
        report_proposals (list['RoundReportProposal']): The proposals a round report covers.
        submitted_at (Union[None, datetime.datetime]):
        has_checklist (bool): Whether the round report answers its step's form.
        can_edit (bool):
        documents (list['RoundMeetingNoteDocument']):
        created (datetime.datetime):
        modified (datetime.datetime):
        body (Union[Unset, str]):
    """

    uuid: UUID
    round_: UUID
    round_uuid: UUID
    round_name: str
    call_uuid: UUID
    call_name: str
    title: str
    author_name: Union[None, str]
    author_uuid: Union[None, UUID]
    call_step_uuid: Union[None, UUID]
    call_step_name: Union[None, str]
    is_report: bool
    report_proposals: list["RoundReportProposal"]
    submitted_at: Union[None, datetime.datetime]
    has_checklist: bool
    can_edit: bool
    documents: list["RoundMeetingNoteDocument"]
    created: datetime.datetime
    modified: datetime.datetime
    body: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        round_ = str(self.round_)

        round_uuid = str(self.round_uuid)

        round_name = self.round_name

        call_uuid = str(self.call_uuid)

        call_name = self.call_name

        title = self.title

        author_name: Union[None, str]
        author_name = self.author_name

        author_uuid: Union[None, str]
        if isinstance(self.author_uuid, UUID):
            author_uuid = str(self.author_uuid)
        else:
            author_uuid = self.author_uuid

        call_step_uuid: Union[None, str]
        if isinstance(self.call_step_uuid, UUID):
            call_step_uuid = str(self.call_step_uuid)
        else:
            call_step_uuid = self.call_step_uuid

        call_step_name: Union[None, str]
        call_step_name = self.call_step_name

        is_report = self.is_report

        report_proposals = []
        for report_proposals_item_data in self.report_proposals:
            report_proposals_item = report_proposals_item_data.to_dict()
            report_proposals.append(report_proposals_item)

        submitted_at: Union[None, str]
        if isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        has_checklist = self.has_checklist

        can_edit = self.can_edit

        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()
            documents.append(documents_item)

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "round": round_,
                "round_uuid": round_uuid,
                "round_name": round_name,
                "call_uuid": call_uuid,
                "call_name": call_name,
                "title": title,
                "author_name": author_name,
                "author_uuid": author_uuid,
                "call_step_uuid": call_step_uuid,
                "call_step_name": call_step_name,
                "is_report": is_report,
                "report_proposals": report_proposals,
                "submitted_at": submitted_at,
                "has_checklist": has_checklist,
                "can_edit": can_edit,
                "documents": documents,
                "created": created,
                "modified": modified,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.round_meeting_note_document import RoundMeetingNoteDocument
        from ..models.round_report_proposal import RoundReportProposal

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        round_ = UUID(d.pop("round"))

        round_uuid = UUID(d.pop("round_uuid"))

        round_name = d.pop("round_name")

        call_uuid = UUID(d.pop("call_uuid"))

        call_name = d.pop("call_name")

        title = d.pop("title")

        def _parse_author_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        author_name = _parse_author_name(d.pop("author_name"))

        def _parse_author_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                author_uuid_type_0 = UUID(data)

                return author_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        author_uuid = _parse_author_uuid(d.pop("author_uuid"))

        def _parse_call_step_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                call_step_uuid_type_0 = UUID(data)

                return call_step_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        call_step_uuid = _parse_call_step_uuid(d.pop("call_step_uuid"))

        def _parse_call_step_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        call_step_name = _parse_call_step_name(d.pop("call_step_name"))

        is_report = d.pop("is_report")

        report_proposals = []
        _report_proposals = d.pop("report_proposals")
        for report_proposals_item_data in _report_proposals:
            report_proposals_item = RoundReportProposal.from_dict(report_proposals_item_data)

            report_proposals.append(report_proposals_item)

        def _parse_submitted_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = isoparse(data)

                return submitted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at"))

        has_checklist = d.pop("has_checklist")

        can_edit = d.pop("can_edit")

        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = RoundMeetingNoteDocument.from_dict(documents_item_data)

            documents.append(documents_item)

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        body = d.pop("body", UNSET)

        round_meeting_note = cls(
            uuid=uuid,
            round_=round_,
            round_uuid=round_uuid,
            round_name=round_name,
            call_uuid=call_uuid,
            call_name=call_name,
            title=title,
            author_name=author_name,
            author_uuid=author_uuid,
            call_step_uuid=call_step_uuid,
            call_step_name=call_step_name,
            is_report=is_report,
            report_proposals=report_proposals,
            submitted_at=submitted_at,
            has_checklist=has_checklist,
            can_edit=can_edit,
            documents=documents,
            created=created,
            modified=modified,
            body=body,
        )

        round_meeting_note.additional_properties = d
        return round_meeting_note

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
