import datetime
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="OfferingFile")


@_attrs_define
class OfferingFile:
    """
    Attributes:
        url (str):
        uuid (UUID):
        name (str):
        offering (str):
        created (datetime.datetime):
        file (str):
    """

    url: str
    uuid: UUID
    name: str
    offering: str
    created: datetime.datetime
    file: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        name = self.name

        offering = self.offering

        created = self.created.isoformat()

        file = self.file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "offering": offering,
                "created": created,
                "file": file,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        offering = d.pop("offering")

        created = isoparse(d.pop("created"))

        file = d.pop("file")

        offering_file = cls(
            url=url,
            uuid=uuid,
            name=name,
            offering=offering,
            created=created,
            file=file,
        )

        offering_file.additional_properties = d
        return offering_file

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
