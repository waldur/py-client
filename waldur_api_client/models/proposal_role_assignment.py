import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.proposal_states import ProposalStates

T = TypeVar("T", bound="ProposalRoleAssignment")


@_attrs_define
class ProposalRoleAssignment:
    """
    Attributes:
        uuid (UUID):
        created (datetime.datetime):
        proposal_uuid (UUID):
        proposal_name (str):
        proposal_slug (str):
        proposal_state (ProposalStates):
        call_uuid (UUID):
        call_name (str):
        role_uuid (UUID):
        role_key (str): Identifier of the role within its call.
        role_name (str):
        user_uuid (UUID):
        user_full_name (str):
        user_email (Union[None, str]): Shown to staff, those overseeing the call and the holder.
        is_lead (bool):
        assigned_by_full_name (Union[None, str]):
        assigned_in_step_name (Union[None, str]):
        revoked_at (Union[None, datetime.datetime]):
        revoked_by_full_name (Union[None, str]):
        revoked_reason (str): Why the role was taken away, when not by hand.
        coi_confirmation_required (Union[None, bool]):
        coi_confirmed_at (Union[None, datetime.datetime]):
        coi_declaration_only (Union[None, bool]):
        coi_declaration_text (Union[None, str]): The conflict-of-interest declaration the holder confirms: as confirmed
            once they did, else as worded now. Empty for the platform's standard declaration, or when none is asked for.
        is_active (bool):
        awaits_coi_confirmation (Union[None, bool]):
        has_standing_conflict (Union[None, bool]): A conflict of interest is recorded between the holder and the
            proposal and not dismissed or waived: the role gives no access meanwhile.
    """

    uuid: UUID
    created: datetime.datetime
    proposal_uuid: UUID
    proposal_name: str
    proposal_slug: str
    proposal_state: ProposalStates
    call_uuid: UUID
    call_name: str
    role_uuid: UUID
    role_key: str
    role_name: str
    user_uuid: UUID
    user_full_name: str
    user_email: Union[None, str]
    is_lead: bool
    assigned_by_full_name: Union[None, str]
    assigned_in_step_name: Union[None, str]
    revoked_at: Union[None, datetime.datetime]
    revoked_by_full_name: Union[None, str]
    revoked_reason: str
    coi_confirmation_required: Union[None, bool]
    coi_confirmed_at: Union[None, datetime.datetime]
    coi_declaration_only: Union[None, bool]
    coi_declaration_text: Union[None, str]
    is_active: bool
    awaits_coi_confirmation: Union[None, bool]
    has_standing_conflict: Union[None, bool]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        created = self.created.isoformat()

        proposal_uuid = str(self.proposal_uuid)

        proposal_name = self.proposal_name

        proposal_slug = self.proposal_slug

        proposal_state = self.proposal_state.value

        call_uuid = str(self.call_uuid)

        call_name = self.call_name

        role_uuid = str(self.role_uuid)

        role_key = self.role_key

        role_name = self.role_name

        user_uuid = str(self.user_uuid)

        user_full_name = self.user_full_name

        user_email: Union[None, str]
        user_email = self.user_email

        is_lead = self.is_lead

        assigned_by_full_name: Union[None, str]
        assigned_by_full_name = self.assigned_by_full_name

        assigned_in_step_name: Union[None, str]
        assigned_in_step_name = self.assigned_in_step_name

        revoked_at: Union[None, str]
        if isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        revoked_by_full_name: Union[None, str]
        revoked_by_full_name = self.revoked_by_full_name

        revoked_reason = self.revoked_reason

        coi_confirmation_required: Union[None, bool]
        coi_confirmation_required = self.coi_confirmation_required

        coi_confirmed_at: Union[None, str]
        if isinstance(self.coi_confirmed_at, datetime.datetime):
            coi_confirmed_at = self.coi_confirmed_at.isoformat()
        else:
            coi_confirmed_at = self.coi_confirmed_at

        coi_declaration_only: Union[None, bool]
        coi_declaration_only = self.coi_declaration_only

        coi_declaration_text: Union[None, str]
        coi_declaration_text = self.coi_declaration_text

        is_active = self.is_active

        awaits_coi_confirmation: Union[None, bool]
        awaits_coi_confirmation = self.awaits_coi_confirmation

        has_standing_conflict: Union[None, bool]
        has_standing_conflict = self.has_standing_conflict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "created": created,
                "proposal_uuid": proposal_uuid,
                "proposal_name": proposal_name,
                "proposal_slug": proposal_slug,
                "proposal_state": proposal_state,
                "call_uuid": call_uuid,
                "call_name": call_name,
                "role_uuid": role_uuid,
                "role_key": role_key,
                "role_name": role_name,
                "user_uuid": user_uuid,
                "user_full_name": user_full_name,
                "user_email": user_email,
                "is_lead": is_lead,
                "assigned_by_full_name": assigned_by_full_name,
                "assigned_in_step_name": assigned_in_step_name,
                "revoked_at": revoked_at,
                "revoked_by_full_name": revoked_by_full_name,
                "revoked_reason": revoked_reason,
                "coi_confirmation_required": coi_confirmation_required,
                "coi_confirmed_at": coi_confirmed_at,
                "coi_declaration_only": coi_declaration_only,
                "coi_declaration_text": coi_declaration_text,
                "is_active": is_active,
                "awaits_coi_confirmation": awaits_coi_confirmation,
                "has_standing_conflict": has_standing_conflict,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        proposal_uuid = UUID(d.pop("proposal_uuid"))

        proposal_name = d.pop("proposal_name")

        proposal_slug = d.pop("proposal_slug")

        proposal_state = ProposalStates(d.pop("proposal_state"))

        call_uuid = UUID(d.pop("call_uuid"))

        call_name = d.pop("call_name")

        role_uuid = UUID(d.pop("role_uuid"))

        role_key = d.pop("role_key")

        role_name = d.pop("role_name")

        user_uuid = UUID(d.pop("user_uuid"))

        user_full_name = d.pop("user_full_name")

        def _parse_user_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        user_email = _parse_user_email(d.pop("user_email"))

        is_lead = d.pop("is_lead")

        def _parse_assigned_by_full_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        assigned_by_full_name = _parse_assigned_by_full_name(d.pop("assigned_by_full_name"))

        def _parse_assigned_in_step_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        assigned_in_step_name = _parse_assigned_in_step_name(d.pop("assigned_in_step_name"))

        def _parse_revoked_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = isoparse(data)

                return revoked_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))

        def _parse_revoked_by_full_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        revoked_by_full_name = _parse_revoked_by_full_name(d.pop("revoked_by_full_name"))

        revoked_reason = d.pop("revoked_reason")

        def _parse_coi_confirmation_required(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        coi_confirmation_required = _parse_coi_confirmation_required(d.pop("coi_confirmation_required"))

        def _parse_coi_confirmed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                coi_confirmed_at_type_0 = isoparse(data)

                return coi_confirmed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        coi_confirmed_at = _parse_coi_confirmed_at(d.pop("coi_confirmed_at"))

        def _parse_coi_declaration_only(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        coi_declaration_only = _parse_coi_declaration_only(d.pop("coi_declaration_only"))

        def _parse_coi_declaration_text(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        coi_declaration_text = _parse_coi_declaration_text(d.pop("coi_declaration_text"))

        is_active = d.pop("is_active")

        def _parse_awaits_coi_confirmation(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        awaits_coi_confirmation = _parse_awaits_coi_confirmation(d.pop("awaits_coi_confirmation"))

        def _parse_has_standing_conflict(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        has_standing_conflict = _parse_has_standing_conflict(d.pop("has_standing_conflict"))

        proposal_role_assignment = cls(
            uuid=uuid,
            created=created,
            proposal_uuid=proposal_uuid,
            proposal_name=proposal_name,
            proposal_slug=proposal_slug,
            proposal_state=proposal_state,
            call_uuid=call_uuid,
            call_name=call_name,
            role_uuid=role_uuid,
            role_key=role_key,
            role_name=role_name,
            user_uuid=user_uuid,
            user_full_name=user_full_name,
            user_email=user_email,
            is_lead=is_lead,
            assigned_by_full_name=assigned_by_full_name,
            assigned_in_step_name=assigned_in_step_name,
            revoked_at=revoked_at,
            revoked_by_full_name=revoked_by_full_name,
            revoked_reason=revoked_reason,
            coi_confirmation_required=coi_confirmation_required,
            coi_confirmed_at=coi_confirmed_at,
            coi_declaration_only=coi_declaration_only,
            coi_declaration_text=coi_declaration_text,
            is_active=is_active,
            awaits_coi_confirmation=awaits_coi_confirmation,
            has_standing_conflict=has_standing_conflict,
        )

        proposal_role_assignment.additional_properties = d
        return proposal_role_assignment

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
