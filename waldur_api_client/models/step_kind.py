from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.call_step_kind_enum import CallStepKindEnum

if TYPE_CHECKING:
    from ..models.step_kind_notification_rule import StepKindNotificationRule
    from ..models.step_outcome_set import StepOutcomeSet


T = TypeVar("T", bound="StepKind")


@_attrs_define
class StepKind:
    """
    Attributes:
        id (CallStepKindEnum):
        name (str):
        description (str):
        outcome_sets (list['StepOutcomeSet']):
        default_outcome_set (str):
        default_completer (str):
        config_fields (list[str]):
        default_notification_rules (list['StepKindNotificationRule']):
        applicant_facing (bool):
    """

    id: CallStepKindEnum
    name: str
    description: str
    outcome_sets: list["StepOutcomeSet"]
    default_outcome_set: str
    default_completer: str
    config_fields: list[str]
    default_notification_rules: list["StepKindNotificationRule"]
    applicant_facing: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id.value

        name = self.name

        description = self.description

        outcome_sets = []
        for outcome_sets_item_data in self.outcome_sets:
            outcome_sets_item = outcome_sets_item_data.to_dict()
            outcome_sets.append(outcome_sets_item)

        default_outcome_set = self.default_outcome_set

        default_completer = self.default_completer

        config_fields = self.config_fields

        default_notification_rules = []
        for default_notification_rules_item_data in self.default_notification_rules:
            default_notification_rules_item = default_notification_rules_item_data.to_dict()
            default_notification_rules.append(default_notification_rules_item)

        applicant_facing = self.applicant_facing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "outcome_sets": outcome_sets,
                "default_outcome_set": default_outcome_set,
                "default_completer": default_completer,
                "config_fields": config_fields,
                "default_notification_rules": default_notification_rules,
                "applicant_facing": applicant_facing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_kind_notification_rule import StepKindNotificationRule
        from ..models.step_outcome_set import StepOutcomeSet

        d = dict(src_dict)
        id = CallStepKindEnum(d.pop("id"))

        name = d.pop("name")

        description = d.pop("description")

        outcome_sets = []
        _outcome_sets = d.pop("outcome_sets")
        for outcome_sets_item_data in _outcome_sets:
            outcome_sets_item = StepOutcomeSet.from_dict(outcome_sets_item_data)

            outcome_sets.append(outcome_sets_item)

        default_outcome_set = d.pop("default_outcome_set")

        default_completer = d.pop("default_completer")

        config_fields = cast(list[str], d.pop("config_fields"))

        default_notification_rules = []
        _default_notification_rules = d.pop("default_notification_rules")
        for default_notification_rules_item_data in _default_notification_rules:
            default_notification_rules_item = StepKindNotificationRule.from_dict(default_notification_rules_item_data)

            default_notification_rules.append(default_notification_rules_item)

        applicant_facing = d.pop("applicant_facing")

        step_kind = cls(
            id=id,
            name=name,
            description=description,
            outcome_sets=outcome_sets,
            default_outcome_set=default_outcome_set,
            default_completer=default_completer,
            config_fields=config_fields,
            default_notification_rules=default_notification_rules,
            applicant_facing=applicant_facing,
        )

        step_kind.additional_properties = d
        return step_kind

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
