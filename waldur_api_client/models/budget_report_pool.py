from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BudgetReportPool")


@_attrs_define
class BudgetReportPool:
    """
    Attributes:
        call_uuid (UUID):
        call_name (str):
        call_slug (str):
        organisation_uuid (UUID): The call's call managing organization.
        organisation_name (str): The name of the call managing organization's customer.
        round_uuid (Union[None, UUID]): Empty: the whole call.
        round_name (Union[None, str]):
        pool_uuid (Union[None, UUID]): Empty: no pool, only what was awarded or asked for.
        within_call_pool (bool): A round's pool whose awards also count against the call-wide pool listed in another
            row: leave it out of sums. A call-wide pool is listed with its whole call's figures also when the report is
            filtered to a round.
        offering_name (str):
        component_type (str):
        component_name (str):
        measured_unit (str):
        limit_period (str):
        offered_total (Union[None, float]):
        requested (float): Asked for by submitted proposals, whatever came of them.
        awarded (float): What the allocation decisions granted, over the whole length of each award.
        remaining (Union[None, float]):
        undecided (float): Asked for by proposals still waiting for their decision.
        awarded_share (Union[None, float]): Awarded out of offered, 0-1.
    """

    call_uuid: UUID
    call_name: str
    call_slug: str
    organisation_uuid: UUID
    organisation_name: str
    round_uuid: Union[None, UUID]
    round_name: Union[None, str]
    pool_uuid: Union[None, UUID]
    within_call_pool: bool
    offering_name: str
    component_type: str
    component_name: str
    measured_unit: str
    limit_period: str
    offered_total: Union[None, float]
    requested: float
    awarded: float
    remaining: Union[None, float]
    undecided: float
    awarded_share: Union[None, float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_uuid = str(self.call_uuid)

        call_name = self.call_name

        call_slug = self.call_slug

        organisation_uuid = str(self.organisation_uuid)

        organisation_name = self.organisation_name

        round_uuid: Union[None, str]
        if isinstance(self.round_uuid, UUID):
            round_uuid = str(self.round_uuid)
        else:
            round_uuid = self.round_uuid

        round_name: Union[None, str]
        round_name = self.round_name

        pool_uuid: Union[None, str]
        if isinstance(self.pool_uuid, UUID):
            pool_uuid = str(self.pool_uuid)
        else:
            pool_uuid = self.pool_uuid

        within_call_pool = self.within_call_pool

        offering_name = self.offering_name

        component_type = self.component_type

        component_name = self.component_name

        measured_unit = self.measured_unit

        limit_period = self.limit_period

        offered_total: Union[None, float]
        offered_total = self.offered_total

        requested = self.requested

        awarded = self.awarded

        remaining: Union[None, float]
        remaining = self.remaining

        undecided = self.undecided

        awarded_share: Union[None, float]
        awarded_share = self.awarded_share

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "call_uuid": call_uuid,
                "call_name": call_name,
                "call_slug": call_slug,
                "organisation_uuid": organisation_uuid,
                "organisation_name": organisation_name,
                "round_uuid": round_uuid,
                "round_name": round_name,
                "pool_uuid": pool_uuid,
                "within_call_pool": within_call_pool,
                "offering_name": offering_name,
                "component_type": component_type,
                "component_name": component_name,
                "measured_unit": measured_unit,
                "limit_period": limit_period,
                "offered_total": offered_total,
                "requested": requested,
                "awarded": awarded,
                "remaining": remaining,
                "undecided": undecided,
                "awarded_share": awarded_share,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        call_uuid = UUID(d.pop("call_uuid"))

        call_name = d.pop("call_name")

        call_slug = d.pop("call_slug")

        organisation_uuid = UUID(d.pop("organisation_uuid"))

        organisation_name = d.pop("organisation_name")

        def _parse_round_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_uuid_type_0 = UUID(data)

                return round_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        round_uuid = _parse_round_uuid(d.pop("round_uuid"))

        def _parse_round_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        round_name = _parse_round_name(d.pop("round_name"))

        def _parse_pool_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pool_uuid_type_0 = UUID(data)

                return pool_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        pool_uuid = _parse_pool_uuid(d.pop("pool_uuid"))

        within_call_pool = d.pop("within_call_pool")

        offering_name = d.pop("offering_name")

        component_type = d.pop("component_type")

        component_name = d.pop("component_name")

        measured_unit = d.pop("measured_unit")

        limit_period = d.pop("limit_period")

        def _parse_offered_total(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        offered_total = _parse_offered_total(d.pop("offered_total"))

        requested = d.pop("requested")

        awarded = d.pop("awarded")

        def _parse_remaining(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        remaining = _parse_remaining(d.pop("remaining"))

        undecided = d.pop("undecided")

        def _parse_awarded_share(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        awarded_share = _parse_awarded_share(d.pop("awarded_share"))

        budget_report_pool = cls(
            call_uuid=call_uuid,
            call_name=call_name,
            call_slug=call_slug,
            organisation_uuid=organisation_uuid,
            organisation_name=organisation_name,
            round_uuid=round_uuid,
            round_name=round_name,
            pool_uuid=pool_uuid,
            within_call_pool=within_call_pool,
            offering_name=offering_name,
            component_type=component_type,
            component_name=component_name,
            measured_unit=measured_unit,
            limit_period=limit_period,
            offered_total=offered_total,
            requested=requested,
            awarded=awarded,
            remaining=remaining,
            undecided=undecided,
            awarded_share=awarded_share,
        )

        budget_report_pool.additional_properties = d
        return budget_report_pool

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
