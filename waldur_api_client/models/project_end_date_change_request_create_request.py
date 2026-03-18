import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ProjectEndDateChangeRequestCreateRequest")


@_attrs_define
class ProjectEndDateChangeRequestCreateRequest:
    """
    Attributes:
        project (str):
        requested_end_date (datetime.date): The requested new end date for the project
    """

    project: str
    requested_end_date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project = self.project

        requested_end_date = self.requested_end_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project": project,
                "requested_end_date": requested_end_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project = d.pop("project")

        requested_end_date = isoparse(d.pop("requested_end_date")).date()

        project_end_date_change_request_create_request = cls(
            project=project,
            requested_end_date=requested_end_date,
        )

        project_end_date_change_request_create_request.additional_properties = d
        return project_end_date_change_request_create_request

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
