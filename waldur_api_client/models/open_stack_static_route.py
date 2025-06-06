from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenStackStaticRoute")


@_attrs_define
class OpenStackStaticRoute:
    """
    Attributes:
        destination (Union[Unset, str]):
        nexthop (Union[Unset, str]):
    """

    destination: Union[Unset, str] = UNSET
    nexthop: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination = self.destination

        nexthop = self.nexthop

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination
        if nexthop is not UNSET:
            field_dict["nexthop"] = nexthop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        destination = d.pop("destination", UNSET)

        nexthop = d.pop("nexthop", UNSET)

        open_stack_static_route = cls(
            destination=destination,
            nexthop=nexthop,
        )

        open_stack_static_route.additional_properties = d
        return open_stack_static_route

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
