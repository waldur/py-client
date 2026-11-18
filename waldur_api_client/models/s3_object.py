import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="S3Object")


@_attrs_define
class S3Object:
    """
    Attributes:
        key (str):
        size (int):
        modified (Union[None, datetime.datetime]):
        etag (str):
        storage_class (str):
    """

    key: str
    size: int
    modified: Union[None, datetime.datetime]
    etag: str
    storage_class: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        size = self.size

        modified: Union[None, str]
        if isinstance(self.modified, datetime.datetime):
            modified = self.modified.isoformat()
        else:
            modified = self.modified

        etag = self.etag

        storage_class = self.storage_class

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "size": size,
                "modified": modified,
                "etag": etag,
                "storage_class": storage_class,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        size = d.pop("size")

        def _parse_modified(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_type_0 = isoparse(data)

                return modified_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        modified = _parse_modified(d.pop("modified"))

        etag = d.pop("etag")

        storage_class = d.pop("storage_class")

        s3_object = cls(
            key=key,
            size=size,
            modified=modified,
            etag=etag,
            storage_class=storage_class,
        )

        s3_object.additional_properties = d
        return s3_object

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
