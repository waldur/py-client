from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.order_flow_source import OrderFlowSource


T = TypeVar("T", bound="OrderFlowRule")


@_attrs_define
class OrderFlowRule:
    """
    Attributes:
        key (str):
        text (str):
        holds (Union[None, bool]): Null: depends on the order.
        skips (Union[None, bool]): When the rule holds, whether the step is skipped. Null when the rule does not hold or
            the outcome depends on the order.
        reached (bool): False when an earlier rule always decides first.
        sources (list['OrderFlowSource']):
    """

    key: str
    text: str
    holds: Union[None, bool]
    skips: Union[None, bool]
    reached: bool
    sources: list["OrderFlowSource"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        text = self.text

        holds: Union[None, bool]
        holds = self.holds

        skips: Union[None, bool]
        skips = self.skips

        reached = self.reached

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "text": text,
                "holds": holds,
                "skips": skips,
                "reached": reached,
                "sources": sources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_flow_source import OrderFlowSource

        d = dict(src_dict)
        key = d.pop("key")

        text = d.pop("text")

        def _parse_holds(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        holds = _parse_holds(d.pop("holds"))

        def _parse_skips(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        skips = _parse_skips(d.pop("skips"))

        reached = d.pop("reached")

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = OrderFlowSource.from_dict(sources_item_data)

            sources.append(sources_item)

        order_flow_rule = cls(
            key=key,
            text=text,
            holds=holds,
            skips=skips,
            reached=reached,
            sources=sources,
        )

        order_flow_rule.additional_properties = d
        return order_flow_rule

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
