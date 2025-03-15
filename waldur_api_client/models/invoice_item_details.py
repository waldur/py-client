from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resource_limit_period import ResourceLimitPeriod


T = TypeVar("T", bound="InvoiceItemDetails")


@_attrs_define
class InvoiceItemDetails:
    """
    Attributes:
        resource_name (str):
        resource_uuid (UUID):
        plan_name (str):
        plan_uuid (UUID):
        offering_type (str):
        offering_name (str):
        offering_uuid (UUID):
        service_provider_name (str):
        service_provider_uuid (UUID):
        plan_component_id (int):
        offering_component_type (str):
        offering_component_name (str):
        resource_limit_periods (list['ResourceLimitPeriod']):
    """

    resource_name: str
    resource_uuid: UUID
    plan_name: str
    plan_uuid: UUID
    offering_type: str
    offering_name: str
    offering_uuid: UUID
    service_provider_name: str
    service_provider_uuid: UUID
    plan_component_id: int
    offering_component_type: str
    offering_component_name: str
    resource_limit_periods: list["ResourceLimitPeriod"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_name = self.resource_name

        resource_uuid = str(self.resource_uuid)

        plan_name = self.plan_name

        plan_uuid = str(self.plan_uuid)

        offering_type = self.offering_type

        offering_name = self.offering_name

        offering_uuid = str(self.offering_uuid)

        service_provider_name = self.service_provider_name

        service_provider_uuid = str(self.service_provider_uuid)

        plan_component_id = self.plan_component_id

        offering_component_type = self.offering_component_type

        offering_component_name = self.offering_component_name

        resource_limit_periods = []
        for resource_limit_periods_item_data in self.resource_limit_periods:
            resource_limit_periods_item = resource_limit_periods_item_data.to_dict()
            resource_limit_periods.append(resource_limit_periods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_name": resource_name,
                "resource_uuid": resource_uuid,
                "plan_name": plan_name,
                "plan_uuid": plan_uuid,
                "offering_type": offering_type,
                "offering_name": offering_name,
                "offering_uuid": offering_uuid,
                "service_provider_name": service_provider_name,
                "service_provider_uuid": service_provider_uuid,
                "plan_component_id": plan_component_id,
                "offering_component_type": offering_component_type,
                "offering_component_name": offering_component_name,
                "resource_limit_periods": resource_limit_periods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_limit_period import ResourceLimitPeriod

        d = dict(src_dict)
        resource_name = d.pop("resource_name")

        resource_uuid = UUID(d.pop("resource_uuid"))

        plan_name = d.pop("plan_name")

        plan_uuid = UUID(d.pop("plan_uuid"))

        offering_type = d.pop("offering_type")

        offering_name = d.pop("offering_name")

        offering_uuid = UUID(d.pop("offering_uuid"))

        service_provider_name = d.pop("service_provider_name")

        service_provider_uuid = UUID(d.pop("service_provider_uuid"))

        plan_component_id = d.pop("plan_component_id")

        offering_component_type = d.pop("offering_component_type")

        offering_component_name = d.pop("offering_component_name")

        resource_limit_periods = []
        _resource_limit_periods = d.pop("resource_limit_periods")
        for resource_limit_periods_item_data in _resource_limit_periods:
            resource_limit_periods_item = ResourceLimitPeriod.from_dict(resource_limit_periods_item_data)

            resource_limit_periods.append(resource_limit_periods_item)

        invoice_item_details = cls(
            resource_name=resource_name,
            resource_uuid=resource_uuid,
            plan_name=plan_name,
            plan_uuid=plan_uuid,
            offering_type=offering_type,
            offering_name=offering_name,
            offering_uuid=offering_uuid,
            service_provider_name=service_provider_name,
            service_provider_uuid=service_provider_uuid,
            plan_component_id=plan_component_id,
            offering_component_type=offering_component_type,
            offering_component_name=offering_component_name,
            resource_limit_periods=resource_limit_periods,
        )

        invoice_item_details.additional_properties = d
        return invoice_item_details

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
