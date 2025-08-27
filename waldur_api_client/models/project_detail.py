from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProjectDetail")


@_attrs_define
class ProjectDetail:
    """
    Attributes:
        project_uuid (UUID):
        project_name (str):
        completion_percentage (float):
        is_completed (bool):
        requires_review (bool):
    """

    project_uuid: UUID
    project_name: str
    completion_percentage: float
    is_completed: bool
    requires_review: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_uuid = str(self.project_uuid)

        project_name = self.project_name

        completion_percentage = self.completion_percentage

        is_completed = self.is_completed

        requires_review = self.requires_review

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_uuid": project_uuid,
                "project_name": project_name,
                "completion_percentage": completion_percentage,
                "is_completed": is_completed,
                "requires_review": requires_review,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_uuid = UUID(d.pop("project_uuid"))

        project_name = d.pop("project_name")

        completion_percentage = d.pop("completion_percentage")

        is_completed = d.pop("is_completed")

        requires_review = d.pop("requires_review")

        project_detail = cls(
            project_uuid=project_uuid,
            project_name=project_name,
            completion_percentage=completion_percentage,
            is_completed=is_completed,
            requires_review=requires_review,
        )

        project_detail.additional_properties = d
        return project_detail

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
