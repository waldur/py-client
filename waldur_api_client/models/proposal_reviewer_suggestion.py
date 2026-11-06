import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.proposal_reviewer_suggestion_status import ProposalReviewerSuggestionStatus

T = TypeVar("T", bound="ProposalReviewerSuggestion")


@_attrs_define
class ProposalReviewerSuggestion:
    """
    Attributes:
        uuid (UUID):
        created (datetime.datetime):
        proposal (UUID):
        proposal_name (str):
        suggested_user (Union[None, UUID]):
        suggested_user_name (Union[None, str]):
        suggested_email (str): E-mail address of a suggested reviewer without a user account.
        note (str): Why this reviewer: expertise.
        suggester_uuid (Union[None, UUID]):
        suggester_name (Union[None, str]):
        step_name (str):
        status (ProposalReviewerSuggestionStatus):
    """

    uuid: UUID
    created: datetime.datetime
    proposal: UUID
    proposal_name: str
    suggested_user: Union[None, UUID]
    suggested_user_name: Union[None, str]
    suggested_email: str
    note: str
    suggester_uuid: Union[None, UUID]
    suggester_name: Union[None, str]
    step_name: str
    status: ProposalReviewerSuggestionStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        created = self.created.isoformat()

        proposal = str(self.proposal)

        proposal_name = self.proposal_name

        suggested_user: Union[None, str]
        if isinstance(self.suggested_user, UUID):
            suggested_user = str(self.suggested_user)
        else:
            suggested_user = self.suggested_user

        suggested_user_name: Union[None, str]
        suggested_user_name = self.suggested_user_name

        suggested_email = self.suggested_email

        note = self.note

        suggester_uuid: Union[None, str]
        if isinstance(self.suggester_uuid, UUID):
            suggester_uuid = str(self.suggester_uuid)
        else:
            suggester_uuid = self.suggester_uuid

        suggester_name: Union[None, str]
        suggester_name = self.suggester_name

        step_name = self.step_name

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "created": created,
                "proposal": proposal,
                "proposal_name": proposal_name,
                "suggested_user": suggested_user,
                "suggested_user_name": suggested_user_name,
                "suggested_email": suggested_email,
                "note": note,
                "suggester_uuid": suggester_uuid,
                "suggester_name": suggester_name,
                "step_name": step_name,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        proposal = UUID(d.pop("proposal"))

        proposal_name = d.pop("proposal_name")

        def _parse_suggested_user(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suggested_user_type_0 = UUID(data)

                return suggested_user_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        suggested_user = _parse_suggested_user(d.pop("suggested_user"))

        def _parse_suggested_user_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        suggested_user_name = _parse_suggested_user_name(d.pop("suggested_user_name"))

        suggested_email = d.pop("suggested_email")

        note = d.pop("note")

        def _parse_suggester_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suggester_uuid_type_0 = UUID(data)

                return suggester_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        suggester_uuid = _parse_suggester_uuid(d.pop("suggester_uuid"))

        def _parse_suggester_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        suggester_name = _parse_suggester_name(d.pop("suggester_name"))

        step_name = d.pop("step_name")

        status = ProposalReviewerSuggestionStatus(d.pop("status"))

        proposal_reviewer_suggestion = cls(
            uuid=uuid,
            created=created,
            proposal=proposal,
            proposal_name=proposal_name,
            suggested_user=suggested_user,
            suggested_user_name=suggested_user_name,
            suggested_email=suggested_email,
            note=note,
            suggester_uuid=suggester_uuid,
            suggester_name=suggester_name,
            step_name=step_name,
            status=status,
        )

        proposal_reviewer_suggestion.additional_properties = d
        return proposal_reviewer_suggestion

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
