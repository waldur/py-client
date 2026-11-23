from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_flow_orderer_kind_enum import OrderFlowOrdererKindEnum

T = TypeVar("T", bound="OrderFlowOrderer")


@_attrs_define
class OrderFlowOrderer:
    """
    Attributes:
        kind (OrderFlowOrdererKindEnum):
        role (Union[None, str]):
        label (str):
    """

    kind: OrderFlowOrdererKindEnum
    role: Union[None, str]
    label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        role: Union[None, str]
        role = self.role

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "role": role,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = OrderFlowOrdererKindEnum(d.pop("kind"))

        def _parse_role(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        role = _parse_role(d.pop("role"))

        label = d.pop("label")

        order_flow_orderer = cls(
            kind=kind,
            role=role,
            label=label,
        )

        order_flow_orderer.additional_properties = d
        return order_flow_orderer

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
