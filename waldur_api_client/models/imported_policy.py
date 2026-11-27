from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.policy_action_choice import PolicyActionChoice
    from ..models.policy_change import PolicyChange


T = TypeVar("T", bound="ImportedPolicy")


@_attrs_define
class ImportedPolicy:
    """
    Attributes:
        exists (bool): Whether the offering has a SLURM periodic usage policy.
        needs_actions (bool): Whether applying would create the policy, so policy_actions must say what it does.
        action_choices (list['PolicyActionChoice']): The actions a SLURM periodic usage policy can take.
        changes (list['PolicyChange']):
        applicable (bool): Whether apply_policy may be set.
        reason (Union[None, str]): Why it cannot be applied, when it cannot.
    """

    exists: bool
    needs_actions: bool
    action_choices: list["PolicyActionChoice"]
    changes: list["PolicyChange"]
    applicable: bool
    reason: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exists = self.exists

        needs_actions = self.needs_actions

        action_choices = []
        for action_choices_item_data in self.action_choices:
            action_choices_item = action_choices_item_data.to_dict()
            action_choices.append(action_choices_item)

        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)

        applicable = self.applicable

        reason: Union[None, str]
        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exists": exists,
                "needs_actions": needs_actions,
                "action_choices": action_choices,
                "changes": changes,
                "applicable": applicable,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_action_choice import PolicyActionChoice
        from ..models.policy_change import PolicyChange

        d = dict(src_dict)
        exists = d.pop("exists")

        needs_actions = d.pop("needs_actions")

        action_choices = []
        _action_choices = d.pop("action_choices")
        for action_choices_item_data in _action_choices:
            action_choices_item = PolicyActionChoice.from_dict(action_choices_item_data)

            action_choices.append(action_choices_item)

        changes = []
        _changes = d.pop("changes")
        for changes_item_data in _changes:
            changes_item = PolicyChange.from_dict(changes_item_data)

            changes.append(changes_item)

        applicable = d.pop("applicable")

        def _parse_reason(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        reason = _parse_reason(d.pop("reason"))

        imported_policy = cls(
            exists=exists,
            needs_actions=needs_actions,
            action_choices=action_choices,
            changes=changes,
            applicable=applicable,
            reason=reason,
        )

        imported_policy.additional_properties = d
        return imported_policy

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
