from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CleanupConsumptionResponse")


@_attrs_define
class CleanupConsumptionResponse:
    """
    Attributes:
        dry_run (bool):
        records_to_delete (int):
        records_deleted (int):
        compensation_items_affected (int):
        invoice_items_affected (int):
        records_kept_issued (int): Records left in place because their charge is on an issued invoice
        records_kept_imported (int): Records left in place because an import settled their month
    """

    dry_run: bool
    records_to_delete: int
    records_deleted: int
    compensation_items_affected: int
    invoice_items_affected: int
    records_kept_issued: int
    records_kept_imported: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dry_run = self.dry_run

        records_to_delete = self.records_to_delete

        records_deleted = self.records_deleted

        compensation_items_affected = self.compensation_items_affected

        invoice_items_affected = self.invoice_items_affected

        records_kept_issued = self.records_kept_issued

        records_kept_imported = self.records_kept_imported

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dry_run": dry_run,
                "records_to_delete": records_to_delete,
                "records_deleted": records_deleted,
                "compensation_items_affected": compensation_items_affected,
                "invoice_items_affected": invoice_items_affected,
                "records_kept_issued": records_kept_issued,
                "records_kept_imported": records_kept_imported,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dry_run = d.pop("dry_run")

        records_to_delete = d.pop("records_to_delete")

        records_deleted = d.pop("records_deleted")

        compensation_items_affected = d.pop("compensation_items_affected")

        invoice_items_affected = d.pop("invoice_items_affected")

        records_kept_issued = d.pop("records_kept_issued")

        records_kept_imported = d.pop("records_kept_imported")

        cleanup_consumption_response = cls(
            dry_run=dry_run,
            records_to_delete=records_to_delete,
            records_deleted=records_deleted,
            compensation_items_affected=compensation_items_affected,
            invoice_items_affected=invoice_items_affected,
            records_kept_issued=records_kept_issued,
            records_kept_imported=records_kept_imported,
        )

        cleanup_consumption_response.additional_properties = d
        return cleanup_consumption_response

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
