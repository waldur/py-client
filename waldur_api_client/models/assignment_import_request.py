from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="AssignmentImportRequest")


@_attrs_define
class AssignmentImportRequest:
    """
    Attributes:
        round_ (UUID): Round of this call whose proposals the file assigns
        file (File): CSV with a header row: reviewer_email, and proposal_slug or proposal_uuid. UTF-8, at most 1 MB.
        dry_run (Union[Unset, bool]): Report what each row would do and change nothing Default: True.
        override_workload_limit (Union[Unset, bool]): Assign even if this takes reviewers above their maximum number of
            open assignments. The override is logged. Default: False.
        manager_notes (Union[Unset, str]): Optional notes stored on the draft batches
    """

    round_: UUID
    file: File
    dry_run: Union[Unset, bool] = True
    override_workload_limit: Union[Unset, bool] = False
    manager_notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        round_ = str(self.round_)

        file = self.file.to_tuple()

        dry_run = self.dry_run

        override_workload_limit = self.override_workload_limit

        manager_notes = self.manager_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "round": round_,
                "file": file,
            }
        )
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if override_workload_limit is not UNSET:
            field_dict["override_workload_limit"] = override_workload_limit
        if manager_notes is not UNSET:
            field_dict["manager_notes"] = manager_notes

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("round", (None, str(self.round_), "text/plain")))

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.dry_run, Unset):
            files.append(("dry_run", (None, str(self.dry_run).encode(), "text/plain")))

        if not isinstance(self.override_workload_limit, Unset):
            files.append(("override_workload_limit", (None, str(self.override_workload_limit).encode(), "text/plain")))

        if not isinstance(self.manager_notes, Unset):
            files.append(("manager_notes", (None, str(self.manager_notes).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        round_ = UUID(d.pop("round"))

        file = File(payload=BytesIO(d.pop("file")))

        dry_run = d.pop("dry_run", UNSET)

        override_workload_limit = d.pop("override_workload_limit", UNSET)

        manager_notes = d.pop("manager_notes", UNSET)

        assignment_import_request = cls(
            round_=round_,
            file=file,
            dry_run=dry_run,
            override_workload_limit=override_workload_limit,
            manager_notes=manager_notes,
        )

        assignment_import_request.additional_properties = d
        return assignment_import_request

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
