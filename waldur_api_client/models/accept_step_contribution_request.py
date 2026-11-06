from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AcceptStepContributionRequest")


@_attrs_define
class AcceptStepContributionRequest:
    """
    Attributes:
        contribution_uuid (UUID):
        confirm_no_conflict (Union[Unset, bool]): Confirms having no conflict of interest with the proposal; required on
            a step that asks its evaluators to. Default: False.
    """

    contribution_uuid: UUID
    confirm_no_conflict: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contribution_uuid = str(self.contribution_uuid)

        confirm_no_conflict = self.confirm_no_conflict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contribution_uuid": contribution_uuid,
            }
        )
        if confirm_no_conflict is not UNSET:
            field_dict["confirm_no_conflict"] = confirm_no_conflict

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contribution_uuid = UUID(d.pop("contribution_uuid"))

        confirm_no_conflict = d.pop("confirm_no_conflict", UNSET)

        accept_step_contribution_request = cls(
            contribution_uuid=contribution_uuid,
            confirm_no_conflict=confirm_no_conflict,
        )

        accept_step_contribution_request.additional_properties = d
        return accept_step_contribution_request

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
