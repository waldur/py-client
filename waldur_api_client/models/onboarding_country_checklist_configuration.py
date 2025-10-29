import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnboardingCountryChecklistConfiguration")


@_attrs_define
class OnboardingCountryChecklistConfiguration:
    """
    Attributes:
        uuid (UUID):
        country (str): ISO country code (e.g., 'EE' for Estonia)
        checklist (int): Checklist to use for this country's onboarding
        checklist_name (str):
        checklist_uuid (UUID):
        created (datetime.datetime):
        modified (datetime.datetime):
        is_active (Union[Unset, bool]): Whether this country configuration is active
    """

    uuid: UUID
    country: str
    checklist: int
    checklist_name: str
    checklist_uuid: UUID
    created: datetime.datetime
    modified: datetime.datetime
    is_active: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        country = self.country

        checklist = self.checklist

        checklist_name = self.checklist_name

        checklist_uuid = str(self.checklist_uuid)

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "country": country,
                "checklist": checklist,
                "checklist_name": checklist_name,
                "checklist_uuid": checklist_uuid,
                "created": created,
                "modified": modified,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        country = d.pop("country")

        checklist = d.pop("checklist")

        checklist_name = d.pop("checklist_name")

        checklist_uuid = UUID(d.pop("checklist_uuid"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        is_active = d.pop("is_active", UNSET)

        onboarding_country_checklist_configuration = cls(
            uuid=uuid,
            country=country,
            checklist=checklist,
            checklist_name=checklist_name,
            checklist_uuid=checklist_uuid,
            created=created,
            modified=modified,
            is_active=is_active,
        )

        onboarding_country_checklist_configuration.additional_properties = d
        return onboarding_country_checklist_configuration

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
