from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventSettings")


@_attrs_define
class EventSettings:
    """
    Attributes:
        stomp_enabled (Union[Unset, bool]):
        stomp_membership_sync_enabled (Union[None, Unset, bool]): Use STOMP for membership sync; the agent follows
            stomp_enabled when this is unset.
        stomp_ws_host (Union[Unset, str]):
        stomp_ws_port (Union[Unset, int]):
        stomp_ws_path (Union[Unset, str]):
        websocket_use_tls (Union[Unset, bool]):
    """

    stomp_enabled: Union[Unset, bool] = UNSET
    stomp_membership_sync_enabled: Union[None, Unset, bool] = UNSET
    stomp_ws_host: Union[Unset, str] = UNSET
    stomp_ws_port: Union[Unset, int] = UNSET
    stomp_ws_path: Union[Unset, str] = UNSET
    websocket_use_tls: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stomp_enabled = self.stomp_enabled

        stomp_membership_sync_enabled: Union[None, Unset, bool]
        if isinstance(self.stomp_membership_sync_enabled, Unset):
            stomp_membership_sync_enabled = UNSET
        else:
            stomp_membership_sync_enabled = self.stomp_membership_sync_enabled

        stomp_ws_host = self.stomp_ws_host

        stomp_ws_port = self.stomp_ws_port

        stomp_ws_path = self.stomp_ws_path

        websocket_use_tls = self.websocket_use_tls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stomp_enabled is not UNSET:
            field_dict["stomp_enabled"] = stomp_enabled
        if stomp_membership_sync_enabled is not UNSET:
            field_dict["stomp_membership_sync_enabled"] = stomp_membership_sync_enabled
        if stomp_ws_host is not UNSET:
            field_dict["stomp_ws_host"] = stomp_ws_host
        if stomp_ws_port is not UNSET:
            field_dict["stomp_ws_port"] = stomp_ws_port
        if stomp_ws_path is not UNSET:
            field_dict["stomp_ws_path"] = stomp_ws_path
        if websocket_use_tls is not UNSET:
            field_dict["websocket_use_tls"] = websocket_use_tls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stomp_enabled = d.pop("stomp_enabled", UNSET)

        def _parse_stomp_membership_sync_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        stomp_membership_sync_enabled = _parse_stomp_membership_sync_enabled(
            d.pop("stomp_membership_sync_enabled", UNSET)
        )

        stomp_ws_host = d.pop("stomp_ws_host", UNSET)

        stomp_ws_port = d.pop("stomp_ws_port", UNSET)

        stomp_ws_path = d.pop("stomp_ws_path", UNSET)

        websocket_use_tls = d.pop("websocket_use_tls", UNSET)

        event_settings = cls(
            stomp_enabled=stomp_enabled,
            stomp_membership_sync_enabled=stomp_membership_sync_enabled,
            stomp_ws_host=stomp_ws_host,
            stomp_ws_port=stomp_ws_port,
            stomp_ws_path=stomp_ws_path,
            websocket_use_tls=websocket_use_tls,
        )

        event_settings.additional_properties = d
        return event_settings

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
