from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_description_coi_declaration_source_enum import WorkflowDescriptionCoiDeclarationSourceEnum

T = TypeVar("T", bound="WorkflowDescriptionCoiDeclaration")


@_attrs_define
class WorkflowDescriptionCoiDeclaration:
    """
    Attributes:
        text (str): The declaration; empty for the platform's standard one.
        source (WorkflowDescriptionCoiDeclarationSourceEnum):
        editable (bool): The call team can edit the wording at any time.
    """

    text: str
    source: WorkflowDescriptionCoiDeclarationSourceEnum
    editable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        source = self.source.value

        editable = self.editable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "source": source,
                "editable": editable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        source = WorkflowDescriptionCoiDeclarationSourceEnum(d.pop("source"))

        editable = d.pop("editable")

        workflow_description_coi_declaration = cls(
            text=text,
            source=source,
            editable=editable,
        )

        workflow_description_coi_declaration.additional_properties = d
        return workflow_description_coi_declaration

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
