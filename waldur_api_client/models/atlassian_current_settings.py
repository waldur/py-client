from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_method_enum import AuthMethodEnum

T = TypeVar("T", bound="AtlassianCurrentSettings")


@_attrs_define
class AtlassianCurrentSettings:
    """
    Attributes:
        atlassian_api_url (str):
        atlassian_project_id (str):
        atlassian_verify_ssl (bool):
        atlassian_use_old_api (bool):
        atlassian_issue_types (list[str]):
        atlassian_custom_issue_field_mapping_enabled (bool):
        atlassian_reporter_field (str):
        atlassian_impact_field (str):
        atlassian_organisation_field (str):
        atlassian_project_field (str):
        atlassian_affected_resource_field (str):
        atlassian_caller_field (str):
        atlassian_template_field (str):
        atlassian_sla_field (str):
        atlassian_resolution_sla_field (str):
        atlassian_satisfaction_field (str):
        atlassian_request_feedback_field (str):
        atlassian_waldur_backend_id_field (str):
        atlassian_default_offering_issue_type (str):
        atlassian_email (str):
        atlassian_username (str):
        atlassian_oauth2_client_id (str):
        auth_method (Union[AuthMethodEnum, None]):
        auth_configured (bool):
    """

    atlassian_api_url: str
    atlassian_project_id: str
    atlassian_verify_ssl: bool
    atlassian_use_old_api: bool
    atlassian_issue_types: list[str]
    atlassian_custom_issue_field_mapping_enabled: bool
    atlassian_reporter_field: str
    atlassian_impact_field: str
    atlassian_organisation_field: str
    atlassian_project_field: str
    atlassian_affected_resource_field: str
    atlassian_caller_field: str
    atlassian_template_field: str
    atlassian_sla_field: str
    atlassian_resolution_sla_field: str
    atlassian_satisfaction_field: str
    atlassian_request_feedback_field: str
    atlassian_waldur_backend_id_field: str
    atlassian_default_offering_issue_type: str
    atlassian_email: str
    atlassian_username: str
    atlassian_oauth2_client_id: str
    auth_method: Union[AuthMethodEnum, None]
    auth_configured: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        atlassian_api_url = self.atlassian_api_url

        atlassian_project_id = self.atlassian_project_id

        atlassian_verify_ssl = self.atlassian_verify_ssl

        atlassian_use_old_api = self.atlassian_use_old_api

        atlassian_issue_types = self.atlassian_issue_types

        atlassian_custom_issue_field_mapping_enabled = self.atlassian_custom_issue_field_mapping_enabled

        atlassian_reporter_field = self.atlassian_reporter_field

        atlassian_impact_field = self.atlassian_impact_field

        atlassian_organisation_field = self.atlassian_organisation_field

        atlassian_project_field = self.atlassian_project_field

        atlassian_affected_resource_field = self.atlassian_affected_resource_field

        atlassian_caller_field = self.atlassian_caller_field

        atlassian_template_field = self.atlassian_template_field

        atlassian_sla_field = self.atlassian_sla_field

        atlassian_resolution_sla_field = self.atlassian_resolution_sla_field

        atlassian_satisfaction_field = self.atlassian_satisfaction_field

        atlassian_request_feedback_field = self.atlassian_request_feedback_field

        atlassian_waldur_backend_id_field = self.atlassian_waldur_backend_id_field

        atlassian_default_offering_issue_type = self.atlassian_default_offering_issue_type

        atlassian_email = self.atlassian_email

        atlassian_username = self.atlassian_username

        atlassian_oauth2_client_id = self.atlassian_oauth2_client_id

        auth_method: Union[None, str]
        if isinstance(self.auth_method, AuthMethodEnum):
            auth_method = self.auth_method.value
        else:
            auth_method = self.auth_method

        auth_configured = self.auth_configured

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ATLASSIAN_API_URL": atlassian_api_url,
                "ATLASSIAN_PROJECT_ID": atlassian_project_id,
                "ATLASSIAN_VERIFY_SSL": atlassian_verify_ssl,
                "ATLASSIAN_USE_OLD_API": atlassian_use_old_api,
                "ATLASSIAN_ISSUE_TYPES": atlassian_issue_types,
                "ATLASSIAN_CUSTOM_ISSUE_FIELD_MAPPING_ENABLED": atlassian_custom_issue_field_mapping_enabled,
                "ATLASSIAN_REPORTER_FIELD": atlassian_reporter_field,
                "ATLASSIAN_IMPACT_FIELD": atlassian_impact_field,
                "ATLASSIAN_ORGANISATION_FIELD": atlassian_organisation_field,
                "ATLASSIAN_PROJECT_FIELD": atlassian_project_field,
                "ATLASSIAN_AFFECTED_RESOURCE_FIELD": atlassian_affected_resource_field,
                "ATLASSIAN_CALLER_FIELD": atlassian_caller_field,
                "ATLASSIAN_TEMPLATE_FIELD": atlassian_template_field,
                "ATLASSIAN_SLA_FIELD": atlassian_sla_field,
                "ATLASSIAN_RESOLUTION_SLA_FIELD": atlassian_resolution_sla_field,
                "ATLASSIAN_SATISFACTION_FIELD": atlassian_satisfaction_field,
                "ATLASSIAN_REQUEST_FEEDBACK_FIELD": atlassian_request_feedback_field,
                "ATLASSIAN_WALDUR_BACKEND_ID_FIELD": atlassian_waldur_backend_id_field,
                "ATLASSIAN_DEFAULT_OFFERING_ISSUE_TYPE": atlassian_default_offering_issue_type,
                "ATLASSIAN_EMAIL": atlassian_email,
                "ATLASSIAN_USERNAME": atlassian_username,
                "ATLASSIAN_OAUTH2_CLIENT_ID": atlassian_oauth2_client_id,
                "auth_method": auth_method,
                "auth_configured": auth_configured,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        atlassian_api_url = d.pop("ATLASSIAN_API_URL")

        atlassian_project_id = d.pop("ATLASSIAN_PROJECT_ID")

        atlassian_verify_ssl = d.pop("ATLASSIAN_VERIFY_SSL")

        atlassian_use_old_api = d.pop("ATLASSIAN_USE_OLD_API")

        atlassian_issue_types = cast(list[str], d.pop("ATLASSIAN_ISSUE_TYPES"))

        atlassian_custom_issue_field_mapping_enabled = d.pop("ATLASSIAN_CUSTOM_ISSUE_FIELD_MAPPING_ENABLED")

        atlassian_reporter_field = d.pop("ATLASSIAN_REPORTER_FIELD")

        atlassian_impact_field = d.pop("ATLASSIAN_IMPACT_FIELD")

        atlassian_organisation_field = d.pop("ATLASSIAN_ORGANISATION_FIELD")

        atlassian_project_field = d.pop("ATLASSIAN_PROJECT_FIELD")

        atlassian_affected_resource_field = d.pop("ATLASSIAN_AFFECTED_RESOURCE_FIELD")

        atlassian_caller_field = d.pop("ATLASSIAN_CALLER_FIELD")

        atlassian_template_field = d.pop("ATLASSIAN_TEMPLATE_FIELD")

        atlassian_sla_field = d.pop("ATLASSIAN_SLA_FIELD")

        atlassian_resolution_sla_field = d.pop("ATLASSIAN_RESOLUTION_SLA_FIELD")

        atlassian_satisfaction_field = d.pop("ATLASSIAN_SATISFACTION_FIELD")

        atlassian_request_feedback_field = d.pop("ATLASSIAN_REQUEST_FEEDBACK_FIELD")

        atlassian_waldur_backend_id_field = d.pop("ATLASSIAN_WALDUR_BACKEND_ID_FIELD")

        atlassian_default_offering_issue_type = d.pop("ATLASSIAN_DEFAULT_OFFERING_ISSUE_TYPE")

        atlassian_email = d.pop("ATLASSIAN_EMAIL")

        atlassian_username = d.pop("ATLASSIAN_USERNAME")

        atlassian_oauth2_client_id = d.pop("ATLASSIAN_OAUTH2_CLIENT_ID")

        def _parse_auth_method(data: object) -> Union[AuthMethodEnum, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_method_type_0 = AuthMethodEnum(data)

                return auth_method_type_0
            except:  # noqa: E722
                pass
            return cast(Union[AuthMethodEnum, None], data)

        auth_method = _parse_auth_method(d.pop("auth_method"))

        auth_configured = d.pop("auth_configured")

        atlassian_current_settings = cls(
            atlassian_api_url=atlassian_api_url,
            atlassian_project_id=atlassian_project_id,
            atlassian_verify_ssl=atlassian_verify_ssl,
            atlassian_use_old_api=atlassian_use_old_api,
            atlassian_issue_types=atlassian_issue_types,
            atlassian_custom_issue_field_mapping_enabled=atlassian_custom_issue_field_mapping_enabled,
            atlassian_reporter_field=atlassian_reporter_field,
            atlassian_impact_field=atlassian_impact_field,
            atlassian_organisation_field=atlassian_organisation_field,
            atlassian_project_field=atlassian_project_field,
            atlassian_affected_resource_field=atlassian_affected_resource_field,
            atlassian_caller_field=atlassian_caller_field,
            atlassian_template_field=atlassian_template_field,
            atlassian_sla_field=atlassian_sla_field,
            atlassian_resolution_sla_field=atlassian_resolution_sla_field,
            atlassian_satisfaction_field=atlassian_satisfaction_field,
            atlassian_request_feedback_field=atlassian_request_feedback_field,
            atlassian_waldur_backend_id_field=atlassian_waldur_backend_id_field,
            atlassian_default_offering_issue_type=atlassian_default_offering_issue_type,
            atlassian_email=atlassian_email,
            atlassian_username=atlassian_username,
            atlassian_oauth2_client_id=atlassian_oauth2_client_id,
            auth_method=auth_method,
            auth_configured=auth_configured,
        )

        atlassian_current_settings.additional_properties = d
        return atlassian_current_settings

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
