from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.s3_versioning_status_enum import S3VersioningStatusEnum

T = TypeVar("T", bound="S3Versioning")


@_attrs_define
class S3Versioning:
    """
    Attributes:
        status (S3VersioningStatusEnum):
        mfa_delete (bool):
    """

    status: S3VersioningStatusEnum
    mfa_delete: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        mfa_delete = self.mfa_delete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "mfa_delete": mfa_delete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = S3VersioningStatusEnum(d.pop("status"))

        mfa_delete = d.pop("mfa_delete")

        s3_versioning = cls(
            status=status,
            mfa_delete=mfa_delete,
        )

        s3_versioning.additional_properties = d
        return s3_versioning

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
