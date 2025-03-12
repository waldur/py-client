from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationGroup")


@_attrs_define
class OrganizationGroup:
    """
    Attributes:
        uuid (UUID):
        url (str):
        name (str):
        parent_uuid (UUID):
        parent_name (str):
        customers_count (int):
        parent (Union[None, Unset, str]):
    """

    uuid: UUID
    url: str
    name: str
    parent_uuid: UUID
    parent_name: str
    customers_count: int
    parent: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        url = self.url

        name = self.name

        parent_uuid = str(self.parent_uuid)

        parent_name = self.parent_name

        customers_count = self.customers_count

        parent: Union[None, Unset, str]
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "url": url,
                "name": name,
                "parent_uuid": parent_uuid,
                "parent_name": parent_name,
                "customers_count": customers_count,
            }
        )
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        url = d.pop("url")

        name = d.pop("name")

        parent_uuid = UUID(d.pop("parent_uuid"))

        parent_name = d.pop("parent_name")

        customers_count = d.pop("customers_count")

        def _parse_parent(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        organization_group = cls(
            uuid=uuid,
            url=url,
            name=name,
            parent_uuid=parent_uuid,
            parent_name=parent_name,
            customers_count=customers_count,
            parent=parent,
        )

        organization_group.additional_properties = d
        return organization_group

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
