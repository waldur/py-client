from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenStepDiscussionRequest")


@_attrs_define
class OpenStepDiscussionRequest:
    """
    Attributes:
        proposal_step_uuid (Union[None, UUID, Unset]): The proposal's step, as workflow_states lists it. On a step run
            once per round, the round's discussion of the proposal's panel.
        round_step_uuid (Union[None, UUID, Unset]): The round step (round_steps of a round).
        panel_uuid (Union[None, UUID, Unset]): With round_step_uuid on a call with panels: whose discussion.
    """

    proposal_step_uuid: Union[None, UUID, Unset] = UNSET
    round_step_uuid: Union[None, UUID, Unset] = UNSET
    panel_uuid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_step_uuid: Union[None, Unset, str]
        if isinstance(self.proposal_step_uuid, Unset):
            proposal_step_uuid = UNSET
        elif isinstance(self.proposal_step_uuid, UUID):
            proposal_step_uuid = str(self.proposal_step_uuid)
        else:
            proposal_step_uuid = self.proposal_step_uuid

        round_step_uuid: Union[None, Unset, str]
        if isinstance(self.round_step_uuid, Unset):
            round_step_uuid = UNSET
        elif isinstance(self.round_step_uuid, UUID):
            round_step_uuid = str(self.round_step_uuid)
        else:
            round_step_uuid = self.round_step_uuid

        panel_uuid: Union[None, Unset, str]
        if isinstance(self.panel_uuid, Unset):
            panel_uuid = UNSET
        elif isinstance(self.panel_uuid, UUID):
            panel_uuid = str(self.panel_uuid)
        else:
            panel_uuid = self.panel_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proposal_step_uuid is not UNSET:
            field_dict["proposal_step_uuid"] = proposal_step_uuid
        if round_step_uuid is not UNSET:
            field_dict["round_step_uuid"] = round_step_uuid
        if panel_uuid is not UNSET:
            field_dict["panel_uuid"] = panel_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_proposal_step_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proposal_step_uuid_type_0 = UUID(data)

                return proposal_step_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        proposal_step_uuid = _parse_proposal_step_uuid(d.pop("proposal_step_uuid", UNSET))

        def _parse_round_step_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_step_uuid_type_0 = UUID(data)

                return round_step_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        round_step_uuid = _parse_round_step_uuid(d.pop("round_step_uuid", UNSET))

        def _parse_panel_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                panel_uuid_type_0 = UUID(data)

                return panel_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        panel_uuid = _parse_panel_uuid(d.pop("panel_uuid", UNSET))

        open_step_discussion_request = cls(
            proposal_step_uuid=proposal_step_uuid,
            round_step_uuid=round_step_uuid,
            panel_uuid=panel_uuid,
        )

        open_step_discussion_request.additional_properties = d
        return open_step_discussion_request

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
