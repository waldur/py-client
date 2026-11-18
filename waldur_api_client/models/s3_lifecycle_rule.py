from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="S3LifecycleRule")


@_attrs_define
class S3LifecycleRule:
    """
    Attributes:
        id (str):
        enabled (bool):
        prefix (str):
        expiration_days (Union[None, int]):
        noncurrent_expiration_days (Union[None, int]):
        abort_multipart_days (Union[None, int]):
        transitions (int):
    """

    id: str
    enabled: bool
    prefix: str
    expiration_days: Union[None, int]
    noncurrent_expiration_days: Union[None, int]
    abort_multipart_days: Union[None, int]
    transitions: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        enabled = self.enabled

        prefix = self.prefix

        expiration_days: Union[None, int]
        expiration_days = self.expiration_days

        noncurrent_expiration_days: Union[None, int]
        noncurrent_expiration_days = self.noncurrent_expiration_days

        abort_multipart_days: Union[None, int]
        abort_multipart_days = self.abort_multipart_days

        transitions = self.transitions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "enabled": enabled,
                "prefix": prefix,
                "expiration_days": expiration_days,
                "noncurrent_expiration_days": noncurrent_expiration_days,
                "abort_multipart_days": abort_multipart_days,
                "transitions": transitions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        enabled = d.pop("enabled")

        prefix = d.pop("prefix")

        def _parse_expiration_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        expiration_days = _parse_expiration_days(d.pop("expiration_days"))

        def _parse_noncurrent_expiration_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        noncurrent_expiration_days = _parse_noncurrent_expiration_days(d.pop("noncurrent_expiration_days"))

        def _parse_abort_multipart_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        abort_multipart_days = _parse_abort_multipart_days(d.pop("abort_multipart_days"))

        transitions = d.pop("transitions")

        s3_lifecycle_rule = cls(
            id=id,
            enabled=enabled,
            prefix=prefix,
            expiration_days=expiration_days,
            noncurrent_expiration_days=noncurrent_expiration_days,
            abort_multipart_days=abort_multipart_days,
            transitions=transitions,
        )

        s3_lifecycle_rule.additional_properties = d
        return s3_lifecycle_rule

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
