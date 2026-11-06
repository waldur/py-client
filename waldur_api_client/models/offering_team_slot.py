import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.step_contribution_status import StepContributionStatus

T = TypeVar("T", bound="OfferingTeamSlot")


@_attrs_define
class OfferingTeamSlot:
    """
    Attributes:
        uuid (UUID):
        proposal_uuid (UUID):
        proposal_name (str):
        proposal_slug (str):
        call_name (str):
        offering_name (str):
        requested_offering_uuid (UUID):
        step_name (str):
        step_key (str):
        status (StepContributionStatus):
        delegate_uuid (Union[None, UUID]):
        delegate_name (Union[None, str]):
        delegate_accepted (bool): The person it was handed to has taken it over.
        stand_in (bool): Nobody is on the offering's team, so the call's managers stand in for it.
        due_at (Union[None, datetime.datetime]):
        overdue (bool):
    """

    uuid: UUID
    proposal_uuid: UUID
    proposal_name: str
    proposal_slug: str
    call_name: str
    offering_name: str
    requested_offering_uuid: UUID
    step_name: str
    step_key: str
    status: StepContributionStatus
    delegate_uuid: Union[None, UUID]
    delegate_name: Union[None, str]
    delegate_accepted: bool
    stand_in: bool
    due_at: Union[None, datetime.datetime]
    overdue: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        proposal_uuid = str(self.proposal_uuid)

        proposal_name = self.proposal_name

        proposal_slug = self.proposal_slug

        call_name = self.call_name

        offering_name = self.offering_name

        requested_offering_uuid = str(self.requested_offering_uuid)

        step_name = self.step_name

        step_key = self.step_key

        status = self.status.value

        delegate_uuid: Union[None, str]
        if isinstance(self.delegate_uuid, UUID):
            delegate_uuid = str(self.delegate_uuid)
        else:
            delegate_uuid = self.delegate_uuid

        delegate_name: Union[None, str]
        delegate_name = self.delegate_name

        delegate_accepted = self.delegate_accepted

        stand_in = self.stand_in

        due_at: Union[None, str]
        if isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        overdue = self.overdue

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "proposal_uuid": proposal_uuid,
                "proposal_name": proposal_name,
                "proposal_slug": proposal_slug,
                "call_name": call_name,
                "offering_name": offering_name,
                "requested_offering_uuid": requested_offering_uuid,
                "step_name": step_name,
                "step_key": step_key,
                "status": status,
                "delegate_uuid": delegate_uuid,
                "delegate_name": delegate_name,
                "delegate_accepted": delegate_accepted,
                "stand_in": stand_in,
                "due_at": due_at,
                "overdue": overdue,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        proposal_uuid = UUID(d.pop("proposal_uuid"))

        proposal_name = d.pop("proposal_name")

        proposal_slug = d.pop("proposal_slug")

        call_name = d.pop("call_name")

        offering_name = d.pop("offering_name")

        requested_offering_uuid = UUID(d.pop("requested_offering_uuid"))

        step_name = d.pop("step_name")

        step_key = d.pop("step_key")

        status = StepContributionStatus(d.pop("status"))

        def _parse_delegate_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegate_uuid_type_0 = UUID(data)

                return delegate_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        delegate_uuid = _parse_delegate_uuid(d.pop("delegate_uuid"))

        def _parse_delegate_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        delegate_name = _parse_delegate_name(d.pop("delegate_name"))

        delegate_accepted = d.pop("delegate_accepted")

        stand_in = d.pop("stand_in")

        def _parse_due_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = isoparse(data)

                return due_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        due_at = _parse_due_at(d.pop("due_at"))

        overdue = d.pop("overdue")

        offering_team_slot = cls(
            uuid=uuid,
            proposal_uuid=proposal_uuid,
            proposal_name=proposal_name,
            proposal_slug=proposal_slug,
            call_name=call_name,
            offering_name=offering_name,
            requested_offering_uuid=requested_offering_uuid,
            step_name=step_name,
            step_key=step_key,
            status=status,
            delegate_uuid=delegate_uuid,
            delegate_name=delegate_name,
            delegate_accepted=delegate_accepted,
            stand_in=stand_in,
            due_at=due_at,
            overdue=overdue,
        )

        offering_team_slot.additional_properties = d
        return offering_team_slot

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
