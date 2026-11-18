from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="S3CorsRule")


@_attrs_define
class S3CorsRule:
    """
    Attributes:
        allowed_origins (list[str]):
        allowed_methods (list[str]):
    """

    allowed_origins: list[str]
    allowed_methods: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_origins = self.allowed_origins

        allowed_methods = self.allowed_methods

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowed_origins": allowed_origins,
                "allowed_methods": allowed_methods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_origins = cast(list[str], d.pop("allowed_origins"))

        allowed_methods = cast(list[str], d.pop("allowed_methods"))

        s3_cors_rule = cls(
            allowed_origins=allowed_origins,
            allowed_methods=allowed_methods,
        )

        s3_cors_rule.additional_properties = d
        return s3_cors_rule

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
