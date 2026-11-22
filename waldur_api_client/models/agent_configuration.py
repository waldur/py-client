from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_configuration_backend_components import AgentConfigurationBackendComponents
    from ..models.agent_configuration_backend_settings import AgentConfigurationBackendSettings
    from ..models.event_settings import EventSettings


T = TypeVar("T", bound="AgentConfiguration")


@_attrs_define
class AgentConfiguration:
    """
    Attributes:
        order_processing_backend (Union[Unset, str]):
        membership_sync_backend (Union[Unset, str]):
        reporting_backend (Union[Unset, str]):
        username_management_backend (Union[Unset, str]):
        custom_backends (Union[Unset, list[str]]): Backends that are not in the plugin catalog, such as a site's own
            plugin. Their settings and components are not validated.
        backend_settings (Union[Unset, AgentConfigurationBackendSettings]):
        backend_components (Union[Unset, AgentConfigurationBackendComponents]):
        event_settings (Union[Unset, EventSettings]):
    """

    order_processing_backend: Union[Unset, str] = UNSET
    membership_sync_backend: Union[Unset, str] = UNSET
    reporting_backend: Union[Unset, str] = UNSET
    username_management_backend: Union[Unset, str] = UNSET
    custom_backends: Union[Unset, list[str]] = UNSET
    backend_settings: Union[Unset, "AgentConfigurationBackendSettings"] = UNSET
    backend_components: Union[Unset, "AgentConfigurationBackendComponents"] = UNSET
    event_settings: Union[Unset, "EventSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_processing_backend = self.order_processing_backend

        membership_sync_backend = self.membership_sync_backend

        reporting_backend = self.reporting_backend

        username_management_backend = self.username_management_backend

        custom_backends: Union[Unset, list[str]] = UNSET
        if not isinstance(self.custom_backends, Unset):
            custom_backends = self.custom_backends

        backend_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backend_settings, Unset):
            backend_settings = self.backend_settings.to_dict()

        backend_components: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backend_components, Unset):
            backend_components = self.backend_components.to_dict()

        event_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_settings, Unset):
            event_settings = self.event_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_processing_backend is not UNSET:
            field_dict["order_processing_backend"] = order_processing_backend
        if membership_sync_backend is not UNSET:
            field_dict["membership_sync_backend"] = membership_sync_backend
        if reporting_backend is not UNSET:
            field_dict["reporting_backend"] = reporting_backend
        if username_management_backend is not UNSET:
            field_dict["username_management_backend"] = username_management_backend
        if custom_backends is not UNSET:
            field_dict["custom_backends"] = custom_backends
        if backend_settings is not UNSET:
            field_dict["backend_settings"] = backend_settings
        if backend_components is not UNSET:
            field_dict["backend_components"] = backend_components
        if event_settings is not UNSET:
            field_dict["event_settings"] = event_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_configuration_backend_components import AgentConfigurationBackendComponents
        from ..models.agent_configuration_backend_settings import AgentConfigurationBackendSettings
        from ..models.event_settings import EventSettings

        d = dict(src_dict)
        order_processing_backend = d.pop("order_processing_backend", UNSET)

        membership_sync_backend = d.pop("membership_sync_backend", UNSET)

        reporting_backend = d.pop("reporting_backend", UNSET)

        username_management_backend = d.pop("username_management_backend", UNSET)

        custom_backends = cast(list[str], d.pop("custom_backends", UNSET))

        _backend_settings = d.pop("backend_settings", UNSET)
        backend_settings: Union[Unset, AgentConfigurationBackendSettings]
        if isinstance(_backend_settings, Unset):
            backend_settings = UNSET
        else:
            backend_settings = AgentConfigurationBackendSettings.from_dict(_backend_settings)

        _backend_components = d.pop("backend_components", UNSET)
        backend_components: Union[Unset, AgentConfigurationBackendComponents]
        if isinstance(_backend_components, Unset):
            backend_components = UNSET
        else:
            backend_components = AgentConfigurationBackendComponents.from_dict(_backend_components)

        _event_settings = d.pop("event_settings", UNSET)
        event_settings: Union[Unset, EventSettings]
        if isinstance(_event_settings, Unset):
            event_settings = UNSET
        else:
            event_settings = EventSettings.from_dict(_event_settings)

        agent_configuration = cls(
            order_processing_backend=order_processing_backend,
            membership_sync_backend=membership_sync_backend,
            reporting_backend=reporting_backend,
            username_management_backend=username_management_backend,
            custom_backends=custom_backends,
            backend_settings=backend_settings,
            backend_components=backend_components,
            event_settings=event_settings,
        )

        agent_configuration.additional_properties = d
        return agent_configuration

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
