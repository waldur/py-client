from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.order_flow_actor import OrderFlowActor
    from ..models.order_flow_check import OrderFlowCheck
    from ..models.order_flow_offering import OrderFlowOffering
    from ..models.order_flow_order_kind import OrderFlowOrderKind
    from ..models.order_flow_orderer import OrderFlowOrderer
    from ..models.order_flow_stats import OrderFlowStats
    from ..models.order_flow_step import OrderFlowStep
    from ..models.order_flow_terminal import OrderFlowTerminal


T = TypeVar("T", bound="OrderFlowDescription")


@_attrs_define
class OrderFlowDescription:
    """
    Attributes:
        offering (OrderFlowOffering):
        order_kind (str):
        supported (bool): Whether the offering processes this kind of order at all.
        reason (str):
        orderer (OrderFlowOrderer):
        order_kinds (list['OrderFlowOrderKind']):
        orderers (list['OrderFlowOrderer']):
        actors (list['OrderFlowActor']):
        checks (list['OrderFlowCheck']):
        steps (list['OrderFlowStep']):
        terminals (list['OrderFlowTerminal']):
        stats (Union['OrderFlowStats', None]):
    """

    offering: "OrderFlowOffering"
    order_kind: str
    supported: bool
    reason: str
    orderer: "OrderFlowOrderer"
    order_kinds: list["OrderFlowOrderKind"]
    orderers: list["OrderFlowOrderer"]
    actors: list["OrderFlowActor"]
    checks: list["OrderFlowCheck"]
    steps: list["OrderFlowStep"]
    terminals: list["OrderFlowTerminal"]
    stats: Union["OrderFlowStats", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.order_flow_stats import OrderFlowStats

        offering = self.offering.to_dict()

        order_kind = self.order_kind

        supported = self.supported

        reason = self.reason

        orderer = self.orderer.to_dict()

        order_kinds = []
        for order_kinds_item_data in self.order_kinds:
            order_kinds_item = order_kinds_item_data.to_dict()
            order_kinds.append(order_kinds_item)

        orderers = []
        for orderers_item_data in self.orderers:
            orderers_item = orderers_item_data.to_dict()
            orderers.append(orderers_item)

        actors = []
        for actors_item_data in self.actors:
            actors_item = actors_item_data.to_dict()
            actors.append(actors_item)

        checks = []
        for checks_item_data in self.checks:
            checks_item = checks_item_data.to_dict()
            checks.append(checks_item)

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        terminals = []
        for terminals_item_data in self.terminals:
            terminals_item = terminals_item_data.to_dict()
            terminals.append(terminals_item)

        stats: Union[None, dict[str, Any]]
        if isinstance(self.stats, OrderFlowStats):
            stats = self.stats.to_dict()
        else:
            stats = self.stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offering": offering,
                "order_kind": order_kind,
                "supported": supported,
                "reason": reason,
                "orderer": orderer,
                "order_kinds": order_kinds,
                "orderers": orderers,
                "actors": actors,
                "checks": checks,
                "steps": steps,
                "terminals": terminals,
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_flow_actor import OrderFlowActor
        from ..models.order_flow_check import OrderFlowCheck
        from ..models.order_flow_offering import OrderFlowOffering
        from ..models.order_flow_order_kind import OrderFlowOrderKind
        from ..models.order_flow_orderer import OrderFlowOrderer
        from ..models.order_flow_stats import OrderFlowStats
        from ..models.order_flow_step import OrderFlowStep
        from ..models.order_flow_terminal import OrderFlowTerminal

        d = dict(src_dict)
        offering = OrderFlowOffering.from_dict(d.pop("offering"))

        order_kind = d.pop("order_kind")

        supported = d.pop("supported")

        reason = d.pop("reason")

        orderer = OrderFlowOrderer.from_dict(d.pop("orderer"))

        order_kinds = []
        _order_kinds = d.pop("order_kinds")
        for order_kinds_item_data in _order_kinds:
            order_kinds_item = OrderFlowOrderKind.from_dict(order_kinds_item_data)

            order_kinds.append(order_kinds_item)

        orderers = []
        _orderers = d.pop("orderers")
        for orderers_item_data in _orderers:
            orderers_item = OrderFlowOrderer.from_dict(orderers_item_data)

            orderers.append(orderers_item)

        actors = []
        _actors = d.pop("actors")
        for actors_item_data in _actors:
            actors_item = OrderFlowActor.from_dict(actors_item_data)

            actors.append(actors_item)

        checks = []
        _checks = d.pop("checks")
        for checks_item_data in _checks:
            checks_item = OrderFlowCheck.from_dict(checks_item_data)

            checks.append(checks_item)

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = OrderFlowStep.from_dict(steps_item_data)

            steps.append(steps_item)

        terminals = []
        _terminals = d.pop("terminals")
        for terminals_item_data in _terminals:
            terminals_item = OrderFlowTerminal.from_dict(terminals_item_data)

            terminals.append(terminals_item)

        def _parse_stats(data: object) -> Union["OrderFlowStats", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_type_1 = OrderFlowStats.from_dict(data)

                return stats_type_1
            except:  # noqa: E722
                pass
            return cast(Union["OrderFlowStats", None], data)

        stats = _parse_stats(d.pop("stats"))

        order_flow_description = cls(
            offering=offering,
            order_kind=order_kind,
            supported=supported,
            reason=reason,
            orderer=orderer,
            order_kinds=order_kinds,
            orderers=orderers,
            actors=actors,
            checks=checks,
            steps=steps,
            terminals=terminals,
            stats=stats,
        )

        order_flow_description.additional_properties = d
        return order_flow_description

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
