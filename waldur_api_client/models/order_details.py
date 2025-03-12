import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.billing_unit import BillingUnit
from ..models.order_state import OrderState
from ..models.request_types import RequestTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_reference import IssueReference
    from ..models.order_details_attributes import OrderDetailsAttributes
    from ..models.order_details_limits import OrderDetailsLimits


T = TypeVar("T", bound="OrderDetails")


@_attrs_define
class OrderDetails:
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
        attributes (OrderDetailsAttributes): Get attributes excluding secret attributes, such as username and password.
        uuid (UUID):
        created (datetime.datetime):
        modified (datetime.datetime):
        resource_uuid (UUID):
        resource_type (str):
        resource_name (str):
        cost (Union[None, str]):
        state (OrderState):
        output (str):
        marketplace_resource_uuid (UUID):
        error_message (str):
        completed_at (Union[None, datetime.datetime]):
        consumer_reviewed_by (str): Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_
            characters
        consumer_reviewed_by_full_name (str):
        consumer_reviewed_by_username (str): Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_
            characters
        consumer_reviewed_at (Union[None, datetime.datetime]):
        provider_reviewed_by (str): Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_
            characters
        provider_reviewed_by_full_name (str):
        provider_reviewed_by_username (str): Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_
            characters
        provider_reviewed_at (Union[None, datetime.datetime]):
        created_by_username (str): Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_
            characters
        created_by_full_name (str):
        created_by_civil_number (Union[None, str]):
        customer_name (str):
        customer_uuid (UUID):
        customer_slug (str):
        project_name (str):
        project_uuid (UUID):
        project_description (str):
        project_slug (str):
        old_plan_name (str):
        new_plan_name (str):
        old_plan_uuid (UUID):
        new_plan_uuid (UUID):
        old_cost_estimate (Union[None, str]):
        new_cost_estimate (Union[None, str]):
        can_terminate (bool):
        fixed_price (float):
        activation_price (float):
        termination_comment (Union[None, str]):
        issue (IssueReference):
        plan (Union[Unset, str]):
        limits (Union[Unset, OrderDetailsLimits]):
        type_ (Union[Unset, RequestTypes]):  Default: RequestTypes.CREATE.
        callback_url (Union[None, Unset, str]):
        backend_id (Union[Unset, str]):
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
    attributes: "OrderDetailsAttributes"
    uuid: UUID
    created: datetime.datetime
    modified: datetime.datetime
    resource_uuid: UUID
    resource_type: str
    resource_name: str
    cost: Union[None, str]
    state: OrderState
    output: str
    marketplace_resource_uuid: UUID
    error_message: str
    completed_at: Union[None, datetime.datetime]
    consumer_reviewed_by: str
    consumer_reviewed_by_full_name: str
    consumer_reviewed_by_username: str
    consumer_reviewed_at: Union[None, datetime.datetime]
    provider_reviewed_by: str
    provider_reviewed_by_full_name: str
    provider_reviewed_by_username: str
    provider_reviewed_at: Union[None, datetime.datetime]
    created_by_username: str
    created_by_full_name: str
    created_by_civil_number: Union[None, str]
    customer_name: str
    customer_uuid: UUID
    customer_slug: str
    project_name: str
    project_uuid: UUID
    project_description: str
    project_slug: str
    old_plan_name: str
    new_plan_name: str
    old_plan_uuid: UUID
    new_plan_uuid: UUID
    old_cost_estimate: Union[None, str]
    new_cost_estimate: Union[None, str]
    can_terminate: bool
    fixed_price: float
    activation_price: float
    termination_comment: Union[None, str]
    issue: "IssueReference"
    plan: Union[Unset, str] = UNSET
    limits: Union[Unset, "OrderDetailsLimits"] = UNSET
    type_: Union[Unset, RequestTypes] = RequestTypes.CREATE
    callback_url: Union[None, Unset, str] = UNSET
    backend_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        uuid = str(self.uuid)

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        resource_uuid = str(self.resource_uuid)

        resource_type = self.resource_type

        resource_name = self.resource_name

        cost: Union[None, str]
        cost = self.cost

        state = self.state.value

        output = self.output

        marketplace_resource_uuid = str(self.marketplace_resource_uuid)

        error_message = self.error_message

        completed_at: Union[None, str]
        if isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        consumer_reviewed_by = self.consumer_reviewed_by

        consumer_reviewed_by_full_name = self.consumer_reviewed_by_full_name

        consumer_reviewed_by_username = self.consumer_reviewed_by_username

        consumer_reviewed_at: Union[None, str]
        if isinstance(self.consumer_reviewed_at, datetime.datetime):
            consumer_reviewed_at = self.consumer_reviewed_at.isoformat()
        else:
            consumer_reviewed_at = self.consumer_reviewed_at

        provider_reviewed_by = self.provider_reviewed_by

        provider_reviewed_by_full_name = self.provider_reviewed_by_full_name

        provider_reviewed_by_username = self.provider_reviewed_by_username

        provider_reviewed_at: Union[None, str]
        if isinstance(self.provider_reviewed_at, datetime.datetime):
            provider_reviewed_at = self.provider_reviewed_at.isoformat()
        else:
            provider_reviewed_at = self.provider_reviewed_at

        created_by_username = self.created_by_username

        created_by_full_name = self.created_by_full_name

        created_by_civil_number: Union[None, str]
        created_by_civil_number = self.created_by_civil_number

        customer_name = self.customer_name

        customer_uuid = str(self.customer_uuid)

        customer_slug = self.customer_slug

        project_name = self.project_name

        project_uuid = str(self.project_uuid)

        project_description = self.project_description

        project_slug = self.project_slug

        old_plan_name = self.old_plan_name

        new_plan_name = self.new_plan_name

        old_plan_uuid = str(self.old_plan_uuid)

        new_plan_uuid = str(self.new_plan_uuid)

        old_cost_estimate: Union[None, str]
        old_cost_estimate = self.old_cost_estimate

        new_cost_estimate: Union[None, str]
        new_cost_estimate = self.new_cost_estimate

        can_terminate = self.can_terminate

        fixed_price = self.fixed_price

        activation_price = self.activation_price

        termination_comment: Union[None, str]
        termination_comment = self.termination_comment

        issue = self.issue.to_dict()

        plan = self.plan

        limits: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        callback_url: Union[None, Unset, str]
        if isinstance(self.callback_url, Unset):
            callback_url = UNSET
        else:
            callback_url = self.callback_url

        backend_id = self.backend_id

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
                "uuid": uuid,
                "created": created,
                "modified": modified,
                "resource_uuid": resource_uuid,
                "resource_type": resource_type,
                "resource_name": resource_name,
                "cost": cost,
                "state": state,
                "output": output,
                "marketplace_resource_uuid": marketplace_resource_uuid,
                "error_message": error_message,
                "completed_at": completed_at,
                "consumer_reviewed_by": consumer_reviewed_by,
                "consumer_reviewed_by_full_name": consumer_reviewed_by_full_name,
                "consumer_reviewed_by_username": consumer_reviewed_by_username,
                "consumer_reviewed_at": consumer_reviewed_at,
                "provider_reviewed_by": provider_reviewed_by,
                "provider_reviewed_by_full_name": provider_reviewed_by_full_name,
                "provider_reviewed_by_username": provider_reviewed_by_username,
                "provider_reviewed_at": provider_reviewed_at,
                "created_by_username": created_by_username,
                "created_by_full_name": created_by_full_name,
                "created_by_civil_number": created_by_civil_number,
                "customer_name": customer_name,
                "customer_uuid": customer_uuid,
                "customer_slug": customer_slug,
                "project_name": project_name,
                "project_uuid": project_uuid,
                "project_description": project_description,
                "project_slug": project_slug,
                "old_plan_name": old_plan_name,
                "new_plan_name": new_plan_name,
                "old_plan_uuid": old_plan_uuid,
                "new_plan_uuid": new_plan_uuid,
                "old_cost_estimate": old_cost_estimate,
                "new_cost_estimate": new_cost_estimate,
                "can_terminate": can_terminate,
                "fixed_price": fixed_price,
                "activation_price": activation_price,
                "termination_comment": termination_comment,
                "issue": issue,
            }
        )
        if plan is not UNSET:
            field_dict["plan"] = plan
        if limits is not UNSET:
            field_dict["limits"] = limits
        if type_ is not UNSET:
            field_dict["type"] = type_
        if callback_url is not UNSET:
            field_dict["callback_url"] = callback_url
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.issue_reference import IssueReference
        from ..models.order_details_attributes import OrderDetailsAttributes
        from ..models.order_details_limits import OrderDetailsLimits

        d = src_dict.copy()
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

        attributes = OrderDetailsAttributes.from_dict(d.pop("attributes"))

        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        resource_uuid = UUID(d.pop("resource_uuid"))

        resource_type = d.pop("resource_type")

        resource_name = d.pop("resource_name")

        def _parse_cost(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        cost = _parse_cost(d.pop("cost"))

        state = OrderState(d.pop("state"))

        output = d.pop("output")

        marketplace_resource_uuid = UUID(d.pop("marketplace_resource_uuid"))

        error_message = d.pop("error_message")

        def _parse_completed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        consumer_reviewed_by = d.pop("consumer_reviewed_by")

        consumer_reviewed_by_full_name = d.pop("consumer_reviewed_by_full_name")

        consumer_reviewed_by_username = d.pop("consumer_reviewed_by_username")

        def _parse_consumer_reviewed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                consumer_reviewed_at_type_0 = isoparse(data)

                return consumer_reviewed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        consumer_reviewed_at = _parse_consumer_reviewed_at(d.pop("consumer_reviewed_at"))

        provider_reviewed_by = d.pop("provider_reviewed_by")

        provider_reviewed_by_full_name = d.pop("provider_reviewed_by_full_name")

        provider_reviewed_by_username = d.pop("provider_reviewed_by_username")

        def _parse_provider_reviewed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_reviewed_at_type_0 = isoparse(data)

                return provider_reviewed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        provider_reviewed_at = _parse_provider_reviewed_at(d.pop("provider_reviewed_at"))

        created_by_username = d.pop("created_by_username")

        created_by_full_name = d.pop("created_by_full_name")

        def _parse_created_by_civil_number(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by_civil_number = _parse_created_by_civil_number(d.pop("created_by_civil_number"))

        customer_name = d.pop("customer_name")

        customer_uuid = UUID(d.pop("customer_uuid"))

        customer_slug = d.pop("customer_slug")

        project_name = d.pop("project_name")

        project_uuid = UUID(d.pop("project_uuid"))

        project_description = d.pop("project_description")

        project_slug = d.pop("project_slug")

        old_plan_name = d.pop("old_plan_name")

        new_plan_name = d.pop("new_plan_name")

        old_plan_uuid = UUID(d.pop("old_plan_uuid"))

        new_plan_uuid = UUID(d.pop("new_plan_uuid"))

        def _parse_old_cost_estimate(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        old_cost_estimate = _parse_old_cost_estimate(d.pop("old_cost_estimate"))

        def _parse_new_cost_estimate(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        new_cost_estimate = _parse_new_cost_estimate(d.pop("new_cost_estimate"))

        can_terminate = d.pop("can_terminate")

        fixed_price = d.pop("fixed_price")

        activation_price = d.pop("activation_price")

        def _parse_termination_comment(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        termination_comment = _parse_termination_comment(d.pop("termination_comment"))

        issue = IssueReference.from_dict(d.pop("issue"))

        plan = d.pop("plan", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: Union[Unset, OrderDetailsLimits]
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = OrderDetailsLimits.from_dict(_limits)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, RequestTypes]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RequestTypes(_type_)

        def _parse_callback_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        callback_url = _parse_callback_url(d.pop("callback_url", UNSET))

        backend_id = d.pop("backend_id", UNSET)

        order_details = cls(
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
            uuid=uuid,
            created=created,
            modified=modified,
            resource_uuid=resource_uuid,
            resource_type=resource_type,
            resource_name=resource_name,
            cost=cost,
            state=state,
            output=output,
            marketplace_resource_uuid=marketplace_resource_uuid,
            error_message=error_message,
            completed_at=completed_at,
            consumer_reviewed_by=consumer_reviewed_by,
            consumer_reviewed_by_full_name=consumer_reviewed_by_full_name,
            consumer_reviewed_by_username=consumer_reviewed_by_username,
            consumer_reviewed_at=consumer_reviewed_at,
            provider_reviewed_by=provider_reviewed_by,
            provider_reviewed_by_full_name=provider_reviewed_by_full_name,
            provider_reviewed_by_username=provider_reviewed_by_username,
            provider_reviewed_at=provider_reviewed_at,
            created_by_username=created_by_username,
            created_by_full_name=created_by_full_name,
            created_by_civil_number=created_by_civil_number,
            customer_name=customer_name,
            customer_uuid=customer_uuid,
            customer_slug=customer_slug,
            project_name=project_name,
            project_uuid=project_uuid,
            project_description=project_description,
            project_slug=project_slug,
            old_plan_name=old_plan_name,
            new_plan_name=new_plan_name,
            old_plan_uuid=old_plan_uuid,
            new_plan_uuid=new_plan_uuid,
            old_cost_estimate=old_cost_estimate,
            new_cost_estimate=new_cost_estimate,
            can_terminate=can_terminate,
            fixed_price=fixed_price,
            activation_price=activation_price,
            termination_comment=termination_comment,
            issue=issue,
            plan=plan,
            limits=limits,
            type_=type_,
            callback_url=callback_url,
            backend_id=backend_id,
        )

        order_details.additional_properties = d
        return order_details

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
