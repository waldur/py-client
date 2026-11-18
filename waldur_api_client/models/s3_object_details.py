import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.s3_acl import S3Acl
    from ..models.s3_metadata_entry import S3MetadataEntry
    from ..models.s3_tag import S3Tag


T = TypeVar("T", bound="S3ObjectDetails")


@_attrs_define
class S3ObjectDetails:
    """
    Attributes:
        bucket (str):
        key (str):
        size (int):
        modified (Union[None, datetime.datetime]):
        etag (str):
        multipart_parts (Union[None, int]): Part count when uploaded in parts.
        content_type (str):
        content_encoding (str):
        content_disposition (str):
        cache_control (str):
        storage_class (str):
        version_id (str):
        encryption (str): Server-side encryption algorithm.
        metadata (list['S3MetadataEntry']): User metadata (x-amz-meta-*).
        lock_mode (str):
        retain_until (Union[None, datetime.datetime]):
        legal_hold (bool):
        acl (Union['S3Acl', None]):
        is_public (Union[None, bool]):
        tags (Union[None, list['S3Tag']]):
        versions (Union[None, int]):
        delete_markers (Union[None, int]):
        versions_truncated (bool): More versions exist than were counted.
        unavailable (list[str]):
    """

    bucket: str
    key: str
    size: int
    modified: Union[None, datetime.datetime]
    etag: str
    multipart_parts: Union[None, int]
    content_type: str
    content_encoding: str
    content_disposition: str
    cache_control: str
    storage_class: str
    version_id: str
    encryption: str
    metadata: list["S3MetadataEntry"]
    lock_mode: str
    retain_until: Union[None, datetime.datetime]
    legal_hold: bool
    acl: Union["S3Acl", None]
    is_public: Union[None, bool]
    tags: Union[None, list["S3Tag"]]
    versions: Union[None, int]
    delete_markers: Union[None, int]
    versions_truncated: bool
    unavailable: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.s3_acl import S3Acl

        bucket = self.bucket

        key = self.key

        size = self.size

        modified: Union[None, str]
        if isinstance(self.modified, datetime.datetime):
            modified = self.modified.isoformat()
        else:
            modified = self.modified

        etag = self.etag

        multipart_parts: Union[None, int]
        multipart_parts = self.multipart_parts

        content_type = self.content_type

        content_encoding = self.content_encoding

        content_disposition = self.content_disposition

        cache_control = self.cache_control

        storage_class = self.storage_class

        version_id = self.version_id

        encryption = self.encryption

        metadata = []
        for metadata_item_data in self.metadata:
            metadata_item = metadata_item_data.to_dict()
            metadata.append(metadata_item)

        lock_mode = self.lock_mode

        retain_until: Union[None, str]
        if isinstance(self.retain_until, datetime.datetime):
            retain_until = self.retain_until.isoformat()
        else:
            retain_until = self.retain_until

        legal_hold = self.legal_hold

        acl: Union[None, dict[str, Any]]
        if isinstance(self.acl, S3Acl):
            acl = self.acl.to_dict()
        else:
            acl = self.acl

        is_public: Union[None, bool]
        is_public = self.is_public

        tags: Union[None, list[dict[str, Any]]]
        if isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        versions: Union[None, int]
        versions = self.versions

        delete_markers: Union[None, int]
        delete_markers = self.delete_markers

        versions_truncated = self.versions_truncated

        unavailable = self.unavailable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "key": key,
                "size": size,
                "modified": modified,
                "etag": etag,
                "multipart_parts": multipart_parts,
                "content_type": content_type,
                "content_encoding": content_encoding,
                "content_disposition": content_disposition,
                "cache_control": cache_control,
                "storage_class": storage_class,
                "version_id": version_id,
                "encryption": encryption,
                "metadata": metadata,
                "lock_mode": lock_mode,
                "retain_until": retain_until,
                "legal_hold": legal_hold,
                "acl": acl,
                "is_public": is_public,
                "tags": tags,
                "versions": versions,
                "delete_markers": delete_markers,
                "versions_truncated": versions_truncated,
                "unavailable": unavailable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_acl import S3Acl
        from ..models.s3_metadata_entry import S3MetadataEntry
        from ..models.s3_tag import S3Tag

        d = dict(src_dict)
        bucket = d.pop("bucket")

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

        def _parse_multipart_parts(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        multipart_parts = _parse_multipart_parts(d.pop("multipart_parts"))

        content_type = d.pop("content_type")

        content_encoding = d.pop("content_encoding")

        content_disposition = d.pop("content_disposition")

        cache_control = d.pop("cache_control")

        storage_class = d.pop("storage_class")

        version_id = d.pop("version_id")

        encryption = d.pop("encryption")

        metadata = []
        _metadata = d.pop("metadata")
        for metadata_item_data in _metadata:
            metadata_item = S3MetadataEntry.from_dict(metadata_item_data)

            metadata.append(metadata_item)

        lock_mode = d.pop("lock_mode")

        def _parse_retain_until(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retain_until_type_0 = isoparse(data)

                return retain_until_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        retain_until = _parse_retain_until(d.pop("retain_until"))

        legal_hold = d.pop("legal_hold")

        def _parse_acl(data: object) -> Union["S3Acl", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                acl_type_1 = S3Acl.from_dict(data)

                return acl_type_1
            except:  # noqa: E722
                pass
            return cast(Union["S3Acl", None], data)

        acl = _parse_acl(d.pop("acl"))

        def _parse_is_public(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        is_public = _parse_is_public(d.pop("is_public"))

        def _parse_tags(data: object) -> Union[None, list["S3Tag"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = S3Tag.from_dict(tags_type_0_item_data)

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["S3Tag"]], data)

        tags = _parse_tags(d.pop("tags"))

        def _parse_versions(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        versions = _parse_versions(d.pop("versions"))

        def _parse_delete_markers(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        delete_markers = _parse_delete_markers(d.pop("delete_markers"))

        versions_truncated = d.pop("versions_truncated")

        unavailable = cast(list[str], d.pop("unavailable"))

        s3_object_details = cls(
            bucket=bucket,
            key=key,
            size=size,
            modified=modified,
            etag=etag,
            multipart_parts=multipart_parts,
            content_type=content_type,
            content_encoding=content_encoding,
            content_disposition=content_disposition,
            cache_control=cache_control,
            storage_class=storage_class,
            version_id=version_id,
            encryption=encryption,
            metadata=metadata,
            lock_mode=lock_mode,
            retain_until=retain_until,
            legal_hold=legal_hold,
            acl=acl,
            is_public=is_public,
            tags=tags,
            versions=versions,
            delete_markers=delete_markers,
            versions_truncated=versions_truncated,
            unavailable=unavailable,
        )

        s3_object_details.additional_properties = d
        return s3_object_details

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
