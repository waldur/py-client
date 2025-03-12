import datetime
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="NestedOfferingFile")


@_attrs_define
class NestedOfferingFile:
    """
    Attributes:
        name (str):
        created (datetime.datetime):
        file (str):
    """

    name: str
    created: datetime.datetime
    file: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created = self.created.isoformat()

        file = self.file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created": created,
                "file": file,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        created = isoparse(d.pop("created"))

        file = d.pop("file")

        nested_offering_file = cls(
            name=name,
            created=created,
            file=file,
        )

        nested_offering_file.additional_properties = d
        return nested_offering_file

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
