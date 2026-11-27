import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.renewal_term_enum import RenewalTermEnum

T = TypeVar("T", bound="RenewalEstimateComponent")


@_attrs_define
class RenewalEstimateComponent:
    """
    Attributes:
        component_type (str):
        component_name (str):
        billing_type (str):
        billing_period (Union[None, str]):
        term (Union[None, RenewalTermEnum]): For a prepaid line, the term it covers: the rest of the current term,
            charged for a raised limit, or the extension.
        current_limit (float):
        new_limit (float):
        unit_price (str):
        measured_unit (str):
        period_description (str):
        period_start (Union[None, datetime.date]):
        period_end (Union[None, datetime.date]):
        quantity (Union[None, str]): For a prepaid line, the units charged: limit x months.
        total (str): The line's price before any volume discount.
        discount_percent (str): The volume discount the invoice will give this line, in percent. 0 when there is none,
            or when it is deferred.
        discount_total (str): The volume discount on this line, as a positive amount.
        discount_deferred (bool): A volume discount may apply on the invoice that cannot be priced now, because it is
            aggregated over the organization's resources.
    """

    component_type: str
    component_name: str
    billing_type: str
    billing_period: Union[None, str]
    term: Union[None, RenewalTermEnum]
    current_limit: float
    new_limit: float
    unit_price: str
    measured_unit: str
    period_description: str
    period_start: Union[None, datetime.date]
    period_end: Union[None, datetime.date]
    quantity: Union[None, str]
    total: str
    discount_percent: str
    discount_total: str
    discount_deferred: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_type = self.component_type

        component_name = self.component_name

        billing_type = self.billing_type

        billing_period: Union[None, str]
        billing_period = self.billing_period

        term: Union[None, str]
        if isinstance(self.term, RenewalTermEnum):
            term = self.term.value
        else:
            term = self.term

        current_limit = self.current_limit

        new_limit = self.new_limit

        unit_price = self.unit_price

        measured_unit = self.measured_unit

        period_description = self.period_description

        period_start: Union[None, str]
        if isinstance(self.period_start, datetime.date):
            period_start = self.period_start.isoformat()
        else:
            period_start = self.period_start

        period_end: Union[None, str]
        if isinstance(self.period_end, datetime.date):
            period_end = self.period_end.isoformat()
        else:
            period_end = self.period_end

        quantity: Union[None, str]
        quantity = self.quantity

        total = self.total

        discount_percent = self.discount_percent

        discount_total = self.discount_total

        discount_deferred = self.discount_deferred

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_type": component_type,
                "component_name": component_name,
                "billing_type": billing_type,
                "billing_period": billing_period,
                "term": term,
                "current_limit": current_limit,
                "new_limit": new_limit,
                "unit_price": unit_price,
                "measured_unit": measured_unit,
                "period_description": period_description,
                "period_start": period_start,
                "period_end": period_end,
                "quantity": quantity,
                "total": total,
                "discount_percent": discount_percent,
                "discount_total": discount_total,
                "discount_deferred": discount_deferred,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_type = d.pop("component_type")

        component_name = d.pop("component_name")

        billing_type = d.pop("billing_type")

        def _parse_billing_period(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        billing_period = _parse_billing_period(d.pop("billing_period"))

        def _parse_term(data: object) -> Union[None, RenewalTermEnum]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                term_type_0 = RenewalTermEnum(data)

                return term_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, RenewalTermEnum], data)

        term = _parse_term(d.pop("term"))

        current_limit = d.pop("current_limit")

        new_limit = d.pop("new_limit")

        unit_price = d.pop("unit_price")

        measured_unit = d.pop("measured_unit")

        period_description = d.pop("period_description")

        def _parse_period_start(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_start_type_0 = isoparse(data).date()

                return period_start_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        period_start = _parse_period_start(d.pop("period_start"))

        def _parse_period_end(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_end_type_0 = isoparse(data).date()

                return period_end_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        period_end = _parse_period_end(d.pop("period_end"))

        def _parse_quantity(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        quantity = _parse_quantity(d.pop("quantity"))

        total = d.pop("total")

        discount_percent = d.pop("discount_percent")

        discount_total = d.pop("discount_total")

        discount_deferred = d.pop("discount_deferred")

        renewal_estimate_component = cls(
            component_type=component_type,
            component_name=component_name,
            billing_type=billing_type,
            billing_period=billing_period,
            term=term,
            current_limit=current_limit,
            new_limit=new_limit,
            unit_price=unit_price,
            measured_unit=measured_unit,
            period_description=period_description,
            period_start=period_start,
            period_end=period_end,
            quantity=quantity,
            total=total,
            discount_percent=discount_percent,
            discount_total=discount_total,
            discount_deferred=discount_deferred,
        )

        renewal_estimate_component.additional_properties = d
        return renewal_estimate_component

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
