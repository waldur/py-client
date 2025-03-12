import datetime
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Attachment")


@_attrs_define
class Attachment:
    """
    Attributes:
        url (str):
        uuid (UUID):
        issue (str):
        issue_key (str):
        created (datetime.datetime):
        file (str):
        mime_type (str):
        file_size (int):
        file_name (str):
        backend_id (str):
        destroy_is_available (bool):
    """

    url: str
    uuid: UUID
    issue: str
    issue_key: str
    created: datetime.datetime
    file: str
    mime_type: str
    file_size: int
    file_name: str
    backend_id: str
    destroy_is_available: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        issue = self.issue

        issue_key = self.issue_key

        created = self.created.isoformat()

        file = self.file

        mime_type = self.mime_type

        file_size = self.file_size

        file_name = self.file_name

        backend_id = self.backend_id

        destroy_is_available = self.destroy_is_available

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "issue": issue,
                "issue_key": issue_key,
                "created": created,
                "file": file,
                "mime_type": mime_type,
                "file_size": file_size,
                "file_name": file_name,
                "backend_id": backend_id,
                "destroy_is_available": destroy_is_available,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        issue = d.pop("issue")

        issue_key = d.pop("issue_key")

        created = isoparse(d.pop("created"))

        file = d.pop("file")

        mime_type = d.pop("mime_type")

        file_size = d.pop("file_size")

        file_name = d.pop("file_name")

        backend_id = d.pop("backend_id")

        destroy_is_available = d.pop("destroy_is_available")

        attachment = cls(
            url=url,
            uuid=uuid,
            issue=issue,
            issue_key=issue_key,
            created=created,
            file=file,
            mime_type=mime_type,
            file_size=file_size,
            file_name=file_name,
            backend_id=backend_id,
            destroy_is_available=destroy_is_available,
        )

        attachment.additional_properties = d
        return attachment

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
