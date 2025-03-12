import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.permission import Permission


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        url (str):
        uuid (UUID):
        username (str): Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters
        slug (str):
        full_name (str):
        email (str):
        civil_number (Union[None, str]):
        token (str):
        registration_method (str): Indicates what registration method was used.
        date_joined (datetime.datetime):
        agreement_date (Union[None, datetime.datetime]): Indicates when the user has agreed with the policy.
        permissions (list['Permission']):
        requested_email (Union[None, str]):
        affiliations (Any): Person's affiliation within organization such as student, faculty, staff.
        identity_provider_name (str):
        identity_provider_label (str):
        identity_provider_management_url (str):
        identity_provider_fields (list[str]):
        identity_source (str): Indicates what identity provider was used.
        has_active_session (bool):
        native_name (Union[Unset, str]):
        job_title (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        organization (Union[Unset, str]):
        description (Union[Unset, str]):
        is_staff (Union[Unset, bool]): Designates whether the user can log into this admin site.
        is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
            of deleting accounts.
        is_support (Union[Unset, bool]): Designates whether the user is a global support user.
        token_lifetime (Union[None, Unset, int]): Token lifetime in seconds.
        preferred_language (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        image (Union[None, Unset, str]):
    """

    url: str
    uuid: UUID
    username: str
    slug: str
    full_name: str
    email: str
    civil_number: Union[None, str]
    token: str
    registration_method: str
    date_joined: datetime.datetime
    agreement_date: Union[None, datetime.datetime]
    permissions: list["Permission"]
    requested_email: Union[None, str]
    affiliations: Any
    identity_provider_name: str
    identity_provider_label: str
    identity_provider_management_url: str
    identity_provider_fields: list[str]
    identity_source: str
    has_active_session: bool
    native_name: Union[Unset, str] = UNSET
    job_title: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    organization: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_staff: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_support: Union[Unset, bool] = UNSET
    token_lifetime: Union[None, Unset, int] = UNSET
    preferred_language: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    image: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        username = self.username

        slug = self.slug

        full_name = self.full_name

        email = self.email

        civil_number: Union[None, str]
        civil_number = self.civil_number

        token = self.token

        registration_method = self.registration_method

        date_joined = self.date_joined.isoformat()

        agreement_date: Union[None, str]
        if isinstance(self.agreement_date, datetime.datetime):
            agreement_date = self.agreement_date.isoformat()
        else:
            agreement_date = self.agreement_date

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.to_dict()
            permissions.append(permissions_item)

        requested_email: Union[None, str]
        requested_email = self.requested_email

        affiliations = self.affiliations

        identity_provider_name = self.identity_provider_name

        identity_provider_label = self.identity_provider_label

        identity_provider_management_url = self.identity_provider_management_url

        identity_provider_fields = self.identity_provider_fields

        identity_source = self.identity_source

        has_active_session = self.has_active_session

        native_name = self.native_name

        job_title = self.job_title

        phone_number = self.phone_number

        organization = self.organization

        description = self.description

        is_staff = self.is_staff

        is_active = self.is_active

        is_support = self.is_support

        token_lifetime: Union[None, Unset, int]
        if isinstance(self.token_lifetime, Unset):
            token_lifetime = UNSET
        else:
            token_lifetime = self.token_lifetime

        preferred_language = self.preferred_language

        first_name = self.first_name

        last_name = self.last_name

        image: Union[None, Unset, str]
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "username": username,
                "slug": slug,
                "full_name": full_name,
                "email": email,
                "civil_number": civil_number,
                "token": token,
                "registration_method": registration_method,
                "date_joined": date_joined,
                "agreement_date": agreement_date,
                "permissions": permissions,
                "requested_email": requested_email,
                "affiliations": affiliations,
                "identity_provider_name": identity_provider_name,
                "identity_provider_label": identity_provider_label,
                "identity_provider_management_url": identity_provider_management_url,
                "identity_provider_fields": identity_provider_fields,
                "identity_source": identity_source,
                "has_active_session": has_active_session,
            }
        )
        if native_name is not UNSET:
            field_dict["native_name"] = native_name
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if organization is not UNSET:
            field_dict["organization"] = organization
        if description is not UNSET:
            field_dict["description"] = description
        if is_staff is not UNSET:
            field_dict["is_staff"] = is_staff
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_support is not UNSET:
            field_dict["is_support"] = is_support
        if token_lifetime is not UNSET:
            field_dict["token_lifetime"] = token_lifetime
        if preferred_language is not UNSET:
            field_dict["preferred_language"] = preferred_language
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.permission import Permission

        d = src_dict.copy()
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        username = d.pop("username")

        slug = d.pop("slug")

        full_name = d.pop("full_name")

        email = d.pop("email")

        def _parse_civil_number(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        civil_number = _parse_civil_number(d.pop("civil_number"))

        token = d.pop("token")

        registration_method = d.pop("registration_method")

        date_joined = isoparse(d.pop("date_joined"))

        def _parse_agreement_date(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agreement_date_type_0 = isoparse(data)

                return agreement_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        agreement_date = _parse_agreement_date(d.pop("agreement_date"))

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = Permission.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        def _parse_requested_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        requested_email = _parse_requested_email(d.pop("requested_email"))

        affiliations = d.pop("affiliations")

        identity_provider_name = d.pop("identity_provider_name")

        identity_provider_label = d.pop("identity_provider_label")

        identity_provider_management_url = d.pop("identity_provider_management_url")

        identity_provider_fields = cast(list[str], d.pop("identity_provider_fields"))

        identity_source = d.pop("identity_source")

        has_active_session = d.pop("has_active_session")

        native_name = d.pop("native_name", UNSET)

        job_title = d.pop("job_title", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        organization = d.pop("organization", UNSET)

        description = d.pop("description", UNSET)

        is_staff = d.pop("is_staff", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_support = d.pop("is_support", UNSET)

        def _parse_token_lifetime(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        token_lifetime = _parse_token_lifetime(d.pop("token_lifetime", UNSET))

        preferred_language = d.pop("preferred_language", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        def _parse_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image = _parse_image(d.pop("image", UNSET))

        user = cls(
            url=url,
            uuid=uuid,
            username=username,
            slug=slug,
            full_name=full_name,
            email=email,
            civil_number=civil_number,
            token=token,
            registration_method=registration_method,
            date_joined=date_joined,
            agreement_date=agreement_date,
            permissions=permissions,
            requested_email=requested_email,
            affiliations=affiliations,
            identity_provider_name=identity_provider_name,
            identity_provider_label=identity_provider_label,
            identity_provider_management_url=identity_provider_management_url,
            identity_provider_fields=identity_provider_fields,
            identity_source=identity_source,
            has_active_session=has_active_session,
            native_name=native_name,
            job_title=job_title,
            phone_number=phone_number,
            organization=organization,
            description=description,
            is_staff=is_staff,
            is_active=is_active,
            is_support=is_support,
            token_lifetime=token_lifetime,
            preferred_language=preferred_language,
            first_name=first_name,
            last_name=last_name,
            image=image,
        )

        user.additional_properties = d
        return user

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
