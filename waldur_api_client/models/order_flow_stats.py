from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.order_flow_state_count import OrderFlowStateCount
    from ..models.order_flow_step_stat import OrderFlowStepStat


T = TypeVar("T", bound="OrderFlowStats")


@_attrs_define
class OrderFlowStats:
    """
    Attributes:
        window_days (int):
        states (list['OrderFlowStateCount']):
        steps (list['OrderFlowStepStat']):
    """

    window_days: int
    states: list["OrderFlowStateCount"]
    steps: list["OrderFlowStepStat"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        window_days = self.window_days

        states = []
        for states_item_data in self.states:
            states_item = states_item_data.to_dict()
            states.append(states_item)

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window_days": window_days,
                "states": states,
                "steps": steps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_flow_state_count import OrderFlowStateCount
        from ..models.order_flow_step_stat import OrderFlowStepStat

        d = dict(src_dict)
        window_days = d.pop("window_days")

        states = []
        _states = d.pop("states")
        for states_item_data in _states:
            states_item = OrderFlowStateCount.from_dict(states_item_data)

            states.append(states_item)

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = OrderFlowStepStat.from_dict(steps_item_data)

            steps.append(steps_item)

        order_flow_stats = cls(
            window_days=window_days,
            states=states,
            steps=steps,
        )

        order_flow_stats.additional_properties = d
        return order_flow_stats

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
