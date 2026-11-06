import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.proposal_states import ProposalStates
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proposal_ranking_recommended_resources import ProposalRankingRecommendedResources
    from ..models.recommended_offering import RecommendedOffering


T = TypeVar("T", bound="ProposalRanking")


@_attrs_define
class ProposalRanking:
    """
    Attributes:
        uuid (UUID):
        round_ (UUID):
        round_uuid (UUID):
        round_name (str):
        call_uuid (UUID):
        call_name (str):
        proposal (UUID):
        proposal_uuid (UUID):
        proposal_name (str):
        proposal_slug (str):
        proposal_state (ProposalStates):
        proposal_panel_uuid (Union[None, UUID]):
        proposal_panel_name (Union[None, str]):
        meeting_note_title (Union[None, str]):
        rank (int):
        recommended_resources_detail (list['RecommendedOffering']): The recommendation named for reading: per requested
            offering, its name and each recommended component's name, unit and amount.
        created_by_name (Union[None, str]):
        is_locked (bool):
        created (datetime.datetime):
        modified (datetime.datetime):
        meeting_note (Union[None, UUID, Unset]): The round report the ranking belongs to; empty for the round's overall
            ranking.
        final_score (Union[None, Unset, float]):
        recommended_resources (Union[Unset, ProposalRankingRecommendedResources]): Recommended amounts per requested
            offering and component: {"<requested offering uuid>": {"<component type>": amount}}.
        notes (Union[Unset, str]):
    """

    uuid: UUID
    round_: UUID
    round_uuid: UUID
    round_name: str
    call_uuid: UUID
    call_name: str
    proposal: UUID
    proposal_uuid: UUID
    proposal_name: str
    proposal_slug: str
    proposal_state: ProposalStates
    proposal_panel_uuid: Union[None, UUID]
    proposal_panel_name: Union[None, str]
    meeting_note_title: Union[None, str]
    rank: int
    recommended_resources_detail: list["RecommendedOffering"]
    created_by_name: Union[None, str]
    is_locked: bool
    created: datetime.datetime
    modified: datetime.datetime
    meeting_note: Union[None, UUID, Unset] = UNSET
    final_score: Union[None, Unset, float] = UNSET
    recommended_resources: Union[Unset, "ProposalRankingRecommendedResources"] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        round_ = str(self.round_)

        round_uuid = str(self.round_uuid)

        round_name = self.round_name

        call_uuid = str(self.call_uuid)

        call_name = self.call_name

        proposal = str(self.proposal)

        proposal_uuid = str(self.proposal_uuid)

        proposal_name = self.proposal_name

        proposal_slug = self.proposal_slug

        proposal_state = self.proposal_state.value

        proposal_panel_uuid: Union[None, str]
        if isinstance(self.proposal_panel_uuid, UUID):
            proposal_panel_uuid = str(self.proposal_panel_uuid)
        else:
            proposal_panel_uuid = self.proposal_panel_uuid

        proposal_panel_name: Union[None, str]
        proposal_panel_name = self.proposal_panel_name

        meeting_note_title: Union[None, str]
        meeting_note_title = self.meeting_note_title

        rank = self.rank

        recommended_resources_detail = []
        for recommended_resources_detail_item_data in self.recommended_resources_detail:
            recommended_resources_detail_item = recommended_resources_detail_item_data.to_dict()
            recommended_resources_detail.append(recommended_resources_detail_item)

        created_by_name: Union[None, str]
        created_by_name = self.created_by_name

        is_locked = self.is_locked

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        meeting_note: Union[None, Unset, str]
        if isinstance(self.meeting_note, Unset):
            meeting_note = UNSET
        elif isinstance(self.meeting_note, UUID):
            meeting_note = str(self.meeting_note)
        else:
            meeting_note = self.meeting_note

        final_score: Union[None, Unset, float]
        if isinstance(self.final_score, Unset):
            final_score = UNSET
        else:
            final_score = self.final_score

        recommended_resources: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recommended_resources, Unset):
            recommended_resources = self.recommended_resources.to_dict()

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "round": round_,
                "round_uuid": round_uuid,
                "round_name": round_name,
                "call_uuid": call_uuid,
                "call_name": call_name,
                "proposal": proposal,
                "proposal_uuid": proposal_uuid,
                "proposal_name": proposal_name,
                "proposal_slug": proposal_slug,
                "proposal_state": proposal_state,
                "proposal_panel_uuid": proposal_panel_uuid,
                "proposal_panel_name": proposal_panel_name,
                "meeting_note_title": meeting_note_title,
                "rank": rank,
                "recommended_resources_detail": recommended_resources_detail,
                "created_by_name": created_by_name,
                "is_locked": is_locked,
                "created": created,
                "modified": modified,
            }
        )
        if meeting_note is not UNSET:
            field_dict["meeting_note"] = meeting_note
        if final_score is not UNSET:
            field_dict["final_score"] = final_score
        if recommended_resources is not UNSET:
            field_dict["recommended_resources"] = recommended_resources
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_ranking_recommended_resources import ProposalRankingRecommendedResources
        from ..models.recommended_offering import RecommendedOffering

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        round_ = UUID(d.pop("round"))

        round_uuid = UUID(d.pop("round_uuid"))

        round_name = d.pop("round_name")

        call_uuid = UUID(d.pop("call_uuid"))

        call_name = d.pop("call_name")

        proposal = UUID(d.pop("proposal"))

        proposal_uuid = UUID(d.pop("proposal_uuid"))

        proposal_name = d.pop("proposal_name")

        proposal_slug = d.pop("proposal_slug")

        proposal_state = ProposalStates(d.pop("proposal_state"))

        def _parse_proposal_panel_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proposal_panel_uuid_type_0 = UUID(data)

                return proposal_panel_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        proposal_panel_uuid = _parse_proposal_panel_uuid(d.pop("proposal_panel_uuid"))

        def _parse_proposal_panel_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        proposal_panel_name = _parse_proposal_panel_name(d.pop("proposal_panel_name"))

        def _parse_meeting_note_title(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        meeting_note_title = _parse_meeting_note_title(d.pop("meeting_note_title"))

        rank = d.pop("rank")

        recommended_resources_detail = []
        _recommended_resources_detail = d.pop("recommended_resources_detail")
        for recommended_resources_detail_item_data in _recommended_resources_detail:
            recommended_resources_detail_item = RecommendedOffering.from_dict(recommended_resources_detail_item_data)

            recommended_resources_detail.append(recommended_resources_detail_item)

        def _parse_created_by_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by_name = _parse_created_by_name(d.pop("created_by_name"))

        is_locked = d.pop("is_locked")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        def _parse_meeting_note(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                meeting_note_type_0 = UUID(data)

                return meeting_note_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        meeting_note = _parse_meeting_note(d.pop("meeting_note", UNSET))

        def _parse_final_score(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        final_score = _parse_final_score(d.pop("final_score", UNSET))

        _recommended_resources = d.pop("recommended_resources", UNSET)
        recommended_resources: Union[Unset, ProposalRankingRecommendedResources]
        if isinstance(_recommended_resources, Unset):
            recommended_resources = UNSET
        else:
            recommended_resources = ProposalRankingRecommendedResources.from_dict(_recommended_resources)

        notes = d.pop("notes", UNSET)

        proposal_ranking = cls(
            uuid=uuid,
            round_=round_,
            round_uuid=round_uuid,
            round_name=round_name,
            call_uuid=call_uuid,
            call_name=call_name,
            proposal=proposal,
            proposal_uuid=proposal_uuid,
            proposal_name=proposal_name,
            proposal_slug=proposal_slug,
            proposal_state=proposal_state,
            proposal_panel_uuid=proposal_panel_uuid,
            proposal_panel_name=proposal_panel_name,
            meeting_note_title=meeting_note_title,
            rank=rank,
            recommended_resources_detail=recommended_resources_detail,
            created_by_name=created_by_name,
            is_locked=is_locked,
            created=created,
            modified=modified,
            meeting_note=meeting_note,
            final_score=final_score,
            recommended_resources=recommended_resources,
            notes=notes,
        )

        proposal_ranking.additional_properties = d
        return proposal_ranking

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
