from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.demo_preset_preview_project import DemoPresetPreviewProject


T = TypeVar("T", bound="DemoPresetPreviewOrganization")


@_attrs_define
class DemoPresetPreviewOrganization:
    """
    Attributes:
        name (str):
        projects (list['DemoPresetPreviewProject']):
    """

    name: str
    projects: list["DemoPresetPreviewProject"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "projects": projects,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.demo_preset_preview_project import DemoPresetPreviewProject

        d = dict(src_dict)
        name = d.pop("name")

        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = DemoPresetPreviewProject.from_dict(projects_item_data)

            projects.append(projects_item)

        demo_preset_preview_organization = cls(
            name=name,
            projects=projects,
        )

        demo_preset_preview_organization.additional_properties = d
        return demo_preset_preview_organization

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
