from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmitStepContributionRequest")


@_attrs_define
class SubmitStepContributionRequest:
    """
    Attributes:
        contribution_uuid (Union[None, UUID, Unset]): The contribution to submit. The caller's own contribution to the
            step when left out.
        step_uuid (Union[None, UUID, Unset]): UUID of the call step, naming the step whose contribution is meant. The
            proposal's current step when left out.
        outcome (Union[Unset, str]): What the contribution concludes. On a per-offering step one of accepted,
            conditionally_accepted or rejected; elsewhere, if given, one of the step's outcomes. Default: ''.
        conditions (Union[Unset, str]): Conditions of a conditional acceptance. Default: ''.
        comment (Union[Unset, str]):  Default: ''.
    """

    contribution_uuid: Union[None, UUID, Unset] = UNSET
    step_uuid: Union[None, UUID, Unset] = UNSET
    outcome: Union[Unset, str] = ""
    conditions: Union[Unset, str] = ""
    comment: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contribution_uuid: Union[None, Unset, str]
        if isinstance(self.contribution_uuid, Unset):
            contribution_uuid = UNSET
        elif isinstance(self.contribution_uuid, UUID):
            contribution_uuid = str(self.contribution_uuid)
        else:
            contribution_uuid = self.contribution_uuid

        step_uuid: Union[None, Unset, str]
        if isinstance(self.step_uuid, Unset):
            step_uuid = UNSET
        elif isinstance(self.step_uuid, UUID):
            step_uuid = str(self.step_uuid)
        else:
            step_uuid = self.step_uuid

        outcome = self.outcome

        conditions = self.conditions

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contribution_uuid is not UNSET:
            field_dict["contribution_uuid"] = contribution_uuid
        if step_uuid is not UNSET:
            field_dict["step_uuid"] = step_uuid
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_contribution_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contribution_uuid_type_0 = UUID(data)

                return contribution_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        contribution_uuid = _parse_contribution_uuid(d.pop("contribution_uuid", UNSET))

        def _parse_step_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                step_uuid_type_0 = UUID(data)

                return step_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        step_uuid = _parse_step_uuid(d.pop("step_uuid", UNSET))

        outcome = d.pop("outcome", UNSET)

        conditions = d.pop("conditions", UNSET)

        comment = d.pop("comment", UNSET)

        submit_step_contribution_request = cls(
            contribution_uuid=contribution_uuid,
            step_uuid=step_uuid,
            outcome=outcome,
            conditions=conditions,
            comment=comment,
        )

        submit_step_contribution_request.additional_properties = d
        return submit_step_contribution_request

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
