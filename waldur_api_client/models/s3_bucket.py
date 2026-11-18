import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.s3_versioning_status_enum import S3VersioningStatusEnum

T = TypeVar("T", bound="S3Bucket")


@_attrs_define
class S3Bucket:
    """
    Attributes:
        name (str):
        created (Union[None, datetime.datetime]):
        objects (Union[None, int]): Null when the gateway reports no statistics.
        size_bytes (Union[None, int]): Null when the gateway reports no statistics.
        versioning (Union[None, S3VersioningStatusEnum]):
        is_public (Union[None, bool]): Readable by anyone through an ACL grant or a public policy; null when the gateway
            would not say.
    """

    name: str
    created: Union[None, datetime.datetime]
    objects: Union[None, int]
    size_bytes: Union[None, int]
    versioning: Union[None, S3VersioningStatusEnum]
    is_public: Union[None, bool]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created: Union[None, str]
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        objects: Union[None, int]
        objects = self.objects

        size_bytes: Union[None, int]
        size_bytes = self.size_bytes

        versioning: Union[None, str]
        if isinstance(self.versioning, S3VersioningStatusEnum):
            versioning = self.versioning.value
        else:
            versioning = self.versioning

        is_public: Union[None, bool]
        is_public = self.is_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created": created,
                "objects": objects,
                "size_bytes": size_bytes,
                "versioning": versioning,
                "is_public": is_public,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_created(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        created = _parse_created(d.pop("created"))

        def _parse_objects(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        objects = _parse_objects(d.pop("objects"))

        def _parse_size_bytes(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        size_bytes = _parse_size_bytes(d.pop("size_bytes"))

        def _parse_versioning(data: object) -> Union[None, S3VersioningStatusEnum]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                versioning_type_0 = S3VersioningStatusEnum(data)

                return versioning_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, S3VersioningStatusEnum], data)

        versioning = _parse_versioning(d.pop("versioning"))

        def _parse_is_public(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        is_public = _parse_is_public(d.pop("is_public"))

        s3_bucket = cls(
            name=name,
            created=created,
            objects=objects,
            size_bytes=size_bytes,
            versioning=versioning,
            is_public=is_public,
        )

        s3_bucket.additional_properties = d
        return s3_bucket

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
