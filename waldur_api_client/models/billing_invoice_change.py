from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.billing_item_change import BillingItemChange


T = TypeVar("T", bound="BillingInvoiceChange")


@_attrs_define
class BillingInvoiceChange:
    """
    Attributes:
        invoice_uuid (str):
        customer_uuid (str):
        customer_name (str):
        year (int):
        month (int):
        state (str):
        total_before (str):
        total_after (str):
        items (list['BillingItemChange']):
    """

    invoice_uuid: str
    customer_uuid: str
    customer_name: str
    year: int
    month: int
    state: str
    total_before: str
    total_after: str
    items: list["BillingItemChange"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invoice_uuid = self.invoice_uuid

        customer_uuid = self.customer_uuid

        customer_name = self.customer_name

        year = self.year

        month = self.month

        state = self.state

        total_before = self.total_before

        total_after = self.total_after

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoice_uuid": invoice_uuid,
                "customer_uuid": customer_uuid,
                "customer_name": customer_name,
                "year": year,
                "month": month,
                "state": state,
                "total_before": total_before,
                "total_after": total_after,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_item_change import BillingItemChange

        d = dict(src_dict)
        invoice_uuid = d.pop("invoice_uuid")

        customer_uuid = d.pop("customer_uuid")

        customer_name = d.pop("customer_name")

        year = d.pop("year")

        month = d.pop("month")

        state = d.pop("state")

        total_before = d.pop("total_before")

        total_after = d.pop("total_after")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = BillingItemChange.from_dict(items_item_data)

            items.append(items_item)

        billing_invoice_change = cls(
            invoice_uuid=invoice_uuid,
            customer_uuid=customer_uuid,
            customer_name=customer_name,
            year=year,
            month=month,
            state=state,
            total_before=total_before,
            total_after=total_after,
            items=items,
        )

        billing_invoice_change.additional_properties = d
        return billing_invoice_change

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
