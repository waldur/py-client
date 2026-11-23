import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.billing_changes_response_result_type_0 import BillingChangesResponseResultType0
    from ..models.billing_invoice_change import BillingInvoiceChange


T = TypeVar("T", bound="BillingChangesResponse")


@_attrs_define
class BillingChangesResponse:
    """
    Attributes:
        action (str):
        year (int):
        month (int):
        resource_uuid (Union[None, str]):
        dry_run (bool):
        taken_at (datetime.datetime):
        result (Union['BillingChangesResponseResultType0', None]): What the underlying task reported.
        invoices (list['BillingInvoiceChange']):
        problems (list[str]): Warnings and errors the run logged, such as a failed Arrow call.
    """

    action: str
    year: int
    month: int
    resource_uuid: Union[None, str]
    dry_run: bool
    taken_at: datetime.datetime
    result: Union["BillingChangesResponseResultType0", None]
    invoices: list["BillingInvoiceChange"]
    problems: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_changes_response_result_type_0 import BillingChangesResponseResultType0

        action = self.action

        year = self.year

        month = self.month

        resource_uuid: Union[None, str]
        resource_uuid = self.resource_uuid

        dry_run = self.dry_run

        taken_at = self.taken_at.isoformat()

        result: Union[None, dict[str, Any]]
        if isinstance(self.result, BillingChangesResponseResultType0):
            result = self.result.to_dict()
        else:
            result = self.result

        invoices = []
        for invoices_item_data in self.invoices:
            invoices_item = invoices_item_data.to_dict()
            invoices.append(invoices_item)

        problems = self.problems

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "year": year,
                "month": month,
                "resource_uuid": resource_uuid,
                "dry_run": dry_run,
                "taken_at": taken_at,
                "result": result,
                "invoices": invoices,
                "problems": problems,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_changes_response_result_type_0 import BillingChangesResponseResultType0
        from ..models.billing_invoice_change import BillingInvoiceChange

        d = dict(src_dict)
        action = d.pop("action")

        year = d.pop("year")

        month = d.pop("month")

        def _parse_resource_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        resource_uuid = _parse_resource_uuid(d.pop("resource_uuid"))

        dry_run = d.pop("dry_run")

        taken_at = isoparse(d.pop("taken_at"))

        def _parse_result(data: object) -> Union["BillingChangesResponseResultType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_0 = BillingChangesResponseResultType0.from_dict(data)

                return result_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BillingChangesResponseResultType0", None], data)

        result = _parse_result(d.pop("result"))

        invoices = []
        _invoices = d.pop("invoices")
        for invoices_item_data in _invoices:
            invoices_item = BillingInvoiceChange.from_dict(invoices_item_data)

            invoices.append(invoices_item)

        problems = cast(list[str], d.pop("problems"))

        billing_changes_response = cls(
            action=action,
            year=year,
            month=month,
            resource_uuid=resource_uuid,
            dry_run=dry_run,
            taken_at=taken_at,
            result=result,
            invoices=invoices,
            problems=problems,
        )

        billing_changes_response.additional_properties = d
        return billing_changes_response

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
