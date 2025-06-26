from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.projects_usages_grouped_by_oecd_usages import ProjectsUsagesGroupedByOecdUsages


T = TypeVar("T", bound="ProjectsUsagesGroupedByOecd")


@_attrs_define
class ProjectsUsagesGroupedByOecd:
    """
    Attributes:
        usages (ProjectsUsagesGroupedByOecdUsages):
    """

    usages: "ProjectsUsagesGroupedByOecdUsages"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        usages = self.usages.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "usages": usages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.projects_usages_grouped_by_oecd_usages import ProjectsUsagesGroupedByOecdUsages

        d = dict(src_dict)
        usages = ProjectsUsagesGroupedByOecdUsages.from_dict(d.pop("usages"))

        projects_usages_grouped_by_oecd = cls(
            usages=usages,
        )

        projects_usages_grouped_by_oecd.additional_properties = d
        return projects_usages_grouped_by_oecd

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
