from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentSettingsRequest")


@_attrs_define
class AgentSettingsRequest:
    """
    Attributes:
        resource_import_enabled (Union[Unset, bool]): Import resources found on the backend into Waldur.
        username_reconciliation_enabled (Union[Unset, bool]): Periodically reconcile usernames from the backend.
        preserve_unmanaged_backend_users (Union[Unset, bool]): Membership sync keeps backend users Waldur has never
            known as offering users, instead of removing every user not on the resource team.
        omit_anomalous_usage_components (Union[Unset, bool]): Report usage without a decreasing component instead of
            withholding the whole report.
    """

    resource_import_enabled: Union[Unset, bool] = UNSET
    username_reconciliation_enabled: Union[Unset, bool] = UNSET
    preserve_unmanaged_backend_users: Union[Unset, bool] = UNSET
    omit_anomalous_usage_components: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_import_enabled = self.resource_import_enabled

        username_reconciliation_enabled = self.username_reconciliation_enabled

        preserve_unmanaged_backend_users = self.preserve_unmanaged_backend_users

        omit_anomalous_usage_components = self.omit_anomalous_usage_components

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_import_enabled is not UNSET:
            field_dict["resource_import_enabled"] = resource_import_enabled
        if username_reconciliation_enabled is not UNSET:
            field_dict["username_reconciliation_enabled"] = username_reconciliation_enabled
        if preserve_unmanaged_backend_users is not UNSET:
            field_dict["preserve_unmanaged_backend_users"] = preserve_unmanaged_backend_users
        if omit_anomalous_usage_components is not UNSET:
            field_dict["omit_anomalous_usage_components"] = omit_anomalous_usage_components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_import_enabled = d.pop("resource_import_enabled", UNSET)

        username_reconciliation_enabled = d.pop("username_reconciliation_enabled", UNSET)

        preserve_unmanaged_backend_users = d.pop("preserve_unmanaged_backend_users", UNSET)

        omit_anomalous_usage_components = d.pop("omit_anomalous_usage_components", UNSET)

        agent_settings_request = cls(
            resource_import_enabled=resource_import_enabled,
            username_reconciliation_enabled=username_reconciliation_enabled,
            preserve_unmanaged_backend_users=preserve_unmanaged_backend_users,
            omit_anomalous_usage_components=omit_anomalous_usage_components,
        )

        agent_settings_request.additional_properties = d
        return agent_settings_request

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
