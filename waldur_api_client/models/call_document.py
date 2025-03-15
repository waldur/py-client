import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallDocument")


@_attrs_define
class CallDocument:
    """
    Attributes:
        uuid (UUID):
        file_name (str):
        created (datetime.datetime):
        file (Union[None, Unset, str]): Documentation for call for proposals.
        description (Union[Unset, str]):
    """

    uuid: UUID
    file_name: str
    created: datetime.datetime
    file: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        file_name = self.file_name

        created = self.created.isoformat()

        file: Union[None, Unset, str]
        if isinstance(self.file, Unset):
            file = UNSET
        else:
            file = self.file

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "file_name": file_name,
                "created": created,
            }
        )
        if file is not UNSET:
            field_dict["file"] = file
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        file_name = d.pop("file_name")

        created = isoparse(d.pop("created"))

        def _parse_file(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file = _parse_file(d.pop("file", UNSET))

        description = d.pop("description", UNSET)

        call_document = cls(
            uuid=uuid,
            file_name=file_name,
            created=created,
            file=file,
            description=description,
        )

        call_document.additional_properties = d
        return call_document

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
