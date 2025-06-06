from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.period_enum import PeriodEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedOfferingEstimatedCostPolicyRequest")


@_attrs_define
class PatchedOfferingEstimatedCostPolicyRequest:
    """
    Attributes:
        scope (Union[Unset, str]):
        actions (Union[Unset, str]):
        options (Union[Unset, Any]): Fields for saving actions extra data. Keys are name of actions.
        limit_cost (Union[Unset, int]):
        period (Union[Unset, PeriodEnum]):
        organization_groups (Union[Unset, list[str]]):
    """

    scope: Union[Unset, str] = UNSET
    actions: Union[Unset, str] = UNSET
    options: Union[Unset, Any] = UNSET
    limit_cost: Union[Unset, int] = UNSET
    period: Union[Unset, PeriodEnum] = UNSET
    organization_groups: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope = self.scope

        actions = self.actions

        options = self.options

        limit_cost = self.limit_cost

        period: Union[Unset, int] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.value

        organization_groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.organization_groups, Unset):
            organization_groups = self.organization_groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if actions is not UNSET:
            field_dict["actions"] = actions
        if options is not UNSET:
            field_dict["options"] = options
        if limit_cost is not UNSET:
            field_dict["limit_cost"] = limit_cost
        if period is not UNSET:
            field_dict["period"] = period
        if organization_groups is not UNSET:
            field_dict["organization_groups"] = organization_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        scope = d.pop("scope", UNSET)

        actions = d.pop("actions", UNSET)

        options = d.pop("options", UNSET)

        limit_cost = d.pop("limit_cost", UNSET)

        _period = d.pop("period", UNSET)
        period: Union[Unset, PeriodEnum]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = PeriodEnum(_period)

        organization_groups = cast(list[str], d.pop("organization_groups", UNSET))

        patched_offering_estimated_cost_policy_request = cls(
            scope=scope,
            actions=actions,
            options=options,
            limit_cost=limit_cost,
            period=period,
            organization_groups=organization_groups,
        )

        patched_offering_estimated_cost_policy_request.additional_properties = d
        return patched_offering_estimated_cost_policy_request

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
