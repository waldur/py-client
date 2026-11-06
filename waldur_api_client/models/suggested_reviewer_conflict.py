from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SuggestedReviewerConflict")


@_attrs_define
class SuggestedReviewerConflict:
    """
    Attributes:
        uuid (UUID):
        status (str):
        coi_type (str):
        severity (str):
    """

    uuid: UUID
    status: str
    coi_type: str
    severity: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        status = self.status

        coi_type = self.coi_type

        severity = self.severity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "status": status,
                "coi_type": coi_type,
                "severity": severity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        status = d.pop("status")

        coi_type = d.pop("coi_type")

        severity = d.pop("severity")

        suggested_reviewer_conflict = cls(
            uuid=uuid,
            status=status,
            coi_type=coi_type,
            severity=severity,
        )

        suggested_reviewer_conflict.additional_properties = d
        return suggested_reviewer_conflict

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
