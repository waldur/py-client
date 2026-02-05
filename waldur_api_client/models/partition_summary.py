from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartitionSummary")


@_attrs_define
class PartitionSummary:
    """
    Attributes:
        uuid (Union[Unset, UUID]):
        partition_name (Union[Unset, str]): Name of the SLURM partition
        priority_tier (Union[None, Unset, int]): Priority tier for scheduling and preemption
        qos (Union[Unset, str]): Quality of Service (QOS) name
    """

    uuid: Union[Unset, UUID] = UNSET
    partition_name: Union[Unset, str] = UNSET
    priority_tier: Union[None, Unset, int] = UNSET
    qos: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: Union[Unset, str] = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        partition_name = self.partition_name

        priority_tier: Union[None, Unset, int]
        if isinstance(self.priority_tier, Unset):
            priority_tier = UNSET
        else:
            priority_tier = self.priority_tier

        qos = self.qos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if partition_name is not UNSET:
            field_dict["partition_name"] = partition_name
        if priority_tier is not UNSET:
            field_dict["priority_tier"] = priority_tier
        if qos is not UNSET:
            field_dict["qos"] = qos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: Union[Unset, UUID]
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        partition_name = d.pop("partition_name", UNSET)

        def _parse_priority_tier(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        priority_tier = _parse_priority_tier(d.pop("priority_tier", UNSET))

        qos = d.pop("qos", UNSET)

        partition_summary = cls(
            uuid=uuid,
            partition_name=partition_name,
            priority_tier=priority_tier,
            qos=qos,
        )

        partition_summary.additional_properties = d
        return partition_summary

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
