import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.period_enum import PeriodEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferingEstimatedCostPolicy")


@_attrs_define
class OfferingEstimatedCostPolicy:
    """
    Attributes:
        uuid (UUID):
        url (str):
        scope (str):
        scope_name (str):
        scope_uuid (UUID):
        actions (str):
        created (datetime.datetime):
        created_by_full_name (str):
        created_by_username (str):
        has_fired (bool):
        fired_datetime (datetime.datetime):
        limit_cost (int):
        period_name (str):
        organization_groups (list[str]):
        options (Union[Unset, Any]): Fields for saving actions extra data. Keys are name of actions.
        period (Union[Unset, PeriodEnum]):
    """

    uuid: UUID
    url: str
    scope: str
    scope_name: str
    scope_uuid: UUID
    actions: str
    created: datetime.datetime
    created_by_full_name: str
    created_by_username: str
    has_fired: bool
    fired_datetime: datetime.datetime
    limit_cost: int
    period_name: str
    organization_groups: list[str]
    options: Union[Unset, Any] = UNSET
    period: Union[Unset, PeriodEnum] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        url = self.url

        scope = self.scope

        scope_name = self.scope_name

        scope_uuid = str(self.scope_uuid)

        actions = self.actions

        created = self.created.isoformat()

        created_by_full_name = self.created_by_full_name

        created_by_username = self.created_by_username

        has_fired = self.has_fired

        fired_datetime = self.fired_datetime.isoformat()

        limit_cost = self.limit_cost

        period_name = self.period_name

        organization_groups = self.organization_groups

        options = self.options

        period: Union[Unset, int] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "url": url,
                "scope": scope,
                "scope_name": scope_name,
                "scope_uuid": scope_uuid,
                "actions": actions,
                "created": created,
                "created_by_full_name": created_by_full_name,
                "created_by_username": created_by_username,
                "has_fired": has_fired,
                "fired_datetime": fired_datetime,
                "limit_cost": limit_cost,
                "period_name": period_name,
                "organization_groups": organization_groups,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = UUID(d.pop("uuid"))

        url = d.pop("url")

        scope = d.pop("scope")

        scope_name = d.pop("scope_name")

        scope_uuid = UUID(d.pop("scope_uuid"))

        actions = d.pop("actions")

        created = isoparse(d.pop("created"))

        created_by_full_name = d.pop("created_by_full_name")

        created_by_username = d.pop("created_by_username")

        has_fired = d.pop("has_fired")

        fired_datetime = isoparse(d.pop("fired_datetime"))

        limit_cost = d.pop("limit_cost")

        period_name = d.pop("period_name")

        organization_groups = cast(list[str], d.pop("organization_groups"))

        options = d.pop("options", UNSET)

        _period = d.pop("period", UNSET)
        period: Union[Unset, PeriodEnum]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = PeriodEnum(_period)

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
            limit_cost=limit_cost,
            period_name=period_name,
            organization_groups=organization_groups,
            options=options,
            period=period,
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
