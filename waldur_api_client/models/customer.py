import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.country_enum import CountryEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_price_estimate import NestedPriceEstimate
    from ..models.organization_group import OrganizationGroup
    from ..models.payment_profile import PaymentProfile
    from ..models.permission_project import PermissionProject


T = TypeVar("T", bound="Customer")


@_attrs_define
class Customer:
    """
    Attributes:
        url (str):
        uuid (UUID):
        created (datetime.datetime):
        organization_groups (list['OrganizationGroup']):
        display_name (str):
        projects (list['PermissionProject']):
        blocked (bool):
        archived (bool):
        default_tax_percent (str):
        accounting_start_date (datetime.datetime):
        projects_count (int):
        users_count (int):
        sponsor_number (Union[None, int]): External ID of the sponsor covering the costs
        country_name (str):
        name (str):
        slug (str):
        agreement_number (str):
        access_subnets (str): Enter a comma separated list of IPv4 or IPv6 CIDR addresses from where connection to self-
            service is allowed.
        domain (str):
        payment_profiles (list['PaymentProfile']):
        customer_credit (Union[None, float]):
        is_service_provider (bool):
        service_provider (str):
        service_provider_uuid (UUID):
        call_managing_organization_uuid (str):
        billing_price_estimate (NestedPriceEstimate):
        backend_id (Union[Unset, str]): Organization identifier in another application.
        image (Union[None, Unset, str]):
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

    url: str
    uuid: UUID
    created: datetime.datetime
    organization_groups: list["OrganizationGroup"]
    display_name: str
    projects: list["PermissionProject"]
    blocked: bool
    archived: bool
    default_tax_percent: str
    accounting_start_date: datetime.datetime
    projects_count: int
    users_count: int
    sponsor_number: Union[None, int]
    country_name: str
    name: str
    slug: str
    agreement_number: str
    access_subnets: str
    domain: str
    payment_profiles: list["PaymentProfile"]
    customer_credit: Union[None, float]
    is_service_provider: bool
    service_provider: str
    service_provider_uuid: UUID
    call_managing_organization_uuid: str
    billing_price_estimate: "NestedPriceEstimate"
    backend_id: Union[Unset, str] = UNSET
    image: Union[None, Unset, str] = UNSET
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
        url = self.url

        uuid = str(self.uuid)

        created = self.created.isoformat()

        organization_groups = []
        for organization_groups_item_data in self.organization_groups:
            organization_groups_item = organization_groups_item_data.to_dict()
            organization_groups.append(organization_groups_item)

        display_name = self.display_name

        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        blocked = self.blocked

        archived = self.archived

        default_tax_percent = self.default_tax_percent

        accounting_start_date = self.accounting_start_date.isoformat()

        projects_count = self.projects_count

        users_count = self.users_count

        sponsor_number: Union[None, int]
        sponsor_number = self.sponsor_number

        country_name = self.country_name

        name = self.name

        slug = self.slug

        agreement_number = self.agreement_number

        access_subnets = self.access_subnets

        domain = self.domain

        payment_profiles = []
        for payment_profiles_item_data in self.payment_profiles:
            payment_profiles_item = payment_profiles_item_data.to_dict()
            payment_profiles.append(payment_profiles_item)

        customer_credit: Union[None, float]
        customer_credit = self.customer_credit

        is_service_provider = self.is_service_provider

        service_provider = self.service_provider

        service_provider_uuid = str(self.service_provider_uuid)

        call_managing_organization_uuid = self.call_managing_organization_uuid

        billing_price_estimate = self.billing_price_estimate.to_dict()

        backend_id = self.backend_id

        image: Union[None, Unset, str]
        if isinstance(self.image, Unset):
            image = UNSET
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
                "url": url,
                "uuid": uuid,
                "created": created,
                "organization_groups": organization_groups,
                "display_name": display_name,
                "projects": projects,
                "blocked": blocked,
                "archived": archived,
                "default_tax_percent": default_tax_percent,
                "accounting_start_date": accounting_start_date,
                "projects_count": projects_count,
                "users_count": users_count,
                "sponsor_number": sponsor_number,
                "country_name": country_name,
                "name": name,
                "slug": slug,
                "agreement_number": agreement_number,
                "access_subnets": access_subnets,
                "domain": domain,
                "payment_profiles": payment_profiles,
                "customer_credit": customer_credit,
                "is_service_provider": is_service_provider,
                "service_provider": service_provider,
                "service_provider_uuid": service_provider_uuid,
                "call_managing_organization_uuid": call_managing_organization_uuid,
                "billing_price_estimate": billing_price_estimate,
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_price_estimate import NestedPriceEstimate
        from ..models.organization_group import OrganizationGroup
        from ..models.payment_profile import PaymentProfile
        from ..models.permission_project import PermissionProject

        d = dict(src_dict)
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        organization_groups = []
        _organization_groups = d.pop("organization_groups")
        for organization_groups_item_data in _organization_groups:
            organization_groups_item = OrganizationGroup.from_dict(organization_groups_item_data)

            organization_groups.append(organization_groups_item)

        display_name = d.pop("display_name")

        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = PermissionProject.from_dict(projects_item_data)

            projects.append(projects_item)

        blocked = d.pop("blocked")

        archived = d.pop("archived")

        default_tax_percent = d.pop("default_tax_percent")

        accounting_start_date = isoparse(d.pop("accounting_start_date"))

        projects_count = d.pop("projects_count")

        users_count = d.pop("users_count")

        def _parse_sponsor_number(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        sponsor_number = _parse_sponsor_number(d.pop("sponsor_number"))

        country_name = d.pop("country_name")

        name = d.pop("name")

        slug = d.pop("slug")

        agreement_number = d.pop("agreement_number")

        access_subnets = d.pop("access_subnets")

        domain = d.pop("domain")

        payment_profiles = []
        _payment_profiles = d.pop("payment_profiles")
        for payment_profiles_item_data in _payment_profiles:
            payment_profiles_item = PaymentProfile.from_dict(payment_profiles_item_data)

            payment_profiles.append(payment_profiles_item)

        def _parse_customer_credit(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        customer_credit = _parse_customer_credit(d.pop("customer_credit"))

        is_service_provider = d.pop("is_service_provider")

        service_provider = d.pop("service_provider")

        service_provider_uuid = UUID(d.pop("service_provider_uuid"))

        call_managing_organization_uuid = d.pop("call_managing_organization_uuid")

        billing_price_estimate = NestedPriceEstimate.from_dict(d.pop("billing_price_estimate"))

        backend_id = d.pop("backend_id", UNSET)

        def _parse_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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

        customer = cls(
            url=url,
            uuid=uuid,
            created=created,
            organization_groups=organization_groups,
            display_name=display_name,
            projects=projects,
            blocked=blocked,
            archived=archived,
            default_tax_percent=default_tax_percent,
            accounting_start_date=accounting_start_date,
            projects_count=projects_count,
            users_count=users_count,
            sponsor_number=sponsor_number,
            country_name=country_name,
            name=name,
            slug=slug,
            agreement_number=agreement_number,
            access_subnets=access_subnets,
            domain=domain,
            payment_profiles=payment_profiles,
            customer_credit=customer_credit,
            is_service_provider=is_service_provider,
            service_provider=service_provider,
            service_provider_uuid=service_provider_uuid,
            call_managing_organization_uuid=call_managing_organization_uuid,
            billing_price_estimate=billing_price_estimate,
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

        customer.additional_properties = d
        return customer

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
