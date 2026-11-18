from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="S3DeleteObjectsRequestRequest")


@_attrs_define
class S3DeleteObjectsRequestRequest:
    """
    Attributes:
        bucket (str):
        keys (Union[Unset, list[str]]): Objects to delete. Give either keys or prefix.
        prefix (Union[Unset, str]): Delete everything under this prefix, up to 10000 objects per call.
    """

    bucket: str
    keys: Union[Unset, list[str]] = UNSET
    prefix: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        keys: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keys, Unset):
            keys = self.keys

        prefix = self.prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
            }
        )
        if keys is not UNSET:
            field_dict["keys"] = keys
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket")

        keys = cast(list[str], d.pop("keys", UNSET))

        prefix = d.pop("prefix", UNSET)

        s3_delete_objects_request_request = cls(
            bucket=bucket,
            keys=keys,
            prefix=prefix,
        )

        s3_delete_objects_request_request.additional_properties = d
        return s3_delete_objects_request_request

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
