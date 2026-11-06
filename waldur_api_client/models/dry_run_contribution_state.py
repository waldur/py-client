from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DryRunContributionState")


@_attrs_define
class DryRunContributionState:
    """
    Attributes:
        slot (int):
        offering (Union[None, int]):
        label (str):
        status (str):
        outcome (Union[None, str]):
        delegated (bool):
    """

    slot: int
    offering: Union[None, int]
    label: str
    status: str
    outcome: Union[None, str]
    delegated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slot = self.slot

        offering: Union[None, int]
        offering = self.offering

        label = self.label

        status = self.status

        outcome: Union[None, str]
        outcome = self.outcome

        delegated = self.delegated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slot": slot,
                "offering": offering,
                "label": label,
                "status": status,
                "outcome": outcome,
                "delegated": delegated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slot = d.pop("slot")

        def _parse_offering(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        offering = _parse_offering(d.pop("offering"))

        label = d.pop("label")

        status = d.pop("status")

        def _parse_outcome(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        outcome = _parse_outcome(d.pop("outcome"))

        delegated = d.pop("delegated")

        dry_run_contribution_state = cls(
            slot=slot,
            offering=offering,
            label=label,
            status=status,
            outcome=outcome,
            delegated=delegated,
        )

        dry_run_contribution_state.additional_properties = d
        return dry_run_contribution_state

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
