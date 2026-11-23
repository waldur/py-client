from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.site_agent_offering_secret import SiteAgentOfferingSecret
    from ..models.site_agent_offering_settings import SiteAgentOfferingSettings


T = TypeVar("T", bound="SiteAgentOfferingConfig")


@_attrs_define
class SiteAgentOfferingConfig:
    """
    Attributes:
        offering (SiteAgentOfferingSettings):
        secrets (list['SiteAgentOfferingSecret']): The backend secrets the offering's backends declare; none of them is
            in offering.
        version (str): sha256 of offering as canonical JSON (sorted keys, no whitespace); changes when, and only when,
            offering does.
    """

    offering: "SiteAgentOfferingSettings"
    secrets: list["SiteAgentOfferingSecret"]
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offering = self.offering.to_dict()

        secrets = []
        for secrets_item_data in self.secrets:
            secrets_item = secrets_item_data.to_dict()
            secrets.append(secrets_item)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offering": offering,
                "secrets": secrets,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.site_agent_offering_secret import SiteAgentOfferingSecret
        from ..models.site_agent_offering_settings import SiteAgentOfferingSettings

        d = dict(src_dict)
        offering = SiteAgentOfferingSettings.from_dict(d.pop("offering"))

        secrets = []
        _secrets = d.pop("secrets")
        for secrets_item_data in _secrets:
            secrets_item = SiteAgentOfferingSecret.from_dict(secrets_item_data)

            secrets.append(secrets_item)

        version = d.pop("version")

        site_agent_offering_config = cls(
            offering=offering,
            secrets=secrets,
            version=version,
        )

        site_agent_offering_config.additional_properties = d
        return site_agent_offering_config

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
