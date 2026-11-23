from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_flow_actor_enum import OrderFlowActorEnum
from ..models.order_flow_step_key_enum import OrderFlowStepKeyEnum
from ..models.order_flow_step_mode_enum import OrderFlowStepModeEnum
from ..models.order_flow_step_status_enum import OrderFlowStepStatusEnum

if TYPE_CHECKING:
    from ..models.order_flow_rule import OrderFlowRule
    from ..models.order_flow_source import OrderFlowSource


T = TypeVar("T", bound="OrderFlowStep")


@_attrs_define
class OrderFlowStep:
    """
    Attributes:
        key (OrderFlowStepKeyEnum):
        label (str):
        actor (OrderFlowActorEnum):
        status (OrderFlowStepStatusEnum):
        summary (str):
        rules (list['OrderFlowRule']):
        sources (list['OrderFlowSource']):
        notes (list[str]):
        can_reject (bool):
        mode (Union[None, OrderFlowStepModeEnum]): Execution only: done when processing returns, or when something
            outside Waldur reports back.
    """

    key: OrderFlowStepKeyEnum
    label: str
    actor: OrderFlowActorEnum
    status: OrderFlowStepStatusEnum
    summary: str
    rules: list["OrderFlowRule"]
    sources: list["OrderFlowSource"]
    notes: list[str]
    can_reject: bool
    mode: Union[None, OrderFlowStepModeEnum]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key.value

        label = self.label

        actor = self.actor.value

        status = self.status.value

        summary = self.summary

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        notes = self.notes

        can_reject = self.can_reject

        mode: Union[None, str]
        if isinstance(self.mode, OrderFlowStepModeEnum):
            mode = self.mode.value
        else:
            mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "actor": actor,
                "status": status,
                "summary": summary,
                "rules": rules,
                "sources": sources,
                "notes": notes,
                "can_reject": can_reject,
                "mode": mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_flow_rule import OrderFlowRule
        from ..models.order_flow_source import OrderFlowSource

        d = dict(src_dict)
        key = OrderFlowStepKeyEnum(d.pop("key"))

        label = d.pop("label")

        actor = OrderFlowActorEnum(d.pop("actor"))

        status = OrderFlowStepStatusEnum(d.pop("status"))

        summary = d.pop("summary")

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = OrderFlowRule.from_dict(rules_item_data)

            rules.append(rules_item)

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = OrderFlowSource.from_dict(sources_item_data)

            sources.append(sources_item)

        notes = cast(list[str], d.pop("notes"))

        can_reject = d.pop("can_reject")

        def _parse_mode(data: object) -> Union[None, OrderFlowStepModeEnum]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_0 = OrderFlowStepModeEnum(data)

                return mode_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, OrderFlowStepModeEnum], data)

        mode = _parse_mode(d.pop("mode"))

        order_flow_step = cls(
            key=key,
            label=label,
            actor=actor,
            status=status,
            summary=summary,
            rules=rules,
            sources=sources,
            notes=notes,
            can_reject=can_reject,
            mode=mode,
        )

        order_flow_step.additional_properties = d
        return order_flow_step

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
