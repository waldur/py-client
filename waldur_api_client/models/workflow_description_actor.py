from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_description_actor_kind_enum import WorkflowDescriptionActorKindEnum

T = TypeVar("T", bound="WorkflowDescriptionActor")


@_attrs_define
class WorkflowDescriptionActor:
    """
    Attributes:
        key (str):
        kind (WorkflowDescriptionActorKindEnum):
        role_key (Union[None, str]):
        label (str):
        notes (list[str]):
        holders (Union[None, int]): How many hold the role on the call; counts only.
    """

    key: str
    kind: WorkflowDescriptionActorKindEnum
    role_key: Union[None, str]
    label: str
    notes: list[str]
    holders: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        kind = self.kind.value

        role_key: Union[None, str]
        role_key = self.role_key

        label = self.label

        notes = self.notes

        holders: Union[None, int]
        holders = self.holders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "kind": kind,
                "role_key": role_key,
                "label": label,
                "notes": notes,
                "holders": holders,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        kind = WorkflowDescriptionActorKindEnum(d.pop("kind"))

        def _parse_role_key(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        role_key = _parse_role_key(d.pop("role_key"))

        label = d.pop("label")

        notes = cast(list[str], d.pop("notes"))

        def _parse_holders(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        holders = _parse_holders(d.pop("holders"))

        workflow_description_actor = cls(
            key=key,
            kind=kind,
            role_key=role_key,
            label=label,
            notes=notes,
            holders=holders,
        )

        workflow_description_actor.additional_properties = d
        return workflow_description_actor

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
