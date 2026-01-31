import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArrowVendorOfferingMappingCreate")


@_attrs_define
class ArrowVendorOfferingMappingCreate:
    """
    Attributes:
        uuid (UUID):
        url (str):
        settings (UUID):
        settings_uuid (UUID):
        arrow_vendor_name (str): Arrow vendor name (e.g., 'Microsoft', 'Amazon Web Services')
        offering (UUID):
        offering_uuid (UUID):
        offering_name (str):
        offering_type (str):
        created (datetime.datetime):
        modified (datetime.datetime):
        is_active (Union[Unset, bool]): Whether this mapping is active
    """

    uuid: UUID
    url: str
    settings: UUID
    settings_uuid: UUID
    arrow_vendor_name: str
    offering: UUID
    offering_uuid: UUID
    offering_name: str
    offering_type: str
    created: datetime.datetime
    modified: datetime.datetime
    is_active: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        url = self.url

        settings = str(self.settings)

        settings_uuid = str(self.settings_uuid)

        arrow_vendor_name = self.arrow_vendor_name

        offering = str(self.offering)

        offering_uuid = str(self.offering_uuid)

        offering_name = self.offering_name

        offering_type = self.offering_type

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "url": url,
                "settings": settings,
                "settings_uuid": settings_uuid,
                "arrow_vendor_name": arrow_vendor_name,
                "offering": offering,
                "offering_uuid": offering_uuid,
                "offering_name": offering_name,
                "offering_type": offering_type,
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

        url = d.pop("url")

        settings = UUID(d.pop("settings"))

        settings_uuid = UUID(d.pop("settings_uuid"))

        arrow_vendor_name = d.pop("arrow_vendor_name")

        offering = UUID(d.pop("offering"))

        offering_uuid = UUID(d.pop("offering_uuid"))

        offering_name = d.pop("offering_name")

        offering_type = d.pop("offering_type")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        is_active = d.pop("is_active", UNSET)

        arrow_vendor_offering_mapping_create = cls(
            uuid=uuid,
            url=url,
            settings=settings,
            settings_uuid=settings_uuid,
            arrow_vendor_name=arrow_vendor_name,
            offering=offering,
            offering_uuid=offering_uuid,
            offering_name=offering_name,
            offering_type=offering_type,
            created=created,
            modified=modified,
            is_active=is_active,
        )

        arrow_vendor_offering_mapping_create.additional_properties = d
        return arrow_vendor_offering_mapping_create

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
