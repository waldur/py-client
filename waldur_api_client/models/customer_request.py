from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.country_enum import CountryEnum
from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="CustomerRequest")


@_attrs_define
class CustomerRequest:
    """
    Attributes:
        name (str):
        backend_id (Union[Unset, str]): Organization identifier in another application.
        image (Union[File, None, Unset]):
        native_name (Union[Unset, str]):
        abbreviation (Union[Unset, str]):
        contact_details (Union[Unset, str]):
        email (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        registration_code (Union[Unset, str]):
        homepage (Union[Unset, str]):
        vat_code (Union[Unset, str]): VAT number
        postal (Union[Unset, str]):
        address (Union[Unset, str]):
        bank_name (Union[Unset, str]):
        latitude (Union[None, Unset, float]):
        longitude (Union[None, Unset, float]):
        bank_account (Union[Unset, str]):
        country (Union[BlankEnum, CountryEnum, Unset]):
    """

    name: str
    backend_id: Union[Unset, str] = UNSET
    image: Union[File, None, Unset] = UNSET
    native_name: Union[Unset, str] = UNSET
    abbreviation: Union[Unset, str] = UNSET
    contact_details: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    registration_code: Union[Unset, str] = UNSET
    homepage: Union[Unset, str] = UNSET
    vat_code: Union[Unset, str] = UNSET
    postal: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    bank_name: Union[Unset, str] = UNSET
    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    bank_account: Union[Unset, str] = UNSET
    country: Union[BlankEnum, CountryEnum, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        backend_id = self.backend_id

        image: Union[FileJsonType, None, Unset]
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, File):
            image = self.image.to_tuple()

        else:
            image = self.image

        native_name = self.native_name

        abbreviation = self.abbreviation

        contact_details = self.contact_details

        email = self.email

        phone_number = self.phone_number

        registration_code = self.registration_code

        homepage = self.homepage

        vat_code = self.vat_code

        postal = self.postal

        address = self.address

        bank_name = self.bank_name

        latitude: Union[None, Unset, float]
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: Union[None, Unset, float]
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        bank_account = self.bank_account

        country: Union[Unset, str]
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, CountryEnum):
            country = self.country.value
        else:
            country = self.country.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if image is not UNSET:
            field_dict["image"] = image
        if native_name is not UNSET:
            field_dict["native_name"] = native_name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if contact_details is not UNSET:
            field_dict["contact_details"] = contact_details
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if registration_code is not UNSET:
            field_dict["registration_code"] = registration_code
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if vat_code is not UNSET:
            field_dict["vat_code"] = vat_code
        if postal is not UNSET:
            field_dict["postal"] = postal
        if address is not UNSET:
            field_dict["address"] = address
        if bank_name is not UNSET:
            field_dict["bank_name"] = bank_name
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if bank_account is not UNSET:
            field_dict["bank_account"] = bank_account
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        backend_id = (
            self.backend_id
            if isinstance(self.backend_id, Unset)
            else (None, str(self.backend_id).encode(), "text/plain")
        )

        image: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, File):
            image = self.image.to_tuple()
        else:
            image = (None, str(self.image).encode(), "text/plain")

        native_name = (
            self.native_name
            if isinstance(self.native_name, Unset)
            else (None, str(self.native_name).encode(), "text/plain")
        )

        abbreviation = (
            self.abbreviation
            if isinstance(self.abbreviation, Unset)
            else (None, str(self.abbreviation).encode(), "text/plain")
        )

        contact_details = (
            self.contact_details
            if isinstance(self.contact_details, Unset)
            else (None, str(self.contact_details).encode(), "text/plain")
        )

        email = self.email if isinstance(self.email, Unset) else (None, str(self.email).encode(), "text/plain")

        phone_number = (
            self.phone_number
            if isinstance(self.phone_number, Unset)
            else (None, str(self.phone_number).encode(), "text/plain")
        )

        registration_code = (
            self.registration_code
            if isinstance(self.registration_code, Unset)
            else (None, str(self.registration_code).encode(), "text/plain")
        )

        homepage = (
            self.homepage if isinstance(self.homepage, Unset) else (None, str(self.homepage).encode(), "text/plain")
        )

        vat_code = (
            self.vat_code if isinstance(self.vat_code, Unset) else (None, str(self.vat_code).encode(), "text/plain")
        )

        postal = self.postal if isinstance(self.postal, Unset) else (None, str(self.postal).encode(), "text/plain")

        address = self.address if isinstance(self.address, Unset) else (None, str(self.address).encode(), "text/plain")

        bank_name = (
            self.bank_name if isinstance(self.bank_name, Unset) else (None, str(self.bank_name).encode(), "text/plain")
        )

        latitude: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.latitude, Unset):
            latitude = UNSET
        elif isinstance(self.latitude, float):
            latitude = (None, str(self.latitude).encode(), "text/plain")
        else:
            latitude = (None, str(self.latitude).encode(), "text/plain")

        longitude: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.longitude, Unset):
            longitude = UNSET
        elif isinstance(self.longitude, float):
            longitude = (None, str(self.longitude).encode(), "text/plain")
        else:
            longitude = (None, str(self.longitude).encode(), "text/plain")

        bank_account = (
            self.bank_account
            if isinstance(self.bank_account, Unset)
            else (None, str(self.bank_account).encode(), "text/plain")
        )

        country: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, CountryEnum):
            country = (None, str(self.country.value).encode(), "text/plain")
        else:
            country = (None, str(self.country.value).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
            }
        )
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if image is not UNSET:
            field_dict["image"] = image
        if native_name is not UNSET:
            field_dict["native_name"] = native_name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if contact_details is not UNSET:
            field_dict["contact_details"] = contact_details
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if registration_code is not UNSET:
            field_dict["registration_code"] = registration_code
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if vat_code is not UNSET:
            field_dict["vat_code"] = vat_code
        if postal is not UNSET:
            field_dict["postal"] = postal
        if address is not UNSET:
            field_dict["address"] = address
        if bank_name is not UNSET:
            field_dict["bank_name"] = bank_name
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if bank_account is not UNSET:
            field_dict["bank_account"] = bank_account
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        backend_id = d.pop("backend_id", UNSET)

        def _parse_image(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                image_type_0 = File(payload=BytesIO(data))

                return image_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        image = _parse_image(d.pop("image", UNSET))

        native_name = d.pop("native_name", UNSET)

        abbreviation = d.pop("abbreviation", UNSET)

        contact_details = d.pop("contact_details", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        registration_code = d.pop("registration_code", UNSET)

        homepage = d.pop("homepage", UNSET)

        vat_code = d.pop("vat_code", UNSET)

        postal = d.pop("postal", UNSET)

        address = d.pop("address", UNSET)

        bank_name = d.pop("bank_name", UNSET)

        def _parse_latitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        bank_account = d.pop("bank_account", UNSET)

        def _parse_country(data: object) -> Union[BlankEnum, CountryEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_type_0 = CountryEnum(data)

                return country_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            country_type_1 = BlankEnum(data)

            return country_type_1

        country = _parse_country(d.pop("country", UNSET))

        customer_request = cls(
            name=name,
            backend_id=backend_id,
            image=image,
            native_name=native_name,
            abbreviation=abbreviation,
            contact_details=contact_details,
            email=email,
            phone_number=phone_number,
            registration_code=registration_code,
            homepage=homepage,
            vat_code=vat_code,
            postal=postal,
            address=address,
            bank_name=bank_name,
            latitude=latitude,
            longitude=longitude,
            bank_account=bank_account,
            country=country,
        )

        customer_request.additional_properties = d
        return customer_request

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
