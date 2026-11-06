from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DryRunLogEntry")


@_attrs_define
class DryRunLogEntry:
    """
    Attributes:
        index (int):
        action (Union[None, int]):
        day (int):
        kind (str):
        step (Union[None, str]):
        step_name (Union[None, str]):
        text (str):
        outcome (Union[None, Unset, str]):
        message (Union[None, Unset, int]):
    """

    index: int
    action: Union[None, int]
    day: int
    kind: str
    step: Union[None, str]
    step_name: Union[None, str]
    text: str
    outcome: Union[None, Unset, str] = UNSET
    message: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        action: Union[None, int]
        action = self.action

        day = self.day

        kind = self.kind

        step: Union[None, str]
        step = self.step

        step_name: Union[None, str]
        step_name = self.step_name

        text = self.text

        outcome: Union[None, Unset, str]
        if isinstance(self.outcome, Unset):
            outcome = UNSET
        else:
            outcome = self.outcome

        message: Union[None, Unset, int]
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "action": action,
                "day": day,
                "kind": kind,
                "step": step,
                "step_name": step_name,
                "text": text,
            }
        )
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index")

        def _parse_action(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        action = _parse_action(d.pop("action"))

        day = d.pop("day")

        kind = d.pop("kind")

        def _parse_step(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        step = _parse_step(d.pop("step"))

        def _parse_step_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        step_name = _parse_step_name(d.pop("step_name"))

        text = d.pop("text")

        def _parse_outcome(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        outcome = _parse_outcome(d.pop("outcome", UNSET))

        def _parse_message(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        message = _parse_message(d.pop("message", UNSET))

        dry_run_log_entry = cls(
            index=index,
            action=action,
            day=day,
            kind=kind,
            step=step,
            step_name=step_name,
            text=text,
            outcome=outcome,
            message=message,
        )

        dry_run_log_entry.additional_properties = d
        return dry_run_log_entry

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
