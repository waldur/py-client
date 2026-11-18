from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.s3_object import S3Object


T = TypeVar("T", bound="S3ObjectList")


@_attrs_define
class S3ObjectList:
    """
    Attributes:
        bucket (str):
        prefix (str):
        folders (list[str]):
        objects (list['S3Object']):
        next_continuation_token (str):
        is_truncated (bool):
    """

    bucket: str
    prefix: str
    folders: list[str]
    objects: list["S3Object"]
    next_continuation_token: str
    is_truncated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        prefix = self.prefix

        folders = self.folders

        objects = []
        for objects_item_data in self.objects:
            objects_item = objects_item_data.to_dict()
            objects.append(objects_item)

        next_continuation_token = self.next_continuation_token

        is_truncated = self.is_truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "prefix": prefix,
                "folders": folders,
                "objects": objects,
                "next_continuation_token": next_continuation_token,
                "is_truncated": is_truncated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_object import S3Object

        d = dict(src_dict)
        bucket = d.pop("bucket")

        prefix = d.pop("prefix")

        folders = cast(list[str], d.pop("folders"))

        objects = []
        _objects = d.pop("objects")
        for objects_item_data in _objects:
            objects_item = S3Object.from_dict(objects_item_data)

            objects.append(objects_item)

        next_continuation_token = d.pop("next_continuation_token")

        is_truncated = d.pop("is_truncated")

        s3_object_list = cls(
            bucket=bucket,
            prefix=prefix,
            folders=folders,
            objects=objects,
            next_continuation_token=next_continuation_token,
            is_truncated=is_truncated,
        )

        s3_object_list.additional_properties = d
        return s3_object_list

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
