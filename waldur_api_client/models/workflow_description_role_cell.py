from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_description_flag_cell import WorkflowDescriptionFlagCell
    from ..models.workflow_description_notified_cell import WorkflowDescriptionNotifiedCell


T = TypeVar("T", bound="WorkflowDescriptionRoleCell")


@_attrs_define
class WorkflowDescriptionRoleCell:
    """
    Attributes:
        actor (str): Key of the actor.
        sees (WorkflowDescriptionFlagCell):
        reads_outputs (WorkflowDescriptionFlagCell):
        contributes (WorkflowDescriptionFlagCell):
        completes (WorkflowDescriptionFlagCell):
        notified (WorkflowDescriptionNotifiedCell):
    """

    actor: str
    sees: "WorkflowDescriptionFlagCell"
    reads_outputs: "WorkflowDescriptionFlagCell"
    contributes: "WorkflowDescriptionFlagCell"
    completes: "WorkflowDescriptionFlagCell"
    notified: "WorkflowDescriptionNotifiedCell"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actor = self.actor

        sees = self.sees.to_dict()

        reads_outputs = self.reads_outputs.to_dict()

        contributes = self.contributes.to_dict()

        completes = self.completes.to_dict()

        notified = self.notified.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actor": actor,
                "sees": sees,
                "reads_outputs": reads_outputs,
                "contributes": contributes,
                "completes": completes,
                "notified": notified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_description_flag_cell import WorkflowDescriptionFlagCell
        from ..models.workflow_description_notified_cell import WorkflowDescriptionNotifiedCell

        d = dict(src_dict)
        actor = d.pop("actor")

        sees = WorkflowDescriptionFlagCell.from_dict(d.pop("sees"))

        reads_outputs = WorkflowDescriptionFlagCell.from_dict(d.pop("reads_outputs"))

        contributes = WorkflowDescriptionFlagCell.from_dict(d.pop("contributes"))

        completes = WorkflowDescriptionFlagCell.from_dict(d.pop("completes"))

        notified = WorkflowDescriptionNotifiedCell.from_dict(d.pop("notified"))

        workflow_description_role_cell = cls(
            actor=actor,
            sees=sees,
            reads_outputs=reads_outputs,
            contributes=contributes,
            completes=completes,
            notified=notified,
        )

        workflow_description_role_cell.additional_properties = d
        return workflow_description_role_cell

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
