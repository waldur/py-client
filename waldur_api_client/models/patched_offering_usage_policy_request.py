import json
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.period_enum import PeriodEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_offering_component_limit_request import NestedOfferingComponentLimitRequest


T = TypeVar("T", bound="PatchedOfferingUsagePolicyRequest")


@_attrs_define
class PatchedOfferingUsagePolicyRequest:
    """
    Attributes:
        scope (Union[Unset, str]):
        actions (Union[Unset, str]):
        options (Union[Unset, Any]): Fields for saving actions extra data. Keys are name of actions.
        organization_groups (Union[Unset, list[str]]):
        component_limits_set (Union[Unset, list['NestedOfferingComponentLimitRequest']]):
        period (Union[Unset, PeriodEnum]):
    """

    scope: Union[Unset, str] = UNSET
    actions: Union[Unset, str] = UNSET
    options: Union[Unset, Any] = UNSET
    organization_groups: Union[Unset, list[str]] = UNSET
    component_limits_set: Union[Unset, list["NestedOfferingComponentLimitRequest"]] = UNSET
    period: Union[Unset, PeriodEnum] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope = self.scope

        actions = self.actions

        options = self.options

        organization_groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.organization_groups, Unset):
            organization_groups = self.organization_groups

        component_limits_set: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.component_limits_set, Unset):
            component_limits_set = []
            for component_limits_set_item_data in self.component_limits_set:
                component_limits_set_item = component_limits_set_item_data.to_dict()
                component_limits_set.append(component_limits_set_item)

        period: Union[Unset, int] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if actions is not UNSET:
            field_dict["actions"] = actions
        if options is not UNSET:
            field_dict["options"] = options
        if organization_groups is not UNSET:
            field_dict["organization_groups"] = organization_groups
        if component_limits_set is not UNSET:
            field_dict["component_limits_set"] = component_limits_set
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        scope = self.scope if isinstance(self.scope, Unset) else (None, str(self.scope).encode(), "text/plain")

        actions = self.actions if isinstance(self.actions, Unset) else (None, str(self.actions).encode(), "text/plain")

        options = self.options if isinstance(self.options, Unset) else (None, str(self.options).encode(), "text/plain")

        organization_groups: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.organization_groups, Unset):
            _temp_organization_groups = self.organization_groups
            organization_groups = (None, json.dumps(_temp_organization_groups).encode(), "application/json")

        component_limits_set: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.component_limits_set, Unset):
            _temp_component_limits_set = []
            for component_limits_set_item_data in self.component_limits_set:
                component_limits_set_item = component_limits_set_item_data.to_dict()
                _temp_component_limits_set.append(component_limits_set_item)
            component_limits_set = (None, json.dumps(_temp_component_limits_set).encode(), "application/json")

        period: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.period, Unset):
            period = (None, str(self.period.value).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if actions is not UNSET:
            field_dict["actions"] = actions
        if options is not UNSET:
            field_dict["options"] = options
        if organization_groups is not UNSET:
            field_dict["organization_groups"] = organization_groups
        if component_limits_set is not UNSET:
            field_dict["component_limits_set"] = component_limits_set
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.nested_offering_component_limit_request import NestedOfferingComponentLimitRequest

        d = src_dict.copy()
        scope = d.pop("scope", UNSET)

        actions = d.pop("actions", UNSET)

        options = d.pop("options", UNSET)

        organization_groups = cast(list[str], d.pop("organization_groups", UNSET))

        component_limits_set = []
        _component_limits_set = d.pop("component_limits_set", UNSET)
        for component_limits_set_item_data in _component_limits_set or []:
            component_limits_set_item = NestedOfferingComponentLimitRequest.from_dict(component_limits_set_item_data)

            component_limits_set.append(component_limits_set_item)

        _period = d.pop("period", UNSET)
        period: Union[Unset, PeriodEnum]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = PeriodEnum(_period)

        patched_offering_usage_policy_request = cls(
            scope=scope,
            actions=actions,
            options=options,
            organization_groups=organization_groups,
            component_limits_set=component_limits_set,
            period=period,
        )

        patched_offering_usage_policy_request.additional_properties = d
        return patched_offering_usage_policy_request

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
