from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_agent_offering_settings_backend_components import SiteAgentOfferingSettingsBackendComponents
    from ..models.site_agent_offering_settings_backend_settings import SiteAgentOfferingSettingsBackendSettings
    from ..models.site_agent_offering_settings_policy_settings import SiteAgentOfferingSettingsPolicySettings


T = TypeVar("T", bound="SiteAgentOfferingSettings")


@_attrs_define
class SiteAgentOfferingSettings:
    """
    Attributes:
        name (str):
        backend_type (str): The backend of the first role set, in role order.
        backend_settings (SiteAgentOfferingSettingsBackendSettings): Settings of the backends, with their secrets left
            out.
        backend_components (SiteAgentOfferingSettingsBackendComponents): The offering's components by type, as the agent
            reads them.
        stomp_enabled (Union[Unset, bool]):
        stomp_membership_sync_enabled (Union[None, Unset, bool]): Use STOMP for membership sync; the agent follows
            stomp_enabled when this is unset.
        stomp_ws_host (Union[Unset, str]):
        stomp_ws_port (Union[Unset, int]):
        stomp_ws_path (Union[Unset, str]):
        websocket_use_tls (Union[Unset, bool]):
        resource_import_enabled (Union[Unset, bool]): Import resources found on the backend into Waldur.
        username_reconciliation_enabled (Union[Unset, bool]): Periodically reconcile usernames from the backend.
        preserve_unmanaged_backend_users (Union[Unset, bool]): Membership sync keeps backend users Waldur has never
            known as offering users, instead of removing every user not on the resource team.
        omit_anomalous_usage_components (Union[Unset, bool]): Report usage without a decreasing component instead of
            withholding the whole report.
        order_processing_backend (Union[Unset, str]):
        membership_sync_backend (Union[Unset, str]):
        reporting_backend (Union[Unset, str]):
        username_management_backend (Union[Unset, str]):
        policy_settings (Union[Unset, SiteAgentOfferingSettingsPolicySettings]): The offering's SLURM periodic usage
            policy, if it has one.
    """

    name: str
    backend_type: str
    backend_settings: "SiteAgentOfferingSettingsBackendSettings"
    backend_components: "SiteAgentOfferingSettingsBackendComponents"
    stomp_enabled: Union[Unset, bool] = UNSET
    stomp_membership_sync_enabled: Union[None, Unset, bool] = UNSET
    stomp_ws_host: Union[Unset, str] = UNSET
    stomp_ws_port: Union[Unset, int] = UNSET
    stomp_ws_path: Union[Unset, str] = UNSET
    websocket_use_tls: Union[Unset, bool] = UNSET
    resource_import_enabled: Union[Unset, bool] = UNSET
    username_reconciliation_enabled: Union[Unset, bool] = UNSET
    preserve_unmanaged_backend_users: Union[Unset, bool] = UNSET
    omit_anomalous_usage_components: Union[Unset, bool] = UNSET
    order_processing_backend: Union[Unset, str] = UNSET
    membership_sync_backend: Union[Unset, str] = UNSET
    reporting_backend: Union[Unset, str] = UNSET
    username_management_backend: Union[Unset, str] = UNSET
    policy_settings: Union[Unset, "SiteAgentOfferingSettingsPolicySettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        backend_type = self.backend_type

        backend_settings = self.backend_settings.to_dict()

        backend_components = self.backend_components.to_dict()

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

        resource_import_enabled = self.resource_import_enabled

        username_reconciliation_enabled = self.username_reconciliation_enabled

        preserve_unmanaged_backend_users = self.preserve_unmanaged_backend_users

        omit_anomalous_usage_components = self.omit_anomalous_usage_components

        order_processing_backend = self.order_processing_backend

        membership_sync_backend = self.membership_sync_backend

        reporting_backend = self.reporting_backend

        username_management_backend = self.username_management_backend

        policy_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.policy_settings, Unset):
            policy_settings = self.policy_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "backend_type": backend_type,
                "backend_settings": backend_settings,
                "backend_components": backend_components,
            }
        )
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
        if resource_import_enabled is not UNSET:
            field_dict["resource_import_enabled"] = resource_import_enabled
        if username_reconciliation_enabled is not UNSET:
            field_dict["username_reconciliation_enabled"] = username_reconciliation_enabled
        if preserve_unmanaged_backend_users is not UNSET:
            field_dict["preserve_unmanaged_backend_users"] = preserve_unmanaged_backend_users
        if omit_anomalous_usage_components is not UNSET:
            field_dict["omit_anomalous_usage_components"] = omit_anomalous_usage_components
        if order_processing_backend is not UNSET:
            field_dict["order_processing_backend"] = order_processing_backend
        if membership_sync_backend is not UNSET:
            field_dict["membership_sync_backend"] = membership_sync_backend
        if reporting_backend is not UNSET:
            field_dict["reporting_backend"] = reporting_backend
        if username_management_backend is not UNSET:
            field_dict["username_management_backend"] = username_management_backend
        if policy_settings is not UNSET:
            field_dict["policy_settings"] = policy_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.site_agent_offering_settings_backend_components import SiteAgentOfferingSettingsBackendComponents
        from ..models.site_agent_offering_settings_backend_settings import SiteAgentOfferingSettingsBackendSettings
        from ..models.site_agent_offering_settings_policy_settings import SiteAgentOfferingSettingsPolicySettings

        d = dict(src_dict)
        name = d.pop("name")

        backend_type = d.pop("backend_type")

        backend_settings = SiteAgentOfferingSettingsBackendSettings.from_dict(d.pop("backend_settings"))

        backend_components = SiteAgentOfferingSettingsBackendComponents.from_dict(d.pop("backend_components"))

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

        resource_import_enabled = d.pop("resource_import_enabled", UNSET)

        username_reconciliation_enabled = d.pop("username_reconciliation_enabled", UNSET)

        preserve_unmanaged_backend_users = d.pop("preserve_unmanaged_backend_users", UNSET)

        omit_anomalous_usage_components = d.pop("omit_anomalous_usage_components", UNSET)

        order_processing_backend = d.pop("order_processing_backend", UNSET)

        membership_sync_backend = d.pop("membership_sync_backend", UNSET)

        reporting_backend = d.pop("reporting_backend", UNSET)

        username_management_backend = d.pop("username_management_backend", UNSET)

        _policy_settings = d.pop("policy_settings", UNSET)
        policy_settings: Union[Unset, SiteAgentOfferingSettingsPolicySettings]
        if isinstance(_policy_settings, Unset):
            policy_settings = UNSET
        else:
            policy_settings = SiteAgentOfferingSettingsPolicySettings.from_dict(_policy_settings)

        site_agent_offering_settings = cls(
            name=name,
            backend_type=backend_type,
            backend_settings=backend_settings,
            backend_components=backend_components,
            stomp_enabled=stomp_enabled,
            stomp_membership_sync_enabled=stomp_membership_sync_enabled,
            stomp_ws_host=stomp_ws_host,
            stomp_ws_port=stomp_ws_port,
            stomp_ws_path=stomp_ws_path,
            websocket_use_tls=websocket_use_tls,
            resource_import_enabled=resource_import_enabled,
            username_reconciliation_enabled=username_reconciliation_enabled,
            preserve_unmanaged_backend_users=preserve_unmanaged_backend_users,
            omit_anomalous_usage_components=omit_anomalous_usage_components,
            order_processing_backend=order_processing_backend,
            membership_sync_backend=membership_sync_backend,
            reporting_backend=reporting_backend,
            username_management_backend=username_management_backend,
            policy_settings=policy_settings,
        )

        site_agent_offering_settings.additional_properties = d
        return site_agent_offering_settings

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
