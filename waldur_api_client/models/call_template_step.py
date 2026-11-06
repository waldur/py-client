from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_phase_enum import WorkflowPhaseEnum

T = TypeVar("T", bound="CallTemplateStep")


@_attrs_define
class CallTemplateStep:
    """
    Attributes:
        name (str):
        kind (Union[None, str]):
        order (Union[None, int]):
        is_enabled (bool):
        phase (WorkflowPhaseEnum):
    """

    name: str
    kind: Union[None, str]
    order: Union[None, int]
    is_enabled: bool
    phase: WorkflowPhaseEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind: Union[None, str]
        kind = self.kind

        order: Union[None, int]
        order = self.order

        is_enabled = self.is_enabled

        phase = self.phase.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "kind": kind,
                "order": order,
                "is_enabled": is_enabled,
                "phase": phase,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_kind(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        kind = _parse_kind(d.pop("kind"))

        def _parse_order(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        order = _parse_order(d.pop("order"))

        is_enabled = d.pop("is_enabled")

        phase = WorkflowPhaseEnum(d.pop("phase"))

        call_template_step = cls(
            name=name,
            kind=kind,
            order=order,
            is_enabled=is_enabled,
            phase=phase,
        )

        call_template_step.additional_properties = d
        return call_template_step

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
