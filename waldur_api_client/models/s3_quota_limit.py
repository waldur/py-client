from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="S3QuotaLimit")


@_attrs_define
class S3QuotaLimit:
    """
    Attributes:
        max_size_bytes (Union[None, int]):
        max_objects (Union[None, int]):
    """

    max_size_bytes: Union[None, int]
    max_objects: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_size_bytes: Union[None, int]
        max_size_bytes = self.max_size_bytes

        max_objects: Union[None, int]
        max_objects = self.max_objects

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max_size_bytes": max_size_bytes,
                "max_objects": max_objects,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_max_size_bytes(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        max_size_bytes = _parse_max_size_bytes(d.pop("max_size_bytes"))

        def _parse_max_objects(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        max_objects = _parse_max_objects(d.pop("max_objects"))

        s3_quota_limit = cls(
            max_size_bytes=max_size_bytes,
            max_objects=max_objects,
        )

        s3_quota_limit.additional_properties = d
        return s3_quota_limit

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
