from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.s3_delete_error import S3DeleteError


T = TypeVar("T", bound="S3DeleteObjectsResult")


@_attrs_define
class S3DeleteObjectsResult:
    """
    Attributes:
        deleted (int):
        errors (list['S3DeleteError']):
        remaining (bool): More objects remain under the prefix; repeat the request.
    """

    deleted: int
    errors: list["S3DeleteError"]
    remaining: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted = self.deleted

        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        remaining = self.remaining

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deleted": deleted,
                "errors": errors,
                "remaining": remaining,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_delete_error import S3DeleteError

        d = dict(src_dict)
        deleted = d.pop("deleted")

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = S3DeleteError.from_dict(errors_item_data)

            errors.append(errors_item)

        remaining = d.pop("remaining")

        s3_delete_objects_result = cls(
            deleted=deleted,
            errors=errors,
            remaining=remaining,
        )

        s3_delete_objects_result.additional_properties = d
        return s3_delete_objects_result

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
