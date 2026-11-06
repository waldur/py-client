from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoundStepProposalResult")


@_attrs_define
class RoundStepProposalResult:
    """
    Attributes:
        proposal_uuid (UUID):
        proposal_name (str):
        detail (str):
        proposal_state (Union[Unset, str]):
        current_step_name (Union[None, Unset, str]):
    """

    proposal_uuid: UUID
    proposal_name: str
    detail: str
    proposal_state: Union[Unset, str] = UNSET
    current_step_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_uuid = str(self.proposal_uuid)

        proposal_name = self.proposal_name

        detail = self.detail

        proposal_state = self.proposal_state

        current_step_name: Union[None, Unset, str]
        if isinstance(self.current_step_name, Unset):
            current_step_name = UNSET
        else:
            current_step_name = self.current_step_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposal_uuid": proposal_uuid,
                "proposal_name": proposal_name,
                "detail": detail,
            }
        )
        if proposal_state is not UNSET:
            field_dict["proposal_state"] = proposal_state
        if current_step_name is not UNSET:
            field_dict["current_step_name"] = current_step_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        proposal_uuid = UUID(d.pop("proposal_uuid"))

        proposal_name = d.pop("proposal_name")

        detail = d.pop("detail")

        proposal_state = d.pop("proposal_state", UNSET)

        def _parse_current_step_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        current_step_name = _parse_current_step_name(d.pop("current_step_name", UNSET))

        round_step_proposal_result = cls(
            proposal_uuid=proposal_uuid,
            proposal_name=proposal_name,
            detail=detail,
            proposal_state=proposal_state,
            current_step_name=current_step_name,
        )

        round_step_proposal_result.additional_properties = d
        return round_step_proposal_result

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
