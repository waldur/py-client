from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferingTemplateAgentRolesRequest")


@_attrs_define
class OfferingTemplateAgentRolesRequest:
    """
    Attributes:
        order_processing_backend (Union[Unset, str]):
        membership_sync_backend (Union[Unset, str]):
        reporting_backend (Union[Unset, str]):
        username_management_backend (Union[Unset, str]):
        custom_backends (Union[Unset, list[str]]): Backends of the site's own, not in the plugin catalog, that the roles
            may name. Added to the template's.
    """

    order_processing_backend: Union[Unset, str] = UNSET
    membership_sync_backend: Union[Unset, str] = UNSET
    reporting_backend: Union[Unset, str] = UNSET
    username_management_backend: Union[Unset, str] = UNSET
    custom_backends: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_processing_backend = self.order_processing_backend

        membership_sync_backend = self.membership_sync_backend

        reporting_backend = self.reporting_backend

        username_management_backend = self.username_management_backend

        custom_backends: Union[Unset, list[str]] = UNSET
        if not isinstance(self.custom_backends, Unset):
            custom_backends = self.custom_backends

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_processing_backend = d.pop("order_processing_backend", UNSET)

        membership_sync_backend = d.pop("membership_sync_backend", UNSET)

        reporting_backend = d.pop("reporting_backend", UNSET)

        username_management_backend = d.pop("username_management_backend", UNSET)

        custom_backends = cast(list[str], d.pop("custom_backends", UNSET))

        offering_template_agent_roles_request = cls(
            order_processing_backend=order_processing_backend,
            membership_sync_backend=membership_sync_backend,
            reporting_backend=reporting_backend,
            username_management_backend=username_management_backend,
            custom_backends=custom_backends,
        )

        offering_template_agent_roles_request.additional_properties = d
        return offering_template_agent_roles_request

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
