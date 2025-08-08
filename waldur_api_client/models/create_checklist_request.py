from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checklist_type_enum import ChecklistTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateChecklistRequest")


@_attrs_define
class CreateChecklistRequest:
    """
    Attributes:
        name (str):
        checklist_type (ChecklistTypeEnum):
        description (Union[Unset, str]):
    """

    name: str
    checklist_type: ChecklistTypeEnum
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        checklist_type = self.checklist_type.value

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "checklist_type": checklist_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        checklist_type = ChecklistTypeEnum(d.pop("checklist_type"))

        description = d.pop("description", UNSET)

        create_checklist_request = cls(
            name=name,
            checklist_type=checklist_type,
            description=description,
        )

        create_checklist_request.additional_properties = d
        return create_checklist_request

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
