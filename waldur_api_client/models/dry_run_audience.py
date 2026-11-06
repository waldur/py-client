from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DryRunAudience")


@_attrs_define
class DryRunAudience:
    """
    Attributes:
        recipient (str):
        actor (Union[None, str]):
        label (str):
        count (int):
        cc_count (Union[Unset, int]): How many were copied (Cc) on the message: on the applicant's mail, the holders of
            the proposal roles the call copies.
    """

    recipient: str
    actor: Union[None, str]
    label: str
    count: int
    cc_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recipient = self.recipient

        actor: Union[None, str]
        actor = self.actor

        label = self.label

        count = self.count

        cc_count = self.cc_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recipient": recipient,
                "actor": actor,
                "label": label,
                "count": count,
            }
        )
        if cc_count is not UNSET:
            field_dict["cc_count"] = cc_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recipient = d.pop("recipient")

        def _parse_actor(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        actor = _parse_actor(d.pop("actor"))

        label = d.pop("label")

        count = d.pop("count")

        cc_count = d.pop("cc_count", UNSET)

        dry_run_audience = cls(
            recipient=recipient,
            actor=actor,
            label=label,
            count=count,
            cc_count=cc_count,
        )

        dry_run_audience.additional_properties = d
        return dry_run_audience

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
