from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_description_ref import WorkflowDescriptionRef
    from ..models.workflow_description_trigger import WorkflowDescriptionTrigger


T = TypeVar("T", bound="WorkflowDescriptionNotifiedCell")


@_attrs_define
class WorkflowDescriptionNotifiedCell:
    """
    Attributes:
        value (bool):
        triggers (list['WorkflowDescriptionTrigger']):
        because (list['WorkflowDescriptionRef']):
    """

    value: bool
    triggers: list["WorkflowDescriptionTrigger"]
    because: list["WorkflowDescriptionRef"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        triggers = []
        for triggers_item_data in self.triggers:
            triggers_item = triggers_item_data.to_dict()
            triggers.append(triggers_item)

        because = []
        for because_item_data in self.because:
            because_item = because_item_data.to_dict()
            because.append(because_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "triggers": triggers,
                "because": because,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_description_ref import WorkflowDescriptionRef
        from ..models.workflow_description_trigger import WorkflowDescriptionTrigger

        d = dict(src_dict)
        value = d.pop("value")

        triggers = []
        _triggers = d.pop("triggers")
        for triggers_item_data in _triggers:
            triggers_item = WorkflowDescriptionTrigger.from_dict(triggers_item_data)

            triggers.append(triggers_item)

        because = []
        _because = d.pop("because")
        for because_item_data in _because:
            because_item = WorkflowDescriptionRef.from_dict(because_item_data)

            because.append(because_item)

        workflow_description_notified_cell = cls(
            value=value,
            triggers=triggers,
            because=because,
        )

        workflow_description_notified_cell.additional_properties = d
        return workflow_description_notified_cell

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
