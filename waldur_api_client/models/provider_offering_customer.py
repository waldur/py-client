from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderOfferingCustomer")


@_attrs_define
class ProviderOfferingCustomer:
    """
    Attributes:
        uuid (UUID):
        name (str):
        slug (str):
        abbreviation (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        email (Union[Unset, str]):
    """

    uuid: UUID
    name: str
    slug: str
    abbreviation: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        slug = self.slug

        abbreviation = self.abbreviation

        phone_number = self.phone_number

        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "slug": slug,
            }
        )
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        slug = d.pop("slug")

        abbreviation = d.pop("abbreviation", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        email = d.pop("email", UNSET)

        provider_offering_customer = cls(
            uuid=uuid,
            name=name,
            slug=slug,
            abbreviation=abbreviation,
            phone_number=phone_number,
            email=email,
        )

        provider_offering_customer.additional_properties = d
        return provider_offering_customer

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
