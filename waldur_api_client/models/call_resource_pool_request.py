from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallResourcePoolRequest")


@_attrs_define
class CallResourcePoolRequest:
    """
    Attributes:
        offered_total (float):
        offering_component_uuid (Union[Unset, UUID]): The component rule of a call offering the pool is of. Or name the
            offering and component instead: a component without a rule gets one bounding nothing.
        requested_offering (Union[Unset, UUID]): With component: the call offering the pool is of.
        component (Union[Unset, str]): With requested_offering: the type of the component.
        round_uuid (Union[None, UUID, Unset]): The round the pool covers. Empty: the whole call.
    """

    offered_total: float
    offering_component_uuid: Union[Unset, UUID] = UNSET
    requested_offering: Union[Unset, UUID] = UNSET
    component: Union[Unset, str] = UNSET
    round_uuid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offered_total = self.offered_total

        offering_component_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.offering_component_uuid, Unset):
            offering_component_uuid = str(self.offering_component_uuid)

        requested_offering: Union[Unset, str] = UNSET
        if not isinstance(self.requested_offering, Unset):
            requested_offering = str(self.requested_offering)

        component = self.component

        round_uuid: Union[None, Unset, str]
        if isinstance(self.round_uuid, Unset):
            round_uuid = UNSET
        elif isinstance(self.round_uuid, UUID):
            round_uuid = str(self.round_uuid)
        else:
            round_uuid = self.round_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offered_total": offered_total,
            }
        )
        if offering_component_uuid is not UNSET:
            field_dict["offering_component_uuid"] = offering_component_uuid
        if requested_offering is not UNSET:
            field_dict["requested_offering"] = requested_offering
        if component is not UNSET:
            field_dict["component"] = component
        if round_uuid is not UNSET:
            field_dict["round_uuid"] = round_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offered_total = d.pop("offered_total")

        _offering_component_uuid = d.pop("offering_component_uuid", UNSET)
        offering_component_uuid: Union[Unset, UUID]
        if isinstance(_offering_component_uuid, Unset):
            offering_component_uuid = UNSET
        else:
            offering_component_uuid = UUID(_offering_component_uuid)

        _requested_offering = d.pop("requested_offering", UNSET)
        requested_offering: Union[Unset, UUID]
        if isinstance(_requested_offering, Unset):
            requested_offering = UNSET
        else:
            requested_offering = UUID(_requested_offering)

        component = d.pop("component", UNSET)

        def _parse_round_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_uuid_type_0 = UUID(data)

                return round_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        round_uuid = _parse_round_uuid(d.pop("round_uuid", UNSET))

        call_resource_pool_request = cls(
            offered_total=offered_total,
            offering_component_uuid=offering_component_uuid,
            requested_offering=requested_offering,
            component=component,
            round_uuid=round_uuid,
        )

        call_resource_pool_request.additional_properties = d
        return call_resource_pool_request

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
