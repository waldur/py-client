import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.resolution_enum import ResolutionEnum

T = TypeVar("T", bound="ProposalChangeRequest")


@_attrs_define
class ProposalChangeRequest:
    """
    Attributes:
        uuid (UUID):
        created (datetime.datetime):
        step_uuid (UUID): UUID of the workflow step instance the changes were asked at.
        step_key (str):
        step_name (str):
        contribution_uuid (Union[None, UUID]):
        message (str): What is to change, for the applicant, or for the contributor of a reopened contribution.
        unlocked_parts (list[str]): The parts the applicant may edit while the request is open: field:<name>, documents,
            resources, team, compliance.
        due_at (Union[None, datetime.datetime]): When the changes are due. Past it, the request lapses and the step
            returns to its actor.
        is_open (bool):
        closed_at (Union[None, datetime.datetime]):
        resolution (ResolutionEnum):
        requested_by_name (Union[None, str]): Who asked; not told to the applicant team, as the step's actor may
            be one of its evaluators.
    """

    uuid: UUID
    created: datetime.datetime
    step_uuid: UUID
    step_key: str
    step_name: str
    contribution_uuid: Union[None, UUID]
    message: str
    unlocked_parts: list[str]
    due_at: Union[None, datetime.datetime]
    is_open: bool
    closed_at: Union[None, datetime.datetime]
    resolution: ResolutionEnum
    requested_by_name: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        created = self.created.isoformat()

        step_uuid = str(self.step_uuid)

        step_key = self.step_key

        step_name = self.step_name

        contribution_uuid: Union[None, str]
        if isinstance(self.contribution_uuid, UUID):
            contribution_uuid = str(self.contribution_uuid)
        else:
            contribution_uuid = self.contribution_uuid

        message = self.message

        unlocked_parts = self.unlocked_parts

        due_at: Union[None, str]
        if isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        is_open = self.is_open

        closed_at: Union[None, str]
        if isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        resolution = self.resolution.value

        requested_by_name: Union[None, str]
        requested_by_name = self.requested_by_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "created": created,
                "step_uuid": step_uuid,
                "step_key": step_key,
                "step_name": step_name,
                "contribution_uuid": contribution_uuid,
                "message": message,
                "unlocked_parts": unlocked_parts,
                "due_at": due_at,
                "is_open": is_open,
                "closed_at": closed_at,
                "resolution": resolution,
                "requested_by_name": requested_by_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        step_uuid = UUID(d.pop("step_uuid"))

        step_key = d.pop("step_key")

        step_name = d.pop("step_name")

        def _parse_contribution_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contribution_uuid_type_0 = UUID(data)

                return contribution_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        contribution_uuid = _parse_contribution_uuid(d.pop("contribution_uuid"))

        message = d.pop("message")

        unlocked_parts = cast(list[str], d.pop("unlocked_parts"))

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

        is_open = d.pop("is_open")

        def _parse_closed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = isoparse(data)

                return closed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        closed_at = _parse_closed_at(d.pop("closed_at"))

        resolution = ResolutionEnum(d.pop("resolution"))

        def _parse_requested_by_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        requested_by_name = _parse_requested_by_name(d.pop("requested_by_name"))

        proposal_change_request = cls(
            uuid=uuid,
            created=created,
            step_uuid=step_uuid,
            step_key=step_key,
            step_name=step_name,
            contribution_uuid=contribution_uuid,
            message=message,
            unlocked_parts=unlocked_parts,
            due_at=due_at,
            is_open=is_open,
            closed_at=closed_at,
            resolution=resolution,
            requested_by_name=requested_by_name,
        )

        proposal_change_request.additional_properties = d
        return proposal_change_request

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
