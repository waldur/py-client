from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.offering_state import OfferingState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_provider_plan import BaseProviderPlan
    from ..models.merged_secret_options import MergedSecretOptions
    from ..models.nested_price_estimate import NestedPriceEstimate
    from ..models.offering_component import OfferingComponent


T = TypeVar("T", bound="ProviderOffering")


@_attrs_define
class ProviderOffering:
    """
    Attributes:
        uuid (UUID):
        customer_uuid (UUID):
        name (str):
        slug (str):
        category_title (str):
        type_ (str):
        state (OfferingState):
        resources_count (int):
        billing_price_estimate (NestedPriceEstimate):
        secret_options (MergedSecretOptions):
        components (Union[Unset, list['OfferingComponent']]):
        plans (Union[Unset, list['BaseProviderPlan']]):
        options (Union[Unset, Any]): Fields describing resource provision form.
        resource_options (Union[Unset, Any]): Fields describing resource report form.
    """

    uuid: UUID
    customer_uuid: UUID
    name: str
    slug: str
    category_title: str
    type_: str
    state: OfferingState
    resources_count: int
    billing_price_estimate: "NestedPriceEstimate"
    secret_options: "MergedSecretOptions"
    components: Union[Unset, list["OfferingComponent"]] = UNSET
    plans: Union[Unset, list["BaseProviderPlan"]] = UNSET
    options: Union[Unset, Any] = UNSET
    resource_options: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        customer_uuid = str(self.customer_uuid)

        name = self.name

        slug = self.slug

        category_title = self.category_title

        type_ = self.type_

        state = self.state.value

        resources_count = self.resources_count

        billing_price_estimate = self.billing_price_estimate.to_dict()

        secret_options = self.secret_options.to_dict()

        components: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)

        plans: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plans, Unset):
            plans = []
            for plans_item_data in self.plans:
                plans_item = plans_item_data.to_dict()
                plans.append(plans_item)

        options = self.options

        resource_options = self.resource_options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "customer_uuid": customer_uuid,
                "name": name,
                "slug": slug,
                "category_title": category_title,
                "type": type_,
                "state": state,
                "resources_count": resources_count,
                "billing_price_estimate": billing_price_estimate,
                "secret_options": secret_options,
            }
        )
        if components is not UNSET:
            field_dict["components"] = components
        if plans is not UNSET:
            field_dict["plans"] = plans
        if options is not UNSET:
            field_dict["options"] = options
        if resource_options is not UNSET:
            field_dict["resource_options"] = resource_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_provider_plan import BaseProviderPlan
        from ..models.merged_secret_options import MergedSecretOptions
        from ..models.nested_price_estimate import NestedPriceEstimate
        from ..models.offering_component import OfferingComponent

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        customer_uuid = UUID(d.pop("customer_uuid"))

        name = d.pop("name")

        slug = d.pop("slug")

        category_title = d.pop("category_title")

        type_ = d.pop("type")

        state = OfferingState(d.pop("state"))

        resources_count = d.pop("resources_count")

        billing_price_estimate = NestedPriceEstimate.from_dict(d.pop("billing_price_estimate"))

        secret_options = MergedSecretOptions.from_dict(d.pop("secret_options"))

        components = []
        _components = d.pop("components", UNSET)
        for components_item_data in _components or []:
            components_item = OfferingComponent.from_dict(components_item_data)

            components.append(components_item)

        plans = []
        _plans = d.pop("plans", UNSET)
        for plans_item_data in _plans or []:
            plans_item = BaseProviderPlan.from_dict(plans_item_data)

            plans.append(plans_item)

        options = d.pop("options", UNSET)

        resource_options = d.pop("resource_options", UNSET)

        provider_offering = cls(
            uuid=uuid,
            customer_uuid=customer_uuid,
            name=name,
            slug=slug,
            category_title=category_title,
            type_=type_,
            state=state,
            resources_count=resources_count,
            billing_price_estimate=billing_price_estimate,
            secret_options=secret_options,
            components=components,
            plans=plans,
            options=options,
            resource_options=resource_options,
        )

        provider_offering.additional_properties = d
        return provider_offering

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
