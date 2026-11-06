from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DryRunNextStep")


@_attrs_define
class DryRunNextStep:
    """
    Attributes:
        step (str):
        name (str):
        outcomes (list[str]):
        contribution_outcomes (list[str]):
        open_slots (list[int]):
        can_reject (bool):
        can_expire (bool):
        can_request_changes (bool):
        can_cancel_changes (bool):
        can_delegate (bool):
        can_reopen (list[int]):
        can_release (bool):
        round_step (bool): Run once per round: taken with a round_step action.
    """

    step: str
    name: str
    outcomes: list[str]
    contribution_outcomes: list[str]
    open_slots: list[int]
    can_reject: bool
    can_expire: bool
    can_request_changes: bool
    can_cancel_changes: bool
    can_delegate: bool
    can_reopen: list[int]
    can_release: bool
    round_step: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step

        name = self.name

        outcomes = self.outcomes

        contribution_outcomes = self.contribution_outcomes

        open_slots = self.open_slots

        can_reject = self.can_reject

        can_expire = self.can_expire

        can_request_changes = self.can_request_changes

        can_cancel_changes = self.can_cancel_changes

        can_delegate = self.can_delegate

        can_reopen = self.can_reopen

        can_release = self.can_release

        round_step = self.round_step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
                "name": name,
                "outcomes": outcomes,
                "contribution_outcomes": contribution_outcomes,
                "open_slots": open_slots,
                "can_reject": can_reject,
                "can_expire": can_expire,
                "can_request_changes": can_request_changes,
                "can_cancel_changes": can_cancel_changes,
                "can_delegate": can_delegate,
                "can_reopen": can_reopen,
                "can_release": can_release,
                "round_step": round_step,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        step = d.pop("step")

        name = d.pop("name")

        outcomes = cast(list[str], d.pop("outcomes"))

        contribution_outcomes = cast(list[str], d.pop("contribution_outcomes"))

        open_slots = cast(list[int], d.pop("open_slots"))

        can_reject = d.pop("can_reject")

        can_expire = d.pop("can_expire")

        can_request_changes = d.pop("can_request_changes")

        can_cancel_changes = d.pop("can_cancel_changes")

        can_delegate = d.pop("can_delegate")

        can_reopen = cast(list[int], d.pop("can_reopen"))

        can_release = d.pop("can_release")

        round_step = d.pop("round_step")

        dry_run_next_step = cls(
            step=step,
            name=name,
            outcomes=outcomes,
            contribution_outcomes=contribution_outcomes,
            open_slots=open_slots,
            can_reject=can_reject,
            can_expire=can_expire,
            can_request_changes=can_request_changes,
            can_cancel_changes=can_cancel_changes,
            can_delegate=can_delegate,
            can_reopen=can_reopen,
            can_release=can_release,
            round_step=round_step,
        )

        dry_run_next_step.additional_properties = d
        return dry_run_next_step

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
