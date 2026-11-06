from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendInvitationsResponse")


@_attrs_define
class SendInvitationsResponse:
    """
    Attributes:
        invitations_sent (int):
        skipped (Union[Unset, list[str]]): Confirmed suggestions left uninvited, and why: their reviewer is no longer in
            good standing, or outside the call's reviewer eligibility.
    """

    invitations_sent: int
    skipped: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invitations_sent = self.invitations_sent

        skipped: Union[Unset, list[str]] = UNSET
        if not isinstance(self.skipped, Unset):
            skipped = self.skipped

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invitations_sent": invitations_sent,
            }
        )
        if skipped is not UNSET:
            field_dict["skipped"] = skipped

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invitations_sent = d.pop("invitations_sent")

        skipped = cast(list[str], d.pop("skipped", UNSET))

        send_invitations_response = cls(
            invitations_sent=invitations_sent,
            skipped=skipped,
        )

        send_invitations_response.additional_properties = d
        return send_invitations_response

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
