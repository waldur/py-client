from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.order_flow_source import OrderFlowSource


T = TypeVar("T", bound="OrderFlowCheck")


@_attrs_define
class OrderFlowCheck:
    """
    Attributes:
        key (str):
        text (str):
        active (bool): Whether the check is configured for this offering.
        sources (list['OrderFlowSource']):
    """

    key: str
    text: str
    active: bool
    sources: list["OrderFlowSource"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        text = self.text

        active = self.active

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
                "active": active,
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

        active = d.pop("active")

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = OrderFlowSource.from_dict(sources_item_data)

            sources.append(sources_item)

        order_flow_check = cls(
            key=key,
            text=text,
            active=active,
            sources=sources,
        )

        order_flow_check.additional_properties = d
        return order_flow_check

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
