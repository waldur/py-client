from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.offering_demand_pool import OfferingDemandPool


T = TypeVar("T", bound="OfferingDemandComponent")


@_attrs_define
class OfferingDemandComponent:
    """
    Attributes:
        type_ (str):
        name (str):
        measured_unit (str):
        limit_period (str): The period the component is limited per: requested and awarded sum the amounts per this
            period, as stored. 'total' is one amount for the whole allocation.
        requested (float): Summed over the requested resources of the row's proposals.
        awarded (Union[None, float]): Summed over the awarded resources of the row's proposals; accepted rows only.
        call_pool (Union['OfferingDemandPool', None]): The call-wide pool, if the call sets one.
        round_pool (Union['OfferingDemandPool', None]): The round's pool, if the call sets one.
    """

    type_: str
    name: str
    measured_unit: str
    limit_period: str
    requested: float
    awarded: Union[None, float]
    call_pool: Union["OfferingDemandPool", None]
    round_pool: Union["OfferingDemandPool", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.offering_demand_pool import OfferingDemandPool

        type_ = self.type_

        name = self.name

        measured_unit = self.measured_unit

        limit_period = self.limit_period

        requested = self.requested

        awarded: Union[None, float]
        awarded = self.awarded

        call_pool: Union[None, dict[str, Any]]
        if isinstance(self.call_pool, OfferingDemandPool):
            call_pool = self.call_pool.to_dict()
        else:
            call_pool = self.call_pool

        round_pool: Union[None, dict[str, Any]]
        if isinstance(self.round_pool, OfferingDemandPool):
            round_pool = self.round_pool.to_dict()
        else:
            round_pool = self.round_pool

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "measured_unit": measured_unit,
                "limit_period": limit_period,
                "requested": requested,
                "awarded": awarded,
                "call_pool": call_pool,
                "round_pool": round_pool,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_demand_pool import OfferingDemandPool

        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        measured_unit = d.pop("measured_unit")

        limit_period = d.pop("limit_period")

        requested = d.pop("requested")

        def _parse_awarded(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        awarded = _parse_awarded(d.pop("awarded"))

        def _parse_call_pool(data: object) -> Union["OfferingDemandPool", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                call_pool_type_1 = OfferingDemandPool.from_dict(data)

                return call_pool_type_1
            except:  # noqa: E722
                pass
            return cast(Union["OfferingDemandPool", None], data)

        call_pool = _parse_call_pool(d.pop("call_pool"))

        def _parse_round_pool(data: object) -> Union["OfferingDemandPool", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                round_pool_type_1 = OfferingDemandPool.from_dict(data)

                return round_pool_type_1
            except:  # noqa: E722
                pass
            return cast(Union["OfferingDemandPool", None], data)

        round_pool = _parse_round_pool(d.pop("round_pool"))

        offering_demand_component = cls(
            type_=type_,
            name=name,
            measured_unit=measured_unit,
            limit_period=limit_period,
            requested=requested,
            awarded=awarded,
            call_pool=call_pool,
            round_pool=round_pool,
        )

        offering_demand_component.additional_properties = d
        return offering_demand_component

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
