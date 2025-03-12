import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.billing_unit import BillingUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_item_details import InvoiceItemDetails


T = TypeVar("T", bound="InvoiceItem")


@_attrs_define
class InvoiceItem:
    """
    Attributes:
        uuid (UUID):
        url (str):
        price (float):
        tax (str):
        total (str):
        factor (int):
        measured_unit (str):
        project_name (str):
        project_uuid (UUID):
        details (InvoiceItemDetails):
        resource_uuid (UUID):
        resource_name (str):
        billing_type (str):
        backend_uuid (Union[None, UUID]):
        credit (bool):
        name (Union[Unset, str]):
        unit_price (Union[Unset, str]):
        unit (Union[Unset, BillingUnit]):
        start (Union[Unset, datetime.datetime]): Date and time when item usage has started.
        end (Union[Unset, datetime.datetime]): Date and time when item usage has ended.
        article_code (Union[Unset, str]):
        quantity (Union[Unset, str]):
        resource (Union[None, Unset, str]):
    """

    uuid: UUID
    url: str
    price: float
    tax: str
    total: str
    factor: int
    measured_unit: str
    project_name: str
    project_uuid: UUID
    details: "InvoiceItemDetails"
    resource_uuid: UUID
    resource_name: str
    billing_type: str
    backend_uuid: Union[None, UUID]
    credit: bool
    name: Union[Unset, str] = UNSET
    unit_price: Union[Unset, str] = UNSET
    unit: Union[Unset, BillingUnit] = UNSET
    start: Union[Unset, datetime.datetime] = UNSET
    end: Union[Unset, datetime.datetime] = UNSET
    article_code: Union[Unset, str] = UNSET
    quantity: Union[Unset, str] = UNSET
    resource: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        url = self.url

        price = self.price

        tax = self.tax

        total = self.total

        factor = self.factor

        measured_unit = self.measured_unit

        project_name = self.project_name

        project_uuid = str(self.project_uuid)

        details = self.details.to_dict()

        resource_uuid = str(self.resource_uuid)

        resource_name = self.resource_name

        billing_type = self.billing_type

        backend_uuid: Union[None, str]
        if isinstance(self.backend_uuid, UUID):
            backend_uuid = str(self.backend_uuid)
        else:
            backend_uuid = self.backend_uuid

        credit = self.credit

        name = self.name

        unit_price = self.unit_price

        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: Union[Unset, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        article_code = self.article_code

        quantity = self.quantity

        resource: Union[None, Unset, str]
        if isinstance(self.resource, Unset):
            resource = UNSET
        else:
            resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "url": url,
                "price": price,
                "tax": tax,
                "total": total,
                "factor": factor,
                "measured_unit": measured_unit,
                "project_name": project_name,
                "project_uuid": project_uuid,
                "details": details,
                "resource_uuid": resource_uuid,
                "resource_name": resource_name,
                "billing_type": billing_type,
                "backend_uuid": backend_uuid,
                "credit": credit,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price
        if unit is not UNSET:
            field_dict["unit"] = unit
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if article_code is not UNSET:
            field_dict["article_code"] = article_code
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.invoice_item_details import InvoiceItemDetails

        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        url = d.pop("url")

        price = d.pop("price")

        tax = d.pop("tax")

        total = d.pop("total")

        factor = d.pop("factor")

        measured_unit = d.pop("measured_unit")

        project_name = d.pop("project_name")

        project_uuid = UUID(d.pop("project_uuid"))

        details = InvoiceItemDetails.from_dict(d.pop("details"))

        resource_uuid = UUID(d.pop("resource_uuid"))

        resource_name = d.pop("resource_name")

        billing_type = d.pop("billing_type")

        def _parse_backend_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backend_uuid_type_0 = UUID(data)

                return backend_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        backend_uuid = _parse_backend_uuid(d.pop("backend_uuid"))

        credit = d.pop("credit")

        name = d.pop("name", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, BillingUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = BillingUnit(_unit)

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

        article_code = d.pop("article_code", UNSET)

        quantity = d.pop("quantity", UNSET)

        def _parse_resource(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resource = _parse_resource(d.pop("resource", UNSET))

        invoice_item = cls(
            uuid=uuid,
            url=url,
            price=price,
            tax=tax,
            total=total,
            factor=factor,
            measured_unit=measured_unit,
            project_name=project_name,
            project_uuid=project_uuid,
            details=details,
            resource_uuid=resource_uuid,
            resource_name=resource_name,
            billing_type=billing_type,
            backend_uuid=backend_uuid,
            credit=credit,
            name=name,
            unit_price=unit_price,
            unit=unit,
            start=start,
            end=end,
            article_code=article_code,
            quantity=quantity,
            resource=resource,
        )

        invoice_item.additional_properties = d
        return invoice_item

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
