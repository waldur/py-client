import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ReviewerSuggestionEntry")


@_attrs_define
class ReviewerSuggestionEntry:
    """
    Attributes:
        uuid (UUID):
        suggester_uuid (Union[None, UUID]):
        suggester_name (Union[None, str]):
        step_name (str):
        note (str):
        created (datetime.datetime):
    """

    uuid: UUID
    suggester_uuid: Union[None, UUID]
    suggester_name: Union[None, str]
    step_name: str
    note: str
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        suggester_uuid: Union[None, str]
        if isinstance(self.suggester_uuid, UUID):
            suggester_uuid = str(self.suggester_uuid)
        else:
            suggester_uuid = self.suggester_uuid

        suggester_name: Union[None, str]
        suggester_name = self.suggester_name

        step_name = self.step_name

        note = self.note

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "suggester_uuid": suggester_uuid,
                "suggester_name": suggester_name,
                "step_name": step_name,
                "note": note,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        def _parse_suggester_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suggester_uuid_type_0 = UUID(data)

                return suggester_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        suggester_uuid = _parse_suggester_uuid(d.pop("suggester_uuid"))

        def _parse_suggester_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        suggester_name = _parse_suggester_name(d.pop("suggester_name"))

        step_name = d.pop("step_name")

        note = d.pop("note")

        created = isoparse(d.pop("created"))

        reviewer_suggestion_entry = cls(
            uuid=uuid,
            suggester_uuid=suggester_uuid,
            suggester_name=suggester_name,
            step_name=step_name,
            note=note,
            created=created,
        )

        reviewer_suggestion_entry.additional_properties = d
        return reviewer_suggestion_entry

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
