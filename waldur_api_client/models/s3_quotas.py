from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scope_enum import ScopeEnum

if TYPE_CHECKING:
    from ..models.s3_quota_limit import S3QuotaLimit


T = TypeVar("T", bound="S3Quotas")


@_attrs_define
class S3Quotas:
    """
    Attributes:
        scope (ScopeEnum):
        total (Union['S3QuotaLimit', None]): Limit across all buckets; null when unlimited.
        per_bucket (Union['S3QuotaLimit', None]): Limit on each bucket; null when unlimited.
    """

    scope: ScopeEnum
    total: Union["S3QuotaLimit", None]
    per_bucket: Union["S3QuotaLimit", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.s3_quota_limit import S3QuotaLimit

        scope = self.scope.value

        total: Union[None, dict[str, Any]]
        if isinstance(self.total, S3QuotaLimit):
            total = self.total.to_dict()
        else:
            total = self.total

        per_bucket: Union[None, dict[str, Any]]
        if isinstance(self.per_bucket, S3QuotaLimit):
            per_bucket = self.per_bucket.to_dict()
        else:
            per_bucket = self.per_bucket

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scope": scope,
                "total": total,
                "per_bucket": per_bucket,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_quota_limit import S3QuotaLimit

        d = dict(src_dict)
        scope = ScopeEnum(d.pop("scope"))

        def _parse_total(data: object) -> Union["S3QuotaLimit", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_type_1 = S3QuotaLimit.from_dict(data)

                return total_type_1
            except:  # noqa: E722
                pass
            return cast(Union["S3QuotaLimit", None], data)

        total = _parse_total(d.pop("total"))

        def _parse_per_bucket(data: object) -> Union["S3QuotaLimit", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                per_bucket_type_1 = S3QuotaLimit.from_dict(data)

                return per_bucket_type_1
            except:  # noqa: E722
                pass
            return cast(Union["S3QuotaLimit", None], data)

        per_bucket = _parse_per_bucket(d.pop("per_bucket"))

        s3_quotas = cls(
            scope=scope,
            total=total,
            per_bucket=per_bucket,
        )

        s3_quotas.additional_properties = d
        return s3_quotas

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
