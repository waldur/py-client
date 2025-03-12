from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationRequest")


@_attrs_define
class InvitationRequest:
    """
    Attributes:
        role (UUID):
        scope (str):
        email (str): Invitation link will be sent to this email. Note that user can accept invitation with different
            email.
        full_name (Union[Unset, str]):
        native_name (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        organization (Union[Unset, str]):
        job_title (Union[Unset, str]):
        civil_number (Union[Unset, str]): Civil number of invited user. If civil number is not defined any user can
            accept invitation.
        extra_invitation_text (Union[Unset, str]):
    """

    role: UUID
    scope: str
    email: str
    full_name: Union[Unset, str] = UNSET
    native_name: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    organization: Union[Unset, str] = UNSET
    job_title: Union[Unset, str] = UNSET
    civil_number: Union[Unset, str] = UNSET
    extra_invitation_text: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = str(self.role)

        scope = self.scope

        email = self.email

        full_name = self.full_name

        native_name = self.native_name

        phone_number = self.phone_number

        organization = self.organization

        job_title = self.job_title

        civil_number = self.civil_number

        extra_invitation_text = self.extra_invitation_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "scope": scope,
                "email": email,
            }
        )
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if native_name is not UNSET:
            field_dict["native_name"] = native_name
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if organization is not UNSET:
            field_dict["organization"] = organization
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if civil_number is not UNSET:
            field_dict["civil_number"] = civil_number
        if extra_invitation_text is not UNSET:
            field_dict["extra_invitation_text"] = extra_invitation_text

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        role = str(self.role)

        scope = (None, str(self.scope).encode(), "text/plain")

        email = (None, str(self.email).encode(), "text/plain")

        full_name = (
            self.full_name if isinstance(self.full_name, Unset) else (None, str(self.full_name).encode(), "text/plain")
        )

        native_name = (
            self.native_name
            if isinstance(self.native_name, Unset)
            else (None, str(self.native_name).encode(), "text/plain")
        )

        phone_number = (
            self.phone_number
            if isinstance(self.phone_number, Unset)
            else (None, str(self.phone_number).encode(), "text/plain")
        )

        organization = (
            self.organization
            if isinstance(self.organization, Unset)
            else (None, str(self.organization).encode(), "text/plain")
        )

        job_title = (
            self.job_title if isinstance(self.job_title, Unset) else (None, str(self.job_title).encode(), "text/plain")
        )

        civil_number = (
            self.civil_number
            if isinstance(self.civil_number, Unset)
            else (None, str(self.civil_number).encode(), "text/plain")
        )

        extra_invitation_text = (
            self.extra_invitation_text
            if isinstance(self.extra_invitation_text, Unset)
            else (None, str(self.extra_invitation_text).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "role": role,
                "scope": scope,
                "email": email,
            }
        )
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if native_name is not UNSET:
            field_dict["native_name"] = native_name
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if organization is not UNSET:
            field_dict["organization"] = organization
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if civil_number is not UNSET:
            field_dict["civil_number"] = civil_number
        if extra_invitation_text is not UNSET:
            field_dict["extra_invitation_text"] = extra_invitation_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        role = UUID(d.pop("role"))

        scope = d.pop("scope")

        email = d.pop("email")

        full_name = d.pop("full_name", UNSET)

        native_name = d.pop("native_name", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        organization = d.pop("organization", UNSET)

        job_title = d.pop("job_title", UNSET)

        civil_number = d.pop("civil_number", UNSET)

        extra_invitation_text = d.pop("extra_invitation_text", UNSET)

        invitation_request = cls(
            role=role,
            scope=scope,
            email=email,
            full_name=full_name,
            native_name=native_name,
            phone_number=phone_number,
            organization=organization,
            job_title=job_title,
            civil_number=civil_number,
            extra_invitation_text=extra_invitation_text,
        )

        invitation_request.additional_properties = d
        return invitation_request

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
