from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.assignment_import_row import AssignmentImportRow
    from ..models.assignment_import_totals import AssignmentImportTotals


T = TypeVar("T", bound="AssignmentImportResponse")


@_attrs_define
class AssignmentImportResponse:
    """
    Attributes:
        dry_run (bool):
        rows (list['AssignmentImportRow']):
        totals (AssignmentImportTotals):
        batch_uuids (list[UUID]): Draft batches created or extended; empty for a dry run
    """

    dry_run: bool
    rows: list["AssignmentImportRow"]
    totals: "AssignmentImportTotals"
    batch_uuids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dry_run = self.dry_run

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        totals = self.totals.to_dict()

        batch_uuids = []
        for batch_uuids_item_data in self.batch_uuids:
            batch_uuids_item = str(batch_uuids_item_data)
            batch_uuids.append(batch_uuids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dry_run": dry_run,
                "rows": rows,
                "totals": totals,
                "batch_uuids": batch_uuids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assignment_import_row import AssignmentImportRow
        from ..models.assignment_import_totals import AssignmentImportTotals

        d = dict(src_dict)
        dry_run = d.pop("dry_run")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = AssignmentImportRow.from_dict(rows_item_data)

            rows.append(rows_item)

        totals = AssignmentImportTotals.from_dict(d.pop("totals"))

        batch_uuids = []
        _batch_uuids = d.pop("batch_uuids")
        for batch_uuids_item_data in _batch_uuids:
            batch_uuids_item = UUID(batch_uuids_item_data)

            batch_uuids.append(batch_uuids_item)

        assignment_import_response = cls(
            dry_run=dry_run,
            rows=rows,
            totals=totals,
            batch_uuids=batch_uuids,
        )

        assignment_import_response.additional_properties = d
        return assignment_import_response

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
