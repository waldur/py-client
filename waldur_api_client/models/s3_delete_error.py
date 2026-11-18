from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="S3DeleteError")


@_attrs_define
class S3DeleteError:
    """
    Attributes:
        key (Union[None, str]):
        code (Union[None, str]):
        detail (Union[None, str]):
    """

    key: Union[None, str]
    code: Union[None, str]
    detail: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key: Union[None, str]
        key = self.key

        code: Union[None, str]
        code = self.code

        detail: Union[None, str]
        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "code": code,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_key(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        key = _parse_key(d.pop("key"))

        def _parse_code(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        code = _parse_code(d.pop("code"))

        def _parse_detail(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        detail = _parse_detail(d.pop("detail"))

        s3_delete_error = cls(
            key=key,
            code=code,
            detail=detail,
        )

        s3_delete_error.additional_properties = d
        return s3_delete_error

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
