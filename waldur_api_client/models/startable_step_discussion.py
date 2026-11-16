import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="StartableStepDiscussion")


@_attrs_define
class StartableStepDiscussion:
    """
    Attributes:
        proposal_step_uuid (Union[None, UUID]):
        round_step_uuid (Union[None, UUID]):
        panel_uuid (Union[None, UUID]):
        panel_name (Union[None, str]):
        call_uuid (UUID):
        call_name (str):
        call_step_uuid (UUID):
        step_name (str):
        round_scoped (bool):
        proposal_uuid (Union[None, UUID]):
        proposal_name (Union[None, str]):
        proposal_slug (Union[None, str]):
        round_uuid (UUID):
        round_name (str):
        due_at (Union[None, datetime.datetime]): When the step is due: the proposal's step deadline, or the round step's
            due date.
    """

    proposal_step_uuid: Union[None, UUID]
    round_step_uuid: Union[None, UUID]
    panel_uuid: Union[None, UUID]
    panel_name: Union[None, str]
    call_uuid: UUID
    call_name: str
    call_step_uuid: UUID
    step_name: str
    round_scoped: bool
    proposal_uuid: Union[None, UUID]
    proposal_name: Union[None, str]
    proposal_slug: Union[None, str]
    round_uuid: UUID
    round_name: str
    due_at: Union[None, datetime.datetime]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_step_uuid: Union[None, str]
        if isinstance(self.proposal_step_uuid, UUID):
            proposal_step_uuid = str(self.proposal_step_uuid)
        else:
            proposal_step_uuid = self.proposal_step_uuid

        round_step_uuid: Union[None, str]
        if isinstance(self.round_step_uuid, UUID):
            round_step_uuid = str(self.round_step_uuid)
        else:
            round_step_uuid = self.round_step_uuid

        panel_uuid: Union[None, str]
        if isinstance(self.panel_uuid, UUID):
            panel_uuid = str(self.panel_uuid)
        else:
            panel_uuid = self.panel_uuid

        panel_name: Union[None, str]
        panel_name = self.panel_name

        call_uuid = str(self.call_uuid)

        call_name = self.call_name

        call_step_uuid = str(self.call_step_uuid)

        step_name = self.step_name

        round_scoped = self.round_scoped

        proposal_uuid: Union[None, str]
        if isinstance(self.proposal_uuid, UUID):
            proposal_uuid = str(self.proposal_uuid)
        else:
            proposal_uuid = self.proposal_uuid

        proposal_name: Union[None, str]
        proposal_name = self.proposal_name

        proposal_slug: Union[None, str]
        proposal_slug = self.proposal_slug

        round_uuid = str(self.round_uuid)

        round_name = self.round_name

        due_at: Union[None, str]
        if isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposal_step_uuid": proposal_step_uuid,
                "round_step_uuid": round_step_uuid,
                "panel_uuid": panel_uuid,
                "panel_name": panel_name,
                "call_uuid": call_uuid,
                "call_name": call_name,
                "call_step_uuid": call_step_uuid,
                "step_name": step_name,
                "round_scoped": round_scoped,
                "proposal_uuid": proposal_uuid,
                "proposal_name": proposal_name,
                "proposal_slug": proposal_slug,
                "round_uuid": round_uuid,
                "round_name": round_name,
                "due_at": due_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_proposal_step_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proposal_step_uuid_type_0 = UUID(data)

                return proposal_step_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        proposal_step_uuid = _parse_proposal_step_uuid(d.pop("proposal_step_uuid"))

        def _parse_round_step_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_step_uuid_type_0 = UUID(data)

                return round_step_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        round_step_uuid = _parse_round_step_uuid(d.pop("round_step_uuid"))

        def _parse_panel_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                panel_uuid_type_0 = UUID(data)

                return panel_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        panel_uuid = _parse_panel_uuid(d.pop("panel_uuid"))

        def _parse_panel_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        panel_name = _parse_panel_name(d.pop("panel_name"))

        call_uuid = UUID(d.pop("call_uuid"))

        call_name = d.pop("call_name")

        call_step_uuid = UUID(d.pop("call_step_uuid"))

        step_name = d.pop("step_name")

        round_scoped = d.pop("round_scoped")

        def _parse_proposal_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proposal_uuid_type_0 = UUID(data)

                return proposal_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        proposal_uuid = _parse_proposal_uuid(d.pop("proposal_uuid"))

        def _parse_proposal_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        proposal_name = _parse_proposal_name(d.pop("proposal_name"))

        def _parse_proposal_slug(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        proposal_slug = _parse_proposal_slug(d.pop("proposal_slug"))

        round_uuid = UUID(d.pop("round_uuid"))

        round_name = d.pop("round_name")

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

        startable_step_discussion = cls(
            proposal_step_uuid=proposal_step_uuid,
            round_step_uuid=round_step_uuid,
            panel_uuid=panel_uuid,
            panel_name=panel_name,
            call_uuid=call_uuid,
            call_name=call_name,
            call_step_uuid=call_step_uuid,
            step_name=step_name,
            round_scoped=round_scoped,
            proposal_uuid=proposal_uuid,
            proposal_name=proposal_name,
            proposal_slug=proposal_slug,
            round_uuid=round_uuid,
            round_name=round_name,
            due_at=due_at,
        )

        startable_step_discussion.additional_properties = d
        return startable_step_discussion

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
