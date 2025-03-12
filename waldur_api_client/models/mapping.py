from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sub_net_mapping import SubNetMapping
    from ..models.volume_type_mapping import VolumeTypeMapping


T = TypeVar("T", bound="Mapping")


@_attrs_define
class Mapping:
    """
    Attributes:
        volume_types (Union[Unset, list['VolumeTypeMapping']]):
        subnets (Union[Unset, list['SubNetMapping']]):
        skip_connection_extnet (Union[Unset, bool]):  Default: False.
        networks (Union[Unset, list[UUID]]):
    """

    volume_types: Union[Unset, list["VolumeTypeMapping"]] = UNSET
    subnets: Union[Unset, list["SubNetMapping"]] = UNSET
    skip_connection_extnet: Union[Unset, bool] = False
    networks: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.volume_types, Unset):
            volume_types = []
            for volume_types_item_data in self.volume_types:
                volume_types_item = volume_types_item_data.to_dict()
                volume_types.append(volume_types_item)

        subnets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.subnets, Unset):
            subnets = []
            for subnets_item_data in self.subnets:
                subnets_item = subnets_item_data.to_dict()
                subnets.append(subnets_item)

        skip_connection_extnet = self.skip_connection_extnet

        networks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = str(networks_item_data)
                networks.append(networks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if volume_types is not UNSET:
            field_dict["volume_types"] = volume_types
        if subnets is not UNSET:
            field_dict["subnets"] = subnets
        if skip_connection_extnet is not UNSET:
            field_dict["skip_connection_extnet"] = skip_connection_extnet
        if networks is not UNSET:
            field_dict["networks"] = networks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.sub_net_mapping import SubNetMapping
        from ..models.volume_type_mapping import VolumeTypeMapping

        d = src_dict.copy()
        volume_types = []
        _volume_types = d.pop("volume_types", UNSET)
        for volume_types_item_data in _volume_types or []:
            volume_types_item = VolumeTypeMapping.from_dict(volume_types_item_data)

            volume_types.append(volume_types_item)

        subnets = []
        _subnets = d.pop("subnets", UNSET)
        for subnets_item_data in _subnets or []:
            subnets_item = SubNetMapping.from_dict(subnets_item_data)

            subnets.append(subnets_item)

        skip_connection_extnet = d.pop("skip_connection_extnet", UNSET)

        networks = []
        _networks = d.pop("networks", UNSET)
        for networks_item_data in _networks or []:
            networks_item = UUID(networks_item_data)

            networks.append(networks_item)

        mapping = cls(
            volume_types=volume_types,
            subnets=subnets,
            skip_connection_extnet=skip_connection_extnet,
            networks=networks,
        )

        mapping.additional_properties = d
        return mapping

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
