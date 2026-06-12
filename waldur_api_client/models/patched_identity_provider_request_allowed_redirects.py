from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchedIdentityProviderRequestAllowedRedirects")


@_attrs_define
class PatchedIdentityProviderRequestAllowedRedirects:
    """List of allowed redirect URLs for OAuth authentication. URLs must be exact matches (origin only: scheme + domain +
    port). HTTPS required except for localhost. No wildcards, paths, query params, or fragments. Example:
    ["https://portal1.example.com", "https://portal2.example.com:8443"]. If empty, falls back to HOMEPORT_URL setting.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        patched_identity_provider_request_allowed_redirects = cls()

        patched_identity_provider_request_allowed_redirects.additional_properties = d
        return patched_identity_provider_request_allowed_redirects

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
