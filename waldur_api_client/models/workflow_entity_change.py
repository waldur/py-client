from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_change_kind import WorkflowChangeKind
from ..models.workflow_change_type import WorkflowChangeType

if TYPE_CHECKING:
    from ..models.workflow_field_change import WorkflowFieldChange


T = TypeVar("T", bound="WorkflowEntityChange")


@_attrs_define
class WorkflowEntityChange:
    """
    Attributes:
        key (str):
        name (str):
        old_name (Union[None, str]):
        change (WorkflowChangeType):
        kind (WorkflowChangeKind):
        moved (bool): Whether the step's place relative to the others changed.
        fields (list['WorkflowFieldChange']):
    """

    key: str
    name: str
    old_name: Union[None, str]
    change: WorkflowChangeType
    kind: WorkflowChangeKind
    moved: bool
    fields: list["WorkflowFieldChange"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        old_name: Union[None, str]
        old_name = self.old_name

        change = self.change.value

        kind = self.kind.value

        moved = self.moved

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "old_name": old_name,
                "change": change,
                "kind": kind,
                "moved": moved,
                "fields": fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_field_change import WorkflowFieldChange

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        def _parse_old_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        old_name = _parse_old_name(d.pop("old_name"))

        change = WorkflowChangeType(d.pop("change"))

        kind = WorkflowChangeKind(d.pop("kind"))

        moved = d.pop("moved")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = WorkflowFieldChange.from_dict(fields_item_data)

            fields.append(fields_item)

        workflow_entity_change = cls(
            key=key,
            name=name,
            old_name=old_name,
            change=change,
            kind=kind,
            moved=moved,
            fields=fields,
        )

        workflow_entity_change.additional_properties = d
        return workflow_entity_change

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
