from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.call_step_kind_enum import CallStepKindEnum
from ..models.team_part_enum import TeamPartEnum
from ..models.workflow_phase_enum import WorkflowPhaseEnum

T = TypeVar("T", bound="OfferingTeamStep")


@_attrs_define
class OfferingTeamStep:
    """
    Attributes:
        uuid (UUID):
        key (str):
        name (str):
        description (str):
        kind (CallStepKindEnum):
        phase (WorkflowPhaseEnum):
        order (int):
        duration_in_days (Union[None, int]):
        team_part (TeamPartEnum):
        per_requested_offering (bool): One contribution per requested offering.
        delegable_within_team (bool): A slot of the step can be handed on to anyone on the offering's team.
        notification_triggers (list[str]): Events of the step the call mails the offering's team about, as notification
            rule triggers (step_started, deadline_approaching, ...).
    """

    uuid: UUID
    key: str
    name: str
    description: str
    kind: CallStepKindEnum
    phase: WorkflowPhaseEnum
    order: int
    duration_in_days: Union[None, int]
    team_part: TeamPartEnum
    per_requested_offering: bool
    delegable_within_team: bool
    notification_triggers: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        key = self.key

        name = self.name

        description = self.description

        kind = self.kind.value

        phase = self.phase.value

        order = self.order

        duration_in_days: Union[None, int]
        duration_in_days = self.duration_in_days

        team_part = self.team_part.value

        per_requested_offering = self.per_requested_offering

        delegable_within_team = self.delegable_within_team

        notification_triggers = self.notification_triggers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "key": key,
                "name": name,
                "description": description,
                "kind": kind,
                "phase": phase,
                "order": order,
                "duration_in_days": duration_in_days,
                "team_part": team_part,
                "per_requested_offering": per_requested_offering,
                "delegable_within_team": delegable_within_team,
                "notification_triggers": notification_triggers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        key = d.pop("key")

        name = d.pop("name")

        description = d.pop("description")

        kind = CallStepKindEnum(d.pop("kind"))

        phase = WorkflowPhaseEnum(d.pop("phase"))

        order = d.pop("order")

        def _parse_duration_in_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        duration_in_days = _parse_duration_in_days(d.pop("duration_in_days"))

        team_part = TeamPartEnum(d.pop("team_part"))

        per_requested_offering = d.pop("per_requested_offering")

        delegable_within_team = d.pop("delegable_within_team")

        notification_triggers = cast(list[str], d.pop("notification_triggers"))

        offering_team_step = cls(
            uuid=uuid,
            key=key,
            name=name,
            description=description,
            kind=kind,
            phase=phase,
            order=order,
            duration_in_days=duration_in_days,
            team_part=team_part,
            per_requested_offering=per_requested_offering,
            delegable_within_team=delegable_within_team,
            notification_triggers=notification_triggers,
        )

        offering_team_step.additional_properties = d
        return offering_team_step

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
