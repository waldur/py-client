import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.policy_period_enum import PolicyPeriodEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offering_estimated_cost_policy_options import OfferingEstimatedCostPolicyOptions


T = TypeVar("T", bound="OfferingEstimatedCostPolicy")


@_attrs_define
class OfferingEstimatedCostPolicy:
    """
    Attributes:
        uuid (Union[Unset, UUID]):
        url (Union[Unset, str]):
        scope (Union[Unset, str]):
        scope_name (Union[Unset, str]):
        scope_uuid (Union[Unset, UUID]):
        actions (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by_full_name (Union[Unset, str]):
        created_by_username (Union[Unset, str]):
        has_fired (Union[Unset, bool]):
        fired_datetime (Union[Unset, datetime.datetime]):
        options (Union[Unset, OfferingEstimatedCostPolicyOptions]): Fields for saving actions extra data. Keys are name
            of actions.
        affected_resources_count (Union[Unset, int]):
        limit_cost (Union[Unset, int]):
        period (Union[Unset, PolicyPeriodEnum]):
        period_name (Union[Unset, str]):
        current_cost (Union[Unset, str]):
        organization_groups (Union[Unset, list[str]]):
        apply_to_all (Union[Unset, bool]): If True, policy applies to all customers. Mutually exclusive with
            organization_groups.
    """

    uuid: Union[Unset, UUID] = UNSET
    url: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    scope_name: Union[Unset, str] = UNSET
    scope_uuid: Union[Unset, UUID] = UNSET
    actions: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by_full_name: Union[Unset, str] = UNSET
    created_by_username: Union[Unset, str] = UNSET
    has_fired: Union[Unset, bool] = UNSET
    fired_datetime: Union[Unset, datetime.datetime] = UNSET
    options: Union[Unset, "OfferingEstimatedCostPolicyOptions"] = UNSET
    affected_resources_count: Union[Unset, int] = UNSET
    limit_cost: Union[Unset, int] = UNSET
    period: Union[Unset, PolicyPeriodEnum] = UNSET
    period_name: Union[Unset, str] = UNSET
    current_cost: Union[Unset, str] = UNSET
    organization_groups: Union[Unset, list[str]] = UNSET
    apply_to_all: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: Union[Unset, str] = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        url = self.url

        scope = self.scope

        scope_name = self.scope_name

        scope_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.scope_uuid, Unset):
            scope_uuid = str(self.scope_uuid)

        actions = self.actions

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by_full_name = self.created_by_full_name

        created_by_username = self.created_by_username

        has_fired = self.has_fired

        fired_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.fired_datetime, Unset):
            fired_datetime = self.fired_datetime.isoformat()

        options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        affected_resources_count = self.affected_resources_count

        limit_cost = self.limit_cost

        period: Union[Unset, int] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.value

        period_name = self.period_name

        current_cost = self.current_cost

        organization_groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.organization_groups, Unset):
            organization_groups = self.organization_groups

        apply_to_all = self.apply_to_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if url is not UNSET:
            field_dict["url"] = url
        if scope is not UNSET:
            field_dict["scope"] = scope
        if scope_name is not UNSET:
            field_dict["scope_name"] = scope_name
        if scope_uuid is not UNSET:
            field_dict["scope_uuid"] = scope_uuid
        if actions is not UNSET:
            field_dict["actions"] = actions
        if created is not UNSET:
            field_dict["created"] = created
        if created_by_full_name is not UNSET:
            field_dict["created_by_full_name"] = created_by_full_name
        if created_by_username is not UNSET:
            field_dict["created_by_username"] = created_by_username
        if has_fired is not UNSET:
            field_dict["has_fired"] = has_fired
        if fired_datetime is not UNSET:
            field_dict["fired_datetime"] = fired_datetime
        if options is not UNSET:
            field_dict["options"] = options
        if affected_resources_count is not UNSET:
            field_dict["affected_resources_count"] = affected_resources_count
        if limit_cost is not UNSET:
            field_dict["limit_cost"] = limit_cost
        if period is not UNSET:
            field_dict["period"] = period
        if period_name is not UNSET:
            field_dict["period_name"] = period_name
        if current_cost is not UNSET:
            field_dict["current_cost"] = current_cost
        if organization_groups is not UNSET:
            field_dict["organization_groups"] = organization_groups
        if apply_to_all is not UNSET:
            field_dict["apply_to_all"] = apply_to_all

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_estimated_cost_policy_options import OfferingEstimatedCostPolicyOptions

        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: Union[Unset, UUID]
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        url = d.pop("url", UNSET)

        scope = d.pop("scope", UNSET)

        scope_name = d.pop("scope_name", UNSET)

        _scope_uuid = d.pop("scope_uuid", UNSET)
        scope_uuid: Union[Unset, UUID]
        if isinstance(_scope_uuid, Unset):
            scope_uuid = UNSET
        else:
            scope_uuid = UUID(_scope_uuid)

        actions = d.pop("actions", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        created_by_full_name = d.pop("created_by_full_name", UNSET)

        created_by_username = d.pop("created_by_username", UNSET)

        has_fired = d.pop("has_fired", UNSET)

        _fired_datetime = d.pop("fired_datetime", UNSET)
        fired_datetime: Union[Unset, datetime.datetime]
        if isinstance(_fired_datetime, Unset):
            fired_datetime = UNSET
        else:
            fired_datetime = isoparse(_fired_datetime)

        _options = d.pop("options", UNSET)
        options: Union[Unset, OfferingEstimatedCostPolicyOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = OfferingEstimatedCostPolicyOptions.from_dict(_options)

        affected_resources_count = d.pop("affected_resources_count", UNSET)

        limit_cost = d.pop("limit_cost", UNSET)

        _period = d.pop("period", UNSET)
        period: Union[Unset, PolicyPeriodEnum]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = PolicyPeriodEnum(_period)

        period_name = d.pop("period_name", UNSET)

        current_cost = d.pop("current_cost", UNSET)

        organization_groups = cast(list[str], d.pop("organization_groups", UNSET))

        apply_to_all = d.pop("apply_to_all", UNSET)

        offering_estimated_cost_policy = cls(
            uuid=uuid,
            url=url,
            scope=scope,
            scope_name=scope_name,
            scope_uuid=scope_uuid,
            actions=actions,
            created=created,
            created_by_full_name=created_by_full_name,
            created_by_username=created_by_username,
            has_fired=has_fired,
            fired_datetime=fired_datetime,
            options=options,
            affected_resources_count=affected_resources_count,
            limit_cost=limit_cost,
            period=period,
            period_name=period_name,
            current_cost=current_cost,
            organization_groups=organization_groups,
            apply_to_all=apply_to_all,
        )

        offering_estimated_cost_policy.additional_properties = d
        return offering_estimated_cost_policy

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
