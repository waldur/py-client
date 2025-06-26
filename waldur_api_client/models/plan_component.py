from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_type_enum import BillingTypeEnum
from ..models.billing_unit import BillingUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanComponent")


@_attrs_define
class PlanComponent:
    """
    Attributes:
        offering_name (str):
        plan_name (str):
        plan_unit (BillingUnit):
        component_name (str): Display name for the measured unit, for example, Floating IP.
        measured_unit (str): Unit of measurement, for example, GB.
        billing_type (BillingTypeEnum):
        amount (Union[Unset, int]):
        price (Union[Unset, str]):
        future_price (Union[None, Unset, str]):
    """

    offering_name: str
    plan_name: str
    plan_unit: BillingUnit
    component_name: str
    measured_unit: str
    billing_type: BillingTypeEnum
    amount: Union[Unset, int] = UNSET
    price: Union[Unset, str] = UNSET
    future_price: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offering_name = self.offering_name

        plan_name = self.plan_name

        plan_unit = self.plan_unit.value

        component_name = self.component_name

        measured_unit = self.measured_unit

        billing_type = self.billing_type.value

        amount = self.amount

        price = self.price

        future_price: Union[None, Unset, str]
        if isinstance(self.future_price, Unset):
            future_price = UNSET
        else:
            future_price = self.future_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offering_name": offering_name,
                "plan_name": plan_name,
                "plan_unit": plan_unit,
                "component_name": component_name,
                "measured_unit": measured_unit,
                "billing_type": billing_type,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if price is not UNSET:
            field_dict["price"] = price
        if future_price is not UNSET:
            field_dict["future_price"] = future_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offering_name = d.pop("offering_name")

        plan_name = d.pop("plan_name")

        plan_unit = BillingUnit(d.pop("plan_unit"))

        component_name = d.pop("component_name")

        measured_unit = d.pop("measured_unit")

        billing_type = BillingTypeEnum(d.pop("billing_type"))

        amount = d.pop("amount", UNSET)

        price = d.pop("price", UNSET)

        def _parse_future_price(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        future_price = _parse_future_price(d.pop("future_price", UNSET))

        plan_component = cls(
            offering_name=offering_name,
            plan_name=plan_name,
            plan_unit=plan_unit,
            component_name=component_name,
            measured_unit=measured_unit,
            billing_type=billing_type,
            amount=amount,
            price=price,
            future_price=future_price,
        )

        plan_component.additional_properties = d
        return plan_component

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
