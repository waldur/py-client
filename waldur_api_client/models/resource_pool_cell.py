from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResourcePoolCell")


@_attrs_define
class ResourcePoolCell:
    """
    Attributes:
        round_uuid (Union[None, UUID]): Empty: the whole call.
        round_name (Union[None, str]):
        pool_uuid (Union[None, UUID]):
        offered_total (Union[None, float]): Empty: the cell has no pool.
        requested (float):
        awarded (float):
        remaining (Union[None, float]):
    """

    round_uuid: Union[None, UUID]
    round_name: Union[None, str]
    pool_uuid: Union[None, UUID]
    offered_total: Union[None, float]
    requested: float
    awarded: float
    remaining: Union[None, float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        offered_total: Union[None, float]
        offered_total = self.offered_total

        requested = self.requested

        awarded = self.awarded

        remaining: Union[None, float]
        remaining = self.remaining

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "round_uuid": round_uuid,
                "round_name": round_name,
                "pool_uuid": pool_uuid,
                "offered_total": offered_total,
                "requested": requested,
                "awarded": awarded,
                "remaining": remaining,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        resource_pool_cell = cls(
            round_uuid=round_uuid,
            round_name=round_name,
            pool_uuid=pool_uuid,
            offered_total=offered_total,
            requested=requested,
            awarded=awarded,
            remaining=remaining,
        )

        resource_pool_cell.additional_properties = d
        return resource_pool_cell

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
