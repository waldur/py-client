from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_flow_actor_enum import OrderFlowActorEnum

T = TypeVar("T", bound="OrderFlowActor")


@_attrs_define
class OrderFlowActor:
    """
    Attributes:
        key (OrderFlowActorEnum):
        label (str):
    """

    key: OrderFlowActorEnum
    label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key.value

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = OrderFlowActorEnum(d.pop("key"))

        label = d.pop("label")

        order_flow_actor = cls(
            key=key,
            label=label,
        )

        order_flow_actor.additional_properties = d
        return order_flow_actor

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
