from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_change_kind import WorkflowChangeKind

if TYPE_CHECKING:
    from ..models.workflow_field_change_added_item import WorkflowFieldChangeAddedItem
    from ..models.workflow_field_change_new_type_0 import WorkflowFieldChangeNewType0
    from ..models.workflow_field_change_old_type_0 import WorkflowFieldChangeOldType0
    from ..models.workflow_field_change_removed_item import WorkflowFieldChangeRemovedItem


T = TypeVar("T", bound="WorkflowFieldChange")


@_attrs_define
class WorkflowFieldChange:
    """
    Attributes:
        field (str):
        kind (WorkflowChangeKind):
        old (Union['WorkflowFieldChangeOldType0', None]):
        new (Union['WorkflowFieldChangeNewType0', None]):
        added (list['WorkflowFieldChangeAddedItem']):
        removed (list['WorkflowFieldChangeRemovedItem']):
    """

    field: str
    kind: WorkflowChangeKind
    old: Union["WorkflowFieldChangeOldType0", None]
    new: Union["WorkflowFieldChangeNewType0", None]
    added: list["WorkflowFieldChangeAddedItem"]
    removed: list["WorkflowFieldChangeRemovedItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_field_change_new_type_0 import WorkflowFieldChangeNewType0
        from ..models.workflow_field_change_old_type_0 import WorkflowFieldChangeOldType0

        field = self.field

        kind = self.kind.value

        old: Union[None, dict[str, Any]]
        if isinstance(self.old, WorkflowFieldChangeOldType0):
            old = self.old.to_dict()
        else:
            old = self.old

        new: Union[None, dict[str, Any]]
        if isinstance(self.new, WorkflowFieldChangeNewType0):
            new = self.new.to_dict()
        else:
            new = self.new

        added = []
        for added_item_data in self.added:
            added_item = added_item_data.to_dict()
            added.append(added_item)

        removed = []
        for removed_item_data in self.removed:
            removed_item = removed_item_data.to_dict()
            removed.append(removed_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "kind": kind,
                "old": old,
                "new": new,
                "added": added,
                "removed": removed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_field_change_added_item import WorkflowFieldChangeAddedItem
        from ..models.workflow_field_change_new_type_0 import WorkflowFieldChangeNewType0
        from ..models.workflow_field_change_old_type_0 import WorkflowFieldChangeOldType0
        from ..models.workflow_field_change_removed_item import WorkflowFieldChangeRemovedItem

        d = dict(src_dict)
        field = d.pop("field")

        kind = WorkflowChangeKind(d.pop("kind"))

        def _parse_old(data: object) -> Union["WorkflowFieldChangeOldType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                old_type_0 = WorkflowFieldChangeOldType0.from_dict(data)

                return old_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WorkflowFieldChangeOldType0", None], data)

        old = _parse_old(d.pop("old"))

        def _parse_new(data: object) -> Union["WorkflowFieldChangeNewType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                new_type_0 = WorkflowFieldChangeNewType0.from_dict(data)

                return new_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WorkflowFieldChangeNewType0", None], data)

        new = _parse_new(d.pop("new"))

        added = []
        _added = d.pop("added")
        for added_item_data in _added:
            added_item = WorkflowFieldChangeAddedItem.from_dict(added_item_data)

            added.append(added_item)

        removed = []
        _removed = d.pop("removed")
        for removed_item_data in _removed:
            removed_item = WorkflowFieldChangeRemovedItem.from_dict(removed_item_data)

            removed.append(removed_item)

        workflow_field_change = cls(
            field=field,
            kind=kind,
            old=old,
            new=new,
            added=added,
            removed=removed,
        )

        workflow_field_change.additional_properties = d
        return workflow_field_change

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
