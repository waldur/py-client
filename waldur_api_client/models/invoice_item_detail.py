import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.billing_unit import BillingUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceItemDetail")


@_attrs_define
class InvoiceItemDetail:
    """
    Attributes:
        invoice (str):
        uuid (UUID):
        resource (Union[None, Unset, str]):
        article_code (Union[Unset, str]):
        unit_price (Union[Unset, str]):
        unit (Union[Unset, BillingUnit]):
        quantity (Union[Unset, str]):
        measured_unit (Union[Unset, str]): Unit of measurement, for example, GB.
        name (Union[Unset, str]):
        start (Union[Unset, datetime.datetime]): Date and time when item usage has started.
        end (Union[Unset, datetime.datetime]): Date and time when item usage has ended.
        details (Union[Unset, Any]): Stores data about scope
    """

    invoice: str
    uuid: UUID
    resource: Union[None, Unset, str] = UNSET
    article_code: Union[Unset, str] = UNSET
    unit_price: Union[Unset, str] = UNSET
    unit: Union[Unset, BillingUnit] = UNSET
    quantity: Union[Unset, str] = UNSET
    measured_unit: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    start: Union[Unset, datetime.datetime] = UNSET
    end: Union[Unset, datetime.datetime] = UNSET
    details: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invoice = self.invoice

        uuid = str(self.uuid)

        resource: Union[None, Unset, str]
        if isinstance(self.resource, Unset):
            resource = UNSET
        else:
            resource = self.resource

        article_code = self.article_code

        unit_price = self.unit_price

        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        quantity = self.quantity

        measured_unit = self.measured_unit

        name = self.name

        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: Union[Unset, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoice": invoice,
                "uuid": uuid,
            }
        )
        if resource is not UNSET:
            field_dict["resource"] = resource
        if article_code is not UNSET:
            field_dict["article_code"] = article_code
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price
        if unit is not UNSET:
            field_dict["unit"] = unit
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if measured_unit is not UNSET:
            field_dict["measured_unit"] = measured_unit
        if name is not UNSET:
            field_dict["name"] = name
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invoice = d.pop("invoice")

        uuid = UUID(d.pop("uuid"))

        def _parse_resource(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resource = _parse_resource(d.pop("resource", UNSET))

        article_code = d.pop("article_code", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, BillingUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = BillingUnit(_unit)

        quantity = d.pop("quantity", UNSET)

        measured_unit = d.pop("measured_unit", UNSET)

        name = d.pop("name", UNSET)

        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.datetime]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        _end = d.pop("end", UNSET)
        end: Union[Unset, datetime.datetime]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        details = d.pop("details", UNSET)

        invoice_item_detail = cls(
            invoice=invoice,
            uuid=uuid,
            resource=resource,
            article_code=article_code,
            unit_price=unit_price,
            unit=unit,
            quantity=quantity,
            measured_unit=measured_unit,
            name=name,
            start=start,
            end=end,
            details=details,
        )

        invoice_item_detail.additional_properties = d
        return invoice_item_detail

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
