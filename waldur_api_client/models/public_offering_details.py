import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.core_states import CoreStates
from ..models.country_enum import CountryEnum
from ..models.offering_state import OfferingState
from ..models.state_code_enum import StateCodeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_public_plan import BasePublicPlan
    from ..models.merged_plugin_options import MergedPluginOptions
    from ..models.nested_campaign import NestedCampaign
    from ..models.nested_endpoint import NestedEndpoint
    from ..models.nested_offering_file import NestedOfferingFile
    from ..models.nested_role import NestedRole
    from ..models.nested_screenshot import NestedScreenshot
    from ..models.offering_component import OfferingComponent
    from ..models.offering_options import OfferingOptions
    from ..models.organization_group import OrganizationGroup
    from ..models.public_offering_details_attributes import PublicOfferingDetailsAttributes
    from ..models.quota import Quota


T = TypeVar("T", bound="PublicOfferingDetails")


@_attrs_define
class PublicOfferingDetails:
    """
    Attributes:
        url (str):
        uuid (UUID):
        created (datetime.datetime):
        name (str):
        slug (str):
        endpoints (list['NestedEndpoint']):
        roles (list['NestedRole']):
        customer_uuid (UUID):
        customer_name (str):
        project (Union[None, str]):
        project_uuid (UUID):
        project_name (str):
        category (str):
        category_uuid (UUID):
        category_title (str):
        attributes (PublicOfferingDetailsAttributes):
        options (OfferingOptions):
        resource_options (OfferingOptions):
        components (list['OfferingComponent']):
        plugin_options (MergedPluginOptions):
        state (OfferingState):
        state_code (StateCodeEnum):
        order_count (int):
        plans (list['BasePublicPlan']):
        screenshots (list['NestedScreenshot']):
        type_ (str):
        scope (str):
        scope_uuid (UUID):
        scope_name (UUID):
        scope_state (CoreStates):
        files (list['NestedOfferingFile']):
        quotas (list['Quota']):
        paused_reason (str):
        citation_count (int): Number of citations of a DOI
        organization_groups (list['OrganizationGroup']):
        total_customers (int):
        total_cost (int):
        total_cost_estimated (int):
        parent_description (str):
        parent_uuid (UUID):
        parent_name (str):
        google_calendar_is_public (bool):
        google_calendar_link (Union[None, str]):
        promotion_campaigns (NestedCampaign):
        description (Union[Unset, str]):
        full_description (Union[Unset, str]):
        terms_of_service (Union[Unset, str]):
        terms_of_service_link (Union[Unset, str]):
        privacy_policy_link (Union[Unset, str]):
        access_url (Union[Unset, str]): Publicly accessible offering access URL
        customer (Union[None, Unset, str]):
        vendor_details (Union[Unset, str]):
        getting_started (Union[Unset, str]):
        integration_guide (Union[Unset, str]):
        thumbnail (Union[None, Unset, str]):
        shared (Union[Unset, bool]): Accessible to all customers.
        billable (Union[Unset, bool]): Purchase and usage is invoiced.
        datacite_doi (Union[Unset, str]):
        latitude (Union[None, Unset, float]):
        longitude (Union[None, Unset, float]):
        country (Union[BlankEnum, CountryEnum, Unset]):
        backend_id (Union[Unset, str]):
        image (Union[None, Unset, str]):
        backend_metadata (Union[Unset, Any]):
    """

    url: str
    uuid: UUID
    created: datetime.datetime
    name: str
    slug: str
    endpoints: list["NestedEndpoint"]
    roles: list["NestedRole"]
    customer_uuid: UUID
    customer_name: str
    project: Union[None, str]
    project_uuid: UUID
    project_name: str
    category: str
    category_uuid: UUID
    category_title: str
    attributes: "PublicOfferingDetailsAttributes"
    options: "OfferingOptions"
    resource_options: "OfferingOptions"
    components: list["OfferingComponent"]
    plugin_options: "MergedPluginOptions"
    state: OfferingState
    state_code: StateCodeEnum
    order_count: int
    plans: list["BasePublicPlan"]
    screenshots: list["NestedScreenshot"]
    type_: str
    scope: str
    scope_uuid: UUID
    scope_name: UUID
    scope_state: CoreStates
    files: list["NestedOfferingFile"]
    quotas: list["Quota"]
    paused_reason: str
    citation_count: int
    organization_groups: list["OrganizationGroup"]
    total_customers: int
    total_cost: int
    total_cost_estimated: int
    parent_description: str
    parent_uuid: UUID
    parent_name: str
    google_calendar_is_public: bool
    google_calendar_link: Union[None, str]
    promotion_campaigns: "NestedCampaign"
    description: Union[Unset, str] = UNSET
    full_description: Union[Unset, str] = UNSET
    terms_of_service: Union[Unset, str] = UNSET
    terms_of_service_link: Union[Unset, str] = UNSET
    privacy_policy_link: Union[Unset, str] = UNSET
    access_url: Union[Unset, str] = UNSET
    customer: Union[None, Unset, str] = UNSET
    vendor_details: Union[Unset, str] = UNSET
    getting_started: Union[Unset, str] = UNSET
    integration_guide: Union[Unset, str] = UNSET
    thumbnail: Union[None, Unset, str] = UNSET
    shared: Union[Unset, bool] = UNSET
    billable: Union[Unset, bool] = UNSET
    datacite_doi: Union[Unset, str] = UNSET
    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    country: Union[BlankEnum, CountryEnum, Unset] = UNSET
    backend_id: Union[Unset, str] = UNSET
    image: Union[None, Unset, str] = UNSET
    backend_metadata: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        created = self.created.isoformat()

        name = self.name

        slug = self.slug

        endpoints = []
        for endpoints_item_data in self.endpoints:
            endpoints_item = endpoints_item_data.to_dict()
            endpoints.append(endpoints_item)

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        customer_uuid = str(self.customer_uuid)

        customer_name = self.customer_name

        project: Union[None, str]
        project = self.project

        project_uuid = str(self.project_uuid)

        project_name = self.project_name

        category = self.category

        category_uuid = str(self.category_uuid)

        category_title = self.category_title

        attributes = self.attributes.to_dict()

        options = self.options.to_dict()

        resource_options = self.resource_options.to_dict()

        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()
            components.append(components_item)

        plugin_options = self.plugin_options.to_dict()

        state = self.state.value

        state_code = self.state_code.value

        order_count = self.order_count

        plans = []
        for plans_item_data in self.plans:
            plans_item = plans_item_data.to_dict()
            plans.append(plans_item)

        screenshots = []
        for screenshots_item_data in self.screenshots:
            screenshots_item = screenshots_item_data.to_dict()
            screenshots.append(screenshots_item)

        type_ = self.type_

        scope = self.scope

        scope_uuid = str(self.scope_uuid)

        scope_name = str(self.scope_name)

        scope_state = self.scope_state.value

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        quotas = []
        for quotas_item_data in self.quotas:
            quotas_item = quotas_item_data.to_dict()
            quotas.append(quotas_item)

        paused_reason = self.paused_reason

        citation_count = self.citation_count

        organization_groups = []
        for organization_groups_item_data in self.organization_groups:
            organization_groups_item = organization_groups_item_data.to_dict()
            organization_groups.append(organization_groups_item)

        total_customers = self.total_customers

        total_cost = self.total_cost

        total_cost_estimated = self.total_cost_estimated

        parent_description = self.parent_description

        parent_uuid = str(self.parent_uuid)

        parent_name = self.parent_name

        google_calendar_is_public = self.google_calendar_is_public

        google_calendar_link: Union[None, str]
        google_calendar_link = self.google_calendar_link

        promotion_campaigns = self.promotion_campaigns.to_dict()

        description = self.description

        full_description = self.full_description

        terms_of_service = self.terms_of_service

        terms_of_service_link = self.terms_of_service_link

        privacy_policy_link = self.privacy_policy_link

        access_url = self.access_url

        customer: Union[None, Unset, str]
        if isinstance(self.customer, Unset):
            customer = UNSET
        else:
            customer = self.customer

        vendor_details = self.vendor_details

        getting_started = self.getting_started

        integration_guide = self.integration_guide

        thumbnail: Union[None, Unset, str]
        if isinstance(self.thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = self.thumbnail

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

        image: Union[None, Unset, str]
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        backend_metadata = self.backend_metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "created": created,
                "name": name,
                "slug": slug,
                "endpoints": endpoints,
                "roles": roles,
                "customer_uuid": customer_uuid,
                "customer_name": customer_name,
                "project": project,
                "project_uuid": project_uuid,
                "project_name": project_name,
                "category": category,
                "category_uuid": category_uuid,
                "category_title": category_title,
                "attributes": attributes,
                "options": options,
                "resource_options": resource_options,
                "components": components,
                "plugin_options": plugin_options,
                "state": state,
                "state_code": state_code,
                "order_count": order_count,
                "plans": plans,
                "screenshots": screenshots,
                "type": type_,
                "scope": scope,
                "scope_uuid": scope_uuid,
                "scope_name": scope_name,
                "scope_state": scope_state,
                "files": files,
                "quotas": quotas,
                "paused_reason": paused_reason,
                "citation_count": citation_count,
                "organization_groups": organization_groups,
                "total_customers": total_customers,
                "total_cost": total_cost,
                "total_cost_estimated": total_cost_estimated,
                "parent_description": parent_description,
                "parent_uuid": parent_uuid,
                "parent_name": parent_name,
                "google_calendar_is_public": google_calendar_is_public,
                "google_calendar_link": google_calendar_link,
                "promotion_campaigns": promotion_campaigns,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if full_description is not UNSET:
            field_dict["full_description"] = full_description
        if terms_of_service is not UNSET:
            field_dict["terms_of_service"] = terms_of_service
        if terms_of_service_link is not UNSET:
            field_dict["terms_of_service_link"] = terms_of_service_link
        if privacy_policy_link is not UNSET:
            field_dict["privacy_policy_link"] = privacy_policy_link
        if access_url is not UNSET:
            field_dict["access_url"] = access_url
        if customer is not UNSET:
            field_dict["customer"] = customer
        if vendor_details is not UNSET:
            field_dict["vendor_details"] = vendor_details
        if getting_started is not UNSET:
            field_dict["getting_started"] = getting_started
        if integration_guide is not UNSET:
            field_dict["integration_guide"] = integration_guide
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_public_plan import BasePublicPlan
        from ..models.merged_plugin_options import MergedPluginOptions
        from ..models.nested_campaign import NestedCampaign
        from ..models.nested_endpoint import NestedEndpoint
        from ..models.nested_offering_file import NestedOfferingFile
        from ..models.nested_role import NestedRole
        from ..models.nested_screenshot import NestedScreenshot
        from ..models.offering_component import OfferingComponent
        from ..models.offering_options import OfferingOptions
        from ..models.organization_group import OrganizationGroup
        from ..models.public_offering_details_attributes import PublicOfferingDetailsAttributes
        from ..models.quota import Quota

        d = dict(src_dict)
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        name = d.pop("name")

        slug = d.pop("slug")

        endpoints = []
        _endpoints = d.pop("endpoints")
        for endpoints_item_data in _endpoints:
            endpoints_item = NestedEndpoint.from_dict(endpoints_item_data)

            endpoints.append(endpoints_item)

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = NestedRole.from_dict(roles_item_data)

            roles.append(roles_item)

        customer_uuid = UUID(d.pop("customer_uuid"))

        customer_name = d.pop("customer_name")

        def _parse_project(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        project = _parse_project(d.pop("project"))

        project_uuid = UUID(d.pop("project_uuid"))

        project_name = d.pop("project_name")

        category = d.pop("category")

        category_uuid = UUID(d.pop("category_uuid"))

        category_title = d.pop("category_title")

        attributes = PublicOfferingDetailsAttributes.from_dict(d.pop("attributes"))

        options = OfferingOptions.from_dict(d.pop("options"))

        resource_options = OfferingOptions.from_dict(d.pop("resource_options"))

        components = []
        _components = d.pop("components")
        for components_item_data in _components:
            components_item = OfferingComponent.from_dict(components_item_data)

            components.append(components_item)

        plugin_options = MergedPluginOptions.from_dict(d.pop("plugin_options"))

        state = OfferingState(d.pop("state"))

        state_code = StateCodeEnum(d.pop("state_code"))

        order_count = d.pop("order_count")

        plans = []
        _plans = d.pop("plans")
        for plans_item_data in _plans:
            plans_item = BasePublicPlan.from_dict(plans_item_data)

            plans.append(plans_item)

        screenshots = []
        _screenshots = d.pop("screenshots")
        for screenshots_item_data in _screenshots:
            screenshots_item = NestedScreenshot.from_dict(screenshots_item_data)

            screenshots.append(screenshots_item)

        type_ = d.pop("type")

        scope = d.pop("scope")

        scope_uuid = UUID(d.pop("scope_uuid"))

        scope_name = UUID(d.pop("scope_name"))

        scope_state = CoreStates(d.pop("scope_state"))

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = NestedOfferingFile.from_dict(files_item_data)

            files.append(files_item)

        quotas = []
        _quotas = d.pop("quotas")
        for quotas_item_data in _quotas:
            quotas_item = Quota.from_dict(quotas_item_data)

            quotas.append(quotas_item)

        paused_reason = d.pop("paused_reason")

        citation_count = d.pop("citation_count")

        organization_groups = []
        _organization_groups = d.pop("organization_groups")
        for organization_groups_item_data in _organization_groups:
            organization_groups_item = OrganizationGroup.from_dict(organization_groups_item_data)

            organization_groups.append(organization_groups_item)

        total_customers = d.pop("total_customers")

        total_cost = d.pop("total_cost")

        total_cost_estimated = d.pop("total_cost_estimated")

        parent_description = d.pop("parent_description")

        parent_uuid = UUID(d.pop("parent_uuid"))

        parent_name = d.pop("parent_name")

        google_calendar_is_public = d.pop("google_calendar_is_public")

        def _parse_google_calendar_link(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        google_calendar_link = _parse_google_calendar_link(d.pop("google_calendar_link"))

        promotion_campaigns = NestedCampaign.from_dict(d.pop("promotion_campaigns"))

        description = d.pop("description", UNSET)

        full_description = d.pop("full_description", UNSET)

        terms_of_service = d.pop("terms_of_service", UNSET)

        terms_of_service_link = d.pop("terms_of_service_link", UNSET)

        privacy_policy_link = d.pop("privacy_policy_link", UNSET)

        access_url = d.pop("access_url", UNSET)

        def _parse_customer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        customer = _parse_customer(d.pop("customer", UNSET))

        vendor_details = d.pop("vendor_details", UNSET)

        getting_started = d.pop("getting_started", UNSET)

        integration_guide = d.pop("integration_guide", UNSET)

        def _parse_thumbnail(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thumbnail = _parse_thumbnail(d.pop("thumbnail", UNSET))

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

        def _parse_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image = _parse_image(d.pop("image", UNSET))

        backend_metadata = d.pop("backend_metadata", UNSET)

        public_offering_details = cls(
            url=url,
            uuid=uuid,
            created=created,
            name=name,
            slug=slug,
            endpoints=endpoints,
            roles=roles,
            customer_uuid=customer_uuid,
            customer_name=customer_name,
            project=project,
            project_uuid=project_uuid,
            project_name=project_name,
            category=category,
            category_uuid=category_uuid,
            category_title=category_title,
            attributes=attributes,
            options=options,
            resource_options=resource_options,
            components=components,
            plugin_options=plugin_options,
            state=state,
            state_code=state_code,
            order_count=order_count,
            plans=plans,
            screenshots=screenshots,
            type_=type_,
            scope=scope,
            scope_uuid=scope_uuid,
            scope_name=scope_name,
            scope_state=scope_state,
            files=files,
            quotas=quotas,
            paused_reason=paused_reason,
            citation_count=citation_count,
            organization_groups=organization_groups,
            total_customers=total_customers,
            total_cost=total_cost,
            total_cost_estimated=total_cost_estimated,
            parent_description=parent_description,
            parent_uuid=parent_uuid,
            parent_name=parent_name,
            google_calendar_is_public=google_calendar_is_public,
            google_calendar_link=google_calendar_link,
            promotion_campaigns=promotion_campaigns,
            description=description,
            full_description=full_description,
            terms_of_service=terms_of_service,
            terms_of_service_link=terms_of_service_link,
            privacy_policy_link=privacy_policy_link,
            access_url=access_url,
            customer=customer,
            vendor_details=vendor_details,
            getting_started=getting_started,
            integration_guide=integration_guide,
            thumbnail=thumbnail,
            shared=shared,
            billable=billable,
            datacite_doi=datacite_doi,
            latitude=latitude,
            longitude=longitude,
            country=country,
            backend_id=backend_id,
            image=image,
            backend_metadata=backend_metadata,
        )

        public_offering_details.additional_properties = d
        return public_offering_details

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
