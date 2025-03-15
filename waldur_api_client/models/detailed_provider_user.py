from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DetailedProviderUser")


@_attrs_define
class DetailedProviderUser:
    """
    Attributes:
        uuid (UUID):
        username (str): Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters
        full_name (str):
        projects_count (int):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        organization (Union[Unset, str]):
        email (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        registration_method (Union[Unset, str]): Indicates what registration method was used.
        affiliations (Union[Unset, Any]): Person's affiliation within organization such as student, faculty, staff.
        is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
            of deleting accounts.
    """

    uuid: UUID
    username: str
    full_name: str
    projects_count: int
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    organization: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    registration_method: Union[Unset, str] = UNSET
    affiliations: Union[Unset, Any] = UNSET
    is_active: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        username = self.username

        full_name = self.full_name

        projects_count = self.projects_count

        first_name = self.first_name

        last_name = self.last_name

        organization = self.organization

        email = self.email

        phone_number = self.phone_number

        registration_method = self.registration_method

        affiliations = self.affiliations

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "username": username,
                "full_name": full_name,
                "projects_count": projects_count,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if registration_method is not UNSET:
            field_dict["registration_method"] = registration_method
        if affiliations is not UNSET:
            field_dict["affiliations"] = affiliations
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        username = d.pop("username")

        full_name = d.pop("full_name")

        projects_count = d.pop("projects_count")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        organization = d.pop("organization", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        registration_method = d.pop("registration_method", UNSET)

        affiliations = d.pop("affiliations", UNSET)

        is_active = d.pop("is_active", UNSET)

        detailed_provider_user = cls(
            uuid=uuid,
            username=username,
            full_name=full_name,
            projects_count=projects_count,
            first_name=first_name,
            last_name=last_name,
            organization=organization,
            email=email,
            phone_number=phone_number,
            registration_method=registration_method,
            affiliations=affiliations,
            is_active=is_active,
        )

        detailed_provider_user.additional_properties = d
        return detailed_provider_user

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
