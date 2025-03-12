from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerDetails")


@_attrs_define
class CustomerDetails:
    """
    Attributes:
        name (str):
        country_name (str):
        address (Union[Unset, str]):
        country (Union[Unset, str]):
        email (Union[Unset, str]):
        postal (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        bank_name (Union[Unset, str]):
        bank_account (Union[Unset, str]):
        vat_code (Union[Unset, str]): VAT number
    """

    name: str
    country_name: str
    address: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    postal: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    bank_name: Union[Unset, str] = UNSET
    bank_account: Union[Unset, str] = UNSET
    vat_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        country_name = self.country_name

        address = self.address

        country = self.country

        email = self.email

        postal = self.postal

        phone_number = self.phone_number

        bank_name = self.bank_name

        bank_account = self.bank_account

        vat_code = self.vat_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "country_name": country_name,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if country is not UNSET:
            field_dict["country"] = country
        if email is not UNSET:
            field_dict["email"] = email
        if postal is not UNSET:
            field_dict["postal"] = postal
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if bank_name is not UNSET:
            field_dict["bank_name"] = bank_name
        if bank_account is not UNSET:
            field_dict["bank_account"] = bank_account
        if vat_code is not UNSET:
            field_dict["vat_code"] = vat_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        country_name = d.pop("country_name")

        address = d.pop("address", UNSET)

        country = d.pop("country", UNSET)

        email = d.pop("email", UNSET)

        postal = d.pop("postal", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        bank_name = d.pop("bank_name", UNSET)

        bank_account = d.pop("bank_account", UNSET)

        vat_code = d.pop("vat_code", UNSET)

        customer_details = cls(
            name=name,
            country_name=country_name,
            address=address,
            country=country,
            email=email,
            postal=postal,
            phone_number=phone_number,
            bank_name=bank_name,
            bank_account=bank_account,
            vat_code=vat_code,
        )

        customer_details.additional_properties = d
        return customer_details

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
