from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.open_stack_static_route_request import OpenStackStaticRouteRequest


T = TypeVar("T", bound="OpenStackRouterSetRoutesRequest")


@_attrs_define
class OpenStackRouterSetRoutesRequest:
    """
    Attributes:
        routes (list['OpenStackStaticRouteRequest']):
    """

    routes: list["OpenStackStaticRouteRequest"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        routes = []
        for routes_item_data in self.routes:
            routes_item = routes_item_data.to_dict()
            routes.append(routes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "routes": routes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_stack_static_route_request import OpenStackStaticRouteRequest

        d = dict(src_dict)
        routes = []
        _routes = d.pop("routes")
        for routes_item_data in _routes:
            routes_item = OpenStackStaticRouteRequest.from_dict(routes_item_data)

            routes.append(routes_item)

        open_stack_router_set_routes_request = cls(
            routes=routes,
        )

        open_stack_router_set_routes_request.additional_properties = d
        return open_stack_router_set_routes_request

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
