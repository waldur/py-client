import json
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="ConstanceSettingsRequest")


@_attrs_define
class ConstanceSettingsRequest:
    """
    Attributes:
        site_name (Union[Unset, str]):
        site_description (Union[Unset, str]):
        homeport_url (Union[Unset, str]):
        site_address (Union[Unset, str]):
        site_email (Union[Unset, str]):
        site_phone (Union[Unset, str]):
        currency_name (Union[Unset, str]):
        thumbnail_size (Union[Unset, str]):
        anonymous_user_can_view_offerings (Union[Unset, bool]):
        anonymous_user_can_view_plans (Union[Unset, bool]):
        notify_staff_about_approvals (Union[Unset, bool]):
        notify_about_resource_change (Union[Unset, bool]):
        disable_sending_notifications_about_resource_update (Union[Unset, bool]):
        marketplace_landing_page (Union[Unset, str]):
        enable_stale_resource_notifications (Union[Unset, bool]):
        enable_resource_end_date (Union[Unset, bool]):
        telemetry_url (Union[Unset, str]):
        telemetry_version (Union[Unset, int]):
        script_run_mode (Union[Unset, str]):
        docker_client (Union[Unset, str]):
        docker_run_options (Union[Unset, str]):
        docker_script_dir (Union[Unset, str]):
        docker_remove_container (Union[Unset, bool]):
        docker_images (Union[Unset, str]):
        docker_volume_name (Union[Unset, str]):
        k8s_namespace (Union[Unset, str]):
        k8s_config_path (Union[Unset, str]):
        k8s_job_timeout (Union[Unset, int]):
        enable_strict_check_accepting_invitation (Union[Unset, bool]):
        invitation_disable_multiple_roles (Union[Unset, bool]):
        default_idp (Union[Unset, str]):
        docs_url (Union[Unset, str]):
        short_page_title (Union[Unset, str]):
        full_page_title (Union[Unset, str]):
        brand_color (Union[Unset, str]):
        hero_link_label (Union[Unset, str]):
        hero_link_url (Union[Unset, str]):
        support_portal_url (Union[Unset, str]):
        common_footer_text (Union[Unset, str]):
        common_footer_html (Union[Unset, str]):
        language_choices (Union[Unset, str]):
        disable_dark_theme (Union[Unset, bool]):
        powered_by_logo (Union[File, None, Unset]):
        hero_image (Union[File, None, Unset]):
        sidebar_logo (Union[File, None, Unset]):
        sidebar_logo_dark (Union[File, None, Unset]):
        sidebar_logo_mobile (Union[File, None, Unset]):
        sidebar_style (Union[Unset, str]):
        site_logo (Union[File, None, Unset]):
        login_logo (Union[File, None, Unset]):
        favicon (Union[File, None, Unset]):
        offering_logo_placeholder (Union[File, None, Unset]):
        waldur_support_enabled (Union[Unset, bool]):
        waldur_support_active_backend_type (Union[Unset, str]):
        waldur_support_display_request_type (Union[Unset, bool]):
        atlassian_use_old_api (Union[Unset, bool]):
        atlassian_use_teenage_api (Union[Unset, bool]):
        atlassian_use_automatic_request_mapping (Union[Unset, bool]):
        atlassian_map_waldur_users_to_servicedesk_agents (Union[Unset, bool]):
        atlassian_strange_setting (Union[Unset, int]):
        atlassian_api_url (Union[Unset, str]):
        atlassian_username (Union[Unset, str]):
        atlassian_password (Union[Unset, str]):
        atlassian_email (Union[Unset, str]):
        atlassian_token (Union[Unset, str]):
        atlassian_verify_ssl (Union[Unset, bool]):
        atlassian_project_id (Union[Unset, str]):
        atlassian_shared_username (Union[Unset, bool]):
        atlassian_custom_issue_field_mapping_enabled (Union[Unset, bool]):
        atlassian_default_offering_issue_type (Union[Unset, str]):
        atlassian_excluded_attachment_types (Union[Unset, str]):
        atlassian_pull_priorities (Union[Unset, bool]):
        atlassian_issue_types (Union[Unset, str]):
        atlassian_description_template (Union[Unset, str]):
        atlassian_summary_template (Union[Unset, str]):
        atlassian_affected_resource_field (Union[Unset, str]):
        atlassian_impact_field (Union[Unset, str]):
        atlassian_organisation_field (Union[Unset, str]):
        atlassian_resolution_sla_field (Union[Unset, str]):
        atlassian_project_field (Union[Unset, str]):
        atlassian_reporter_field (Union[Unset, str]):
        atlassian_caller_field (Union[Unset, str]):
        atlassian_sla_field (Union[Unset, str]):
        atlassian_linked_issue_type (Union[Unset, str]):
        atlassian_satisfaction_field (Union[Unset, str]):
        atlassian_request_feedback_field (Union[Unset, str]):
        atlassian_template_field (Union[Unset, str]):
        zammad_api_url (Union[Unset, str]):
        zammad_token (Union[Unset, str]):
        zammad_group (Union[Unset, str]):
        zammad_article_type (Union[Unset, str]):
        zammad_comment_marker (Union[Unset, str]):
        zammad_comment_prefix (Union[Unset, str]):
        zammad_comment_cooldown_duration (Union[Unset, int]):
        smax_api_url (Union[Unset, str]):
        smax_tenant_id (Union[Unset, str]):
        smax_login (Union[Unset, str]):
        smax_password (Union[Unset, str]):
        smax_organisation_field (Union[Unset, str]):
        smax_project_field (Union[Unset, str]):
        smax_affected_resource_field (Union[Unset, str]):
        smax_times_to_pull (Union[Unset, int]):
        smax_seconds_to_wait (Union[Unset, int]):
        smax_creation_source_name (Union[Unset, str]):
        smax_requests_offering (Union[Unset, str]):
        smax_verify_ssl (Union[Unset, bool]):
        proposal_review_duration (Union[Unset, int]):
        user_table_columns (Union[Unset, str]):
        auto_approve_user_tos (Union[Unset, bool]):
        freeipa_enabled (Union[Unset, bool]):
        freeipa_hostname (Union[Unset, str]):
        freeipa_username (Union[Unset, str]):
        freeipa_password (Union[Unset, str]):
        freeipa_verify_ssl (Union[Unset, bool]):
        freeipa_username_prefix (Union[Unset, str]):
        freeipa_groupname_prefix (Union[Unset, str]):
        freeipa_blacklisted_usernames (Union[Unset, list[str]]):
        freeipa_group_synchronization_enabled (Union[Unset, bool]):
        keycloak_icon (Union[File, None, Unset]):
        countries (Union[Unset, list[str]]):
    """

    site_name: Union[Unset, str] = UNSET
    site_description: Union[Unset, str] = UNSET
    homeport_url: Union[Unset, str] = UNSET
    site_address: Union[Unset, str] = UNSET
    site_email: Union[Unset, str] = UNSET
    site_phone: Union[Unset, str] = UNSET
    currency_name: Union[Unset, str] = UNSET
    thumbnail_size: Union[Unset, str] = UNSET
    anonymous_user_can_view_offerings: Union[Unset, bool] = UNSET
    anonymous_user_can_view_plans: Union[Unset, bool] = UNSET
    notify_staff_about_approvals: Union[Unset, bool] = UNSET
    notify_about_resource_change: Union[Unset, bool] = UNSET
    disable_sending_notifications_about_resource_update: Union[Unset, bool] = UNSET
    marketplace_landing_page: Union[Unset, str] = UNSET
    enable_stale_resource_notifications: Union[Unset, bool] = UNSET
    enable_resource_end_date: Union[Unset, bool] = UNSET
    telemetry_url: Union[Unset, str] = UNSET
    telemetry_version: Union[Unset, int] = UNSET
    script_run_mode: Union[Unset, str] = UNSET
    docker_client: Union[Unset, str] = UNSET
    docker_run_options: Union[Unset, str] = UNSET
    docker_script_dir: Union[Unset, str] = UNSET
    docker_remove_container: Union[Unset, bool] = UNSET
    docker_images: Union[Unset, str] = UNSET
    docker_volume_name: Union[Unset, str] = UNSET
    k8s_namespace: Union[Unset, str] = UNSET
    k8s_config_path: Union[Unset, str] = UNSET
    k8s_job_timeout: Union[Unset, int] = UNSET
    enable_strict_check_accepting_invitation: Union[Unset, bool] = UNSET
    invitation_disable_multiple_roles: Union[Unset, bool] = UNSET
    default_idp: Union[Unset, str] = UNSET
    docs_url: Union[Unset, str] = UNSET
    short_page_title: Union[Unset, str] = UNSET
    full_page_title: Union[Unset, str] = UNSET
    brand_color: Union[Unset, str] = UNSET
    hero_link_label: Union[Unset, str] = UNSET
    hero_link_url: Union[Unset, str] = UNSET
    support_portal_url: Union[Unset, str] = UNSET
    common_footer_text: Union[Unset, str] = UNSET
    common_footer_html: Union[Unset, str] = UNSET
    language_choices: Union[Unset, str] = UNSET
    disable_dark_theme: Union[Unset, bool] = UNSET
    powered_by_logo: Union[File, None, Unset] = UNSET
    hero_image: Union[File, None, Unset] = UNSET
    sidebar_logo: Union[File, None, Unset] = UNSET
    sidebar_logo_dark: Union[File, None, Unset] = UNSET
    sidebar_logo_mobile: Union[File, None, Unset] = UNSET
    sidebar_style: Union[Unset, str] = UNSET
    site_logo: Union[File, None, Unset] = UNSET
    login_logo: Union[File, None, Unset] = UNSET
    favicon: Union[File, None, Unset] = UNSET
    offering_logo_placeholder: Union[File, None, Unset] = UNSET
    waldur_support_enabled: Union[Unset, bool] = UNSET
    waldur_support_active_backend_type: Union[Unset, str] = UNSET
    waldur_support_display_request_type: Union[Unset, bool] = UNSET
    atlassian_use_old_api: Union[Unset, bool] = UNSET
    atlassian_use_teenage_api: Union[Unset, bool] = UNSET
    atlassian_use_automatic_request_mapping: Union[Unset, bool] = UNSET
    atlassian_map_waldur_users_to_servicedesk_agents: Union[Unset, bool] = UNSET
    atlassian_strange_setting: Union[Unset, int] = UNSET
    atlassian_api_url: Union[Unset, str] = UNSET
    atlassian_username: Union[Unset, str] = UNSET
    atlassian_password: Union[Unset, str] = UNSET
    atlassian_email: Union[Unset, str] = UNSET
    atlassian_token: Union[Unset, str] = UNSET
    atlassian_verify_ssl: Union[Unset, bool] = UNSET
    atlassian_project_id: Union[Unset, str] = UNSET
    atlassian_shared_username: Union[Unset, bool] = UNSET
    atlassian_custom_issue_field_mapping_enabled: Union[Unset, bool] = UNSET
    atlassian_default_offering_issue_type: Union[Unset, str] = UNSET
    atlassian_excluded_attachment_types: Union[Unset, str] = UNSET
    atlassian_pull_priorities: Union[Unset, bool] = UNSET
    atlassian_issue_types: Union[Unset, str] = UNSET
    atlassian_description_template: Union[Unset, str] = UNSET
    atlassian_summary_template: Union[Unset, str] = UNSET
    atlassian_affected_resource_field: Union[Unset, str] = UNSET
    atlassian_impact_field: Union[Unset, str] = UNSET
    atlassian_organisation_field: Union[Unset, str] = UNSET
    atlassian_resolution_sla_field: Union[Unset, str] = UNSET
    atlassian_project_field: Union[Unset, str] = UNSET
    atlassian_reporter_field: Union[Unset, str] = UNSET
    atlassian_caller_field: Union[Unset, str] = UNSET
    atlassian_sla_field: Union[Unset, str] = UNSET
    atlassian_linked_issue_type: Union[Unset, str] = UNSET
    atlassian_satisfaction_field: Union[Unset, str] = UNSET
    atlassian_request_feedback_field: Union[Unset, str] = UNSET
    atlassian_template_field: Union[Unset, str] = UNSET
    zammad_api_url: Union[Unset, str] = UNSET
    zammad_token: Union[Unset, str] = UNSET
    zammad_group: Union[Unset, str] = UNSET
    zammad_article_type: Union[Unset, str] = UNSET
    zammad_comment_marker: Union[Unset, str] = UNSET
    zammad_comment_prefix: Union[Unset, str] = UNSET
    zammad_comment_cooldown_duration: Union[Unset, int] = UNSET
    smax_api_url: Union[Unset, str] = UNSET
    smax_tenant_id: Union[Unset, str] = UNSET
    smax_login: Union[Unset, str] = UNSET
    smax_password: Union[Unset, str] = UNSET
    smax_organisation_field: Union[Unset, str] = UNSET
    smax_project_field: Union[Unset, str] = UNSET
    smax_affected_resource_field: Union[Unset, str] = UNSET
    smax_times_to_pull: Union[Unset, int] = UNSET
    smax_seconds_to_wait: Union[Unset, int] = UNSET
    smax_creation_source_name: Union[Unset, str] = UNSET
    smax_requests_offering: Union[Unset, str] = UNSET
    smax_verify_ssl: Union[Unset, bool] = UNSET
    proposal_review_duration: Union[Unset, int] = UNSET
    user_table_columns: Union[Unset, str] = UNSET
    auto_approve_user_tos: Union[Unset, bool] = UNSET
    freeipa_enabled: Union[Unset, bool] = UNSET
    freeipa_hostname: Union[Unset, str] = UNSET
    freeipa_username: Union[Unset, str] = UNSET
    freeipa_password: Union[Unset, str] = UNSET
    freeipa_verify_ssl: Union[Unset, bool] = UNSET
    freeipa_username_prefix: Union[Unset, str] = UNSET
    freeipa_groupname_prefix: Union[Unset, str] = UNSET
    freeipa_blacklisted_usernames: Union[Unset, list[str]] = UNSET
    freeipa_group_synchronization_enabled: Union[Unset, bool] = UNSET
    keycloak_icon: Union[File, None, Unset] = UNSET
    countries: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_name = self.site_name

        site_description = self.site_description

        homeport_url = self.homeport_url

        site_address = self.site_address

        site_email = self.site_email

        site_phone = self.site_phone

        currency_name = self.currency_name

        thumbnail_size = self.thumbnail_size

        anonymous_user_can_view_offerings = self.anonymous_user_can_view_offerings

        anonymous_user_can_view_plans = self.anonymous_user_can_view_plans

        notify_staff_about_approvals = self.notify_staff_about_approvals

        notify_about_resource_change = self.notify_about_resource_change

        disable_sending_notifications_about_resource_update = self.disable_sending_notifications_about_resource_update

        marketplace_landing_page = self.marketplace_landing_page

        enable_stale_resource_notifications = self.enable_stale_resource_notifications

        enable_resource_end_date = self.enable_resource_end_date

        telemetry_url = self.telemetry_url

        telemetry_version = self.telemetry_version

        script_run_mode = self.script_run_mode

        docker_client = self.docker_client

        docker_run_options = self.docker_run_options

        docker_script_dir = self.docker_script_dir

        docker_remove_container = self.docker_remove_container

        docker_images = self.docker_images

        docker_volume_name = self.docker_volume_name

        k8s_namespace = self.k8s_namespace

        k8s_config_path = self.k8s_config_path

        k8s_job_timeout = self.k8s_job_timeout

        enable_strict_check_accepting_invitation = self.enable_strict_check_accepting_invitation

        invitation_disable_multiple_roles = self.invitation_disable_multiple_roles

        default_idp = self.default_idp

        docs_url = self.docs_url

        short_page_title = self.short_page_title

        full_page_title = self.full_page_title

        brand_color = self.brand_color

        hero_link_label = self.hero_link_label

        hero_link_url = self.hero_link_url

        support_portal_url = self.support_portal_url

        common_footer_text = self.common_footer_text

        common_footer_html = self.common_footer_html

        language_choices = self.language_choices

        disable_dark_theme = self.disable_dark_theme

        powered_by_logo: Union[FileJsonType, None, Unset]
        if isinstance(self.powered_by_logo, Unset):
            powered_by_logo = UNSET
        elif isinstance(self.powered_by_logo, File):
            powered_by_logo = self.powered_by_logo.to_tuple()

        else:
            powered_by_logo = self.powered_by_logo

        hero_image: Union[FileJsonType, None, Unset]
        if isinstance(self.hero_image, Unset):
            hero_image = UNSET
        elif isinstance(self.hero_image, File):
            hero_image = self.hero_image.to_tuple()

        else:
            hero_image = self.hero_image

        sidebar_logo: Union[FileJsonType, None, Unset]
        if isinstance(self.sidebar_logo, Unset):
            sidebar_logo = UNSET
        elif isinstance(self.sidebar_logo, File):
            sidebar_logo = self.sidebar_logo.to_tuple()

        else:
            sidebar_logo = self.sidebar_logo

        sidebar_logo_dark: Union[FileJsonType, None, Unset]
        if isinstance(self.sidebar_logo_dark, Unset):
            sidebar_logo_dark = UNSET
        elif isinstance(self.sidebar_logo_dark, File):
            sidebar_logo_dark = self.sidebar_logo_dark.to_tuple()

        else:
            sidebar_logo_dark = self.sidebar_logo_dark

        sidebar_logo_mobile: Union[FileJsonType, None, Unset]
        if isinstance(self.sidebar_logo_mobile, Unset):
            sidebar_logo_mobile = UNSET
        elif isinstance(self.sidebar_logo_mobile, File):
            sidebar_logo_mobile = self.sidebar_logo_mobile.to_tuple()

        else:
            sidebar_logo_mobile = self.sidebar_logo_mobile

        sidebar_style = self.sidebar_style

        site_logo: Union[FileJsonType, None, Unset]
        if isinstance(self.site_logo, Unset):
            site_logo = UNSET
        elif isinstance(self.site_logo, File):
            site_logo = self.site_logo.to_tuple()

        else:
            site_logo = self.site_logo

        login_logo: Union[FileJsonType, None, Unset]
        if isinstance(self.login_logo, Unset):
            login_logo = UNSET
        elif isinstance(self.login_logo, File):
            login_logo = self.login_logo.to_tuple()

        else:
            login_logo = self.login_logo

        favicon: Union[FileJsonType, None, Unset]
        if isinstance(self.favicon, Unset):
            favicon = UNSET
        elif isinstance(self.favicon, File):
            favicon = self.favicon.to_tuple()

        else:
            favicon = self.favicon

        offering_logo_placeholder: Union[FileJsonType, None, Unset]
        if isinstance(self.offering_logo_placeholder, Unset):
            offering_logo_placeholder = UNSET
        elif isinstance(self.offering_logo_placeholder, File):
            offering_logo_placeholder = self.offering_logo_placeholder.to_tuple()

        else:
            offering_logo_placeholder = self.offering_logo_placeholder

        waldur_support_enabled = self.waldur_support_enabled

        waldur_support_active_backend_type = self.waldur_support_active_backend_type

        waldur_support_display_request_type = self.waldur_support_display_request_type

        atlassian_use_old_api = self.atlassian_use_old_api

        atlassian_use_teenage_api = self.atlassian_use_teenage_api

        atlassian_use_automatic_request_mapping = self.atlassian_use_automatic_request_mapping

        atlassian_map_waldur_users_to_servicedesk_agents = self.atlassian_map_waldur_users_to_servicedesk_agents

        atlassian_strange_setting = self.atlassian_strange_setting

        atlassian_api_url = self.atlassian_api_url

        atlassian_username = self.atlassian_username

        atlassian_password = self.atlassian_password

        atlassian_email = self.atlassian_email

        atlassian_token = self.atlassian_token

        atlassian_verify_ssl = self.atlassian_verify_ssl

        atlassian_project_id = self.atlassian_project_id

        atlassian_shared_username = self.atlassian_shared_username

        atlassian_custom_issue_field_mapping_enabled = self.atlassian_custom_issue_field_mapping_enabled

        atlassian_default_offering_issue_type = self.atlassian_default_offering_issue_type

        atlassian_excluded_attachment_types = self.atlassian_excluded_attachment_types

        atlassian_pull_priorities = self.atlassian_pull_priorities

        atlassian_issue_types = self.atlassian_issue_types

        atlassian_description_template = self.atlassian_description_template

        atlassian_summary_template = self.atlassian_summary_template

        atlassian_affected_resource_field = self.atlassian_affected_resource_field

        atlassian_impact_field = self.atlassian_impact_field

        atlassian_organisation_field = self.atlassian_organisation_field

        atlassian_resolution_sla_field = self.atlassian_resolution_sla_field

        atlassian_project_field = self.atlassian_project_field

        atlassian_reporter_field = self.atlassian_reporter_field

        atlassian_caller_field = self.atlassian_caller_field

        atlassian_sla_field = self.atlassian_sla_field

        atlassian_linked_issue_type = self.atlassian_linked_issue_type

        atlassian_satisfaction_field = self.atlassian_satisfaction_field

        atlassian_request_feedback_field = self.atlassian_request_feedback_field

        atlassian_template_field = self.atlassian_template_field

        zammad_api_url = self.zammad_api_url

        zammad_token = self.zammad_token

        zammad_group = self.zammad_group

        zammad_article_type = self.zammad_article_type

        zammad_comment_marker = self.zammad_comment_marker

        zammad_comment_prefix = self.zammad_comment_prefix

        zammad_comment_cooldown_duration = self.zammad_comment_cooldown_duration

        smax_api_url = self.smax_api_url

        smax_tenant_id = self.smax_tenant_id

        smax_login = self.smax_login

        smax_password = self.smax_password

        smax_organisation_field = self.smax_organisation_field

        smax_project_field = self.smax_project_field

        smax_affected_resource_field = self.smax_affected_resource_field

        smax_times_to_pull = self.smax_times_to_pull

        smax_seconds_to_wait = self.smax_seconds_to_wait

        smax_creation_source_name = self.smax_creation_source_name

        smax_requests_offering = self.smax_requests_offering

        smax_verify_ssl = self.smax_verify_ssl

        proposal_review_duration = self.proposal_review_duration

        user_table_columns = self.user_table_columns

        auto_approve_user_tos = self.auto_approve_user_tos

        freeipa_enabled = self.freeipa_enabled

        freeipa_hostname = self.freeipa_hostname

        freeipa_username = self.freeipa_username

        freeipa_password = self.freeipa_password

        freeipa_verify_ssl = self.freeipa_verify_ssl

        freeipa_username_prefix = self.freeipa_username_prefix

        freeipa_groupname_prefix = self.freeipa_groupname_prefix

        freeipa_blacklisted_usernames: Union[Unset, list[str]] = UNSET
        if not isinstance(self.freeipa_blacklisted_usernames, Unset):
            freeipa_blacklisted_usernames = self.freeipa_blacklisted_usernames

        freeipa_group_synchronization_enabled = self.freeipa_group_synchronization_enabled

        keycloak_icon: Union[FileJsonType, None, Unset]
        if isinstance(self.keycloak_icon, Unset):
            keycloak_icon = UNSET
        elif isinstance(self.keycloak_icon, File):
            keycloak_icon = self.keycloak_icon.to_tuple()

        else:
            keycloak_icon = self.keycloak_icon

        countries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_name is not UNSET:
            field_dict["SITE_NAME"] = site_name
        if site_description is not UNSET:
            field_dict["SITE_DESCRIPTION"] = site_description
        if homeport_url is not UNSET:
            field_dict["HOMEPORT_URL"] = homeport_url
        if site_address is not UNSET:
            field_dict["SITE_ADDRESS"] = site_address
        if site_email is not UNSET:
            field_dict["SITE_EMAIL"] = site_email
        if site_phone is not UNSET:
            field_dict["SITE_PHONE"] = site_phone
        if currency_name is not UNSET:
            field_dict["CURRENCY_NAME"] = currency_name
        if thumbnail_size is not UNSET:
            field_dict["THUMBNAIL_SIZE"] = thumbnail_size
        if anonymous_user_can_view_offerings is not UNSET:
            field_dict["ANONYMOUS_USER_CAN_VIEW_OFFERINGS"] = anonymous_user_can_view_offerings
        if anonymous_user_can_view_plans is not UNSET:
            field_dict["ANONYMOUS_USER_CAN_VIEW_PLANS"] = anonymous_user_can_view_plans
        if notify_staff_about_approvals is not UNSET:
            field_dict["NOTIFY_STAFF_ABOUT_APPROVALS"] = notify_staff_about_approvals
        if notify_about_resource_change is not UNSET:
            field_dict["NOTIFY_ABOUT_RESOURCE_CHANGE"] = notify_about_resource_change
        if disable_sending_notifications_about_resource_update is not UNSET:
            field_dict["DISABLE_SENDING_NOTIFICATIONS_ABOUT_RESOURCE_UPDATE"] = (
                disable_sending_notifications_about_resource_update
            )
        if marketplace_landing_page is not UNSET:
            field_dict["MARKETPLACE_LANDING_PAGE"] = marketplace_landing_page
        if enable_stale_resource_notifications is not UNSET:
            field_dict["ENABLE_STALE_RESOURCE_NOTIFICATIONS"] = enable_stale_resource_notifications
        if enable_resource_end_date is not UNSET:
            field_dict["ENABLE_RESOURCE_END_DATE"] = enable_resource_end_date
        if telemetry_url is not UNSET:
            field_dict["TELEMETRY_URL"] = telemetry_url
        if telemetry_version is not UNSET:
            field_dict["TELEMETRY_VERSION"] = telemetry_version
        if script_run_mode is not UNSET:
            field_dict["SCRIPT_RUN_MODE"] = script_run_mode
        if docker_client is not UNSET:
            field_dict["DOCKER_CLIENT"] = docker_client
        if docker_run_options is not UNSET:
            field_dict["DOCKER_RUN_OPTIONS"] = docker_run_options
        if docker_script_dir is not UNSET:
            field_dict["DOCKER_SCRIPT_DIR"] = docker_script_dir
        if docker_remove_container is not UNSET:
            field_dict["DOCKER_REMOVE_CONTAINER"] = docker_remove_container
        if docker_images is not UNSET:
            field_dict["DOCKER_IMAGES"] = docker_images
        if docker_volume_name is not UNSET:
            field_dict["DOCKER_VOLUME_NAME"] = docker_volume_name
        if k8s_namespace is not UNSET:
            field_dict["K8S_NAMESPACE"] = k8s_namespace
        if k8s_config_path is not UNSET:
            field_dict["K8S_CONFIG_PATH"] = k8s_config_path
        if k8s_job_timeout is not UNSET:
            field_dict["K8S_JOB_TIMEOUT"] = k8s_job_timeout
        if enable_strict_check_accepting_invitation is not UNSET:
            field_dict["ENABLE_STRICT_CHECK_ACCEPTING_INVITATION"] = enable_strict_check_accepting_invitation
        if invitation_disable_multiple_roles is not UNSET:
            field_dict["INVITATION_DISABLE_MULTIPLE_ROLES"] = invitation_disable_multiple_roles
        if default_idp is not UNSET:
            field_dict["DEFAULT_IDP"] = default_idp
        if docs_url is not UNSET:
            field_dict["DOCS_URL"] = docs_url
        if short_page_title is not UNSET:
            field_dict["SHORT_PAGE_TITLE"] = short_page_title
        if full_page_title is not UNSET:
            field_dict["FULL_PAGE_TITLE"] = full_page_title
        if brand_color is not UNSET:
            field_dict["BRAND_COLOR"] = brand_color
        if hero_link_label is not UNSET:
            field_dict["HERO_LINK_LABEL"] = hero_link_label
        if hero_link_url is not UNSET:
            field_dict["HERO_LINK_URL"] = hero_link_url
        if support_portal_url is not UNSET:
            field_dict["SUPPORT_PORTAL_URL"] = support_portal_url
        if common_footer_text is not UNSET:
            field_dict["COMMON_FOOTER_TEXT"] = common_footer_text
        if common_footer_html is not UNSET:
            field_dict["COMMON_FOOTER_HTML"] = common_footer_html
        if language_choices is not UNSET:
            field_dict["LANGUAGE_CHOICES"] = language_choices
        if disable_dark_theme is not UNSET:
            field_dict["DISABLE_DARK_THEME"] = disable_dark_theme
        if powered_by_logo is not UNSET:
            field_dict["POWERED_BY_LOGO"] = powered_by_logo
        if hero_image is not UNSET:
            field_dict["HERO_IMAGE"] = hero_image
        if sidebar_logo is not UNSET:
            field_dict["SIDEBAR_LOGO"] = sidebar_logo
        if sidebar_logo_dark is not UNSET:
            field_dict["SIDEBAR_LOGO_DARK"] = sidebar_logo_dark
        if sidebar_logo_mobile is not UNSET:
            field_dict["SIDEBAR_LOGO_MOBILE"] = sidebar_logo_mobile
        if sidebar_style is not UNSET:
            field_dict["SIDEBAR_STYLE"] = sidebar_style
        if site_logo is not UNSET:
            field_dict["SITE_LOGO"] = site_logo
        if login_logo is not UNSET:
            field_dict["LOGIN_LOGO"] = login_logo
        if favicon is not UNSET:
            field_dict["FAVICON"] = favicon
        if offering_logo_placeholder is not UNSET:
            field_dict["OFFERING_LOGO_PLACEHOLDER"] = offering_logo_placeholder
        if waldur_support_enabled is not UNSET:
            field_dict["WALDUR_SUPPORT_ENABLED"] = waldur_support_enabled
        if waldur_support_active_backend_type is not UNSET:
            field_dict["WALDUR_SUPPORT_ACTIVE_BACKEND_TYPE"] = waldur_support_active_backend_type
        if waldur_support_display_request_type is not UNSET:
            field_dict["WALDUR_SUPPORT_DISPLAY_REQUEST_TYPE"] = waldur_support_display_request_type
        if atlassian_use_old_api is not UNSET:
            field_dict["ATLASSIAN_USE_OLD_API"] = atlassian_use_old_api
        if atlassian_use_teenage_api is not UNSET:
            field_dict["ATLASSIAN_USE_TEENAGE_API"] = atlassian_use_teenage_api
        if atlassian_use_automatic_request_mapping is not UNSET:
            field_dict["ATLASSIAN_USE_AUTOMATIC_REQUEST_MAPPING"] = atlassian_use_automatic_request_mapping
        if atlassian_map_waldur_users_to_servicedesk_agents is not UNSET:
            field_dict["ATLASSIAN_MAP_WALDUR_USERS_TO_SERVICEDESK_AGENTS"] = (
                atlassian_map_waldur_users_to_servicedesk_agents
            )
        if atlassian_strange_setting is not UNSET:
            field_dict["ATLASSIAN_STRANGE_SETTING"] = atlassian_strange_setting
        if atlassian_api_url is not UNSET:
            field_dict["ATLASSIAN_API_URL"] = atlassian_api_url
        if atlassian_username is not UNSET:
            field_dict["ATLASSIAN_USERNAME"] = atlassian_username
        if atlassian_password is not UNSET:
            field_dict["ATLASSIAN_PASSWORD"] = atlassian_password
        if atlassian_email is not UNSET:
            field_dict["ATLASSIAN_EMAIL"] = atlassian_email
        if atlassian_token is not UNSET:
            field_dict["ATLASSIAN_TOKEN"] = atlassian_token
        if atlassian_verify_ssl is not UNSET:
            field_dict["ATLASSIAN_VERIFY_SSL"] = atlassian_verify_ssl
        if atlassian_project_id is not UNSET:
            field_dict["ATLASSIAN_PROJECT_ID"] = atlassian_project_id
        if atlassian_shared_username is not UNSET:
            field_dict["ATLASSIAN_SHARED_USERNAME"] = atlassian_shared_username
        if atlassian_custom_issue_field_mapping_enabled is not UNSET:
            field_dict["ATLASSIAN_CUSTOM_ISSUE_FIELD_MAPPING_ENABLED"] = atlassian_custom_issue_field_mapping_enabled
        if atlassian_default_offering_issue_type is not UNSET:
            field_dict["ATLASSIAN_DEFAULT_OFFERING_ISSUE_TYPE"] = atlassian_default_offering_issue_type
        if atlassian_excluded_attachment_types is not UNSET:
            field_dict["ATLASSIAN_EXCLUDED_ATTACHMENT_TYPES"] = atlassian_excluded_attachment_types
        if atlassian_pull_priorities is not UNSET:
            field_dict["ATLASSIAN_PULL_PRIORITIES"] = atlassian_pull_priorities
        if atlassian_issue_types is not UNSET:
            field_dict["ATLASSIAN_ISSUE_TYPES"] = atlassian_issue_types
        if atlassian_description_template is not UNSET:
            field_dict["ATLASSIAN_DESCRIPTION_TEMPLATE"] = atlassian_description_template
        if atlassian_summary_template is not UNSET:
            field_dict["ATLASSIAN_SUMMARY_TEMPLATE"] = atlassian_summary_template
        if atlassian_affected_resource_field is not UNSET:
            field_dict["ATLASSIAN_AFFECTED_RESOURCE_FIELD"] = atlassian_affected_resource_field
        if atlassian_impact_field is not UNSET:
            field_dict["ATLASSIAN_IMPACT_FIELD"] = atlassian_impact_field
        if atlassian_organisation_field is not UNSET:
            field_dict["ATLASSIAN_ORGANISATION_FIELD"] = atlassian_organisation_field
        if atlassian_resolution_sla_field is not UNSET:
            field_dict["ATLASSIAN_RESOLUTION_SLA_FIELD"] = atlassian_resolution_sla_field
        if atlassian_project_field is not UNSET:
            field_dict["ATLASSIAN_PROJECT_FIELD"] = atlassian_project_field
        if atlassian_reporter_field is not UNSET:
            field_dict["ATLASSIAN_REPORTER_FIELD"] = atlassian_reporter_field
        if atlassian_caller_field is not UNSET:
            field_dict["ATLASSIAN_CALLER_FIELD"] = atlassian_caller_field
        if atlassian_sla_field is not UNSET:
            field_dict["ATLASSIAN_SLA_FIELD"] = atlassian_sla_field
        if atlassian_linked_issue_type is not UNSET:
            field_dict["ATLASSIAN_LINKED_ISSUE_TYPE"] = atlassian_linked_issue_type
        if atlassian_satisfaction_field is not UNSET:
            field_dict["ATLASSIAN_SATISFACTION_FIELD"] = atlassian_satisfaction_field
        if atlassian_request_feedback_field is not UNSET:
            field_dict["ATLASSIAN_REQUEST_FEEDBACK_FIELD"] = atlassian_request_feedback_field
        if atlassian_template_field is not UNSET:
            field_dict["ATLASSIAN_TEMPLATE_FIELD"] = atlassian_template_field
        if zammad_api_url is not UNSET:
            field_dict["ZAMMAD_API_URL"] = zammad_api_url
        if zammad_token is not UNSET:
            field_dict["ZAMMAD_TOKEN"] = zammad_token
        if zammad_group is not UNSET:
            field_dict["ZAMMAD_GROUP"] = zammad_group
        if zammad_article_type is not UNSET:
            field_dict["ZAMMAD_ARTICLE_TYPE"] = zammad_article_type
        if zammad_comment_marker is not UNSET:
            field_dict["ZAMMAD_COMMENT_MARKER"] = zammad_comment_marker
        if zammad_comment_prefix is not UNSET:
            field_dict["ZAMMAD_COMMENT_PREFIX"] = zammad_comment_prefix
        if zammad_comment_cooldown_duration is not UNSET:
            field_dict["ZAMMAD_COMMENT_COOLDOWN_DURATION"] = zammad_comment_cooldown_duration
        if smax_api_url is not UNSET:
            field_dict["SMAX_API_URL"] = smax_api_url
        if smax_tenant_id is not UNSET:
            field_dict["SMAX_TENANT_ID"] = smax_tenant_id
        if smax_login is not UNSET:
            field_dict["SMAX_LOGIN"] = smax_login
        if smax_password is not UNSET:
            field_dict["SMAX_PASSWORD"] = smax_password
        if smax_organisation_field is not UNSET:
            field_dict["SMAX_ORGANISATION_FIELD"] = smax_organisation_field
        if smax_project_field is not UNSET:
            field_dict["SMAX_PROJECT_FIELD"] = smax_project_field
        if smax_affected_resource_field is not UNSET:
            field_dict["SMAX_AFFECTED_RESOURCE_FIELD"] = smax_affected_resource_field
        if smax_times_to_pull is not UNSET:
            field_dict["SMAX_TIMES_TO_PULL"] = smax_times_to_pull
        if smax_seconds_to_wait is not UNSET:
            field_dict["SMAX_SECONDS_TO_WAIT"] = smax_seconds_to_wait
        if smax_creation_source_name is not UNSET:
            field_dict["SMAX_CREATION_SOURCE_NAME"] = smax_creation_source_name
        if smax_requests_offering is not UNSET:
            field_dict["SMAX_REQUESTS_OFFERING"] = smax_requests_offering
        if smax_verify_ssl is not UNSET:
            field_dict["SMAX_VERIFY_SSL"] = smax_verify_ssl
        if proposal_review_duration is not UNSET:
            field_dict["PROPOSAL_REVIEW_DURATION"] = proposal_review_duration
        if user_table_columns is not UNSET:
            field_dict["USER_TABLE_COLUMNS"] = user_table_columns
        if auto_approve_user_tos is not UNSET:
            field_dict["AUTO_APPROVE_USER_TOS"] = auto_approve_user_tos
        if freeipa_enabled is not UNSET:
            field_dict["FREEIPA_ENABLED"] = freeipa_enabled
        if freeipa_hostname is not UNSET:
            field_dict["FREEIPA_HOSTNAME"] = freeipa_hostname
        if freeipa_username is not UNSET:
            field_dict["FREEIPA_USERNAME"] = freeipa_username
        if freeipa_password is not UNSET:
            field_dict["FREEIPA_PASSWORD"] = freeipa_password
        if freeipa_verify_ssl is not UNSET:
            field_dict["FREEIPA_VERIFY_SSL"] = freeipa_verify_ssl
        if freeipa_username_prefix is not UNSET:
            field_dict["FREEIPA_USERNAME_PREFIX"] = freeipa_username_prefix
        if freeipa_groupname_prefix is not UNSET:
            field_dict["FREEIPA_GROUPNAME_PREFIX"] = freeipa_groupname_prefix
        if freeipa_blacklisted_usernames is not UNSET:
            field_dict["FREEIPA_BLACKLISTED_USERNAMES"] = freeipa_blacklisted_usernames
        if freeipa_group_synchronization_enabled is not UNSET:
            field_dict["FREEIPA_GROUP_SYNCHRONIZATION_ENABLED"] = freeipa_group_synchronization_enabled
        if keycloak_icon is not UNSET:
            field_dict["KEYCLOAK_ICON"] = keycloak_icon
        if countries is not UNSET:
            field_dict["COUNTRIES"] = countries

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        site_name = (
            self.site_name if isinstance(self.site_name, Unset) else (None, str(self.site_name).encode(), "text/plain")
        )

        site_description = (
            self.site_description
            if isinstance(self.site_description, Unset)
            else (None, str(self.site_description).encode(), "text/plain")
        )

        homeport_url = (
            self.homeport_url
            if isinstance(self.homeport_url, Unset)
            else (None, str(self.homeport_url).encode(), "text/plain")
        )

        site_address = (
            self.site_address
            if isinstance(self.site_address, Unset)
            else (None, str(self.site_address).encode(), "text/plain")
        )

        site_email = (
            self.site_email
            if isinstance(self.site_email, Unset)
            else (None, str(self.site_email).encode(), "text/plain")
        )

        site_phone = (
            self.site_phone
            if isinstance(self.site_phone, Unset)
            else (None, str(self.site_phone).encode(), "text/plain")
        )

        currency_name = (
            self.currency_name
            if isinstance(self.currency_name, Unset)
            else (None, str(self.currency_name).encode(), "text/plain")
        )

        thumbnail_size = (
            self.thumbnail_size
            if isinstance(self.thumbnail_size, Unset)
            else (None, str(self.thumbnail_size).encode(), "text/plain")
        )

        anonymous_user_can_view_offerings = (
            self.anonymous_user_can_view_offerings
            if isinstance(self.anonymous_user_can_view_offerings, Unset)
            else (None, str(self.anonymous_user_can_view_offerings).encode(), "text/plain")
        )

        anonymous_user_can_view_plans = (
            self.anonymous_user_can_view_plans
            if isinstance(self.anonymous_user_can_view_plans, Unset)
            else (None, str(self.anonymous_user_can_view_plans).encode(), "text/plain")
        )

        notify_staff_about_approvals = (
            self.notify_staff_about_approvals
            if isinstance(self.notify_staff_about_approvals, Unset)
            else (None, str(self.notify_staff_about_approvals).encode(), "text/plain")
        )

        notify_about_resource_change = (
            self.notify_about_resource_change
            if isinstance(self.notify_about_resource_change, Unset)
            else (None, str(self.notify_about_resource_change).encode(), "text/plain")
        )

        disable_sending_notifications_about_resource_update = (
            self.disable_sending_notifications_about_resource_update
            if isinstance(self.disable_sending_notifications_about_resource_update, Unset)
            else (None, str(self.disable_sending_notifications_about_resource_update).encode(), "text/plain")
        )

        marketplace_landing_page = (
            self.marketplace_landing_page
            if isinstance(self.marketplace_landing_page, Unset)
            else (None, str(self.marketplace_landing_page).encode(), "text/plain")
        )

        enable_stale_resource_notifications = (
            self.enable_stale_resource_notifications
            if isinstance(self.enable_stale_resource_notifications, Unset)
            else (None, str(self.enable_stale_resource_notifications).encode(), "text/plain")
        )

        enable_resource_end_date = (
            self.enable_resource_end_date
            if isinstance(self.enable_resource_end_date, Unset)
            else (None, str(self.enable_resource_end_date).encode(), "text/plain")
        )

        telemetry_url = (
            self.telemetry_url
            if isinstance(self.telemetry_url, Unset)
            else (None, str(self.telemetry_url).encode(), "text/plain")
        )

        telemetry_version = (
            self.telemetry_version
            if isinstance(self.telemetry_version, Unset)
            else (None, str(self.telemetry_version).encode(), "text/plain")
        )

        script_run_mode = (
            self.script_run_mode
            if isinstance(self.script_run_mode, Unset)
            else (None, str(self.script_run_mode).encode(), "text/plain")
        )

        docker_client = (
            self.docker_client
            if isinstance(self.docker_client, Unset)
            else (None, str(self.docker_client).encode(), "text/plain")
        )

        docker_run_options = (
            self.docker_run_options
            if isinstance(self.docker_run_options, Unset)
            else (None, str(self.docker_run_options).encode(), "text/plain")
        )

        docker_script_dir = (
            self.docker_script_dir
            if isinstance(self.docker_script_dir, Unset)
            else (None, str(self.docker_script_dir).encode(), "text/plain")
        )

        docker_remove_container = (
            self.docker_remove_container
            if isinstance(self.docker_remove_container, Unset)
            else (None, str(self.docker_remove_container).encode(), "text/plain")
        )

        docker_images = (
            self.docker_images
            if isinstance(self.docker_images, Unset)
            else (None, str(self.docker_images).encode(), "text/plain")
        )

        docker_volume_name = (
            self.docker_volume_name
            if isinstance(self.docker_volume_name, Unset)
            else (None, str(self.docker_volume_name).encode(), "text/plain")
        )

        k8s_namespace = (
            self.k8s_namespace
            if isinstance(self.k8s_namespace, Unset)
            else (None, str(self.k8s_namespace).encode(), "text/plain")
        )

        k8s_config_path = (
            self.k8s_config_path
            if isinstance(self.k8s_config_path, Unset)
            else (None, str(self.k8s_config_path).encode(), "text/plain")
        )

        k8s_job_timeout = (
            self.k8s_job_timeout
            if isinstance(self.k8s_job_timeout, Unset)
            else (None, str(self.k8s_job_timeout).encode(), "text/plain")
        )

        enable_strict_check_accepting_invitation = (
            self.enable_strict_check_accepting_invitation
            if isinstance(self.enable_strict_check_accepting_invitation, Unset)
            else (None, str(self.enable_strict_check_accepting_invitation).encode(), "text/plain")
        )

        invitation_disable_multiple_roles = (
            self.invitation_disable_multiple_roles
            if isinstance(self.invitation_disable_multiple_roles, Unset)
            else (None, str(self.invitation_disable_multiple_roles).encode(), "text/plain")
        )

        default_idp = (
            self.default_idp
            if isinstance(self.default_idp, Unset)
            else (None, str(self.default_idp).encode(), "text/plain")
        )

        docs_url = (
            self.docs_url if isinstance(self.docs_url, Unset) else (None, str(self.docs_url).encode(), "text/plain")
        )

        short_page_title = (
            self.short_page_title
            if isinstance(self.short_page_title, Unset)
            else (None, str(self.short_page_title).encode(), "text/plain")
        )

        full_page_title = (
            self.full_page_title
            if isinstance(self.full_page_title, Unset)
            else (None, str(self.full_page_title).encode(), "text/plain")
        )

        brand_color = (
            self.brand_color
            if isinstance(self.brand_color, Unset)
            else (None, str(self.brand_color).encode(), "text/plain")
        )

        hero_link_label = (
            self.hero_link_label
            if isinstance(self.hero_link_label, Unset)
            else (None, str(self.hero_link_label).encode(), "text/plain")
        )

        hero_link_url = (
            self.hero_link_url
            if isinstance(self.hero_link_url, Unset)
            else (None, str(self.hero_link_url).encode(), "text/plain")
        )

        support_portal_url = (
            self.support_portal_url
            if isinstance(self.support_portal_url, Unset)
            else (None, str(self.support_portal_url).encode(), "text/plain")
        )

        common_footer_text = (
            self.common_footer_text
            if isinstance(self.common_footer_text, Unset)
            else (None, str(self.common_footer_text).encode(), "text/plain")
        )

        common_footer_html = (
            self.common_footer_html
            if isinstance(self.common_footer_html, Unset)
            else (None, str(self.common_footer_html).encode(), "text/plain")
        )

        language_choices = (
            self.language_choices
            if isinstance(self.language_choices, Unset)
            else (None, str(self.language_choices).encode(), "text/plain")
        )

        disable_dark_theme = (
            self.disable_dark_theme
            if isinstance(self.disable_dark_theme, Unset)
            else (None, str(self.disable_dark_theme).encode(), "text/plain")
        )

        powered_by_logo: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.powered_by_logo, Unset):
            powered_by_logo = UNSET
        elif isinstance(self.powered_by_logo, File):
            powered_by_logo = self.powered_by_logo.to_tuple()
        else:
            powered_by_logo = (None, str(self.powered_by_logo).encode(), "text/plain")

        hero_image: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.hero_image, Unset):
            hero_image = UNSET
        elif isinstance(self.hero_image, File):
            hero_image = self.hero_image.to_tuple()
        else:
            hero_image = (None, str(self.hero_image).encode(), "text/plain")

        sidebar_logo: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.sidebar_logo, Unset):
            sidebar_logo = UNSET
        elif isinstance(self.sidebar_logo, File):
            sidebar_logo = self.sidebar_logo.to_tuple()
        else:
            sidebar_logo = (None, str(self.sidebar_logo).encode(), "text/plain")

        sidebar_logo_dark: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.sidebar_logo_dark, Unset):
            sidebar_logo_dark = UNSET
        elif isinstance(self.sidebar_logo_dark, File):
            sidebar_logo_dark = self.sidebar_logo_dark.to_tuple()
        else:
            sidebar_logo_dark = (None, str(self.sidebar_logo_dark).encode(), "text/plain")

        sidebar_logo_mobile: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.sidebar_logo_mobile, Unset):
            sidebar_logo_mobile = UNSET
        elif isinstance(self.sidebar_logo_mobile, File):
            sidebar_logo_mobile = self.sidebar_logo_mobile.to_tuple()
        else:
            sidebar_logo_mobile = (None, str(self.sidebar_logo_mobile).encode(), "text/plain")

        sidebar_style = (
            self.sidebar_style
            if isinstance(self.sidebar_style, Unset)
            else (None, str(self.sidebar_style).encode(), "text/plain")
        )

        site_logo: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.site_logo, Unset):
            site_logo = UNSET
        elif isinstance(self.site_logo, File):
            site_logo = self.site_logo.to_tuple()
        else:
            site_logo = (None, str(self.site_logo).encode(), "text/plain")

        login_logo: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.login_logo, Unset):
            login_logo = UNSET
        elif isinstance(self.login_logo, File):
            login_logo = self.login_logo.to_tuple()
        else:
            login_logo = (None, str(self.login_logo).encode(), "text/plain")

        favicon: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.favicon, Unset):
            favicon = UNSET
        elif isinstance(self.favicon, File):
            favicon = self.favicon.to_tuple()
        else:
            favicon = (None, str(self.favicon).encode(), "text/plain")

        offering_logo_placeholder: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.offering_logo_placeholder, Unset):
            offering_logo_placeholder = UNSET
        elif isinstance(self.offering_logo_placeholder, File):
            offering_logo_placeholder = self.offering_logo_placeholder.to_tuple()
        else:
            offering_logo_placeholder = (None, str(self.offering_logo_placeholder).encode(), "text/plain")

        waldur_support_enabled = (
            self.waldur_support_enabled
            if isinstance(self.waldur_support_enabled, Unset)
            else (None, str(self.waldur_support_enabled).encode(), "text/plain")
        )

        waldur_support_active_backend_type = (
            self.waldur_support_active_backend_type
            if isinstance(self.waldur_support_active_backend_type, Unset)
            else (None, str(self.waldur_support_active_backend_type).encode(), "text/plain")
        )

        waldur_support_display_request_type = (
            self.waldur_support_display_request_type
            if isinstance(self.waldur_support_display_request_type, Unset)
            else (None, str(self.waldur_support_display_request_type).encode(), "text/plain")
        )

        atlassian_use_old_api = (
            self.atlassian_use_old_api
            if isinstance(self.atlassian_use_old_api, Unset)
            else (None, str(self.atlassian_use_old_api).encode(), "text/plain")
        )

        atlassian_use_teenage_api = (
            self.atlassian_use_teenage_api
            if isinstance(self.atlassian_use_teenage_api, Unset)
            else (None, str(self.atlassian_use_teenage_api).encode(), "text/plain")
        )

        atlassian_use_automatic_request_mapping = (
            self.atlassian_use_automatic_request_mapping
            if isinstance(self.atlassian_use_automatic_request_mapping, Unset)
            else (None, str(self.atlassian_use_automatic_request_mapping).encode(), "text/plain")
        )

        atlassian_map_waldur_users_to_servicedesk_agents = (
            self.atlassian_map_waldur_users_to_servicedesk_agents
            if isinstance(self.atlassian_map_waldur_users_to_servicedesk_agents, Unset)
            else (None, str(self.atlassian_map_waldur_users_to_servicedesk_agents).encode(), "text/plain")
        )

        atlassian_strange_setting = (
            self.atlassian_strange_setting
            if isinstance(self.atlassian_strange_setting, Unset)
            else (None, str(self.atlassian_strange_setting).encode(), "text/plain")
        )

        atlassian_api_url = (
            self.atlassian_api_url
            if isinstance(self.atlassian_api_url, Unset)
            else (None, str(self.atlassian_api_url).encode(), "text/plain")
        )

        atlassian_username = (
            self.atlassian_username
            if isinstance(self.atlassian_username, Unset)
            else (None, str(self.atlassian_username).encode(), "text/plain")
        )

        atlassian_password = (
            self.atlassian_password
            if isinstance(self.atlassian_password, Unset)
            else (None, str(self.atlassian_password).encode(), "text/plain")
        )

        atlassian_email = (
            self.atlassian_email
            if isinstance(self.atlassian_email, Unset)
            else (None, str(self.atlassian_email).encode(), "text/plain")
        )

        atlassian_token = (
            self.atlassian_token
            if isinstance(self.atlassian_token, Unset)
            else (None, str(self.atlassian_token).encode(), "text/plain")
        )

        atlassian_verify_ssl = (
            self.atlassian_verify_ssl
            if isinstance(self.atlassian_verify_ssl, Unset)
            else (None, str(self.atlassian_verify_ssl).encode(), "text/plain")
        )

        atlassian_project_id = (
            self.atlassian_project_id
            if isinstance(self.atlassian_project_id, Unset)
            else (None, str(self.atlassian_project_id).encode(), "text/plain")
        )

        atlassian_shared_username = (
            self.atlassian_shared_username
            if isinstance(self.atlassian_shared_username, Unset)
            else (None, str(self.atlassian_shared_username).encode(), "text/plain")
        )

        atlassian_custom_issue_field_mapping_enabled = (
            self.atlassian_custom_issue_field_mapping_enabled
            if isinstance(self.atlassian_custom_issue_field_mapping_enabled, Unset)
            else (None, str(self.atlassian_custom_issue_field_mapping_enabled).encode(), "text/plain")
        )

        atlassian_default_offering_issue_type = (
            self.atlassian_default_offering_issue_type
            if isinstance(self.atlassian_default_offering_issue_type, Unset)
            else (None, str(self.atlassian_default_offering_issue_type).encode(), "text/plain")
        )

        atlassian_excluded_attachment_types = (
            self.atlassian_excluded_attachment_types
            if isinstance(self.atlassian_excluded_attachment_types, Unset)
            else (None, str(self.atlassian_excluded_attachment_types).encode(), "text/plain")
        )

        atlassian_pull_priorities = (
            self.atlassian_pull_priorities
            if isinstance(self.atlassian_pull_priorities, Unset)
            else (None, str(self.atlassian_pull_priorities).encode(), "text/plain")
        )

        atlassian_issue_types = (
            self.atlassian_issue_types
            if isinstance(self.atlassian_issue_types, Unset)
            else (None, str(self.atlassian_issue_types).encode(), "text/plain")
        )

        atlassian_description_template = (
            self.atlassian_description_template
            if isinstance(self.atlassian_description_template, Unset)
            else (None, str(self.atlassian_description_template).encode(), "text/plain")
        )

        atlassian_summary_template = (
            self.atlassian_summary_template
            if isinstance(self.atlassian_summary_template, Unset)
            else (None, str(self.atlassian_summary_template).encode(), "text/plain")
        )

        atlassian_affected_resource_field = (
            self.atlassian_affected_resource_field
            if isinstance(self.atlassian_affected_resource_field, Unset)
            else (None, str(self.atlassian_affected_resource_field).encode(), "text/plain")
        )

        atlassian_impact_field = (
            self.atlassian_impact_field
            if isinstance(self.atlassian_impact_field, Unset)
            else (None, str(self.atlassian_impact_field).encode(), "text/plain")
        )

        atlassian_organisation_field = (
            self.atlassian_organisation_field
            if isinstance(self.atlassian_organisation_field, Unset)
            else (None, str(self.atlassian_organisation_field).encode(), "text/plain")
        )

        atlassian_resolution_sla_field = (
            self.atlassian_resolution_sla_field
            if isinstance(self.atlassian_resolution_sla_field, Unset)
            else (None, str(self.atlassian_resolution_sla_field).encode(), "text/plain")
        )

        atlassian_project_field = (
            self.atlassian_project_field
            if isinstance(self.atlassian_project_field, Unset)
            else (None, str(self.atlassian_project_field).encode(), "text/plain")
        )

        atlassian_reporter_field = (
            self.atlassian_reporter_field
            if isinstance(self.atlassian_reporter_field, Unset)
            else (None, str(self.atlassian_reporter_field).encode(), "text/plain")
        )

        atlassian_caller_field = (
            self.atlassian_caller_field
            if isinstance(self.atlassian_caller_field, Unset)
            else (None, str(self.atlassian_caller_field).encode(), "text/plain")
        )

        atlassian_sla_field = (
            self.atlassian_sla_field
            if isinstance(self.atlassian_sla_field, Unset)
            else (None, str(self.atlassian_sla_field).encode(), "text/plain")
        )

        atlassian_linked_issue_type = (
            self.atlassian_linked_issue_type
            if isinstance(self.atlassian_linked_issue_type, Unset)
            else (None, str(self.atlassian_linked_issue_type).encode(), "text/plain")
        )

        atlassian_satisfaction_field = (
            self.atlassian_satisfaction_field
            if isinstance(self.atlassian_satisfaction_field, Unset)
            else (None, str(self.atlassian_satisfaction_field).encode(), "text/plain")
        )

        atlassian_request_feedback_field = (
            self.atlassian_request_feedback_field
            if isinstance(self.atlassian_request_feedback_field, Unset)
            else (None, str(self.atlassian_request_feedback_field).encode(), "text/plain")
        )

        atlassian_template_field = (
            self.atlassian_template_field
            if isinstance(self.atlassian_template_field, Unset)
            else (None, str(self.atlassian_template_field).encode(), "text/plain")
        )

        zammad_api_url = (
            self.zammad_api_url
            if isinstance(self.zammad_api_url, Unset)
            else (None, str(self.zammad_api_url).encode(), "text/plain")
        )

        zammad_token = (
            self.zammad_token
            if isinstance(self.zammad_token, Unset)
            else (None, str(self.zammad_token).encode(), "text/plain")
        )

        zammad_group = (
            self.zammad_group
            if isinstance(self.zammad_group, Unset)
            else (None, str(self.zammad_group).encode(), "text/plain")
        )

        zammad_article_type = (
            self.zammad_article_type
            if isinstance(self.zammad_article_type, Unset)
            else (None, str(self.zammad_article_type).encode(), "text/plain")
        )

        zammad_comment_marker = (
            self.zammad_comment_marker
            if isinstance(self.zammad_comment_marker, Unset)
            else (None, str(self.zammad_comment_marker).encode(), "text/plain")
        )

        zammad_comment_prefix = (
            self.zammad_comment_prefix
            if isinstance(self.zammad_comment_prefix, Unset)
            else (None, str(self.zammad_comment_prefix).encode(), "text/plain")
        )

        zammad_comment_cooldown_duration = (
            self.zammad_comment_cooldown_duration
            if isinstance(self.zammad_comment_cooldown_duration, Unset)
            else (None, str(self.zammad_comment_cooldown_duration).encode(), "text/plain")
        )

        smax_api_url = (
            self.smax_api_url
            if isinstance(self.smax_api_url, Unset)
            else (None, str(self.smax_api_url).encode(), "text/plain")
        )

        smax_tenant_id = (
            self.smax_tenant_id
            if isinstance(self.smax_tenant_id, Unset)
            else (None, str(self.smax_tenant_id).encode(), "text/plain")
        )

        smax_login = (
            self.smax_login
            if isinstance(self.smax_login, Unset)
            else (None, str(self.smax_login).encode(), "text/plain")
        )

        smax_password = (
            self.smax_password
            if isinstance(self.smax_password, Unset)
            else (None, str(self.smax_password).encode(), "text/plain")
        )

        smax_organisation_field = (
            self.smax_organisation_field
            if isinstance(self.smax_organisation_field, Unset)
            else (None, str(self.smax_organisation_field).encode(), "text/plain")
        )

        smax_project_field = (
            self.smax_project_field
            if isinstance(self.smax_project_field, Unset)
            else (None, str(self.smax_project_field).encode(), "text/plain")
        )

        smax_affected_resource_field = (
            self.smax_affected_resource_field
            if isinstance(self.smax_affected_resource_field, Unset)
            else (None, str(self.smax_affected_resource_field).encode(), "text/plain")
        )

        smax_times_to_pull = (
            self.smax_times_to_pull
            if isinstance(self.smax_times_to_pull, Unset)
            else (None, str(self.smax_times_to_pull).encode(), "text/plain")
        )

        smax_seconds_to_wait = (
            self.smax_seconds_to_wait
            if isinstance(self.smax_seconds_to_wait, Unset)
            else (None, str(self.smax_seconds_to_wait).encode(), "text/plain")
        )

        smax_creation_source_name = (
            self.smax_creation_source_name
            if isinstance(self.smax_creation_source_name, Unset)
            else (None, str(self.smax_creation_source_name).encode(), "text/plain")
        )

        smax_requests_offering = (
            self.smax_requests_offering
            if isinstance(self.smax_requests_offering, Unset)
            else (None, str(self.smax_requests_offering).encode(), "text/plain")
        )

        smax_verify_ssl = (
            self.smax_verify_ssl
            if isinstance(self.smax_verify_ssl, Unset)
            else (None, str(self.smax_verify_ssl).encode(), "text/plain")
        )

        proposal_review_duration = (
            self.proposal_review_duration
            if isinstance(self.proposal_review_duration, Unset)
            else (None, str(self.proposal_review_duration).encode(), "text/plain")
        )

        user_table_columns = (
            self.user_table_columns
            if isinstance(self.user_table_columns, Unset)
            else (None, str(self.user_table_columns).encode(), "text/plain")
        )

        auto_approve_user_tos = (
            self.auto_approve_user_tos
            if isinstance(self.auto_approve_user_tos, Unset)
            else (None, str(self.auto_approve_user_tos).encode(), "text/plain")
        )

        freeipa_enabled = (
            self.freeipa_enabled
            if isinstance(self.freeipa_enabled, Unset)
            else (None, str(self.freeipa_enabled).encode(), "text/plain")
        )

        freeipa_hostname = (
            self.freeipa_hostname
            if isinstance(self.freeipa_hostname, Unset)
            else (None, str(self.freeipa_hostname).encode(), "text/plain")
        )

        freeipa_username = (
            self.freeipa_username
            if isinstance(self.freeipa_username, Unset)
            else (None, str(self.freeipa_username).encode(), "text/plain")
        )

        freeipa_password = (
            self.freeipa_password
            if isinstance(self.freeipa_password, Unset)
            else (None, str(self.freeipa_password).encode(), "text/plain")
        )

        freeipa_verify_ssl = (
            self.freeipa_verify_ssl
            if isinstance(self.freeipa_verify_ssl, Unset)
            else (None, str(self.freeipa_verify_ssl).encode(), "text/plain")
        )

        freeipa_username_prefix = (
            self.freeipa_username_prefix
            if isinstance(self.freeipa_username_prefix, Unset)
            else (None, str(self.freeipa_username_prefix).encode(), "text/plain")
        )

        freeipa_groupname_prefix = (
            self.freeipa_groupname_prefix
            if isinstance(self.freeipa_groupname_prefix, Unset)
            else (None, str(self.freeipa_groupname_prefix).encode(), "text/plain")
        )

        freeipa_blacklisted_usernames: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.freeipa_blacklisted_usernames, Unset):
            _temp_freeipa_blacklisted_usernames = self.freeipa_blacklisted_usernames
            freeipa_blacklisted_usernames = (
                None,
                json.dumps(_temp_freeipa_blacklisted_usernames).encode(),
                "application/json",
            )

        freeipa_group_synchronization_enabled = (
            self.freeipa_group_synchronization_enabled
            if isinstance(self.freeipa_group_synchronization_enabled, Unset)
            else (None, str(self.freeipa_group_synchronization_enabled).encode(), "text/plain")
        )

        keycloak_icon: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.keycloak_icon, Unset):
            keycloak_icon = UNSET
        elif isinstance(self.keycloak_icon, File):
            keycloak_icon = self.keycloak_icon.to_tuple()
        else:
            keycloak_icon = (None, str(self.keycloak_icon).encode(), "text/plain")

        countries: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.countries, Unset):
            _temp_countries = self.countries
            countries = (None, json.dumps(_temp_countries).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if site_name is not UNSET:
            field_dict["SITE_NAME"] = site_name
        if site_description is not UNSET:
            field_dict["SITE_DESCRIPTION"] = site_description
        if homeport_url is not UNSET:
            field_dict["HOMEPORT_URL"] = homeport_url
        if site_address is not UNSET:
            field_dict["SITE_ADDRESS"] = site_address
        if site_email is not UNSET:
            field_dict["SITE_EMAIL"] = site_email
        if site_phone is not UNSET:
            field_dict["SITE_PHONE"] = site_phone
        if currency_name is not UNSET:
            field_dict["CURRENCY_NAME"] = currency_name
        if thumbnail_size is not UNSET:
            field_dict["THUMBNAIL_SIZE"] = thumbnail_size
        if anonymous_user_can_view_offerings is not UNSET:
            field_dict["ANONYMOUS_USER_CAN_VIEW_OFFERINGS"] = anonymous_user_can_view_offerings
        if anonymous_user_can_view_plans is not UNSET:
            field_dict["ANONYMOUS_USER_CAN_VIEW_PLANS"] = anonymous_user_can_view_plans
        if notify_staff_about_approvals is not UNSET:
            field_dict["NOTIFY_STAFF_ABOUT_APPROVALS"] = notify_staff_about_approvals
        if notify_about_resource_change is not UNSET:
            field_dict["NOTIFY_ABOUT_RESOURCE_CHANGE"] = notify_about_resource_change
        if disable_sending_notifications_about_resource_update is not UNSET:
            field_dict["DISABLE_SENDING_NOTIFICATIONS_ABOUT_RESOURCE_UPDATE"] = (
                disable_sending_notifications_about_resource_update
            )
        if marketplace_landing_page is not UNSET:
            field_dict["MARKETPLACE_LANDING_PAGE"] = marketplace_landing_page
        if enable_stale_resource_notifications is not UNSET:
            field_dict["ENABLE_STALE_RESOURCE_NOTIFICATIONS"] = enable_stale_resource_notifications
        if enable_resource_end_date is not UNSET:
            field_dict["ENABLE_RESOURCE_END_DATE"] = enable_resource_end_date
        if telemetry_url is not UNSET:
            field_dict["TELEMETRY_URL"] = telemetry_url
        if telemetry_version is not UNSET:
            field_dict["TELEMETRY_VERSION"] = telemetry_version
        if script_run_mode is not UNSET:
            field_dict["SCRIPT_RUN_MODE"] = script_run_mode
        if docker_client is not UNSET:
            field_dict["DOCKER_CLIENT"] = docker_client
        if docker_run_options is not UNSET:
            field_dict["DOCKER_RUN_OPTIONS"] = docker_run_options
        if docker_script_dir is not UNSET:
            field_dict["DOCKER_SCRIPT_DIR"] = docker_script_dir
        if docker_remove_container is not UNSET:
            field_dict["DOCKER_REMOVE_CONTAINER"] = docker_remove_container
        if docker_images is not UNSET:
            field_dict["DOCKER_IMAGES"] = docker_images
        if docker_volume_name is not UNSET:
            field_dict["DOCKER_VOLUME_NAME"] = docker_volume_name
        if k8s_namespace is not UNSET:
            field_dict["K8S_NAMESPACE"] = k8s_namespace
        if k8s_config_path is not UNSET:
            field_dict["K8S_CONFIG_PATH"] = k8s_config_path
        if k8s_job_timeout is not UNSET:
            field_dict["K8S_JOB_TIMEOUT"] = k8s_job_timeout
        if enable_strict_check_accepting_invitation is not UNSET:
            field_dict["ENABLE_STRICT_CHECK_ACCEPTING_INVITATION"] = enable_strict_check_accepting_invitation
        if invitation_disable_multiple_roles is not UNSET:
            field_dict["INVITATION_DISABLE_MULTIPLE_ROLES"] = invitation_disable_multiple_roles
        if default_idp is not UNSET:
            field_dict["DEFAULT_IDP"] = default_idp
        if docs_url is not UNSET:
            field_dict["DOCS_URL"] = docs_url
        if short_page_title is not UNSET:
            field_dict["SHORT_PAGE_TITLE"] = short_page_title
        if full_page_title is not UNSET:
            field_dict["FULL_PAGE_TITLE"] = full_page_title
        if brand_color is not UNSET:
            field_dict["BRAND_COLOR"] = brand_color
        if hero_link_label is not UNSET:
            field_dict["HERO_LINK_LABEL"] = hero_link_label
        if hero_link_url is not UNSET:
            field_dict["HERO_LINK_URL"] = hero_link_url
        if support_portal_url is not UNSET:
            field_dict["SUPPORT_PORTAL_URL"] = support_portal_url
        if common_footer_text is not UNSET:
            field_dict["COMMON_FOOTER_TEXT"] = common_footer_text
        if common_footer_html is not UNSET:
            field_dict["COMMON_FOOTER_HTML"] = common_footer_html
        if language_choices is not UNSET:
            field_dict["LANGUAGE_CHOICES"] = language_choices
        if disable_dark_theme is not UNSET:
            field_dict["DISABLE_DARK_THEME"] = disable_dark_theme
        if powered_by_logo is not UNSET:
            field_dict["POWERED_BY_LOGO"] = powered_by_logo
        if hero_image is not UNSET:
            field_dict["HERO_IMAGE"] = hero_image
        if sidebar_logo is not UNSET:
            field_dict["SIDEBAR_LOGO"] = sidebar_logo
        if sidebar_logo_dark is not UNSET:
            field_dict["SIDEBAR_LOGO_DARK"] = sidebar_logo_dark
        if sidebar_logo_mobile is not UNSET:
            field_dict["SIDEBAR_LOGO_MOBILE"] = sidebar_logo_mobile
        if sidebar_style is not UNSET:
            field_dict["SIDEBAR_STYLE"] = sidebar_style
        if site_logo is not UNSET:
            field_dict["SITE_LOGO"] = site_logo
        if login_logo is not UNSET:
            field_dict["LOGIN_LOGO"] = login_logo
        if favicon is not UNSET:
            field_dict["FAVICON"] = favicon
        if offering_logo_placeholder is not UNSET:
            field_dict["OFFERING_LOGO_PLACEHOLDER"] = offering_logo_placeholder
        if waldur_support_enabled is not UNSET:
            field_dict["WALDUR_SUPPORT_ENABLED"] = waldur_support_enabled
        if waldur_support_active_backend_type is not UNSET:
            field_dict["WALDUR_SUPPORT_ACTIVE_BACKEND_TYPE"] = waldur_support_active_backend_type
        if waldur_support_display_request_type is not UNSET:
            field_dict["WALDUR_SUPPORT_DISPLAY_REQUEST_TYPE"] = waldur_support_display_request_type
        if atlassian_use_old_api is not UNSET:
            field_dict["ATLASSIAN_USE_OLD_API"] = atlassian_use_old_api
        if atlassian_use_teenage_api is not UNSET:
            field_dict["ATLASSIAN_USE_TEENAGE_API"] = atlassian_use_teenage_api
        if atlassian_use_automatic_request_mapping is not UNSET:
            field_dict["ATLASSIAN_USE_AUTOMATIC_REQUEST_MAPPING"] = atlassian_use_automatic_request_mapping
        if atlassian_map_waldur_users_to_servicedesk_agents is not UNSET:
            field_dict["ATLASSIAN_MAP_WALDUR_USERS_TO_SERVICEDESK_AGENTS"] = (
                atlassian_map_waldur_users_to_servicedesk_agents
            )
        if atlassian_strange_setting is not UNSET:
            field_dict["ATLASSIAN_STRANGE_SETTING"] = atlassian_strange_setting
        if atlassian_api_url is not UNSET:
            field_dict["ATLASSIAN_API_URL"] = atlassian_api_url
        if atlassian_username is not UNSET:
            field_dict["ATLASSIAN_USERNAME"] = atlassian_username
        if atlassian_password is not UNSET:
            field_dict["ATLASSIAN_PASSWORD"] = atlassian_password
        if atlassian_email is not UNSET:
            field_dict["ATLASSIAN_EMAIL"] = atlassian_email
        if atlassian_token is not UNSET:
            field_dict["ATLASSIAN_TOKEN"] = atlassian_token
        if atlassian_verify_ssl is not UNSET:
            field_dict["ATLASSIAN_VERIFY_SSL"] = atlassian_verify_ssl
        if atlassian_project_id is not UNSET:
            field_dict["ATLASSIAN_PROJECT_ID"] = atlassian_project_id
        if atlassian_shared_username is not UNSET:
            field_dict["ATLASSIAN_SHARED_USERNAME"] = atlassian_shared_username
        if atlassian_custom_issue_field_mapping_enabled is not UNSET:
            field_dict["ATLASSIAN_CUSTOM_ISSUE_FIELD_MAPPING_ENABLED"] = atlassian_custom_issue_field_mapping_enabled
        if atlassian_default_offering_issue_type is not UNSET:
            field_dict["ATLASSIAN_DEFAULT_OFFERING_ISSUE_TYPE"] = atlassian_default_offering_issue_type
        if atlassian_excluded_attachment_types is not UNSET:
            field_dict["ATLASSIAN_EXCLUDED_ATTACHMENT_TYPES"] = atlassian_excluded_attachment_types
        if atlassian_pull_priorities is not UNSET:
            field_dict["ATLASSIAN_PULL_PRIORITIES"] = atlassian_pull_priorities
        if atlassian_issue_types is not UNSET:
            field_dict["ATLASSIAN_ISSUE_TYPES"] = atlassian_issue_types
        if atlassian_description_template is not UNSET:
            field_dict["ATLASSIAN_DESCRIPTION_TEMPLATE"] = atlassian_description_template
        if atlassian_summary_template is not UNSET:
            field_dict["ATLASSIAN_SUMMARY_TEMPLATE"] = atlassian_summary_template
        if atlassian_affected_resource_field is not UNSET:
            field_dict["ATLASSIAN_AFFECTED_RESOURCE_FIELD"] = atlassian_affected_resource_field
        if atlassian_impact_field is not UNSET:
            field_dict["ATLASSIAN_IMPACT_FIELD"] = atlassian_impact_field
        if atlassian_organisation_field is not UNSET:
            field_dict["ATLASSIAN_ORGANISATION_FIELD"] = atlassian_organisation_field
        if atlassian_resolution_sla_field is not UNSET:
            field_dict["ATLASSIAN_RESOLUTION_SLA_FIELD"] = atlassian_resolution_sla_field
        if atlassian_project_field is not UNSET:
            field_dict["ATLASSIAN_PROJECT_FIELD"] = atlassian_project_field
        if atlassian_reporter_field is not UNSET:
            field_dict["ATLASSIAN_REPORTER_FIELD"] = atlassian_reporter_field
        if atlassian_caller_field is not UNSET:
            field_dict["ATLASSIAN_CALLER_FIELD"] = atlassian_caller_field
        if atlassian_sla_field is not UNSET:
            field_dict["ATLASSIAN_SLA_FIELD"] = atlassian_sla_field
        if atlassian_linked_issue_type is not UNSET:
            field_dict["ATLASSIAN_LINKED_ISSUE_TYPE"] = atlassian_linked_issue_type
        if atlassian_satisfaction_field is not UNSET:
            field_dict["ATLASSIAN_SATISFACTION_FIELD"] = atlassian_satisfaction_field
        if atlassian_request_feedback_field is not UNSET:
            field_dict["ATLASSIAN_REQUEST_FEEDBACK_FIELD"] = atlassian_request_feedback_field
        if atlassian_template_field is not UNSET:
            field_dict["ATLASSIAN_TEMPLATE_FIELD"] = atlassian_template_field
        if zammad_api_url is not UNSET:
            field_dict["ZAMMAD_API_URL"] = zammad_api_url
        if zammad_token is not UNSET:
            field_dict["ZAMMAD_TOKEN"] = zammad_token
        if zammad_group is not UNSET:
            field_dict["ZAMMAD_GROUP"] = zammad_group
        if zammad_article_type is not UNSET:
            field_dict["ZAMMAD_ARTICLE_TYPE"] = zammad_article_type
        if zammad_comment_marker is not UNSET:
            field_dict["ZAMMAD_COMMENT_MARKER"] = zammad_comment_marker
        if zammad_comment_prefix is not UNSET:
            field_dict["ZAMMAD_COMMENT_PREFIX"] = zammad_comment_prefix
        if zammad_comment_cooldown_duration is not UNSET:
            field_dict["ZAMMAD_COMMENT_COOLDOWN_DURATION"] = zammad_comment_cooldown_duration
        if smax_api_url is not UNSET:
            field_dict["SMAX_API_URL"] = smax_api_url
        if smax_tenant_id is not UNSET:
            field_dict["SMAX_TENANT_ID"] = smax_tenant_id
        if smax_login is not UNSET:
            field_dict["SMAX_LOGIN"] = smax_login
        if smax_password is not UNSET:
            field_dict["SMAX_PASSWORD"] = smax_password
        if smax_organisation_field is not UNSET:
            field_dict["SMAX_ORGANISATION_FIELD"] = smax_organisation_field
        if smax_project_field is not UNSET:
            field_dict["SMAX_PROJECT_FIELD"] = smax_project_field
        if smax_affected_resource_field is not UNSET:
            field_dict["SMAX_AFFECTED_RESOURCE_FIELD"] = smax_affected_resource_field
        if smax_times_to_pull is not UNSET:
            field_dict["SMAX_TIMES_TO_PULL"] = smax_times_to_pull
        if smax_seconds_to_wait is not UNSET:
            field_dict["SMAX_SECONDS_TO_WAIT"] = smax_seconds_to_wait
        if smax_creation_source_name is not UNSET:
            field_dict["SMAX_CREATION_SOURCE_NAME"] = smax_creation_source_name
        if smax_requests_offering is not UNSET:
            field_dict["SMAX_REQUESTS_OFFERING"] = smax_requests_offering
        if smax_verify_ssl is not UNSET:
            field_dict["SMAX_VERIFY_SSL"] = smax_verify_ssl
        if proposal_review_duration is not UNSET:
            field_dict["PROPOSAL_REVIEW_DURATION"] = proposal_review_duration
        if user_table_columns is not UNSET:
            field_dict["USER_TABLE_COLUMNS"] = user_table_columns
        if auto_approve_user_tos is not UNSET:
            field_dict["AUTO_APPROVE_USER_TOS"] = auto_approve_user_tos
        if freeipa_enabled is not UNSET:
            field_dict["FREEIPA_ENABLED"] = freeipa_enabled
        if freeipa_hostname is not UNSET:
            field_dict["FREEIPA_HOSTNAME"] = freeipa_hostname
        if freeipa_username is not UNSET:
            field_dict["FREEIPA_USERNAME"] = freeipa_username
        if freeipa_password is not UNSET:
            field_dict["FREEIPA_PASSWORD"] = freeipa_password
        if freeipa_verify_ssl is not UNSET:
            field_dict["FREEIPA_VERIFY_SSL"] = freeipa_verify_ssl
        if freeipa_username_prefix is not UNSET:
            field_dict["FREEIPA_USERNAME_PREFIX"] = freeipa_username_prefix
        if freeipa_groupname_prefix is not UNSET:
            field_dict["FREEIPA_GROUPNAME_PREFIX"] = freeipa_groupname_prefix
        if freeipa_blacklisted_usernames is not UNSET:
            field_dict["FREEIPA_BLACKLISTED_USERNAMES"] = freeipa_blacklisted_usernames
        if freeipa_group_synchronization_enabled is not UNSET:
            field_dict["FREEIPA_GROUP_SYNCHRONIZATION_ENABLED"] = freeipa_group_synchronization_enabled
        if keycloak_icon is not UNSET:
            field_dict["KEYCLOAK_ICON"] = keycloak_icon
        if countries is not UNSET:
            field_dict["COUNTRIES"] = countries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        site_name = d.pop("SITE_NAME", UNSET)

        site_description = d.pop("SITE_DESCRIPTION", UNSET)

        homeport_url = d.pop("HOMEPORT_URL", UNSET)

        site_address = d.pop("SITE_ADDRESS", UNSET)

        site_email = d.pop("SITE_EMAIL", UNSET)

        site_phone = d.pop("SITE_PHONE", UNSET)

        currency_name = d.pop("CURRENCY_NAME", UNSET)

        thumbnail_size = d.pop("THUMBNAIL_SIZE", UNSET)

        anonymous_user_can_view_offerings = d.pop("ANONYMOUS_USER_CAN_VIEW_OFFERINGS", UNSET)

        anonymous_user_can_view_plans = d.pop("ANONYMOUS_USER_CAN_VIEW_PLANS", UNSET)

        notify_staff_about_approvals = d.pop("NOTIFY_STAFF_ABOUT_APPROVALS", UNSET)

        notify_about_resource_change = d.pop("NOTIFY_ABOUT_RESOURCE_CHANGE", UNSET)

        disable_sending_notifications_about_resource_update = d.pop(
            "DISABLE_SENDING_NOTIFICATIONS_ABOUT_RESOURCE_UPDATE", UNSET
        )

        marketplace_landing_page = d.pop("MARKETPLACE_LANDING_PAGE", UNSET)

        enable_stale_resource_notifications = d.pop("ENABLE_STALE_RESOURCE_NOTIFICATIONS", UNSET)

        enable_resource_end_date = d.pop("ENABLE_RESOURCE_END_DATE", UNSET)

        telemetry_url = d.pop("TELEMETRY_URL", UNSET)

        telemetry_version = d.pop("TELEMETRY_VERSION", UNSET)

        script_run_mode = d.pop("SCRIPT_RUN_MODE", UNSET)

        docker_client = d.pop("DOCKER_CLIENT", UNSET)

        docker_run_options = d.pop("DOCKER_RUN_OPTIONS", UNSET)

        docker_script_dir = d.pop("DOCKER_SCRIPT_DIR", UNSET)

        docker_remove_container = d.pop("DOCKER_REMOVE_CONTAINER", UNSET)

        docker_images = d.pop("DOCKER_IMAGES", UNSET)

        docker_volume_name = d.pop("DOCKER_VOLUME_NAME", UNSET)

        k8s_namespace = d.pop("K8S_NAMESPACE", UNSET)

        k8s_config_path = d.pop("K8S_CONFIG_PATH", UNSET)

        k8s_job_timeout = d.pop("K8S_JOB_TIMEOUT", UNSET)

        enable_strict_check_accepting_invitation = d.pop("ENABLE_STRICT_CHECK_ACCEPTING_INVITATION", UNSET)

        invitation_disable_multiple_roles = d.pop("INVITATION_DISABLE_MULTIPLE_ROLES", UNSET)

        default_idp = d.pop("DEFAULT_IDP", UNSET)

        docs_url = d.pop("DOCS_URL", UNSET)

        short_page_title = d.pop("SHORT_PAGE_TITLE", UNSET)

        full_page_title = d.pop("FULL_PAGE_TITLE", UNSET)

        brand_color = d.pop("BRAND_COLOR", UNSET)

        hero_link_label = d.pop("HERO_LINK_LABEL", UNSET)

        hero_link_url = d.pop("HERO_LINK_URL", UNSET)

        support_portal_url = d.pop("SUPPORT_PORTAL_URL", UNSET)

        common_footer_text = d.pop("COMMON_FOOTER_TEXT", UNSET)

        common_footer_html = d.pop("COMMON_FOOTER_HTML", UNSET)

        language_choices = d.pop("LANGUAGE_CHOICES", UNSET)

        disable_dark_theme = d.pop("DISABLE_DARK_THEME", UNSET)

        def _parse_powered_by_logo(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                powered_by_logo_type_0 = File(payload=BytesIO(data))

                return powered_by_logo_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        powered_by_logo = _parse_powered_by_logo(d.pop("POWERED_BY_LOGO", UNSET))

        def _parse_hero_image(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                hero_image_type_0 = File(payload=BytesIO(data))

                return hero_image_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        hero_image = _parse_hero_image(d.pop("HERO_IMAGE", UNSET))

        def _parse_sidebar_logo(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                sidebar_logo_type_0 = File(payload=BytesIO(data))

                return sidebar_logo_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        sidebar_logo = _parse_sidebar_logo(d.pop("SIDEBAR_LOGO", UNSET))

        def _parse_sidebar_logo_dark(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                sidebar_logo_dark_type_0 = File(payload=BytesIO(data))

                return sidebar_logo_dark_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        sidebar_logo_dark = _parse_sidebar_logo_dark(d.pop("SIDEBAR_LOGO_DARK", UNSET))

        def _parse_sidebar_logo_mobile(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                sidebar_logo_mobile_type_0 = File(payload=BytesIO(data))

                return sidebar_logo_mobile_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        sidebar_logo_mobile = _parse_sidebar_logo_mobile(d.pop("SIDEBAR_LOGO_MOBILE", UNSET))

        sidebar_style = d.pop("SIDEBAR_STYLE", UNSET)

        def _parse_site_logo(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                site_logo_type_0 = File(payload=BytesIO(data))

                return site_logo_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        site_logo = _parse_site_logo(d.pop("SITE_LOGO", UNSET))

        def _parse_login_logo(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                login_logo_type_0 = File(payload=BytesIO(data))

                return login_logo_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        login_logo = _parse_login_logo(d.pop("LOGIN_LOGO", UNSET))

        def _parse_favicon(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                favicon_type_0 = File(payload=BytesIO(data))

                return favicon_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        favicon = _parse_favicon(d.pop("FAVICON", UNSET))

        def _parse_offering_logo_placeholder(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                offering_logo_placeholder_type_0 = File(payload=BytesIO(data))

                return offering_logo_placeholder_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        offering_logo_placeholder = _parse_offering_logo_placeholder(d.pop("OFFERING_LOGO_PLACEHOLDER", UNSET))

        waldur_support_enabled = d.pop("WALDUR_SUPPORT_ENABLED", UNSET)

        waldur_support_active_backend_type = d.pop("WALDUR_SUPPORT_ACTIVE_BACKEND_TYPE", UNSET)

        waldur_support_display_request_type = d.pop("WALDUR_SUPPORT_DISPLAY_REQUEST_TYPE", UNSET)

        atlassian_use_old_api = d.pop("ATLASSIAN_USE_OLD_API", UNSET)

        atlassian_use_teenage_api = d.pop("ATLASSIAN_USE_TEENAGE_API", UNSET)

        atlassian_use_automatic_request_mapping = d.pop("ATLASSIAN_USE_AUTOMATIC_REQUEST_MAPPING", UNSET)

        atlassian_map_waldur_users_to_servicedesk_agents = d.pop(
            "ATLASSIAN_MAP_WALDUR_USERS_TO_SERVICEDESK_AGENTS", UNSET
        )

        atlassian_strange_setting = d.pop("ATLASSIAN_STRANGE_SETTING", UNSET)

        atlassian_api_url = d.pop("ATLASSIAN_API_URL", UNSET)

        atlassian_username = d.pop("ATLASSIAN_USERNAME", UNSET)

        atlassian_password = d.pop("ATLASSIAN_PASSWORD", UNSET)

        atlassian_email = d.pop("ATLASSIAN_EMAIL", UNSET)

        atlassian_token = d.pop("ATLASSIAN_TOKEN", UNSET)

        atlassian_verify_ssl = d.pop("ATLASSIAN_VERIFY_SSL", UNSET)

        atlassian_project_id = d.pop("ATLASSIAN_PROJECT_ID", UNSET)

        atlassian_shared_username = d.pop("ATLASSIAN_SHARED_USERNAME", UNSET)

        atlassian_custom_issue_field_mapping_enabled = d.pop("ATLASSIAN_CUSTOM_ISSUE_FIELD_MAPPING_ENABLED", UNSET)

        atlassian_default_offering_issue_type = d.pop("ATLASSIAN_DEFAULT_OFFERING_ISSUE_TYPE", UNSET)

        atlassian_excluded_attachment_types = d.pop("ATLASSIAN_EXCLUDED_ATTACHMENT_TYPES", UNSET)

        atlassian_pull_priorities = d.pop("ATLASSIAN_PULL_PRIORITIES", UNSET)

        atlassian_issue_types = d.pop("ATLASSIAN_ISSUE_TYPES", UNSET)

        atlassian_description_template = d.pop("ATLASSIAN_DESCRIPTION_TEMPLATE", UNSET)

        atlassian_summary_template = d.pop("ATLASSIAN_SUMMARY_TEMPLATE", UNSET)

        atlassian_affected_resource_field = d.pop("ATLASSIAN_AFFECTED_RESOURCE_FIELD", UNSET)

        atlassian_impact_field = d.pop("ATLASSIAN_IMPACT_FIELD", UNSET)

        atlassian_organisation_field = d.pop("ATLASSIAN_ORGANISATION_FIELD", UNSET)

        atlassian_resolution_sla_field = d.pop("ATLASSIAN_RESOLUTION_SLA_FIELD", UNSET)

        atlassian_project_field = d.pop("ATLASSIAN_PROJECT_FIELD", UNSET)

        atlassian_reporter_field = d.pop("ATLASSIAN_REPORTER_FIELD", UNSET)

        atlassian_caller_field = d.pop("ATLASSIAN_CALLER_FIELD", UNSET)

        atlassian_sla_field = d.pop("ATLASSIAN_SLA_FIELD", UNSET)

        atlassian_linked_issue_type = d.pop("ATLASSIAN_LINKED_ISSUE_TYPE", UNSET)

        atlassian_satisfaction_field = d.pop("ATLASSIAN_SATISFACTION_FIELD", UNSET)

        atlassian_request_feedback_field = d.pop("ATLASSIAN_REQUEST_FEEDBACK_FIELD", UNSET)

        atlassian_template_field = d.pop("ATLASSIAN_TEMPLATE_FIELD", UNSET)

        zammad_api_url = d.pop("ZAMMAD_API_URL", UNSET)

        zammad_token = d.pop("ZAMMAD_TOKEN", UNSET)

        zammad_group = d.pop("ZAMMAD_GROUP", UNSET)

        zammad_article_type = d.pop("ZAMMAD_ARTICLE_TYPE", UNSET)

        zammad_comment_marker = d.pop("ZAMMAD_COMMENT_MARKER", UNSET)

        zammad_comment_prefix = d.pop("ZAMMAD_COMMENT_PREFIX", UNSET)

        zammad_comment_cooldown_duration = d.pop("ZAMMAD_COMMENT_COOLDOWN_DURATION", UNSET)

        smax_api_url = d.pop("SMAX_API_URL", UNSET)

        smax_tenant_id = d.pop("SMAX_TENANT_ID", UNSET)

        smax_login = d.pop("SMAX_LOGIN", UNSET)

        smax_password = d.pop("SMAX_PASSWORD", UNSET)

        smax_organisation_field = d.pop("SMAX_ORGANISATION_FIELD", UNSET)

        smax_project_field = d.pop("SMAX_PROJECT_FIELD", UNSET)

        smax_affected_resource_field = d.pop("SMAX_AFFECTED_RESOURCE_FIELD", UNSET)

        smax_times_to_pull = d.pop("SMAX_TIMES_TO_PULL", UNSET)

        smax_seconds_to_wait = d.pop("SMAX_SECONDS_TO_WAIT", UNSET)

        smax_creation_source_name = d.pop("SMAX_CREATION_SOURCE_NAME", UNSET)

        smax_requests_offering = d.pop("SMAX_REQUESTS_OFFERING", UNSET)

        smax_verify_ssl = d.pop("SMAX_VERIFY_SSL", UNSET)

        proposal_review_duration = d.pop("PROPOSAL_REVIEW_DURATION", UNSET)

        user_table_columns = d.pop("USER_TABLE_COLUMNS", UNSET)

        auto_approve_user_tos = d.pop("AUTO_APPROVE_USER_TOS", UNSET)

        freeipa_enabled = d.pop("FREEIPA_ENABLED", UNSET)

        freeipa_hostname = d.pop("FREEIPA_HOSTNAME", UNSET)

        freeipa_username = d.pop("FREEIPA_USERNAME", UNSET)

        freeipa_password = d.pop("FREEIPA_PASSWORD", UNSET)

        freeipa_verify_ssl = d.pop("FREEIPA_VERIFY_SSL", UNSET)

        freeipa_username_prefix = d.pop("FREEIPA_USERNAME_PREFIX", UNSET)

        freeipa_groupname_prefix = d.pop("FREEIPA_GROUPNAME_PREFIX", UNSET)

        freeipa_blacklisted_usernames = cast(list[str], d.pop("FREEIPA_BLACKLISTED_USERNAMES", UNSET))

        freeipa_group_synchronization_enabled = d.pop("FREEIPA_GROUP_SYNCHRONIZATION_ENABLED", UNSET)

        def _parse_keycloak_icon(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                keycloak_icon_type_0 = File(payload=BytesIO(data))

                return keycloak_icon_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        keycloak_icon = _parse_keycloak_icon(d.pop("KEYCLOAK_ICON", UNSET))

        countries = cast(list[str], d.pop("COUNTRIES", UNSET))

        constance_settings_request = cls(
            site_name=site_name,
            site_description=site_description,
            homeport_url=homeport_url,
            site_address=site_address,
            site_email=site_email,
            site_phone=site_phone,
            currency_name=currency_name,
            thumbnail_size=thumbnail_size,
            anonymous_user_can_view_offerings=anonymous_user_can_view_offerings,
            anonymous_user_can_view_plans=anonymous_user_can_view_plans,
            notify_staff_about_approvals=notify_staff_about_approvals,
            notify_about_resource_change=notify_about_resource_change,
            disable_sending_notifications_about_resource_update=disable_sending_notifications_about_resource_update,
            marketplace_landing_page=marketplace_landing_page,
            enable_stale_resource_notifications=enable_stale_resource_notifications,
            enable_resource_end_date=enable_resource_end_date,
            telemetry_url=telemetry_url,
            telemetry_version=telemetry_version,
            script_run_mode=script_run_mode,
            docker_client=docker_client,
            docker_run_options=docker_run_options,
            docker_script_dir=docker_script_dir,
            docker_remove_container=docker_remove_container,
            docker_images=docker_images,
            docker_volume_name=docker_volume_name,
            k8s_namespace=k8s_namespace,
            k8s_config_path=k8s_config_path,
            k8s_job_timeout=k8s_job_timeout,
            enable_strict_check_accepting_invitation=enable_strict_check_accepting_invitation,
            invitation_disable_multiple_roles=invitation_disable_multiple_roles,
            default_idp=default_idp,
            docs_url=docs_url,
            short_page_title=short_page_title,
            full_page_title=full_page_title,
            brand_color=brand_color,
            hero_link_label=hero_link_label,
            hero_link_url=hero_link_url,
            support_portal_url=support_portal_url,
            common_footer_text=common_footer_text,
            common_footer_html=common_footer_html,
            language_choices=language_choices,
            disable_dark_theme=disable_dark_theme,
            powered_by_logo=powered_by_logo,
            hero_image=hero_image,
            sidebar_logo=sidebar_logo,
            sidebar_logo_dark=sidebar_logo_dark,
            sidebar_logo_mobile=sidebar_logo_mobile,
            sidebar_style=sidebar_style,
            site_logo=site_logo,
            login_logo=login_logo,
            favicon=favicon,
            offering_logo_placeholder=offering_logo_placeholder,
            waldur_support_enabled=waldur_support_enabled,
            waldur_support_active_backend_type=waldur_support_active_backend_type,
            waldur_support_display_request_type=waldur_support_display_request_type,
            atlassian_use_old_api=atlassian_use_old_api,
            atlassian_use_teenage_api=atlassian_use_teenage_api,
            atlassian_use_automatic_request_mapping=atlassian_use_automatic_request_mapping,
            atlassian_map_waldur_users_to_servicedesk_agents=atlassian_map_waldur_users_to_servicedesk_agents,
            atlassian_strange_setting=atlassian_strange_setting,
            atlassian_api_url=atlassian_api_url,
            atlassian_username=atlassian_username,
            atlassian_password=atlassian_password,
            atlassian_email=atlassian_email,
            atlassian_token=atlassian_token,
            atlassian_verify_ssl=atlassian_verify_ssl,
            atlassian_project_id=atlassian_project_id,
            atlassian_shared_username=atlassian_shared_username,
            atlassian_custom_issue_field_mapping_enabled=atlassian_custom_issue_field_mapping_enabled,
            atlassian_default_offering_issue_type=atlassian_default_offering_issue_type,
            atlassian_excluded_attachment_types=atlassian_excluded_attachment_types,
            atlassian_pull_priorities=atlassian_pull_priorities,
            atlassian_issue_types=atlassian_issue_types,
            atlassian_description_template=atlassian_description_template,
            atlassian_summary_template=atlassian_summary_template,
            atlassian_affected_resource_field=atlassian_affected_resource_field,
            atlassian_impact_field=atlassian_impact_field,
            atlassian_organisation_field=atlassian_organisation_field,
            atlassian_resolution_sla_field=atlassian_resolution_sla_field,
            atlassian_project_field=atlassian_project_field,
            atlassian_reporter_field=atlassian_reporter_field,
            atlassian_caller_field=atlassian_caller_field,
            atlassian_sla_field=atlassian_sla_field,
            atlassian_linked_issue_type=atlassian_linked_issue_type,
            atlassian_satisfaction_field=atlassian_satisfaction_field,
            atlassian_request_feedback_field=atlassian_request_feedback_field,
            atlassian_template_field=atlassian_template_field,
            zammad_api_url=zammad_api_url,
            zammad_token=zammad_token,
            zammad_group=zammad_group,
            zammad_article_type=zammad_article_type,
            zammad_comment_marker=zammad_comment_marker,
            zammad_comment_prefix=zammad_comment_prefix,
            zammad_comment_cooldown_duration=zammad_comment_cooldown_duration,
            smax_api_url=smax_api_url,
            smax_tenant_id=smax_tenant_id,
            smax_login=smax_login,
            smax_password=smax_password,
            smax_organisation_field=smax_organisation_field,
            smax_project_field=smax_project_field,
            smax_affected_resource_field=smax_affected_resource_field,
            smax_times_to_pull=smax_times_to_pull,
            smax_seconds_to_wait=smax_seconds_to_wait,
            smax_creation_source_name=smax_creation_source_name,
            smax_requests_offering=smax_requests_offering,
            smax_verify_ssl=smax_verify_ssl,
            proposal_review_duration=proposal_review_duration,
            user_table_columns=user_table_columns,
            auto_approve_user_tos=auto_approve_user_tos,
            freeipa_enabled=freeipa_enabled,
            freeipa_hostname=freeipa_hostname,
            freeipa_username=freeipa_username,
            freeipa_password=freeipa_password,
            freeipa_verify_ssl=freeipa_verify_ssl,
            freeipa_username_prefix=freeipa_username_prefix,
            freeipa_groupname_prefix=freeipa_groupname_prefix,
            freeipa_blacklisted_usernames=freeipa_blacklisted_usernames,
            freeipa_group_synchronization_enabled=freeipa_group_synchronization_enabled,
            keycloak_icon=keycloak_icon,
            countries=countries,
        )

        constance_settings_request.additional_properties = d
        return constance_settings_request

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
