from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProposalRoleCandidate")


@_attrs_define
class ProposalRoleCandidate:
    """
    Attributes:
        uuid (UUID):
        full_name (str):
        email (Union[None, str]): Shown to staff and those overseeing the call only.
        username (str):
        holds_role (bool): Whether the user already holds the role on the proposal.
        holds_other_role (bool): The user holds another evaluator role on the proposal; one person holds one, so they
            cannot be assigned.
        held_role_name (Union[None, str]): The evaluator role the user holds on the proposal, if any.
        has_recorded_conflict (Union[None, bool]): A conflict of interest is recorded for the user and the proposal;
            they cannot be assigned. Shown to staff and those overseeing the call only, null for anyone else.
        has_reviewer_profile (bool): Without a reviewer profile no conflict can be on record: the user is checked by
            their own declaration only.
    """

    uuid: UUID
    full_name: str
    email: Union[None, str]
    username: str
    holds_role: bool
    holds_other_role: bool
    held_role_name: Union[None, str]
    has_recorded_conflict: Union[None, bool]
    has_reviewer_profile: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        full_name = self.full_name

        email: Union[None, str]
        email = self.email

        username = self.username

        holds_role = self.holds_role

        holds_other_role = self.holds_other_role

        held_role_name: Union[None, str]
        held_role_name = self.held_role_name

        has_recorded_conflict: Union[None, bool]
        has_recorded_conflict = self.has_recorded_conflict

        has_reviewer_profile = self.has_reviewer_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "full_name": full_name,
                "email": email,
                "username": username,
                "holds_role": holds_role,
                "holds_other_role": holds_other_role,
                "held_role_name": held_role_name,
                "has_recorded_conflict": has_recorded_conflict,
                "has_reviewer_profile": has_reviewer_profile,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        full_name = d.pop("full_name")

        def _parse_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        email = _parse_email(d.pop("email"))

        username = d.pop("username")

        holds_role = d.pop("holds_role")

        holds_other_role = d.pop("holds_other_role")

        def _parse_held_role_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        held_role_name = _parse_held_role_name(d.pop("held_role_name"))

        def _parse_has_recorded_conflict(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        has_recorded_conflict = _parse_has_recorded_conflict(d.pop("has_recorded_conflict"))

        has_reviewer_profile = d.pop("has_reviewer_profile")

        proposal_role_candidate = cls(
            uuid=uuid,
            full_name=full_name,
            email=email,
            username=username,
            holds_role=holds_role,
            holds_other_role=holds_other_role,
            held_role_name=held_role_name,
            has_recorded_conflict=has_recorded_conflict,
            has_reviewer_profile=has_reviewer_profile,
        )

        proposal_role_candidate.additional_properties = d
        return proposal_role_candidate

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
