from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_description_call_extra import WorkflowDescriptionCallExtra
    from ..models.workflow_description_call_settings import WorkflowDescriptionCallSettings
    from ..models.workflow_description_round import WorkflowDescriptionRound


T = TypeVar("T", bound="WorkflowDescriptionCall")


@_attrs_define
class WorkflowDescriptionCall:
    """
    Attributes:
        name (str):
        state (Union[None, str]):
        template (Union[None, str]):
        settings (WorkflowDescriptionCallSettings):
        target_decision_days (Union[None, int]):
        rounds (list['WorkflowDescriptionRound']):
        extra (WorkflowDescriptionCallExtra):
    """

    name: str
    state: Union[None, str]
    template: Union[None, str]
    settings: "WorkflowDescriptionCallSettings"
    target_decision_days: Union[None, int]
    rounds: list["WorkflowDescriptionRound"]
    extra: "WorkflowDescriptionCallExtra"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        state: Union[None, str]
        state = self.state

        template: Union[None, str]
        template = self.template

        settings = self.settings.to_dict()

        target_decision_days: Union[None, int]
        target_decision_days = self.target_decision_days

        rounds = []
        for rounds_item_data in self.rounds:
            rounds_item = rounds_item_data.to_dict()
            rounds.append(rounds_item)

        extra = self.extra.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "state": state,
                "template": template,
                "settings": settings,
                "target_decision_days": target_decision_days,
                "rounds": rounds,
                "extra": extra,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_description_call_extra import WorkflowDescriptionCallExtra
        from ..models.workflow_description_call_settings import WorkflowDescriptionCallSettings
        from ..models.workflow_description_round import WorkflowDescriptionRound

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_state(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        state = _parse_state(d.pop("state"))

        def _parse_template(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        template = _parse_template(d.pop("template"))

        settings = WorkflowDescriptionCallSettings.from_dict(d.pop("settings"))

        def _parse_target_decision_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        target_decision_days = _parse_target_decision_days(d.pop("target_decision_days"))

        rounds = []
        _rounds = d.pop("rounds")
        for rounds_item_data in _rounds:
            rounds_item = WorkflowDescriptionRound.from_dict(rounds_item_data)

            rounds.append(rounds_item)

        extra = WorkflowDescriptionCallExtra.from_dict(d.pop("extra"))

        workflow_description_call = cls(
            name=name,
            state=state,
            template=template,
            settings=settings,
            target_decision_days=target_decision_days,
            rounds=rounds,
            extra=extra,
        )

        workflow_description_call.additional_properties = d
        return workflow_description_call

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
