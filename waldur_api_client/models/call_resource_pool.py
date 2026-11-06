import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallResourcePool")


@_attrs_define
class CallResourcePool:
    """
    Attributes:
        uuid (UUID):
        url (str):
        requested_offering_uuid (UUID):
        offering_name (str):
        component_type (str): Type of the offering component: one billed by its limit that the call offering's plan
            prices.
        round_name (Union[None, str]):
        offered_total (float):
        created (datetime.datetime):
        offering_component_uuid (Union[Unset, UUID]): The component rule of a call offering the pool is of. Or name the
            offering and component instead: a component without a rule gets one bounding nothing.
        round_uuid (Union[None, UUID, Unset]): The round the pool covers. Empty: the whole call.
    """

    uuid: UUID
    url: str
    requested_offering_uuid: UUID
    offering_name: str
    component_type: str
    round_name: Union[None, str]
    offered_total: float
    created: datetime.datetime
    offering_component_uuid: Union[Unset, UUID] = UNSET
    round_uuid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        url = self.url

        requested_offering_uuid = str(self.requested_offering_uuid)

        offering_name = self.offering_name

        component_type = self.component_type

        round_name: Union[None, str]
        round_name = self.round_name

        offered_total = self.offered_total

        created = self.created.isoformat()

        offering_component_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.offering_component_uuid, Unset):
            offering_component_uuid = str(self.offering_component_uuid)

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
                "uuid": uuid,
                "url": url,
                "requested_offering_uuid": requested_offering_uuid,
                "offering_name": offering_name,
                "component_type": component_type,
                "round_name": round_name,
                "offered_total": offered_total,
                "created": created,
            }
        )
        if offering_component_uuid is not UNSET:
            field_dict["offering_component_uuid"] = offering_component_uuid
        if round_uuid is not UNSET:
            field_dict["round_uuid"] = round_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        url = d.pop("url")

        requested_offering_uuid = UUID(d.pop("requested_offering_uuid"))

        offering_name = d.pop("offering_name")

        component_type = d.pop("component_type")

        def _parse_round_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        round_name = _parse_round_name(d.pop("round_name"))

        offered_total = d.pop("offered_total")

        created = isoparse(d.pop("created"))

        _offering_component_uuid = d.pop("offering_component_uuid", UNSET)
        offering_component_uuid: Union[Unset, UUID]
        if isinstance(_offering_component_uuid, Unset):
            offering_component_uuid = UNSET
        else:
            offering_component_uuid = UUID(_offering_component_uuid)

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

        call_resource_pool = cls(
            uuid=uuid,
            url=url,
            requested_offering_uuid=requested_offering_uuid,
            offering_name=offering_name,
            component_type=component_type,
            round_name=round_name,
            offered_total=offered_total,
            created=created,
            offering_component_uuid=offering_component_uuid,
            round_uuid=round_uuid,
        )

        call_resource_pool.additional_properties = d
        return call_resource_pool

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
