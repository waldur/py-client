from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_flow_source_kind_enum import OrderFlowSourceKindEnum

if TYPE_CHECKING:
    from ..models.order_flow_source_value_type_0 import OrderFlowSourceValueType0


T = TypeVar("T", bound="OrderFlowSource")


@_attrs_define
class OrderFlowSource:
    """
    Attributes:
        kind (OrderFlowSourceKindEnum):
        field (str):
        editable (bool): Whether the offering's provider can change it.
        value (Union['OrderFlowSourceValueType0', None]): Current value, for settings that have one.
    """

    kind: OrderFlowSourceKindEnum
    field: str
    editable: bool
    value: Union["OrderFlowSourceValueType0", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.order_flow_source_value_type_0 import OrderFlowSourceValueType0

        kind = self.kind.value

        field = self.field

        editable = self.editable

        value: Union[None, dict[str, Any]]
        if isinstance(self.value, OrderFlowSourceValueType0):
            value = self.value.to_dict()
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "field": field,
                "editable": editable,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_flow_source_value_type_0 import OrderFlowSourceValueType0

        d = dict(src_dict)
        kind = OrderFlowSourceKindEnum(d.pop("kind"))

        field = d.pop("field")

        editable = d.pop("editable")

        def _parse_value(data: object) -> Union["OrderFlowSourceValueType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = OrderFlowSourceValueType0.from_dict(data)

                return value_type_0
            except:  # noqa: E722
                pass
            return cast(Union["OrderFlowSourceValueType0", None], data)

        value = _parse_value(d.pop("value"))

        order_flow_source = cls(
            kind=kind,
            field=field,
            editable=editable,
            value=value,
        )

        order_flow_source.additional_properties = d
        return order_flow_source

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
