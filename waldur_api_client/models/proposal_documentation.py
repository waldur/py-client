import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ProposalDocumentation")


@_attrs_define
class ProposalDocumentation:
    """
    Attributes:
        uuid (UUID):
        file (str): Upload supporting documentation in PDF format.
        file_name (str):
        file_size (Union[None, int]):
        file_hash (Union[None, str]): SHA-256 of the file's content, as the duplicate check compares it: a client can
            tell a file is already attached before uploading it.
        created (datetime.datetime):
    """

    uuid: UUID
    file: str
    file_name: str
    file_size: Union[None, int]
    file_hash: Union[None, str]
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        file = self.file

        file_name = self.file_name

        file_size: Union[None, int]
        file_size = self.file_size

        file_hash: Union[None, str]
        file_hash = self.file_hash

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "file": file,
                "file_name": file_name,
                "file_size": file_size,
                "file_hash": file_hash,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        file = d.pop("file")

        file_name = d.pop("file_name")

        def _parse_file_size(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        file_size = _parse_file_size(d.pop("file_size"))

        def _parse_file_hash(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        file_hash = _parse_file_hash(d.pop("file_hash"))

        created = isoparse(d.pop("created"))

        proposal_documentation = cls(
            uuid=uuid,
            file=file,
            file_name=file_name,
            file_size=file_size,
            file_hash=file_hash,
            created=created,
        )

        proposal_documentation.additional_properties = d
        return proposal_documentation

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
