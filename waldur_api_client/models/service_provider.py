import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_group import OrganizationGroup


T = TypeVar("T", bound="ServiceProvider")


@_attrs_define
class ServiceProvider:
    """
    Attributes:
        url (str):
        uuid (UUID):
        created (datetime.datetime):
        customer (str):
        customer_name (str):
        customer_uuid (UUID):
        customer_image (str):
        customer_abbreviation (str):
        customer_slug (str):
        customer_native_name (str):
        customer_country (str):
        organization_groups (list['OrganizationGroup']):
        offering_count (int):
        description (Union[Unset, str]):
        image (Union[None, Unset, str]):
    """

    url: str
    uuid: UUID
    created: datetime.datetime
    customer: str
    customer_name: str
    customer_uuid: UUID
    customer_image: str
    customer_abbreviation: str
    customer_slug: str
    customer_native_name: str
    customer_country: str
    organization_groups: list["OrganizationGroup"]
    offering_count: int
    description: Union[Unset, str] = UNSET
    image: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        created = self.created.isoformat()

        customer = self.customer

        customer_name = self.customer_name

        customer_uuid = str(self.customer_uuid)

        customer_image = self.customer_image

        customer_abbreviation = self.customer_abbreviation

        customer_slug = self.customer_slug

        customer_native_name = self.customer_native_name

        customer_country = self.customer_country

        organization_groups = []
        for organization_groups_item_data in self.organization_groups:
            organization_groups_item = organization_groups_item_data.to_dict()
            organization_groups.append(organization_groups_item)

        offering_count = self.offering_count

        description = self.description

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
                "created": created,
                "customer": customer,
                "customer_name": customer_name,
                "customer_uuid": customer_uuid,
                "customer_image": customer_image,
                "customer_abbreviation": customer_abbreviation,
                "customer_slug": customer_slug,
                "customer_native_name": customer_native_name,
                "customer_country": customer_country,
                "organization_groups": organization_groups,
                "offering_count": offering_count,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_group import OrganizationGroup

        d = dict(src_dict)
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        customer = d.pop("customer")

        customer_name = d.pop("customer_name")

        customer_uuid = UUID(d.pop("customer_uuid"))

        customer_image = d.pop("customer_image")

        customer_abbreviation = d.pop("customer_abbreviation")

        customer_slug = d.pop("customer_slug")

        customer_native_name = d.pop("customer_native_name")

        customer_country = d.pop("customer_country")

        organization_groups = []
        _organization_groups = d.pop("organization_groups")
        for organization_groups_item_data in _organization_groups:
            organization_groups_item = OrganizationGroup.from_dict(organization_groups_item_data)

            organization_groups.append(organization_groups_item)

        offering_count = d.pop("offering_count")

        description = d.pop("description", UNSET)

        def _parse_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image = _parse_image(d.pop("image", UNSET))

        service_provider = cls(
            url=url,
            uuid=uuid,
            created=created,
            customer=customer,
            customer_name=customer_name,
            customer_uuid=customer_uuid,
            customer_image=customer_image,
            customer_abbreviation=customer_abbreviation,
            customer_slug=customer_slug,
            customer_native_name=customer_native_name,
            customer_country=customer_country,
            organization_groups=organization_groups,
            offering_count=offering_count,
            description=description,
            image=image,
        )

        service_provider.additional_properties = d
        return service_provider

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
