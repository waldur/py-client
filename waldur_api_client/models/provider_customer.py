from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_price_estimate import NestedPriceEstimate
    from ..models.payment_profile import PaymentProfile
    from ..models.provider_project import ProviderProject
    from ..models.provider_user import ProviderUser


T = TypeVar("T", bound="ProviderCustomer")


@_attrs_define
class ProviderCustomer:
    """
    Attributes:
        uuid (UUID):
        name (str):
        slug (str):
        payment_profiles (list['PaymentProfile']):
        billing_price_estimate (NestedPriceEstimate):
        projects_count (int):
        users_count (int):
        projects (list['ProviderProject']):
        users (list['ProviderUser']):
        abbreviation (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        email (Union[Unset, str]):
    """

    uuid: UUID
    name: str
    slug: str
    payment_profiles: list["PaymentProfile"]
    billing_price_estimate: "NestedPriceEstimate"
    projects_count: int
    users_count: int
    projects: list["ProviderProject"]
    users: list["ProviderUser"]
    abbreviation: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        slug = self.slug

        payment_profiles = []
        for payment_profiles_item_data in self.payment_profiles:
            payment_profiles_item = payment_profiles_item_data.to_dict()
            payment_profiles.append(payment_profiles_item)

        billing_price_estimate = self.billing_price_estimate.to_dict()

        projects_count = self.projects_count

        users_count = self.users_count

        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

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
                "payment_profiles": payment_profiles,
                "billing_price_estimate": billing_price_estimate,
                "projects_count": projects_count,
                "users_count": users_count,
                "projects": projects,
                "users": users,
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
        from ..models.nested_price_estimate import NestedPriceEstimate
        from ..models.payment_profile import PaymentProfile
        from ..models.provider_project import ProviderProject
        from ..models.provider_user import ProviderUser

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        slug = d.pop("slug")

        payment_profiles = []
        _payment_profiles = d.pop("payment_profiles")
        for payment_profiles_item_data in _payment_profiles:
            payment_profiles_item = PaymentProfile.from_dict(payment_profiles_item_data)

            payment_profiles.append(payment_profiles_item)

        billing_price_estimate = NestedPriceEstimate.from_dict(d.pop("billing_price_estimate"))

        projects_count = d.pop("projects_count")

        users_count = d.pop("users_count")

        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = ProviderProject.from_dict(projects_item_data)

            projects.append(projects_item)

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = ProviderUser.from_dict(users_item_data)

            users.append(users_item)

        abbreviation = d.pop("abbreviation", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        email = d.pop("email", UNSET)

        provider_customer = cls(
            uuid=uuid,
            name=name,
            slug=slug,
            payment_profiles=payment_profiles,
            billing_price_estimate=billing_price_estimate,
            projects_count=projects_count,
            users_count=users_count,
            projects=projects,
            users=users,
            abbreviation=abbreviation,
            phone_number=phone_number,
            email=email,
        )

        provider_customer.additional_properties = d
        return provider_customer

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
