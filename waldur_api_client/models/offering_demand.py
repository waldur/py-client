import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.call_states import CallStates
from ..models.round_status_enum import RoundStatusEnum
from ..models.state_group_enum import StateGroupEnum

if TYPE_CHECKING:
    from ..models.offering_demand_component import OfferingDemandComponent


T = TypeVar("T", bound="OfferingDemand")


@_attrs_define
class OfferingDemand:
    """
    Attributes:
        offering_uuid (UUID):
        offering_name (str):
        provider_uuid (UUID):
        provider_name (str):
        requested_offering_uuid (UUID):
        call_uuid (UUID):
        call_name (str):
        call_state (CallStates):
        round_uuid (UUID):
        round_name (str):
        round_start_time (datetime.datetime):
        round_cutoff_time (Union[None, datetime.datetime]):
        round_status (RoundStatusEnum):
        state_group (StateGroupEnum):
        proposals_count (int):
        components (list['OfferingDemandComponent']): Empty for closed rows, which only count proposals.
    """

    offering_uuid: UUID
    offering_name: str
    provider_uuid: UUID
    provider_name: str
    requested_offering_uuid: UUID
    call_uuid: UUID
    call_name: str
    call_state: CallStates
    round_uuid: UUID
    round_name: str
    round_start_time: datetime.datetime
    round_cutoff_time: Union[None, datetime.datetime]
    round_status: RoundStatusEnum
    state_group: StateGroupEnum
    proposals_count: int
    components: list["OfferingDemandComponent"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offering_uuid = str(self.offering_uuid)

        offering_name = self.offering_name

        provider_uuid = str(self.provider_uuid)

        provider_name = self.provider_name

        requested_offering_uuid = str(self.requested_offering_uuid)

        call_uuid = str(self.call_uuid)

        call_name = self.call_name

        call_state = self.call_state.value

        round_uuid = str(self.round_uuid)

        round_name = self.round_name

        round_start_time = self.round_start_time.isoformat()

        round_cutoff_time: Union[None, str]
        if isinstance(self.round_cutoff_time, datetime.datetime):
            round_cutoff_time = self.round_cutoff_time.isoformat()
        else:
            round_cutoff_time = self.round_cutoff_time

        round_status = self.round_status.value

        state_group = self.state_group.value

        proposals_count = self.proposals_count

        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()
            components.append(components_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offering_uuid": offering_uuid,
                "offering_name": offering_name,
                "provider_uuid": provider_uuid,
                "provider_name": provider_name,
                "requested_offering_uuid": requested_offering_uuid,
                "call_uuid": call_uuid,
                "call_name": call_name,
                "call_state": call_state,
                "round_uuid": round_uuid,
                "round_name": round_name,
                "round_start_time": round_start_time,
                "round_cutoff_time": round_cutoff_time,
                "round_status": round_status,
                "state_group": state_group,
                "proposals_count": proposals_count,
                "components": components,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_demand_component import OfferingDemandComponent

        d = dict(src_dict)
        offering_uuid = UUID(d.pop("offering_uuid"))

        offering_name = d.pop("offering_name")

        provider_uuid = UUID(d.pop("provider_uuid"))

        provider_name = d.pop("provider_name")

        requested_offering_uuid = UUID(d.pop("requested_offering_uuid"))

        call_uuid = UUID(d.pop("call_uuid"))

        call_name = d.pop("call_name")

        call_state = CallStates(d.pop("call_state"))

        round_uuid = UUID(d.pop("round_uuid"))

        round_name = d.pop("round_name")

        round_start_time = isoparse(d.pop("round_start_time"))

        def _parse_round_cutoff_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_cutoff_time_type_0 = isoparse(data)

                return round_cutoff_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        round_cutoff_time = _parse_round_cutoff_time(d.pop("round_cutoff_time"))

        round_status = RoundStatusEnum(d.pop("round_status"))

        state_group = StateGroupEnum(d.pop("state_group"))

        proposals_count = d.pop("proposals_count")

        components = []
        _components = d.pop("components")
        for components_item_data in _components:
            components_item = OfferingDemandComponent.from_dict(components_item_data)

            components.append(components_item)

        offering_demand = cls(
            offering_uuid=offering_uuid,
            offering_name=offering_name,
            provider_uuid=provider_uuid,
            provider_name=provider_name,
            requested_offering_uuid=requested_offering_uuid,
            call_uuid=call_uuid,
            call_name=call_name,
            call_state=call_state,
            round_uuid=round_uuid,
            round_name=round_name,
            round_start_time=round_start_time,
            round_cutoff_time=round_cutoff_time,
            round_status=round_status,
            state_group=state_group,
            proposals_count=proposals_count,
            components=components,
        )

        offering_demand.additional_properties = d
        return offering_demand

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
