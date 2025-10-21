from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectRecoveryRequest")


@_attrs_define
class ProjectRecoveryRequest:
    """
    Attributes:
        restore_team_members (Union[Unset, bool]): Whether to automatically restore team members who had access before
            project deletion (staff only) Default: False.
        send_invitations_to_previous_members (Union[Unset, bool]): Whether to send invitations to users who had access
            before project deletion Default: False.
    """

    restore_team_members: Union[Unset, bool] = False
    send_invitations_to_previous_members: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restore_team_members = self.restore_team_members

        send_invitations_to_previous_members = self.send_invitations_to_previous_members

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if restore_team_members is not UNSET:
            field_dict["restore_team_members"] = restore_team_members
        if send_invitations_to_previous_members is not UNSET:
            field_dict["send_invitations_to_previous_members"] = send_invitations_to_previous_members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restore_team_members = d.pop("restore_team_members", UNSET)

        send_invitations_to_previous_members = d.pop("send_invitations_to_previous_members", UNSET)

        project_recovery_request = cls(
            restore_team_members=restore_team_members,
            send_invitations_to_previous_members=send_invitations_to_previous_members,
        )

        project_recovery_request.additional_properties = d
        return project_recovery_request

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
