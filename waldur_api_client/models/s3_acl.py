from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.s3_grant import S3Grant


T = TypeVar("T", bound="S3Acl")


@_attrs_define
class S3Acl:
    """
    Attributes:
        owner (str):
        grants (list['S3Grant']):
    """

    owner: str
    grants: list["S3Grant"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner = self.owner

        grants = []
        for grants_item_data in self.grants:
            grants_item = grants_item_data.to_dict()
            grants.append(grants_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "grants": grants,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_grant import S3Grant

        d = dict(src_dict)
        owner = d.pop("owner")

        grants = []
        _grants = d.pop("grants")
        for grants_item_data in _grants:
            grants_item = S3Grant.from_dict(grants_item_data)

            grants.append(grants_item)

        s3_acl = cls(
            owner=owner,
            grants=grants,
        )

        s3_acl.additional_properties = d
        return s3_acl

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
