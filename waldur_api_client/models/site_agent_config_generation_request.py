from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.configuration_source_enum import ConfigurationSourceEnum
from ..models.secret_format_enum import SecretFormatEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteAgentConfigGenerationRequest")


@_attrs_define
class SiteAgentConfigGenerationRequest:
    """
    Attributes:
        backend_id (Union[Unset, str]): Only the offering whose backend ID is exactly this.
        backend_id_startswith (Union[Unset, str]): Only offerings whose backend ID starts with this, such as every
            offering of one cluster.
        offering_uuids (Union[Unset, list[UUID]]): Site agent offerings to include. With backend_id or
            backend_id_startswith, only those of them that match. At least one of the three is required.
        include_policy_settings (Union[Unset, bool]): Include SLURM periodic usage policy settings in configuration
            Default: True.
        waldur_api_url (Union[Unset, str]): Waldur API URL (defaults to current server URL)
        timezone (Union[Unset, str]): Timezone for the site agent Default: 'UTC'.
        secret_format (Union[Unset, SecretFormatEnum]):  Default: SecretFormatEnum.COMMENT.
        configuration_source (Union[Unset, ConfigurationSourceEnum]):  Default: ConfigurationSourceEnum.LOCAL.
    """

    backend_id: Union[Unset, str] = UNSET
    backend_id_startswith: Union[Unset, str] = UNSET
    offering_uuids: Union[Unset, list[UUID]] = UNSET
    include_policy_settings: Union[Unset, bool] = True
    waldur_api_url: Union[Unset, str] = UNSET
    timezone: Union[Unset, str] = "UTC"
    secret_format: Union[Unset, SecretFormatEnum] = SecretFormatEnum.COMMENT
    configuration_source: Union[Unset, ConfigurationSourceEnum] = ConfigurationSourceEnum.LOCAL
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backend_id = self.backend_id

        backend_id_startswith = self.backend_id_startswith

        offering_uuids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.offering_uuids, Unset):
            offering_uuids = []
            for offering_uuids_item_data in self.offering_uuids:
                offering_uuids_item = str(offering_uuids_item_data)
                offering_uuids.append(offering_uuids_item)

        include_policy_settings = self.include_policy_settings

        waldur_api_url = self.waldur_api_url

        timezone = self.timezone

        secret_format: Union[Unset, str] = UNSET
        if not isinstance(self.secret_format, Unset):
            secret_format = self.secret_format.value

        configuration_source: Union[Unset, str] = UNSET
        if not isinstance(self.configuration_source, Unset):
            configuration_source = self.configuration_source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if backend_id_startswith is not UNSET:
            field_dict["backend_id_startswith"] = backend_id_startswith
        if offering_uuids is not UNSET:
            field_dict["offering_uuids"] = offering_uuids
        if include_policy_settings is not UNSET:
            field_dict["include_policy_settings"] = include_policy_settings
        if waldur_api_url is not UNSET:
            field_dict["waldur_api_url"] = waldur_api_url
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if secret_format is not UNSET:
            field_dict["secret_format"] = secret_format
        if configuration_source is not UNSET:
            field_dict["configuration_source"] = configuration_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backend_id = d.pop("backend_id", UNSET)

        backend_id_startswith = d.pop("backend_id_startswith", UNSET)

        offering_uuids = []
        _offering_uuids = d.pop("offering_uuids", UNSET)
        for offering_uuids_item_data in _offering_uuids or []:
            offering_uuids_item = UUID(offering_uuids_item_data)

            offering_uuids.append(offering_uuids_item)

        include_policy_settings = d.pop("include_policy_settings", UNSET)

        waldur_api_url = d.pop("waldur_api_url", UNSET)

        timezone = d.pop("timezone", UNSET)

        _secret_format = d.pop("secret_format", UNSET)
        secret_format: Union[Unset, SecretFormatEnum]
        if isinstance(_secret_format, Unset):
            secret_format = UNSET
        else:
            secret_format = SecretFormatEnum(_secret_format)

        _configuration_source = d.pop("configuration_source", UNSET)
        configuration_source: Union[Unset, ConfigurationSourceEnum]
        if isinstance(_configuration_source, Unset):
            configuration_source = UNSET
        else:
            configuration_source = ConfigurationSourceEnum(_configuration_source)

        site_agent_config_generation_request = cls(
            backend_id=backend_id,
            backend_id_startswith=backend_id_startswith,
            offering_uuids=offering_uuids,
            include_policy_settings=include_policy_settings,
            waldur_api_url=waldur_api_url,
            timezone=timezone,
            secret_format=secret_format,
            configuration_source=configuration_source,
        )

        site_agent_config_generation_request.additional_properties = d
        return site_agent_config_generation_request

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
