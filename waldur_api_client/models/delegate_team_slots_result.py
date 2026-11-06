from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delegate_team_slots_result_skipped import DelegateTeamSlotsResultSkipped


T = TypeVar("T", bound="DelegateTeamSlotsResult")


@_attrs_define
class DelegateTeamSlotsResult:
    """
    Attributes:
        handed_on (list[UUID]):
        skipped (DelegateTeamSlotsResultSkipped): Slots left as they were, with why, by uuid.
    """

    handed_on: list[UUID]
    skipped: "DelegateTeamSlotsResultSkipped"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        handed_on = []
        for handed_on_item_data in self.handed_on:
            handed_on_item = str(handed_on_item_data)
            handed_on.append(handed_on_item)

        skipped = self.skipped.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "handed_on": handed_on,
                "skipped": skipped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delegate_team_slots_result_skipped import DelegateTeamSlotsResultSkipped

        d = dict(src_dict)
        handed_on = []
        _handed_on = d.pop("handed_on")
        for handed_on_item_data in _handed_on:
            handed_on_item = UUID(handed_on_item_data)

            handed_on.append(handed_on_item)

        skipped = DelegateTeamSlotsResultSkipped.from_dict(d.pop("skipped"))

        delegate_team_slots_result = cls(
            handed_on=handed_on,
            skipped=skipped,
        )

        delegate_team_slots_result.additional_properties = d
        return delegate_team_slots_result

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
