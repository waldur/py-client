from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedIdentityProviderRequest")


@_attrs_define
class PatchedIdentityProviderRequest:
    """
    Attributes:
        provider (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        client_id (Union[Unset, str]): ID of application used for OAuth authentication.
        verify_ssl (Union[Unset, bool]):
        enable_post_logout_redirect (Union[Unset, bool]):
        enable_pkce (Union[Unset, bool]):
        discovery_url (Union[Unset, str]): The endpoint for endpoint discovery.
        label (Union[Unset, str]): Human-readable identity provider is label.
        management_url (Union[Unset, str]): The endpoint for user details management.
        protected_fields (Union[Unset, Any]):
    """

    provider: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    client_id: Union[Unset, str] = UNSET
    verify_ssl: Union[Unset, bool] = UNSET
    enable_post_logout_redirect: Union[Unset, bool] = UNSET
    enable_pkce: Union[Unset, bool] = UNSET
    discovery_url: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    management_url: Union[Unset, str] = UNSET
    protected_fields: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        is_active = self.is_active

        client_id = self.client_id

        verify_ssl = self.verify_ssl

        enable_post_logout_redirect = self.enable_post_logout_redirect

        enable_pkce = self.enable_pkce

        discovery_url = self.discovery_url

        label = self.label

        management_url = self.management_url

        protected_fields = self.protected_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if verify_ssl is not UNSET:
            field_dict["verify_ssl"] = verify_ssl
        if enable_post_logout_redirect is not UNSET:
            field_dict["enable_post_logout_redirect"] = enable_post_logout_redirect
        if enable_pkce is not UNSET:
            field_dict["enable_pkce"] = enable_pkce
        if discovery_url is not UNSET:
            field_dict["discovery_url"] = discovery_url
        if label is not UNSET:
            field_dict["label"] = label
        if management_url is not UNSET:
            field_dict["management_url"] = management_url
        if protected_fields is not UNSET:
            field_dict["protected_fields"] = protected_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        provider = (
            self.provider if isinstance(self.provider, Unset) else (None, str(self.provider).encode(), "text/plain")
        )

        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )

        client_id = (
            self.client_id if isinstance(self.client_id, Unset) else (None, str(self.client_id).encode(), "text/plain")
        )

        verify_ssl = (
            self.verify_ssl
            if isinstance(self.verify_ssl, Unset)
            else (None, str(self.verify_ssl).encode(), "text/plain")
        )

        enable_post_logout_redirect = (
            self.enable_post_logout_redirect
            if isinstance(self.enable_post_logout_redirect, Unset)
            else (None, str(self.enable_post_logout_redirect).encode(), "text/plain")
        )

        enable_pkce = (
            self.enable_pkce
            if isinstance(self.enable_pkce, Unset)
            else (None, str(self.enable_pkce).encode(), "text/plain")
        )

        discovery_url = (
            self.discovery_url
            if isinstance(self.discovery_url, Unset)
            else (None, str(self.discovery_url).encode(), "text/plain")
        )

        label = self.label if isinstance(self.label, Unset) else (None, str(self.label).encode(), "text/plain")

        management_url = (
            self.management_url
            if isinstance(self.management_url, Unset)
            else (None, str(self.management_url).encode(), "text/plain")
        )

        protected_fields = (
            self.protected_fields
            if isinstance(self.protected_fields, Unset)
            else (None, str(self.protected_fields).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if verify_ssl is not UNSET:
            field_dict["verify_ssl"] = verify_ssl
        if enable_post_logout_redirect is not UNSET:
            field_dict["enable_post_logout_redirect"] = enable_post_logout_redirect
        if enable_pkce is not UNSET:
            field_dict["enable_pkce"] = enable_pkce
        if discovery_url is not UNSET:
            field_dict["discovery_url"] = discovery_url
        if label is not UNSET:
            field_dict["label"] = label
        if management_url is not UNSET:
            field_dict["management_url"] = management_url
        if protected_fields is not UNSET:
            field_dict["protected_fields"] = protected_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = d.pop("provider", UNSET)

        is_active = d.pop("is_active", UNSET)

        client_id = d.pop("client_id", UNSET)

        verify_ssl = d.pop("verify_ssl", UNSET)

        enable_post_logout_redirect = d.pop("enable_post_logout_redirect", UNSET)

        enable_pkce = d.pop("enable_pkce", UNSET)

        discovery_url = d.pop("discovery_url", UNSET)

        label = d.pop("label", UNSET)

        management_url = d.pop("management_url", UNSET)

        protected_fields = d.pop("protected_fields", UNSET)

        patched_identity_provider_request = cls(
            provider=provider,
            is_active=is_active,
            client_id=client_id,
            verify_ssl=verify_ssl,
            enable_post_logout_redirect=enable_post_logout_redirect,
            enable_pkce=enable_pkce,
            discovery_url=discovery_url,
            label=label,
            management_url=management_url,
            protected_fields=protected_fields,
        )

        patched_identity_provider_request.additional_properties = d
        return patched_identity_provider_request

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
