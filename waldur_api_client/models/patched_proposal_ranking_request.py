from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_proposal_ranking_request_recommended_resources import (
        PatchedProposalRankingRequestRecommendedResources,
    )


T = TypeVar("T", bound="PatchedProposalRankingRequest")


@_attrs_define
class PatchedProposalRankingRequest:
    """
    Attributes:
        round_ (Union[Unset, UUID]):
        proposal (Union[Unset, UUID]):
        meeting_note (Union[None, UUID, Unset]): The round report the ranking belongs to; empty for the round's overall
            ranking.
        rank (Union[Unset, int]):
        final_score (Union[None, Unset, float]):
        recommended_resources (Union[Unset, PatchedProposalRankingRequestRecommendedResources]): Recommended amounts per
            requested offering and component: {"<requested offering uuid>": {"<component type>": amount}}.
        notes (Union[Unset, str]):
    """

    round_: Union[Unset, UUID] = UNSET
    proposal: Union[Unset, UUID] = UNSET
    meeting_note: Union[None, UUID, Unset] = UNSET
    rank: Union[Unset, int] = UNSET
    final_score: Union[None, Unset, float] = UNSET
    recommended_resources: Union[Unset, "PatchedProposalRankingRequestRecommendedResources"] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        round_: Union[Unset, str] = UNSET
        if not isinstance(self.round_, Unset):
            round_ = str(self.round_)

        proposal: Union[Unset, str] = UNSET
        if not isinstance(self.proposal, Unset):
            proposal = str(self.proposal)

        meeting_note: Union[None, Unset, str]
        if isinstance(self.meeting_note, Unset):
            meeting_note = UNSET
        elif isinstance(self.meeting_note, UUID):
            meeting_note = str(self.meeting_note)
        else:
            meeting_note = self.meeting_note

        rank = self.rank

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
        field_dict.update({})
        if round_ is not UNSET:
            field_dict["round"] = round_
        if proposal is not UNSET:
            field_dict["proposal"] = proposal
        if meeting_note is not UNSET:
            field_dict["meeting_note"] = meeting_note
        if rank is not UNSET:
            field_dict["rank"] = rank
        if final_score is not UNSET:
            field_dict["final_score"] = final_score
        if recommended_resources is not UNSET:
            field_dict["recommended_resources"] = recommended_resources
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patched_proposal_ranking_request_recommended_resources import (
            PatchedProposalRankingRequestRecommendedResources,
        )

        d = dict(src_dict)
        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, UUID]
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = UUID(_round_)

        _proposal = d.pop("proposal", UNSET)
        proposal: Union[Unset, UUID]
        if isinstance(_proposal, Unset):
            proposal = UNSET
        else:
            proposal = UUID(_proposal)

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

        rank = d.pop("rank", UNSET)

        def _parse_final_score(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        final_score = _parse_final_score(d.pop("final_score", UNSET))

        _recommended_resources = d.pop("recommended_resources", UNSET)
        recommended_resources: Union[Unset, PatchedProposalRankingRequestRecommendedResources]
        if isinstance(_recommended_resources, Unset):
            recommended_resources = UNSET
        else:
            recommended_resources = PatchedProposalRankingRequestRecommendedResources.from_dict(_recommended_resources)

        notes = d.pop("notes", UNSET)

        patched_proposal_ranking_request = cls(
            round_=round_,
            proposal=proposal,
            meeting_note=meeting_note,
            rank=rank,
            final_score=final_score,
            recommended_resources=recommended_resources,
            notes=notes,
        )

        patched_proposal_ranking_request.additional_properties = d
        return patched_proposal_ranking_request

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
