from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwardedProposal")


@_attrs_define
class AwardedProposal:
    """
    Attributes:
        proposal_uuid (Union[Unset, UUID]):
        proposal_name (Union[Unset, str]):
        call_uuid (Union[Unset, UUID]):
        call_name (Union[Unset, str]):
        round_uuid (Union[Unset, UUID]):
        round_name (Union[Unset, str]):
        can_read (Union[Unset, bool]): Whether the viewer may open the proposal: its team and the call's overseers do; a
            collaborator added to the project later sees only where it came from.
    """

    proposal_uuid: Union[Unset, UUID] = UNSET
    proposal_name: Union[Unset, str] = UNSET
    call_uuid: Union[Unset, UUID] = UNSET
    call_name: Union[Unset, str] = UNSET
    round_uuid: Union[Unset, UUID] = UNSET
    round_name: Union[Unset, str] = UNSET
    can_read: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.proposal_uuid, Unset):
            proposal_uuid = str(self.proposal_uuid)

        proposal_name = self.proposal_name

        call_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.call_uuid, Unset):
            call_uuid = str(self.call_uuid)

        call_name = self.call_name

        round_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.round_uuid, Unset):
            round_uuid = str(self.round_uuid)

        round_name = self.round_name

        can_read = self.can_read

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proposal_uuid is not UNSET:
            field_dict["proposal_uuid"] = proposal_uuid
        if proposal_name is not UNSET:
            field_dict["proposal_name"] = proposal_name
        if call_uuid is not UNSET:
            field_dict["call_uuid"] = call_uuid
        if call_name is not UNSET:
            field_dict["call_name"] = call_name
        if round_uuid is not UNSET:
            field_dict["round_uuid"] = round_uuid
        if round_name is not UNSET:
            field_dict["round_name"] = round_name
        if can_read is not UNSET:
            field_dict["can_read"] = can_read

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _proposal_uuid = d.pop("proposal_uuid", UNSET)
        proposal_uuid: Union[Unset, UUID]
        if isinstance(_proposal_uuid, Unset):
            proposal_uuid = UNSET
        else:
            proposal_uuid = UUID(_proposal_uuid)

        proposal_name = d.pop("proposal_name", UNSET)

        _call_uuid = d.pop("call_uuid", UNSET)
        call_uuid: Union[Unset, UUID]
        if isinstance(_call_uuid, Unset):
            call_uuid = UNSET
        else:
            call_uuid = UUID(_call_uuid)

        call_name = d.pop("call_name", UNSET)

        _round_uuid = d.pop("round_uuid", UNSET)
        round_uuid: Union[Unset, UUID]
        if isinstance(_round_uuid, Unset):
            round_uuid = UNSET
        else:
            round_uuid = UUID(_round_uuid)

        round_name = d.pop("round_name", UNSET)

        can_read = d.pop("can_read", UNSET)

        awarded_proposal = cls(
            proposal_uuid=proposal_uuid,
            proposal_name=proposal_name,
            call_uuid=call_uuid,
            call_name=call_name,
            round_uuid=round_uuid,
            round_name=round_name,
            can_read=can_read,
        )

        awarded_proposal.additional_properties = d
        return awarded_proposal

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
