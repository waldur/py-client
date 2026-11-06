from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProposalBudgetEntry")


@_attrs_define
class ProposalBudgetEntry:
    """
    Attributes:
        pool_uuid (UUID):
        offering_name (str):
        component_type (str):
        round_name (Union[None, str]): The round the pool covers; empty for the whole call.
        offered_total (float):
        awarded_so_far (float): Awarded to the other proposals the pool covers.
        remaining (float):
        award (Union[None, float]): What this proposal's award draws from it.
        fits (bool):
    """

    pool_uuid: UUID
    offering_name: str
    component_type: str
    round_name: Union[None, str]
    offered_total: float
    awarded_so_far: float
    remaining: float
    award: Union[None, float]
    fits: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pool_uuid = str(self.pool_uuid)

        offering_name = self.offering_name

        component_type = self.component_type

        round_name: Union[None, str]
        round_name = self.round_name

        offered_total = self.offered_total

        awarded_so_far = self.awarded_so_far

        remaining = self.remaining

        award: Union[None, float]
        award = self.award

        fits = self.fits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pool_uuid": pool_uuid,
                "offering_name": offering_name,
                "component_type": component_type,
                "round_name": round_name,
                "offered_total": offered_total,
                "awarded_so_far": awarded_so_far,
                "remaining": remaining,
                "award": award,
                "fits": fits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pool_uuid = UUID(d.pop("pool_uuid"))

        offering_name = d.pop("offering_name")

        component_type = d.pop("component_type")

        def _parse_round_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        round_name = _parse_round_name(d.pop("round_name"))

        offered_total = d.pop("offered_total")

        awarded_so_far = d.pop("awarded_so_far")

        remaining = d.pop("remaining")

        def _parse_award(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        award = _parse_award(d.pop("award"))

        fits = d.pop("fits")

        proposal_budget_entry = cls(
            pool_uuid=pool_uuid,
            offering_name=offering_name,
            component_type=component_type,
            round_name=round_name,
            offered_total=offered_total,
            awarded_so_far=awarded_so_far,
            remaining=remaining,
            award=award,
            fits=fits,
        )

        proposal_budget_entry.additional_properties = d
        return proposal_budget_entry

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
