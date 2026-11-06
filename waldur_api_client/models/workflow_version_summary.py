from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowVersionSummary")


@_attrs_define
class WorkflowVersionSummary:
    """
    Attributes:
        behaviour (Union[Unset, int]):
        cosmetic (Union[Unset, int]):
        steps_added (Union[Unset, int]):
        steps_removed (Union[Unset, int]):
        steps_changed (Union[Unset, int]):
        steps_moved (Union[Unset, int]):
    """

    behaviour: Union[Unset, int] = UNSET
    cosmetic: Union[Unset, int] = UNSET
    steps_added: Union[Unset, int] = UNSET
    steps_removed: Union[Unset, int] = UNSET
    steps_changed: Union[Unset, int] = UNSET
    steps_moved: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        behaviour = self.behaviour

        cosmetic = self.cosmetic

        steps_added = self.steps_added

        steps_removed = self.steps_removed

        steps_changed = self.steps_changed

        steps_moved = self.steps_moved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if behaviour is not UNSET:
            field_dict["behaviour"] = behaviour
        if cosmetic is not UNSET:
            field_dict["cosmetic"] = cosmetic
        if steps_added is not UNSET:
            field_dict["steps_added"] = steps_added
        if steps_removed is not UNSET:
            field_dict["steps_removed"] = steps_removed
        if steps_changed is not UNSET:
            field_dict["steps_changed"] = steps_changed
        if steps_moved is not UNSET:
            field_dict["steps_moved"] = steps_moved

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        behaviour = d.pop("behaviour", UNSET)

        cosmetic = d.pop("cosmetic", UNSET)

        steps_added = d.pop("steps_added", UNSET)

        steps_removed = d.pop("steps_removed", UNSET)

        steps_changed = d.pop("steps_changed", UNSET)

        steps_moved = d.pop("steps_moved", UNSET)

        workflow_version_summary = cls(
            behaviour=behaviour,
            cosmetic=cosmetic,
            steps_added=steps_added,
            steps_removed=steps_removed,
            steps_changed=steps_changed,
            steps_moved=steps_moved,
        )

        workflow_version_summary.additional_properties = d
        return workflow_version_summary

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
