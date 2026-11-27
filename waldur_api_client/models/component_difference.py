from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ComponentDifference")


@_attrs_define
class ComponentDifference:
    """
    Attributes:
        component (str):
        field (str):
        offering (Any): The offering component's value; null when it has none.
        imported (Any):
        applicable (bool): Whether apply_components may name this difference.
        reason (Union[None, str]): Why it cannot be applied, when it cannot.
    """

    component: str
    field: str
    offering: Any
    imported: Any
    applicable: bool
    reason: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component = self.component

        field = self.field

        offering = self.offering

        imported = self.imported

        applicable = self.applicable

        reason: Union[None, str]
        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component": component,
                "field": field,
                "offering": offering,
                "imported": imported,
                "applicable": applicable,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component = d.pop("component")

        field = d.pop("field")

        offering = d.pop("offering")

        imported = d.pop("imported")

        applicable = d.pop("applicable")

        def _parse_reason(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        reason = _parse_reason(d.pop("reason"))

        component_difference = cls(
            component=component,
            field=field,
            offering=offering,
            imported=imported,
            applicable=applicable,
            reason=reason,
        )

        component_difference.additional_properties = d
        return component_difference

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
