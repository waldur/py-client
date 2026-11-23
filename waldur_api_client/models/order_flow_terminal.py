from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_flow_terminal_key_enum import OrderFlowTerminalKeyEnum

T = TypeVar("T", bound="OrderFlowTerminal")


@_attrs_define
class OrderFlowTerminal:
    """
    Attributes:
        key (OrderFlowTerminalKeyEnum):
        from_steps (list[str]):
        retry (bool): Whether an order ending here can be retried.
    """

    key: OrderFlowTerminalKeyEnum
    from_steps: list[str]
    retry: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key.value

        from_steps = self.from_steps

        retry = self.retry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "from_steps": from_steps,
                "retry": retry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = OrderFlowTerminalKeyEnum(d.pop("key"))

        from_steps = cast(list[str], d.pop("from_steps"))

        retry = d.pop("retry")

        order_flow_terminal = cls(
            key=key,
            from_steps=from_steps,
            retry=retry,
        )

        order_flow_terminal.additional_properties = d
        return order_flow_terminal

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
