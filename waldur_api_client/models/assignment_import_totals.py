from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssignmentImportTotals")


@_attrs_define
class AssignmentImportTotals:
    """
    Attributes:
        ready (int):
        created (int):
        coi_blocked (int):
        skipped (int):
        error (int):
    """

    ready: int
    created: int
    coi_blocked: int
    skipped: int
    error: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ready = self.ready

        created = self.created

        coi_blocked = self.coi_blocked

        skipped = self.skipped

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ready": ready,
                "created": created,
                "coi_blocked": coi_blocked,
                "skipped": skipped,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ready = d.pop("ready")

        created = d.pop("created")

        coi_blocked = d.pop("coi_blocked")

        skipped = d.pop("skipped")

        error = d.pop("error")

        assignment_import_totals = cls(
            ready=ready,
            created=created,
            coi_blocked=coi_blocked,
            skipped=skipped,
            error=error,
        )

        assignment_import_totals.additional_properties = d
        return assignment_import_totals

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
