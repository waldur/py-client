from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.offering_team_person import OfferingTeamPerson


T = TypeVar("T", bound="OfferingTeam")


@_attrs_define
class OfferingTeam:
    """
    Attributes:
        managers (list['OfferingTeamPerson']): The offering's managers: they do the team's part of each step.
        delegates (list['OfferingTeamPerson']): Everyone else with a role on the offering: a slot of a step that may be
            handed within the team can be handed to them.
    """

    managers: list["OfferingTeamPerson"]
    delegates: list["OfferingTeamPerson"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        managers = []
        for managers_item_data in self.managers:
            managers_item = managers_item_data.to_dict()
            managers.append(managers_item)

        delegates = []
        for delegates_item_data in self.delegates:
            delegates_item = delegates_item_data.to_dict()
            delegates.append(delegates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "managers": managers,
                "delegates": delegates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_team_person import OfferingTeamPerson

        d = dict(src_dict)
        managers = []
        _managers = d.pop("managers")
        for managers_item_data in _managers:
            managers_item = OfferingTeamPerson.from_dict(managers_item_data)

            managers.append(managers_item)

        delegates = []
        _delegates = d.pop("delegates")
        for delegates_item_data in _delegates:
            delegates_item = OfferingTeamPerson.from_dict(delegates_item_data)

            delegates.append(delegates_item)

        offering_team = cls(
            managers=managers,
            delegates=delegates,
        )

        offering_team.additional_properties = d
        return offering_team

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
