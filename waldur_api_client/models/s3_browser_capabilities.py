from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.s3_browser_flavor_enum import S3BrowserFlavorEnum

T = TypeVar("T", bound="S3BrowserCapabilities")


@_attrs_define
class S3BrowserCapabilities:
    """
    Attributes:
        flavor (S3BrowserFlavorEnum):
        bucket_stats (bool): Buckets carry an object count and bytes used.
        bucket_parts (list[str]): Bucket details the gateway implements; others are always null.
        object_parts (list[str]): Object details (acl, tags, versions) the gateway implements.
    """

    flavor: S3BrowserFlavorEnum
    bucket_stats: bool
    bucket_parts: list[str]
    object_parts: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flavor = self.flavor.value

        bucket_stats = self.bucket_stats

        bucket_parts = self.bucket_parts

        object_parts = self.object_parts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "flavor": flavor,
                "bucket_stats": bucket_stats,
                "bucket_parts": bucket_parts,
                "object_parts": object_parts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        flavor = S3BrowserFlavorEnum(d.pop("flavor"))

        bucket_stats = d.pop("bucket_stats")

        bucket_parts = cast(list[str], d.pop("bucket_parts"))

        object_parts = cast(list[str], d.pop("object_parts"))

        s3_browser_capabilities = cls(
            flavor=flavor,
            bucket_stats=bucket_stats,
            bucket_parts=bucket_parts,
            object_parts=object_parts,
        )

        s3_browser_capabilities.additional_properties = d
        return s3_browser_capabilities

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
