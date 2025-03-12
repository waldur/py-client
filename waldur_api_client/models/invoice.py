import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.invoice_state_enum import InvoiceStateEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_details import CustomerDetails
    from ..models.invoice_item import InvoiceItem


T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    """
    Attributes:
        url (str):
        uuid (UUID):
        number (int):
        customer (str):
        price (str):
        tax (str):
        total (str):
        issuer_details (CustomerDetails):
        due_date (datetime.date):
        customer_details (CustomerDetails):
        items (list['InvoiceItem']):
        state (Union[Unset, InvoiceStateEnum]):
        year (Union[Unset, int]):
        month (Union[Unset, int]):
        invoice_date (Union[None, Unset, datetime.date]): Date then invoice moved from state pending to created.
        backend_id (Union[Unset, str]):
        payment_url (Union[Unset, str]): URL for initiating payment via payment gateway.
        reference_number (Union[Unset, str]): Reference number associated with the invoice.
    """

    url: str
    uuid: UUID
    number: int
    customer: str
    price: str
    tax: str
    total: str
    issuer_details: "CustomerDetails"
    due_date: datetime.date
    customer_details: "CustomerDetails"
    items: list["InvoiceItem"]
    state: Union[Unset, InvoiceStateEnum] = UNSET
    year: Union[Unset, int] = UNSET
    month: Union[Unset, int] = UNSET
    invoice_date: Union[None, Unset, datetime.date] = UNSET
    backend_id: Union[Unset, str] = UNSET
    payment_url: Union[Unset, str] = UNSET
    reference_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        number = self.number

        customer = self.customer

        price = self.price

        tax = self.tax

        total = self.total

        issuer_details = self.issuer_details.to_dict()

        due_date = self.due_date.isoformat()

        customer_details = self.customer_details.to_dict()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        year = self.year

        month = self.month

        invoice_date: Union[None, Unset, str]
        if isinstance(self.invoice_date, Unset):
            invoice_date = UNSET
        elif isinstance(self.invoice_date, datetime.date):
            invoice_date = self.invoice_date.isoformat()
        else:
            invoice_date = self.invoice_date

        backend_id = self.backend_id

        payment_url = self.payment_url

        reference_number = self.reference_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "number": number,
                "customer": customer,
                "price": price,
                "tax": tax,
                "total": total,
                "issuer_details": issuer_details,
                "due_date": due_date,
                "customer_details": customer_details,
                "items": items,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state
        if year is not UNSET:
            field_dict["year"] = year
        if month is not UNSET:
            field_dict["month"] = month
        if invoice_date is not UNSET:
            field_dict["invoice_date"] = invoice_date
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if payment_url is not UNSET:
            field_dict["payment_url"] = payment_url
        if reference_number is not UNSET:
            field_dict["reference_number"] = reference_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.customer_details import CustomerDetails
        from ..models.invoice_item import InvoiceItem

        d = src_dict.copy()
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        number = d.pop("number")

        customer = d.pop("customer")

        price = d.pop("price")

        tax = d.pop("tax")

        total = d.pop("total")

        issuer_details = CustomerDetails.from_dict(d.pop("issuer_details"))

        due_date = isoparse(d.pop("due_date")).date()

        customer_details = CustomerDetails.from_dict(d.pop("customer_details"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = InvoiceItem.from_dict(items_item_data)

            items.append(items_item)

        _state = d.pop("state", UNSET)
        state: Union[Unset, InvoiceStateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = InvoiceStateEnum(_state)

        year = d.pop("year", UNSET)

        month = d.pop("month", UNSET)

        def _parse_invoice_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invoice_date_type_0 = isoparse(data).date()

                return invoice_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        invoice_date = _parse_invoice_date(d.pop("invoice_date", UNSET))

        backend_id = d.pop("backend_id", UNSET)

        payment_url = d.pop("payment_url", UNSET)

        reference_number = d.pop("reference_number", UNSET)

        invoice = cls(
            url=url,
            uuid=uuid,
            number=number,
            customer=customer,
            price=price,
            tax=tax,
            total=total,
            issuer_details=issuer_details,
            due_date=due_date,
            customer_details=customer_details,
            items=items,
            state=state,
            year=year,
            month=month,
            invoice_date=invoice_date,
            backend_id=backend_id,
            payment_url=payment_url,
            reference_number=reference_number,
        )

        invoice.additional_properties = d
        return invoice

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
