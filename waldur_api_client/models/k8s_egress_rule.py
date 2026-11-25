from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.destination_type_enum import DestinationTypeEnum
from ..models.k8s_egress_rule_protocol_enum import K8SEgressRuleProtocolEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="K8SEgressRule")


@_attrs_define
class K8SEgressRule:
    """
    Attributes:
        name (str):
        destination_type (DestinationTypeEnum):
        destination (str): An IPv4 or IPv6 network for a cidr rule; a domain name, optionally led by a *. wildcard, for
            a domain rule.
        uuid (Union[Unset, str]): A client-side row id, kept as given. Ignored by the server.
        protocol (Union[BlankEnum, K8SEgressRuleProtocolEnum, None, Unset]): Empty for any protocol.
        port_range_min (Union[None, Unset, int]): Empty for any port.
        port_range_max (Union[None, Unset, int]): Empty for a single port, port_range_min.
        description (Union[None, Unset, str]):
    """

    name: str
    destination_type: DestinationTypeEnum
    destination: str
    uuid: Union[Unset, str] = UNSET
    protocol: Union[BlankEnum, K8SEgressRuleProtocolEnum, None, Unset] = UNSET
    port_range_min: Union[None, Unset, int] = UNSET
    port_range_max: Union[None, Unset, int] = UNSET
    description: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        destination_type = self.destination_type.value

        destination = self.destination

        uuid = self.uuid

        protocol: Union[None, Unset, str]
        if isinstance(self.protocol, Unset):
            protocol = UNSET
        elif isinstance(self.protocol, K8SEgressRuleProtocolEnum):
            protocol = self.protocol.value
        elif isinstance(self.protocol, BlankEnum):
            protocol = self.protocol.value
        else:
            protocol = self.protocol

        port_range_min: Union[None, Unset, int]
        if isinstance(self.port_range_min, Unset):
            port_range_min = UNSET
        else:
            port_range_min = self.port_range_min

        port_range_max: Union[None, Unset, int]
        if isinstance(self.port_range_max, Unset):
            port_range_max = UNSET
        else:
            port_range_max = self.port_range_max

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "destination_type": destination_type,
                "destination": destination,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if port_range_min is not UNSET:
            field_dict["port_range_min"] = port_range_min
        if port_range_max is not UNSET:
            field_dict["port_range_max"] = port_range_max
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        destination_type = DestinationTypeEnum(d.pop("destination_type"))

        destination = d.pop("destination")

        uuid = d.pop("uuid", UNSET)

        def _parse_protocol(data: object) -> Union[BlankEnum, K8SEgressRuleProtocolEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                protocol_type_0 = K8SEgressRuleProtocolEnum(data)

                return protocol_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                protocol_type_1 = BlankEnum(data)

                return protocol_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, K8SEgressRuleProtocolEnum, None, Unset], data)

        protocol = _parse_protocol(d.pop("protocol", UNSET))

        def _parse_port_range_min(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port_range_min = _parse_port_range_min(d.pop("port_range_min", UNSET))

        def _parse_port_range_max(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port_range_max = _parse_port_range_max(d.pop("port_range_max", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        k8s_egress_rule = cls(
            name=name,
            destination_type=destination_type,
            destination=destination,
            uuid=uuid,
            protocol=protocol,
            port_range_min=port_range_min,
            port_range_max=port_range_max,
            description=description,
        )

        k8s_egress_rule.additional_properties = d
        return k8s_egress_rule

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
