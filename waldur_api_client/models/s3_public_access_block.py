from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="S3PublicAccessBlock")


@_attrs_define
class S3PublicAccessBlock:
    """
    Attributes:
        block_public_acls (bool):
        ignore_public_acls (bool):
        block_public_policy (bool):
        restrict_public_buckets (bool):
    """

    block_public_acls: bool
    ignore_public_acls: bool
    block_public_policy: bool
    restrict_public_buckets: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_public_acls = self.block_public_acls

        ignore_public_acls = self.ignore_public_acls

        block_public_policy = self.block_public_policy

        restrict_public_buckets = self.restrict_public_buckets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "block_public_acls": block_public_acls,
                "ignore_public_acls": ignore_public_acls,
                "block_public_policy": block_public_policy,
                "restrict_public_buckets": restrict_public_buckets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block_public_acls = d.pop("block_public_acls")

        ignore_public_acls = d.pop("ignore_public_acls")

        block_public_policy = d.pop("block_public_policy")

        restrict_public_buckets = d.pop("restrict_public_buckets")

        s3_public_access_block = cls(
            block_public_acls=block_public_acls,
            ignore_public_acls=ignore_public_acls,
            block_public_policy=block_public_policy,
            restrict_public_buckets=restrict_public_buckets,
        )

        s3_public_access_block.additional_properties = d
        return s3_public_access_block

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
