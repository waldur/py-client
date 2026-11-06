from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.eligible_from_enum import EligibleFromEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedCallProposalRoleRequest")


@_attrs_define
class PatchedCallProposalRoleRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        eligible_from (Union[Unset, EligibleFromEnum]):
        min_holders (Union[Unset, int]): How many holders an assignment step for this role needs before it can complete.
        max_holders (Union[None, Unset, int]): How many people may hold the role on one proposal. Empty: no limit.
        allows_lead (Union[Unset, bool]): Whether one holder is marked as the lead.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    eligible_from: Union[Unset, EligibleFromEnum] = UNSET
    min_holders: Union[Unset, int] = UNSET
    max_holders: Union[None, Unset, int] = UNSET
    allows_lead: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        eligible_from: Union[Unset, str] = UNSET
        if not isinstance(self.eligible_from, Unset):
            eligible_from = self.eligible_from.value

        min_holders = self.min_holders

        max_holders: Union[None, Unset, int]
        if isinstance(self.max_holders, Unset):
            max_holders = UNSET
        else:
            max_holders = self.max_holders

        allows_lead = self.allows_lead

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if eligible_from is not UNSET:
            field_dict["eligible_from"] = eligible_from
        if min_holders is not UNSET:
            field_dict["min_holders"] = min_holders
        if max_holders is not UNSET:
            field_dict["max_holders"] = max_holders
        if allows_lead is not UNSET:
            field_dict["allows_lead"] = allows_lead

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _eligible_from = d.pop("eligible_from", UNSET)
        eligible_from: Union[Unset, EligibleFromEnum]
        if isinstance(_eligible_from, Unset):
            eligible_from = UNSET
        else:
            eligible_from = EligibleFromEnum(_eligible_from)

        min_holders = d.pop("min_holders", UNSET)

        def _parse_max_holders(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_holders = _parse_max_holders(d.pop("max_holders", UNSET))

        allows_lead = d.pop("allows_lead", UNSET)

        patched_call_proposal_role_request = cls(
            name=name,
            description=description,
            eligible_from=eligible_from,
            min_holders=min_holders,
            max_holders=max_holders,
            allows_lead=allows_lead,
        )

        patched_call_proposal_role_request.additional_properties = d
        return patched_call_proposal_role_request

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
