from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NestedRemoteLocalCategory")


@_attrs_define
class NestedRemoteLocalCategory:
    """
    Attributes:
        local_category (str):
        remote_category (UUID):
        local_category_name (str):
        local_category_uuid (UUID):
        remote_category_name (Union[Unset, str]):
    """

    local_category: str
    remote_category: UUID
    local_category_name: str
    local_category_uuid: UUID
    remote_category_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        local_category = self.local_category

        remote_category = str(self.remote_category)

        local_category_name = self.local_category_name

        local_category_uuid = str(self.local_category_uuid)

        remote_category_name = self.remote_category_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "local_category": local_category,
                "remote_category": remote_category,
                "local_category_name": local_category_name,
                "local_category_uuid": local_category_uuid,
            }
        )
        if remote_category_name is not UNSET:
            field_dict["remote_category_name"] = remote_category_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        local_category = d.pop("local_category")

        remote_category = UUID(d.pop("remote_category"))

        local_category_name = d.pop("local_category_name")

        local_category_uuid = UUID(d.pop("local_category_uuid"))

        remote_category_name = d.pop("remote_category_name", UNSET)

        nested_remote_local_category = cls(
            local_category=local_category,
            remote_category=remote_category,
            local_category_name=local_category_name,
            local_category_uuid=local_category_uuid,
            remote_category_name=remote_category_name,
        )

        nested_remote_local_category.additional_properties = d
        return nested_remote_local_category

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
