from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OfferingTemplateCreateOfferingRequestBackendSettings")


@_attrs_define
class OfferingTemplateCreateOfferingRequestBackendSettings:
    """Backend settings of the site agent, by name, over the template's: what the chosen role backends need that the
    template does not set. A nested mapping is merged key by key. Checked as the agent configuration's backend_settings;
    secrets are refused, they stay in the agent configuration file on the agent host. Site agent templates only.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offering_template_create_offering_request_backend_settings = cls()

        offering_template_create_offering_request_backend_settings.additional_properties = d
        return offering_template_create_offering_request_backend_settings

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
