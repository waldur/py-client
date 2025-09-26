import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum
from ..models.country_enum import CountryEnum
from ..types import UNSET, File, Unset

if TYPE_CHECKING:
    from ..models.base_provider_plan_request import BaseProviderPlanRequest
    from ..models.offering_component_request import OfferingComponentRequest
    from ..models.offering_create_request_multipart_limits import OfferingCreateRequestMultipartLimits
    from ..models.offering_options_request import OfferingOptionsRequest


T = TypeVar("T", bound="OfferingCreateRequestMultipart")


@_attrs_define
class OfferingCreateRequestMultipart:
    """
    Attributes:
        name (str):
        category (str):
        type_ (str):
        slug (Union[Unset, str]):
        description (Union[Unset, str]):
        full_description (Union[Unset, str]):
        privacy_policy_link (Union[Unset, str]):
        access_url (Union[Unset, str]): Publicly accessible offering access URL
        customer (Union[None, Unset, str]):
        attributes (Union[Unset, Any]):
        options (Union[Unset, OfferingOptionsRequest]):
        resource_options (Union[Unset, OfferingOptionsRequest]):
        components (Union[Unset, list['OfferingComponentRequest']]):
        vendor_details (Union[Unset, str]):
        getting_started (Union[Unset, str]):
        integration_guide (Union[Unset, str]):
        thumbnail (Union[File, None, Unset]):
        plans (Union[Unset, list['BaseProviderPlanRequest']]):
        shared (Union[Unset, bool]): Accessible to all customers.
        billable (Union[Unset, bool]): Purchase and usage is invoiced.
        datacite_doi (Union[Unset, str]):
        latitude (Union[None, Unset, float]):
        longitude (Union[None, Unset, float]):
        country (Union[BlankEnum, CountryEnum, Unset]):
        backend_id (Union[Unset, str]):
        image (Union[File, None, Unset]):
        backend_metadata (Union[Unset, Any]):
        compliance_checklist (Union[None, Unset, str]): Checklist that offering users must complete for compliance
        limits (Union[Unset, OfferingCreateRequestMultipartLimits]):
    """

    name: str
    category: str
    type_: str
    slug: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    full_description: Union[Unset, str] = UNSET
    privacy_policy_link: Union[Unset, str] = UNSET
    access_url: Union[Unset, str] = UNSET
    customer: Union[None, Unset, str] = UNSET
    attributes: Union[Unset, Any] = UNSET
    options: Union[Unset, "OfferingOptionsRequest"] = UNSET
    resource_options: Union[Unset, "OfferingOptionsRequest"] = UNSET
    components: Union[Unset, list["OfferingComponentRequest"]] = UNSET
    vendor_details: Union[Unset, str] = UNSET
    getting_started: Union[Unset, str] = UNSET
    integration_guide: Union[Unset, str] = UNSET
    thumbnail: Union[File, None, Unset] = UNSET
    plans: Union[Unset, list["BaseProviderPlanRequest"]] = UNSET
    shared: Union[Unset, bool] = UNSET
    billable: Union[Unset, bool] = UNSET
    datacite_doi: Union[Unset, str] = UNSET
    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    country: Union[BlankEnum, CountryEnum, Unset] = UNSET
    backend_id: Union[Unset, str] = UNSET
    image: Union[File, None, Unset] = UNSET
    backend_metadata: Union[Unset, Any] = UNSET
    compliance_checklist: Union[None, Unset, str] = UNSET
    limits: Union[Unset, "OfferingCreateRequestMultipartLimits"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        category = self.category

        type_ = self.type_

        slug = self.slug

        description = self.description

        full_description = self.full_description

        privacy_policy_link = self.privacy_policy_link

        access_url = self.access_url

        customer: Union[None, Unset, str]
        if isinstance(self.customer, Unset):
            customer = UNSET
        else:
            customer = self.customer

        attributes = self.attributes

        options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        resource_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resource_options, Unset):
            resource_options = self.resource_options.to_dict()

        components: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)

        vendor_details = self.vendor_details

        getting_started = self.getting_started

        integration_guide = self.integration_guide

        thumbnail: Union[None, Unset, types.FileTypes]
        if isinstance(self.thumbnail, Unset):
            thumbnail = UNSET
        elif isinstance(self.thumbnail, File):
            thumbnail = self.thumbnail.to_tuple()

        else:
            thumbnail = self.thumbnail

        plans: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plans, Unset):
            plans = []
            for plans_item_data in self.plans:
                plans_item = plans_item_data.to_dict()
                plans.append(plans_item)

        shared = self.shared

        billable = self.billable

        datacite_doi = self.datacite_doi

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

        country: Union[Unset, str]
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, CountryEnum):
            country = self.country.value
        else:
            country = self.country.value

        backend_id = self.backend_id

        image: Union[None, Unset, types.FileTypes]
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, File):
            image = self.image.to_tuple()

        else:
            image = self.image

        backend_metadata = self.backend_metadata

        compliance_checklist: Union[None, Unset, str]
        if isinstance(self.compliance_checklist, Unset):
            compliance_checklist = UNSET
        else:
            compliance_checklist = self.compliance_checklist

        limits: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "category": category,
                "type": type_,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if full_description is not UNSET:
            field_dict["full_description"] = full_description
        if privacy_policy_link is not UNSET:
            field_dict["privacy_policy_link"] = privacy_policy_link
        if access_url is not UNSET:
            field_dict["access_url"] = access_url
        if customer is not UNSET:
            field_dict["customer"] = customer
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if options is not UNSET:
            field_dict["options"] = options
        if resource_options is not UNSET:
            field_dict["resource_options"] = resource_options
        if components is not UNSET:
            field_dict["components"] = components
        if vendor_details is not UNSET:
            field_dict["vendor_details"] = vendor_details
        if getting_started is not UNSET:
            field_dict["getting_started"] = getting_started
        if integration_guide is not UNSET:
            field_dict["integration_guide"] = integration_guide
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if plans is not UNSET:
            field_dict["plans"] = plans
        if shared is not UNSET:
            field_dict["shared"] = shared
        if billable is not UNSET:
            field_dict["billable"] = billable
        if datacite_doi is not UNSET:
            field_dict["datacite_doi"] = datacite_doi
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if country is not UNSET:
            field_dict["country"] = country
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if image is not UNSET:
            field_dict["image"] = image
        if backend_metadata is not UNSET:
            field_dict["backend_metadata"] = backend_metadata
        if compliance_checklist is not UNSET:
            field_dict["compliance_checklist"] = compliance_checklist
        if limits is not UNSET:
            field_dict["limits"] = limits

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("category", (None, str(self.category).encode(), "text/plain")))

        files.append(("type", (None, str(self.type_).encode(), "text/plain")))

        if not isinstance(self.slug, Unset):
            files.append(("slug", (None, str(self.slug).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.full_description, Unset):
            files.append(("full_description", (None, str(self.full_description).encode(), "text/plain")))

        if not isinstance(self.privacy_policy_link, Unset):
            files.append(("privacy_policy_link", (None, str(self.privacy_policy_link).encode(), "text/plain")))

        if not isinstance(self.access_url, Unset):
            files.append(("access_url", (None, str(self.access_url).encode(), "text/plain")))

        if not isinstance(self.customer, Unset):
            if isinstance(self.customer, str):
                files.append(("customer", (None, str(self.customer).encode(), "text/plain")))
            else:
                files.append(("customer", (None, str(self.customer).encode(), "text/plain")))

        if not isinstance(self.attributes, Unset):
            files.append(("attributes", (None, str(self.attributes).encode(), "text/plain")))

        if not isinstance(self.options, Unset):
            files.append(("options", (None, json.dumps(self.options.to_dict()).encode(), "application/json")))

        if not isinstance(self.resource_options, Unset):
            files.append(
                ("resource_options", (None, json.dumps(self.resource_options.to_dict()).encode(), "application/json"))
            )

        if not isinstance(self.components, Unset):
            for components_item_element in self.components:
                files.append(
                    ("components", (None, json.dumps(components_item_element.to_dict()).encode(), "application/json"))
                )

        if not isinstance(self.vendor_details, Unset):
            files.append(("vendor_details", (None, str(self.vendor_details).encode(), "text/plain")))

        if not isinstance(self.getting_started, Unset):
            files.append(("getting_started", (None, str(self.getting_started).encode(), "text/plain")))

        if not isinstance(self.integration_guide, Unset):
            files.append(("integration_guide", (None, str(self.integration_guide).encode(), "text/plain")))

        if not isinstance(self.thumbnail, Unset):
            if isinstance(self.thumbnail, File):
                files.append(("thumbnail", self.thumbnail.to_tuple()))
            else:
                files.append(("thumbnail", (None, str(self.thumbnail).encode(), "text/plain")))

        if not isinstance(self.plans, Unset):
            for plans_item_element in self.plans:
                files.append(("plans", (None, json.dumps(plans_item_element.to_dict()).encode(), "application/json")))

        if not isinstance(self.shared, Unset):
            files.append(("shared", (None, str(self.shared).encode(), "text/plain")))

        if not isinstance(self.billable, Unset):
            files.append(("billable", (None, str(self.billable).encode(), "text/plain")))

        if not isinstance(self.datacite_doi, Unset):
            files.append(("datacite_doi", (None, str(self.datacite_doi).encode(), "text/plain")))

        if not isinstance(self.latitude, Unset):
            if isinstance(self.latitude, float):
                files.append(("latitude", (None, str(self.latitude).encode(), "text/plain")))
            else:
                files.append(("latitude", (None, str(self.latitude).encode(), "text/plain")))

        if not isinstance(self.longitude, Unset):
            if isinstance(self.longitude, float):
                files.append(("longitude", (None, str(self.longitude).encode(), "text/plain")))
            else:
                files.append(("longitude", (None, str(self.longitude).encode(), "text/plain")))

        if not isinstance(self.country, Unset):
            if isinstance(self.country, CountryEnum):
                files.append(("country", (None, str(self.country.value).encode(), "text/plain")))
            else:
                files.append(("country", (None, str(self.country.value).encode(), "text/plain")))

        if not isinstance(self.backend_id, Unset):
            files.append(("backend_id", (None, str(self.backend_id).encode(), "text/plain")))

        if not isinstance(self.image, Unset):
            if isinstance(self.image, File):
                files.append(("image", self.image.to_tuple()))
            else:
                files.append(("image", (None, str(self.image).encode(), "text/plain")))

        if not isinstance(self.backend_metadata, Unset):
            files.append(("backend_metadata", (None, str(self.backend_metadata).encode(), "text/plain")))

        if not isinstance(self.compliance_checklist, Unset):
            if isinstance(self.compliance_checklist, str):
                files.append(("compliance_checklist", (None, str(self.compliance_checklist).encode(), "text/plain")))
            else:
                files.append(("compliance_checklist", (None, str(self.compliance_checklist).encode(), "text/plain")))

        if not isinstance(self.limits, Unset):
            files.append(("limits", (None, json.dumps(self.limits.to_dict()).encode(), "application/json")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_provider_plan_request import BaseProviderPlanRequest
        from ..models.offering_component_request import OfferingComponentRequest
        from ..models.offering_create_request_multipart_limits import OfferingCreateRequestMultipartLimits
        from ..models.offering_options_request import OfferingOptionsRequest

        d = dict(src_dict)
        name = d.pop("name")

        category = d.pop("category")

        type_ = d.pop("type")

        slug = d.pop("slug", UNSET)

        description = d.pop("description", UNSET)

        full_description = d.pop("full_description", UNSET)

        privacy_policy_link = d.pop("privacy_policy_link", UNSET)

        access_url = d.pop("access_url", UNSET)

        def _parse_customer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        customer = _parse_customer(d.pop("customer", UNSET))

        attributes = d.pop("attributes", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, OfferingOptionsRequest]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = OfferingOptionsRequest.from_dict(_options)

        _resource_options = d.pop("resource_options", UNSET)
        resource_options: Union[Unset, OfferingOptionsRequest]
        if isinstance(_resource_options, Unset):
            resource_options = UNSET
        else:
            resource_options = OfferingOptionsRequest.from_dict(_resource_options)

        components = []
        _components = d.pop("components", UNSET)
        for components_item_data in _components or []:
            components_item = OfferingComponentRequest.from_dict(components_item_data)

            components.append(components_item)

        vendor_details = d.pop("vendor_details", UNSET)

        getting_started = d.pop("getting_started", UNSET)

        integration_guide = d.pop("integration_guide", UNSET)

        def _parse_thumbnail(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                thumbnail_type_0 = File(payload=BytesIO(data))

                return thumbnail_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        thumbnail = _parse_thumbnail(d.pop("thumbnail", UNSET))

        plans = []
        _plans = d.pop("plans", UNSET)
        for plans_item_data in _plans or []:
            plans_item = BaseProviderPlanRequest.from_dict(plans_item_data)

            plans.append(plans_item)

        shared = d.pop("shared", UNSET)

        billable = d.pop("billable", UNSET)

        datacite_doi = d.pop("datacite_doi", UNSET)

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

        backend_metadata = d.pop("backend_metadata", UNSET)

        def _parse_compliance_checklist(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        compliance_checklist = _parse_compliance_checklist(d.pop("compliance_checklist", UNSET))

        _limits = d.pop("limits", UNSET)
        limits: Union[Unset, OfferingCreateRequestMultipartLimits]
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = OfferingCreateRequestMultipartLimits.from_dict(_limits)

        offering_create_request_multipart = cls(
            name=name,
            category=category,
            type_=type_,
            slug=slug,
            description=description,
            full_description=full_description,
            privacy_policy_link=privacy_policy_link,
            access_url=access_url,
            customer=customer,
            attributes=attributes,
            options=options,
            resource_options=resource_options,
            components=components,
            vendor_details=vendor_details,
            getting_started=getting_started,
            integration_guide=integration_guide,
            thumbnail=thumbnail,
            plans=plans,
            shared=shared,
            billable=billable,
            datacite_doi=datacite_doi,
            latitude=latitude,
            longitude=longitude,
            country=country,
            backend_id=backend_id,
            image=image,
            backend_metadata=backend_metadata,
            compliance_checklist=compliance_checklist,
            limits=limits,
        )

        offering_create_request_multipart.additional_properties = d
        return offering_create_request_multipart

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
