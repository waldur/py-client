from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OfferingTeamPerson")


@_attrs_define
class OfferingTeamPerson:
    """
    Attributes:
        uuid (UUID):
        full_name (str):
        email (str):
        role_name (str):
        role_description (str):
    """

    uuid: UUID
    full_name: str
    email: str
    role_name: str
    role_description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        full_name = self.full_name

        email = self.email

        role_name = self.role_name

        role_description = self.role_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "full_name": full_name,
                "email": email,
                "role_name": role_name,
                "role_description": role_description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        full_name = d.pop("full_name")

        email = d.pop("email")

        role_name = d.pop("role_name")

        role_description = d.pop("role_description")

        offering_team_person = cls(
            uuid=uuid,
            full_name=full_name,
            email=email,
            role_name=role_name,
            role_description=role_description,
        )

        offering_team_person.additional_properties = d
        return offering_team_person

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
