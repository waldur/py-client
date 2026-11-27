from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_component_field_enum import AgentComponentFieldEnum

T = TypeVar("T", bound="ApplyComponentRequest")


@_attrs_define
class ApplyComponentRequest:
    """
    Attributes:
        component (str):
        field (AgentComponentFieldEnum):
    """

    component: str
    field: AgentComponentFieldEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component = self.component

        field = self.field.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component": component,
                "field": field,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component = d.pop("component")

        field = AgentComponentFieldEnum(d.pop("field"))

        apply_component_request = cls(
            component=component,
            field=field,
        )

        apply_component_request.additional_properties = d
        return apply_component_request

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
