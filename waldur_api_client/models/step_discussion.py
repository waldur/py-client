import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.step_discussion_participant import StepDiscussionParticipant


T = TypeVar("T", bound="StepDiscussion")


@_attrs_define
class StepDiscussion:
    """
    Attributes:
        uuid (UUID):
        state (str): open, or closed with its step.
        opened_at (datetime.datetime):
        closed_at (Union[None, datetime.datetime]):
        opened_by_uuid (Union[None, UUID]):
        opened_by_name (Union[None, str]):
        call_uuid (UUID):
        call_name (str):
        call_step_uuid (UUID):
        step_key (str):
        step_name (str):
        round_scoped (bool): Whether it is a round step's discussion.
        proposal_step_uuid (Union[None, UUID]): The proposal's step discussed; null for a round step.
        proposal_uuid (Union[None, UUID]):
        proposal_name (Union[None, str]):
        proposal_slug (Union[None, str]):
        round_step_uuid (Union[None, UUID]): The round step discussed; null for a proposal's step.
        round_uuid (UUID): The round of the round step, or of the proposal.
        round_name (str):
        panel_uuid (Union[None, UUID]): The panel of a round step's discussion on a call with panels.
        panel_name (Union[None, str]):
        room_uuid (Union[None, UUID]): The discussion's Matrix room (matrix/rooms), once created.
        room_id (Union[None, str]): The Matrix room ID, e.g. !abc:domain, once created.
        room_state (Union[None, str]): The room's state in Waldur: creating, active, archived...
        export_uuid (Union[None, UUID]): The export of the room's history made when the discussion closed
            (matrix/exports), for those who may download it: the call's managers, staff and support. Null otherwise, and
            until it is made.
        participants (list['StepDiscussionParticipant']): Once closed, who took part; while open, who is in the room
            now.
    """

    uuid: UUID
    state: str
    opened_at: datetime.datetime
    closed_at: Union[None, datetime.datetime]
    opened_by_uuid: Union[None, UUID]
    opened_by_name: Union[None, str]
    call_uuid: UUID
    call_name: str
    call_step_uuid: UUID
    step_key: str
    step_name: str
    round_scoped: bool
    proposal_step_uuid: Union[None, UUID]
    proposal_uuid: Union[None, UUID]
    proposal_name: Union[None, str]
    proposal_slug: Union[None, str]
    round_step_uuid: Union[None, UUID]
    round_uuid: UUID
    round_name: str
    panel_uuid: Union[None, UUID]
    panel_name: Union[None, str]
    room_uuid: Union[None, UUID]
    room_id: Union[None, str]
    room_state: Union[None, str]
    export_uuid: Union[None, UUID]
    participants: list["StepDiscussionParticipant"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        state = self.state

        opened_at = self.opened_at.isoformat()

        closed_at: Union[None, str]
        if isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        opened_by_uuid: Union[None, str]
        if isinstance(self.opened_by_uuid, UUID):
            opened_by_uuid = str(self.opened_by_uuid)
        else:
            opened_by_uuid = self.opened_by_uuid

        opened_by_name: Union[None, str]
        opened_by_name = self.opened_by_name

        call_uuid = str(self.call_uuid)

        call_name = self.call_name

        call_step_uuid = str(self.call_step_uuid)

        step_key = self.step_key

        step_name = self.step_name

        round_scoped = self.round_scoped

        proposal_step_uuid: Union[None, str]
        if isinstance(self.proposal_step_uuid, UUID):
            proposal_step_uuid = str(self.proposal_step_uuid)
        else:
            proposal_step_uuid = self.proposal_step_uuid

        proposal_uuid: Union[None, str]
        if isinstance(self.proposal_uuid, UUID):
            proposal_uuid = str(self.proposal_uuid)
        else:
            proposal_uuid = self.proposal_uuid

        proposal_name: Union[None, str]
        proposal_name = self.proposal_name

        proposal_slug: Union[None, str]
        proposal_slug = self.proposal_slug

        round_step_uuid: Union[None, str]
        if isinstance(self.round_step_uuid, UUID):
            round_step_uuid = str(self.round_step_uuid)
        else:
            round_step_uuid = self.round_step_uuid

        round_uuid = str(self.round_uuid)

        round_name = self.round_name

        panel_uuid: Union[None, str]
        if isinstance(self.panel_uuid, UUID):
            panel_uuid = str(self.panel_uuid)
        else:
            panel_uuid = self.panel_uuid

        panel_name: Union[None, str]
        panel_name = self.panel_name

        room_uuid: Union[None, str]
        if isinstance(self.room_uuid, UUID):
            room_uuid = str(self.room_uuid)
        else:
            room_uuid = self.room_uuid

        room_id: Union[None, str]
        room_id = self.room_id

        room_state: Union[None, str]
        room_state = self.room_state

        export_uuid: Union[None, str]
        if isinstance(self.export_uuid, UUID):
            export_uuid = str(self.export_uuid)
        else:
            export_uuid = self.export_uuid

        participants = []
        for participants_item_data in self.participants:
            participants_item = participants_item_data.to_dict()
            participants.append(participants_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "state": state,
                "opened_at": opened_at,
                "closed_at": closed_at,
                "opened_by_uuid": opened_by_uuid,
                "opened_by_name": opened_by_name,
                "call_uuid": call_uuid,
                "call_name": call_name,
                "call_step_uuid": call_step_uuid,
                "step_key": step_key,
                "step_name": step_name,
                "round_scoped": round_scoped,
                "proposal_step_uuid": proposal_step_uuid,
                "proposal_uuid": proposal_uuid,
                "proposal_name": proposal_name,
                "proposal_slug": proposal_slug,
                "round_step_uuid": round_step_uuid,
                "round_uuid": round_uuid,
                "round_name": round_name,
                "panel_uuid": panel_uuid,
                "panel_name": panel_name,
                "room_uuid": room_uuid,
                "room_id": room_id,
                "room_state": room_state,
                "export_uuid": export_uuid,
                "participants": participants,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_discussion_participant import StepDiscussionParticipant

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        state = d.pop("state")

        opened_at = isoparse(d.pop("opened_at"))

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

        def _parse_opened_by_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opened_by_uuid_type_0 = UUID(data)

                return opened_by_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        opened_by_uuid = _parse_opened_by_uuid(d.pop("opened_by_uuid"))

        def _parse_opened_by_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        opened_by_name = _parse_opened_by_name(d.pop("opened_by_name"))

        call_uuid = UUID(d.pop("call_uuid"))

        call_name = d.pop("call_name")

        call_step_uuid = UUID(d.pop("call_step_uuid"))

        step_key = d.pop("step_key")

        step_name = d.pop("step_name")

        round_scoped = d.pop("round_scoped")

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

        round_uuid = UUID(d.pop("round_uuid"))

        round_name = d.pop("round_name")

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

        def _parse_room_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                room_uuid_type_0 = UUID(data)

                return room_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        room_uuid = _parse_room_uuid(d.pop("room_uuid"))

        def _parse_room_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        room_id = _parse_room_id(d.pop("room_id"))

        def _parse_room_state(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        room_state = _parse_room_state(d.pop("room_state"))

        def _parse_export_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                export_uuid_type_0 = UUID(data)

                return export_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        export_uuid = _parse_export_uuid(d.pop("export_uuid"))

        participants = []
        _participants = d.pop("participants")
        for participants_item_data in _participants:
            participants_item = StepDiscussionParticipant.from_dict(participants_item_data)

            participants.append(participants_item)

        step_discussion = cls(
            uuid=uuid,
            state=state,
            opened_at=opened_at,
            closed_at=closed_at,
            opened_by_uuid=opened_by_uuid,
            opened_by_name=opened_by_name,
            call_uuid=call_uuid,
            call_name=call_name,
            call_step_uuid=call_step_uuid,
            step_key=step_key,
            step_name=step_name,
            round_scoped=round_scoped,
            proposal_step_uuid=proposal_step_uuid,
            proposal_uuid=proposal_uuid,
            proposal_name=proposal_name,
            proposal_slug=proposal_slug,
            round_step_uuid=round_step_uuid,
            round_uuid=round_uuid,
            round_name=round_name,
            panel_uuid=panel_uuid,
            panel_name=panel_name,
            room_uuid=room_uuid,
            room_id=room_id,
            room_state=room_state,
            export_uuid=export_uuid,
            participants=participants,
        )

        step_discussion.additional_properties = d
        return step_discussion

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
