import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.billing_unit import BillingUnit
from ..models.resource_state import ResourceState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backend_metadata import BackendMetadata
    from ..models.nested_endpoint import NestedEndpoint
    from ..models.order_details import OrderDetails
    from ..models.report_section import ReportSection
    from ..models.resource_attributes import ResourceAttributes
    from ..models.resource_current_usages import ResourceCurrentUsages
    from ..models.resource_limits import ResourceLimits


T = TypeVar("T", bound="Resource")


@_attrs_define
class Resource:
    """
    Attributes:
        offering (str):
        offering_name (str):
        offering_uuid (UUID):
        offering_description (str):
        offering_image (str):
        offering_thumbnail (str):
        offering_type (str):
        offering_terms_of_service (str):
        offering_shared (bool): Accessible to all customers.
        offering_billable (bool): Purchase and usage is invoiced.
        offering_plugin_options (Any): Public data used by specific plugin, such as storage mode for OpenStack.
        provider_name (str):
        provider_uuid (UUID):
        category_title (str):
        category_uuid (UUID):
        category_icon (str):
        plan_unit (BillingUnit):
        plan_name (str):
        plan_uuid (UUID):
        plan_description (str):
        attributes (ResourceAttributes):
        limits (ResourceLimits):
        uuid (UUID):
        created (datetime.datetime):
        modified (datetime.datetime):
        url (str):
        scope (str):
        description (str):
        state (ResourceState):
        resource_uuid (UUID):
        backend_id (str):
        effective_id (str):
        resource_type (Union[None, str]):
        project (str):
        project_uuid (UUID):
        project_name (str):
        project_description (str):
        project_end_date (Union[None, datetime.date]): The date is inclusive. Once reached, all project resource will be
            scheduled for termination.
        project_end_date_requested_by (str):
        customer_uuid (UUID):
        customer_name (str):
        parent_offering_uuid (UUID):
        parent_offering_name (str):
        parent_uuid (UUID):
        parent_name (str):
        backend_metadata (BackendMetadata):
        is_usage_based (bool):
        is_limit_based (bool):
        name (str):
        slug (str):
        current_usages (ResourceCurrentUsages):
        can_terminate (bool):
        report (list['ReportSection']):
        end_date_requested_by (Union[None, str]):
        username (Union[None, str]):
        limit_usage (Union[None, float]):
        restrict_member_access (bool):
        endpoints (list['NestedEndpoint']):
        error_message (str):
        error_traceback (str):
        offering_customer_uuid (UUID):
        options (Any):
        available_actions (list[str]):
        last_sync (datetime.datetime):
        order_in_progress (Union['OrderDetails', None]):
        creation_order (Union['OrderDetails', None]):
        plan (Union[Unset, str]):
        end_date (Union[None, Unset, datetime.date]): The date is inclusive. Once reached, a resource will be scheduled
            for termination.
        downscaled (Union[Unset, bool]):
        paused (Union[Unset, bool]):
    """

    offering: str
    offering_name: str
    offering_uuid: UUID
    offering_description: str
    offering_image: str
    offering_thumbnail: str
    offering_type: str
    offering_terms_of_service: str
    offering_shared: bool
    offering_billable: bool
    offering_plugin_options: Any
    provider_name: str
    provider_uuid: UUID
    category_title: str
    category_uuid: UUID
    category_icon: str
    plan_unit: BillingUnit
    plan_name: str
    plan_uuid: UUID
    plan_description: str
    attributes: "ResourceAttributes"
    limits: "ResourceLimits"
    uuid: UUID
    created: datetime.datetime
    modified: datetime.datetime
    url: str
    scope: str
    description: str
    state: ResourceState
    resource_uuid: UUID
    backend_id: str
    effective_id: str
    resource_type: Union[None, str]
    project: str
    project_uuid: UUID
    project_name: str
    project_description: str
    project_end_date: Union[None, datetime.date]
    project_end_date_requested_by: str
    customer_uuid: UUID
    customer_name: str
    parent_offering_uuid: UUID
    parent_offering_name: str
    parent_uuid: UUID
    parent_name: str
    backend_metadata: "BackendMetadata"
    is_usage_based: bool
    is_limit_based: bool
    name: str
    slug: str
    current_usages: "ResourceCurrentUsages"
    can_terminate: bool
    report: list["ReportSection"]
    end_date_requested_by: Union[None, str]
    username: Union[None, str]
    limit_usage: Union[None, float]
    restrict_member_access: bool
    endpoints: list["NestedEndpoint"]
    error_message: str
    error_traceback: str
    offering_customer_uuid: UUID
    options: Any
    available_actions: list[str]
    last_sync: datetime.datetime
    order_in_progress: Union["OrderDetails", None]
    creation_order: Union["OrderDetails", None]
    plan: Union[Unset, str] = UNSET
    end_date: Union[None, Unset, datetime.date] = UNSET
    downscaled: Union[Unset, bool] = UNSET
    paused: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.order_details import OrderDetails

        offering = self.offering

        offering_name = self.offering_name

        offering_uuid = str(self.offering_uuid)

        offering_description = self.offering_description

        offering_image = self.offering_image

        offering_thumbnail = self.offering_thumbnail

        offering_type = self.offering_type

        offering_terms_of_service = self.offering_terms_of_service

        offering_shared = self.offering_shared

        offering_billable = self.offering_billable

        offering_plugin_options = self.offering_plugin_options

        provider_name = self.provider_name

        provider_uuid = str(self.provider_uuid)

        category_title = self.category_title

        category_uuid = str(self.category_uuid)

        category_icon = self.category_icon

        plan_unit = self.plan_unit.value

        plan_name = self.plan_name

        plan_uuid = str(self.plan_uuid)

        plan_description = self.plan_description

        attributes = self.attributes.to_dict()

        limits = self.limits.to_dict()

        uuid = str(self.uuid)

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        url = self.url

        scope = self.scope

        description = self.description

        state = self.state.value

        resource_uuid = str(self.resource_uuid)

        backend_id = self.backend_id

        effective_id = self.effective_id

        resource_type: Union[None, str]
        resource_type = self.resource_type

        project = self.project

        project_uuid = str(self.project_uuid)

        project_name = self.project_name

        project_description = self.project_description

        project_end_date: Union[None, str]
        if isinstance(self.project_end_date, datetime.date):
            project_end_date = self.project_end_date.isoformat()
        else:
            project_end_date = self.project_end_date

        project_end_date_requested_by = self.project_end_date_requested_by

        customer_uuid = str(self.customer_uuid)

        customer_name = self.customer_name

        parent_offering_uuid = str(self.parent_offering_uuid)

        parent_offering_name = self.parent_offering_name

        parent_uuid = str(self.parent_uuid)

        parent_name = self.parent_name

        backend_metadata = self.backend_metadata.to_dict()

        is_usage_based = self.is_usage_based

        is_limit_based = self.is_limit_based

        name = self.name

        slug = self.slug

        current_usages = self.current_usages.to_dict()

        can_terminate = self.can_terminate

        report = []
        for report_item_data in self.report:
            report_item = report_item_data.to_dict()
            report.append(report_item)

        end_date_requested_by: Union[None, str]
        end_date_requested_by = self.end_date_requested_by

        username: Union[None, str]
        username = self.username

        limit_usage: Union[None, float]
        limit_usage = self.limit_usage

        restrict_member_access = self.restrict_member_access

        endpoints = []
        for endpoints_item_data in self.endpoints:
            endpoints_item = endpoints_item_data.to_dict()
            endpoints.append(endpoints_item)

        error_message = self.error_message

        error_traceback = self.error_traceback

        offering_customer_uuid = str(self.offering_customer_uuid)

        options = self.options

        available_actions = self.available_actions

        last_sync = self.last_sync.isoformat()

        order_in_progress: Union[None, dict[str, Any]]
        if isinstance(self.order_in_progress, OrderDetails):
            order_in_progress = self.order_in_progress.to_dict()
        else:
            order_in_progress = self.order_in_progress

        creation_order: Union[None, dict[str, Any]]
        if isinstance(self.creation_order, OrderDetails):
            creation_order = self.creation_order.to_dict()
        else:
            creation_order = self.creation_order

        plan = self.plan

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        downscaled = self.downscaled

        paused = self.paused

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offering": offering,
                "offering_name": offering_name,
                "offering_uuid": offering_uuid,
                "offering_description": offering_description,
                "offering_image": offering_image,
                "offering_thumbnail": offering_thumbnail,
                "offering_type": offering_type,
                "offering_terms_of_service": offering_terms_of_service,
                "offering_shared": offering_shared,
                "offering_billable": offering_billable,
                "offering_plugin_options": offering_plugin_options,
                "provider_name": provider_name,
                "provider_uuid": provider_uuid,
                "category_title": category_title,
                "category_uuid": category_uuid,
                "category_icon": category_icon,
                "plan_unit": plan_unit,
                "plan_name": plan_name,
                "plan_uuid": plan_uuid,
                "plan_description": plan_description,
                "attributes": attributes,
                "limits": limits,
                "uuid": uuid,
                "created": created,
                "modified": modified,
                "url": url,
                "scope": scope,
                "description": description,
                "state": state,
                "resource_uuid": resource_uuid,
                "backend_id": backend_id,
                "effective_id": effective_id,
                "resource_type": resource_type,
                "project": project,
                "project_uuid": project_uuid,
                "project_name": project_name,
                "project_description": project_description,
                "project_end_date": project_end_date,
                "project_end_date_requested_by": project_end_date_requested_by,
                "customer_uuid": customer_uuid,
                "customer_name": customer_name,
                "parent_offering_uuid": parent_offering_uuid,
                "parent_offering_name": parent_offering_name,
                "parent_uuid": parent_uuid,
                "parent_name": parent_name,
                "backend_metadata": backend_metadata,
                "is_usage_based": is_usage_based,
                "is_limit_based": is_limit_based,
                "name": name,
                "slug": slug,
                "current_usages": current_usages,
                "can_terminate": can_terminate,
                "report": report,
                "end_date_requested_by": end_date_requested_by,
                "username": username,
                "limit_usage": limit_usage,
                "restrict_member_access": restrict_member_access,
                "endpoints": endpoints,
                "error_message": error_message,
                "error_traceback": error_traceback,
                "offering_customer_uuid": offering_customer_uuid,
                "options": options,
                "available_actions": available_actions,
                "last_sync": last_sync,
                "order_in_progress": order_in_progress,
                "creation_order": creation_order,
            }
        )
        if plan is not UNSET:
            field_dict["plan"] = plan
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if downscaled is not UNSET:
            field_dict["downscaled"] = downscaled
        if paused is not UNSET:
            field_dict["paused"] = paused

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backend_metadata import BackendMetadata
        from ..models.nested_endpoint import NestedEndpoint
        from ..models.order_details import OrderDetails
        from ..models.report_section import ReportSection
        from ..models.resource_attributes import ResourceAttributes
        from ..models.resource_current_usages import ResourceCurrentUsages
        from ..models.resource_limits import ResourceLimits

        d = dict(src_dict)
        offering = d.pop("offering")

        offering_name = d.pop("offering_name")

        offering_uuid = UUID(d.pop("offering_uuid"))

        offering_description = d.pop("offering_description")

        offering_image = d.pop("offering_image")

        offering_thumbnail = d.pop("offering_thumbnail")

        offering_type = d.pop("offering_type")

        offering_terms_of_service = d.pop("offering_terms_of_service")

        offering_shared = d.pop("offering_shared")

        offering_billable = d.pop("offering_billable")

        offering_plugin_options = d.pop("offering_plugin_options")

        provider_name = d.pop("provider_name")

        provider_uuid = UUID(d.pop("provider_uuid"))

        category_title = d.pop("category_title")

        category_uuid = UUID(d.pop("category_uuid"))

        category_icon = d.pop("category_icon")

        plan_unit = BillingUnit(d.pop("plan_unit"))

        plan_name = d.pop("plan_name")

        plan_uuid = UUID(d.pop("plan_uuid"))

        plan_description = d.pop("plan_description")

        attributes = ResourceAttributes.from_dict(d.pop("attributes"))

        limits = ResourceLimits.from_dict(d.pop("limits"))

        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        url = d.pop("url")

        scope = d.pop("scope")

        description = d.pop("description")

        state = ResourceState(d.pop("state"))

        resource_uuid = UUID(d.pop("resource_uuid"))

        backend_id = d.pop("backend_id")

        effective_id = d.pop("effective_id")

        def _parse_resource_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        resource_type = _parse_resource_type(d.pop("resource_type"))

        project = d.pop("project")

        project_uuid = UUID(d.pop("project_uuid"))

        project_name = d.pop("project_name")

        project_description = d.pop("project_description")

        def _parse_project_end_date(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_end_date_type_0 = isoparse(data).date()

                return project_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        project_end_date = _parse_project_end_date(d.pop("project_end_date"))

        project_end_date_requested_by = d.pop("project_end_date_requested_by")

        customer_uuid = UUID(d.pop("customer_uuid"))

        customer_name = d.pop("customer_name")

        parent_offering_uuid = UUID(d.pop("parent_offering_uuid"))

        parent_offering_name = d.pop("parent_offering_name")

        parent_uuid = UUID(d.pop("parent_uuid"))

        parent_name = d.pop("parent_name")

        backend_metadata = BackendMetadata.from_dict(d.pop("backend_metadata"))

        is_usage_based = d.pop("is_usage_based")

        is_limit_based = d.pop("is_limit_based")

        name = d.pop("name")

        slug = d.pop("slug")

        current_usages = ResourceCurrentUsages.from_dict(d.pop("current_usages"))

        can_terminate = d.pop("can_terminate")

        report = []
        _report = d.pop("report")
        for report_item_data in _report:
            report_item = ReportSection.from_dict(report_item_data)

            report.append(report_item)

        def _parse_end_date_requested_by(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        end_date_requested_by = _parse_end_date_requested_by(d.pop("end_date_requested_by"))

        def _parse_username(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        username = _parse_username(d.pop("username"))

        def _parse_limit_usage(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        limit_usage = _parse_limit_usage(d.pop("limit_usage"))

        restrict_member_access = d.pop("restrict_member_access")

        endpoints = []
        _endpoints = d.pop("endpoints")
        for endpoints_item_data in _endpoints:
            endpoints_item = NestedEndpoint.from_dict(endpoints_item_data)

            endpoints.append(endpoints_item)

        error_message = d.pop("error_message")

        error_traceback = d.pop("error_traceback")

        offering_customer_uuid = UUID(d.pop("offering_customer_uuid"))

        options = d.pop("options")

        available_actions = cast(list[str], d.pop("available_actions"))

        last_sync = isoparse(d.pop("last_sync"))

        def _parse_order_in_progress(data: object) -> Union["OrderDetails", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                order_in_progress_type_1 = OrderDetails.from_dict(data)

                return order_in_progress_type_1
            except:  # noqa: E722
                pass
            return cast(Union["OrderDetails", None], data)

        order_in_progress = _parse_order_in_progress(d.pop("order_in_progress"))

        def _parse_creation_order(data: object) -> Union["OrderDetails", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                creation_order_type_1 = OrderDetails.from_dict(data)

                return creation_order_type_1
            except:  # noqa: E722
                pass
            return cast(Union["OrderDetails", None], data)

        creation_order = _parse_creation_order(d.pop("creation_order"))

        plan = d.pop("plan", UNSET)

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data).date()

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        downscaled = d.pop("downscaled", UNSET)

        paused = d.pop("paused", UNSET)

        resource = cls(
            offering=offering,
            offering_name=offering_name,
            offering_uuid=offering_uuid,
            offering_description=offering_description,
            offering_image=offering_image,
            offering_thumbnail=offering_thumbnail,
            offering_type=offering_type,
            offering_terms_of_service=offering_terms_of_service,
            offering_shared=offering_shared,
            offering_billable=offering_billable,
            offering_plugin_options=offering_plugin_options,
            provider_name=provider_name,
            provider_uuid=provider_uuid,
            category_title=category_title,
            category_uuid=category_uuid,
            category_icon=category_icon,
            plan_unit=plan_unit,
            plan_name=plan_name,
            plan_uuid=plan_uuid,
            plan_description=plan_description,
            attributes=attributes,
            limits=limits,
            uuid=uuid,
            created=created,
            modified=modified,
            url=url,
            scope=scope,
            description=description,
            state=state,
            resource_uuid=resource_uuid,
            backend_id=backend_id,
            effective_id=effective_id,
            resource_type=resource_type,
            project=project,
            project_uuid=project_uuid,
            project_name=project_name,
            project_description=project_description,
            project_end_date=project_end_date,
            project_end_date_requested_by=project_end_date_requested_by,
            customer_uuid=customer_uuid,
            customer_name=customer_name,
            parent_offering_uuid=parent_offering_uuid,
            parent_offering_name=parent_offering_name,
            parent_uuid=parent_uuid,
            parent_name=parent_name,
            backend_metadata=backend_metadata,
            is_usage_based=is_usage_based,
            is_limit_based=is_limit_based,
            name=name,
            slug=slug,
            current_usages=current_usages,
            can_terminate=can_terminate,
            report=report,
            end_date_requested_by=end_date_requested_by,
            username=username,
            limit_usage=limit_usage,
            restrict_member_access=restrict_member_access,
            endpoints=endpoints,
            error_message=error_message,
            error_traceback=error_traceback,
            offering_customer_uuid=offering_customer_uuid,
            options=options,
            available_actions=available_actions,
            last_sync=last_sync,
            order_in_progress=order_in_progress,
            creation_order=creation_order,
            plan=plan,
            end_date=end_date,
            downscaled=downscaled,
            paused=paused,
        )

        resource.additional_properties = d
        return resource

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
