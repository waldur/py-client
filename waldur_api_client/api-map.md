# Waldur API — API Map

Endpoints organized by domain. Each endpoint is available as:
`waldur_api_client.api.<domain>.<operation_id>.sync(client=client, ...)`

---

## access-subnets
Module: `waldur_api_client.api.access_subnets`

- `access_subnets_list` GET `/api/access-subnets/` — List access subnets (4 query params)
- `access_subnets_count` HEAD `/api/access-subnets/` — List access subnets (4 query params)
- `access_subnets_create` POST `/api/access-subnets/` — Create an access subnet (request body)
- `access_subnets_retrieve` GET `/api/access-subnets/{uuid}/` — Retrieve access subnet (path: uuid)
- `access_subnets_update` PUT `/api/access-subnets/{uuid}/` — Update an access subnet (path: uuid | request body)
- `access_subnets_partial_update` PATCH `/api/access-subnets/{uuid}/` — Partially update an access subnet (path: uuid | request body)
- `access_subnets_destroy` DELETE `/api/access-subnets/{uuid}/` — Delete an access subnet (path: uuid)

## admin
Module: `waldur_api_client.api.admin`

- `admin_arrow_billing_sync_items_list` GET `/api/admin/arrow/billing-sync-items/` (8 query params)
- `admin_arrow_billing_sync_items_count` HEAD `/api/admin/arrow/billing-sync-items/` — Get number of items in the collection matching the request parameters (8 query params)
- `admin_arrow_billing_sync_items_retrieve` GET `/api/admin/arrow/billing-sync-items/{uuid}/` (path: uuid)
- `admin_arrow_billing_syncs_list` GET `/api/admin/arrow/billing-syncs/` (9 query params)
- `admin_arrow_billing_syncs_count` HEAD `/api/admin/arrow/billing-syncs/` — Get number of items in the collection matching the request parameters (9 query params)
- `admin_arrow_billing_syncs_cleanup_consumption` POST `/api/admin/arrow/billing-syncs/cleanup_consumption/` — Delete consumption records with optional dry-run preview (request body)
- `admin_arrow_billing_syncs_consumption_statistics_retrieve` GET `/api/admin/arrow/billing-syncs/consumption_statistics/` — Get consumption statistics (no params)
- `admin_arrow_billing_syncs_consumption_statistics_count` HEAD `/api/admin/arrow/billing-syncs/consumption_statistics/` — Get number of items in the collection matching the request parameters (no params)
- `admin_arrow_billing_syncs_consumption_status_retrieve` GET `/api/admin/arrow/billing-syncs/consumption_status/` — Get current consumption sync status (no params)
- `admin_arrow_billing_syncs_consumption_status_count` HEAD `/api/admin/arrow/billing-syncs/consumption_status/` — Get number of items in the collection matching the request parameters (no params)
- `admin_arrow_billing_syncs_fetch_billing_export` POST `/api/admin/arrow/billing-syncs/fetch_billing_export/` — Fetch raw billing export from Arrow API (request body)
- `admin_arrow_billing_syncs_fetch_consumption` POST `/api/admin/arrow/billing-syncs/fetch_consumption/` — Fetch raw consumption data from Arrow API (request body)
- `admin_arrow_billing_syncs_fetch_license_info` POST `/api/admin/arrow/billing-syncs/fetch_license_info/` — Fetch license details from Arrow API (request body)
- `admin_arrow_billing_syncs_pause_sync` POST `/api/admin/arrow/billing-syncs/pause_sync/` — Pause consumption sync operations (request body)
- `admin_arrow_billing_syncs_pending_records_list` GET `/api/admin/arrow/billing-syncs/pending_records/` — List pending consumption records (not yet finalized) (9 query params)
- `admin_arrow_billing_syncs_pending_records_count` HEAD `/api/admin/arrow/billing-syncs/pending_records/` — Get number of items in the collection matching the request parameters (9 query params)
- `admin_arrow_billing_syncs_reconcile` POST `/api/admin/arrow/billing-syncs/reconcile/` — Trigger reconciliation for a specific period (request body)
- `admin_arrow_billing_syncs_resume_sync` POST `/api/admin/arrow/billing-syncs/resume_sync/` — Resume consumption sync operations (request body)
- `admin_arrow_billing_syncs_sync_resource_historical_consumption` POST `/api/admin/arrow/billing-syncs/sync_resource_historical_consumption/` — Sync historical consumption for a specific resource from Arrow (request body)
- `admin_arrow_billing_syncs_sync_resources` POST `/api/admin/arrow/billing-syncs/sync_resources/` — Sync Arrow IAAS subscriptions to Waldur Resources (request body)
- `admin_arrow_billing_syncs_trigger_consumption_sync` POST `/api/admin/arrow/billing-syncs/trigger_consumption_sync/` — Trigger consumption sync for a specific period (request body)
- `admin_arrow_billing_syncs_trigger_reconciliation` POST `/api/admin/arrow/billing-syncs/trigger_reconciliation/` — Trigger reconciliation (check billing export and apply adjustments) (request body)
- `admin_arrow_billing_syncs_trigger_sync` POST `/api/admin/arrow/billing-syncs/trigger_sync/` — Trigger billing sync for a specific period (request body)
- `admin_arrow_billing_syncs_retrieve` GET `/api/admin/arrow/billing-syncs/{uuid}/` (path: uuid)
- `admin_arrow_consumption_records_list` GET `/api/admin/arrow/consumption-records/` (10 query params)
- `admin_arrow_consumption_records_count` HEAD `/api/admin/arrow/consumption-records/` — Get number of items in the collection matching the request parameters (10 query params)
- `admin_arrow_consumption_records_retrieve` GET `/api/admin/arrow/consumption-records/{uuid}/` (path: uuid)
- `admin_arrow_customer_mappings_list` GET `/api/admin/arrow/customer-mappings/` (7 query params)
- `admin_arrow_customer_mappings_count` HEAD `/api/admin/arrow/customer-mappings/` — Get number of items in the collection matching the request parameters (7 query params)
- `admin_arrow_customer_mappings_create` POST `/api/admin/arrow/customer-mappings/` (request body)
- `admin_arrow_customer_mappings_available_customers_retrieve` GET `/api/admin/arrow/customer-mappings/available_customers/` — Get available Arrow customers that are not yet mapped, with suggestions for Waldur organization matches (no params)
- `admin_arrow_customer_mappings_available_customers_count` HEAD `/api/admin/arrow/customer-mappings/available_customers/` — Get number of items in the collection matching the request parameters (no params)
- `admin_arrow_customer_mappings_sync_from_arrow` POST `/api/admin/arrow/customer-mappings/sync_from_arrow/` — Sync customer list from Arrow and update arrow_company_name (request body)
- `admin_arrow_customer_mappings_retrieve` GET `/api/admin/arrow/customer-mappings/{uuid}/` (path: uuid)
- `admin_arrow_customer_mappings_update` PUT `/api/admin/arrow/customer-mappings/{uuid}/` (path: uuid | request body)
- `admin_arrow_customer_mappings_partial_update` PATCH `/api/admin/arrow/customer-mappings/{uuid}/` (path: uuid | request body)
- `admin_arrow_customer_mappings_destroy` DELETE `/api/admin/arrow/customer-mappings/{uuid}/` (path: uuid)
- `admin_arrow_customer_mappings_billing_summary_retrieve` GET `/api/admin/arrow/customer-mappings/{uuid}/billing_summary/` — Get billing and consumption summary for this customer mapping (path: uuid)
- `admin_arrow_customer_mappings_discover_licenses_retrieve` GET `/api/admin/arrow/customer-mappings/{uuid}/discover_licenses/` — Discover Arrow licenses for this customer and show linkable Waldur resources (path: uuid)
- `admin_arrow_customer_mappings_fetch_arrow_data_retrieve` GET `/api/admin/arrow/customer-mappings/{uuid}/fetch_arrow_data/` — Fetch fresh consumption and billing data from Arrow API for this customer (path: uuid)
- `admin_arrow_customer_mappings_import_license` POST `/api/admin/arrow/customer-mappings/{uuid}/import_license/` — Import an Arrow license as a new Waldur resource (path: uuid | request body)
- `admin_arrow_customer_mappings_link_resource` POST `/api/admin/arrow/customer-mappings/{uuid}/link_resource/` — Link a Waldur resource to an Arrow license by setting its backend_id (path: uuid | request body)
- `admin_arrow_settings_list` GET `/api/admin/arrow/settings/` (2 query params)
- `admin_arrow_settings_count` HEAD `/api/admin/arrow/settings/` — Get number of items in the collection matching the request parameters (2 query params)
- `admin_arrow_settings_create` POST `/api/admin/arrow/settings/` (request body)
- `admin_arrow_settings_discover_customers` POST `/api/admin/arrow/settings/discover_customers/` — Discover Arrow customers and suggest mappings to Waldur customers (request body)
- `admin_arrow_settings_preview_settings` POST `/api/admin/arrow/settings/preview_settings/` — Preview settings configuration before saving (request body)
- `admin_arrow_settings_save_settings` POST `/api/admin/arrow/settings/save_settings/` — Save Arrow settings and customer mappings (request body)
- `admin_arrow_settings_validate_credentials` POST `/api/admin/arrow/settings/validate_credentials/` — Validate Arrow API credentials without saving them (request body)
- `admin_arrow_settings_retrieve` GET `/api/admin/arrow/settings/{uuid}/` (path: uuid)
- `admin_arrow_settings_update` PUT `/api/admin/arrow/settings/{uuid}/` (path: uuid | request body)
- `admin_arrow_settings_partial_update` PATCH `/api/admin/arrow/settings/{uuid}/` (path: uuid | request body)
- `admin_arrow_settings_destroy` DELETE `/api/admin/arrow/settings/{uuid}/` (path: uuid)
- `admin_arrow_vendor_offering_mappings_list` GET `/api/admin/arrow/vendor-offering-mappings/` (6 query params)
- `admin_arrow_vendor_offering_mappings_count` HEAD `/api/admin/arrow/vendor-offering-mappings/` — Get number of items in the collection matching the request parameters (6 query params)
- `admin_arrow_vendor_offering_mappings_create` POST `/api/admin/arrow/vendor-offering-mappings/` (request body)
- `admin_arrow_vendor_offering_mappings_vendor_choices_list` GET `/api/admin/arrow/vendor-offering-mappings/vendor_choices/` — Get vendor names from Arrow catalog API (IAAS category) (6 query params)
- `admin_arrow_vendor_offering_mappings_vendor_choices_count` HEAD `/api/admin/arrow/vendor-offering-mappings/vendor_choices/` — Get number of items in the collection matching the request parameters (6 query params)
- `admin_arrow_vendor_offering_mappings_retrieve` GET `/api/admin/arrow/vendor-offering-mappings/{uuid}/` (path: uuid)
- `admin_arrow_vendor_offering_mappings_update` PUT `/api/admin/arrow/vendor-offering-mappings/{uuid}/` (path: uuid | request body)
- `admin_arrow_vendor_offering_mappings_partial_update` PATCH `/api/admin/arrow/vendor-offering-mappings/{uuid}/` (path: uuid | request body)
- `admin_arrow_vendor_offering_mappings_destroy` DELETE `/api/admin/arrow/vendor-offering-mappings/{uuid}/` (path: uuid)

## admin-announcements
Module: `waldur_api_client.api.admin_announcements`

- `admin_announcements_list` GET `/api/admin-announcements/` (5 query params)
- `admin_announcements_count` HEAD `/api/admin-announcements/` — Get number of items in the collection matching the request parameters (4 query params)
- `admin_announcements_create` POST `/api/admin-announcements/` (request body)
- `admin_announcements_retrieve` GET `/api/admin-announcements/{uuid}/` (path: uuid | 1 query param)
- `admin_announcements_update` PUT `/api/admin-announcements/{uuid}/` (path: uuid | request body)
- `admin_announcements_partial_update` PATCH `/api/admin-announcements/{uuid}/` (path: uuid | request body)
- `admin_announcements_destroy` DELETE `/api/admin-announcements/{uuid}/` (path: uuid)

## api-auth
Module: `waldur_api_client.api.api_auth`

- `api_auth_eduteams_complete_retrieve` GET `/api-auth/eduteams/complete/` (2 query params)
- `api_auth_eduteams_init_retrieve` GET `/api-auth/eduteams/init/` — Redirect user to OIDC authorization endpoint (no params)
- `api_auth_keycloak_complete_retrieve` GET `/api-auth/keycloak/complete/` (2 query params)
- `api_auth_keycloak_init_retrieve` GET `/api-auth/keycloak/init/` — Redirect user to OIDC authorization endpoint (no params)
- `api_auth_logout` POST `/api-auth/logout/` — Log out (no params)
- `api_auth_password` POST `/api-auth/password/` — Obtain authentication token (request body)
- `api_auth_saml2_login` POST `/api-auth/saml2/login/` (request body)
- `api_auth_saml2_login_complete` POST `/api-auth/saml2/login/complete/` (request body)
- `api_auth_saml2_logout_retrieve` GET `/api-auth/saml2/logout/` (no params)
- `api_auth_saml2_logout_complete_retrieve` GET `/api-auth/saml2/logout/complete/` — For IdPs which send GET requests (no params)
- `api_auth_saml2_logout_complete` POST `/api-auth/saml2/logout/complete/` — For IdPs which send POST requests (request body)
- `api_auth_saml2_providers_list` GET `/api-auth/saml2/providers/` (1 query param)
- `api_auth_tara_complete_retrieve` GET `/api-auth/tara/complete/` (2 query params)
- `api_auth_tara_init_retrieve` GET `/api-auth/tara/init/` — Redirect user to OIDC authorization endpoint (no params)

## assignment-batches
Module: `waldur_api_client.api.assignment_batches`

- `assignment_batches_list` GET `/api/assignment-batches/` (8 query params)
- `assignment_batches_count` HEAD `/api/assignment-batches/` — Get number of items in the collection matching the request parameters (8 query params)
- `assignment_batches_create` POST `/api/assignment-batches/` (request body)
- `assignment_batches_retrieve` GET `/api/assignment-batches/{uuid}/` (path: uuid)
- `assignment_batches_update` PUT `/api/assignment-batches/{uuid}/` (path: uuid | request body)
- `assignment_batches_partial_update` PATCH `/api/assignment-batches/{uuid}/` (path: uuid | request body)
- `assignment_batches_destroy` DELETE `/api/assignment-batches/{uuid}/` (path: uuid)
- `assignment_batches_cancel` POST `/api/assignment-batches/{uuid}/cancel/` — Cancel this assignment batch (path: uuid)
- `assignment_batches_extend_deadline` POST `/api/assignment-batches/{uuid}/extend-deadline/` — Extend or modify the expiration date for an assignment batch (path: uuid | request body)
- `assignment_batches_send` POST `/api/assignment-batches/{uuid}/send/` — Send this assignment batch invitation to the reviewer (path: uuid | request body)

## assignment-items
Module: `waldur_api_client.api.assignment_items`

- `assignment_items_list` GET `/api/assignment-items/` (8 query params)
- `assignment_items_count` HEAD `/api/assignment-items/` — Get number of items in the collection matching the request parameters (8 query params)
- `assignment_items_create` POST `/api/assignment-items/` (request body)
- `assignment_items_retrieve` GET `/api/assignment-items/{uuid}/` (path: uuid)
- `assignment_items_update` PUT `/api/assignment-items/{uuid}/` (path: uuid | request body)
- `assignment_items_partial_update` PATCH `/api/assignment-items/{uuid}/` (path: uuid | request body)
- `assignment_items_destroy` DELETE `/api/assignment-items/{uuid}/` (path: uuid)
- `assignment_items_accept` POST `/api/assignment-items/{uuid}/accept/` — Accept this assignment item (path: uuid)
- `assignment_items_decline` POST `/api/assignment-items/{uuid}/decline/` — Decline this assignment item (path: uuid | request body)
- `assignment_items_reassign` POST `/api/assignment-items/{uuid}/reassign/` — Reassign this item to a different reviewer (path: uuid | request body)
- `assignment_items_suggest_alternatives_retrieve` GET `/api/assignment-items/{uuid}/suggest_alternatives/` — Suggest alternative reviewers for a declined assignment (path: uuid)

## auth-tokens
Module: `waldur_api_client.api.auth_tokens`

- `auth_tokens_list` GET `/api/auth-tokens/` (no params)
- `auth_tokens_count` HEAD `/api/auth-tokens/` — Get number of items in the collection matching the request parameters (no params)
- `auth_tokens_retrieve` GET `/api/auth-tokens/{user_id}/` (path: user_id)
- `auth_tokens_destroy` DELETE `/api/auth-tokens/{user_id}/` (path: user_id)

## auth-valimo
Module: `waldur_api_client.api.auth_valimo`

- `auth_valimo_create` POST `/api/auth-valimo/` (request body)
- `auth_valimo_result` POST `/api/auth-valimo/result/` — To get PKI login status and details - issue post request against /api/auth-valimo/result/
        with uuid in parameters (request body)

## autoprovisioning-rules
Module: `waldur_api_client.api.autoprovisioning_rules`

- `autoprovisioning_rules_list` GET `/api/autoprovisioning-rules/` — Manage autoprovisioning rules (no params)
- `autoprovisioning_rules_count` HEAD `/api/autoprovisioning-rules/` — Get number of items in the collection matching the request parameters (no params)
- `autoprovisioning_rules_create` POST `/api/autoprovisioning-rules/` — Manage autoprovisioning rules (request body)
- `autoprovisioning_rules_retrieve` GET `/api/autoprovisioning-rules/{uuid}/` — Manage autoprovisioning rules (path: uuid)
- `autoprovisioning_rules_update` PUT `/api/autoprovisioning-rules/{uuid}/` — Manage autoprovisioning rules (path: uuid | request body)
- `autoprovisioning_rules_partial_update` PATCH `/api/autoprovisioning-rules/{uuid}/` — Manage autoprovisioning rules (path: uuid | request body)
- `autoprovisioning_rules_destroy` DELETE `/api/autoprovisioning-rules/{uuid}/` — Manage autoprovisioning rules (path: uuid)

## aws-images
Module: `waldur_api_client.api.aws_images`

- `aws_images_list` GET `/api/aws-images/` (3 query params)
- `aws_images_count` HEAD `/api/aws-images/` — Get number of items in the collection matching the request parameters (3 query params)
- `aws_images_retrieve` GET `/api/aws-images/{uuid}/` (path: uuid)

## aws-instances
Module: `waldur_api_client.api.aws_instances`

- `aws_instances_list` GET `/api/aws-instances/` (19 query params)
- `aws_instances_count` HEAD `/api/aws-instances/` — Get number of items in the collection matching the request parameters (18 query params)
- `aws_instances_create` POST `/api/aws-instances/` (request body)
- `aws_instances_retrieve` GET `/api/aws-instances/{uuid}/` (path: uuid | 1 query param)
- `aws_instances_update` PUT `/api/aws-instances/{uuid}/` (path: uuid | request body)
- `aws_instances_partial_update` PATCH `/api/aws-instances/{uuid}/` (path: uuid | request body)
- `aws_instances_destroy` DELETE `/api/aws-instances/{uuid}/` (path: uuid)
- `aws_instances_pull` POST `/api/aws-instances/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `aws_instances_resize` POST `/api/aws-instances/{uuid}/resize/` (path: uuid | request body)
- `aws_instances_restart` POST `/api/aws-instances/{uuid}/restart/` (path: uuid)
- `aws_instances_set_erred` POST `/api/aws-instances/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `aws_instances_set_ok` POST `/api/aws-instances/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `aws_instances_start` POST `/api/aws-instances/{uuid}/start/` (path: uuid)
- `aws_instances_stop` POST `/api/aws-instances/{uuid}/stop/` (path: uuid)
- `aws_instances_unlink` POST `/api/aws-instances/{uuid}/unlink/` — Unlink resource (path: uuid)

## aws-regions
Module: `waldur_api_client.api.aws_regions`

- `aws_regions_list` GET `/api/aws-regions/` (2 query params)
- `aws_regions_count` HEAD `/api/aws-regions/` — Get number of items in the collection matching the request parameters (2 query params)
- `aws_regions_retrieve` GET `/api/aws-regions/{uuid}/` (path: uuid)

## aws-sizes
Module: `waldur_api_client.api.aws_sizes`

- `aws_sizes_list` GET `/api/aws-sizes/` (3 query params)
- `aws_sizes_count` HEAD `/api/aws-sizes/` — Get number of items in the collection matching the request parameters (3 query params)
- `aws_sizes_retrieve` GET `/api/aws-sizes/{uuid}/` (path: uuid)

## aws-volumes
Module: `waldur_api_client.api.aws_volumes`

- `aws_volumes_list` GET `/api/aws-volumes/` (1 query param)
- `aws_volumes_count` HEAD `/api/aws-volumes/` — Get number of items in the collection matching the request parameters (no params)
- `aws_volumes_create` POST `/api/aws-volumes/` (request body)
- `aws_volumes_retrieve` GET `/api/aws-volumes/{uuid}/` (path: uuid | 1 query param)
- `aws_volumes_update` PUT `/api/aws-volumes/{uuid}/` (path: uuid | request body)
- `aws_volumes_partial_update` PATCH `/api/aws-volumes/{uuid}/` (path: uuid)
- `aws_volumes_destroy` DELETE `/api/aws-volumes/{uuid}/` (path: uuid)
- `aws_volumes_attach` POST `/api/aws-volumes/{uuid}/attach/` (path: uuid | request body)
- `aws_volumes_detach` POST `/api/aws-volumes/{uuid}/detach/` (path: uuid)
- `aws_volumes_pull` POST `/api/aws-volumes/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `aws_volumes_set_erred` POST `/api/aws-volumes/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `aws_volumes_set_ok` POST `/api/aws-volumes/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `aws_volumes_unlink` POST `/api/aws-volumes/{uuid}/unlink/` — Unlink resource (path: uuid)

## azure-images
Module: `waldur_api_client.api.azure_images`

- `azure_images_list` GET `/api/azure-images/` (6 query params)
- `azure_images_count` HEAD `/api/azure-images/` — Get number of items in the collection matching the request parameters (6 query params)
- `azure_images_retrieve` GET `/api/azure-images/{uuid}/` (path: uuid)

## azure-locations
Module: `waldur_api_client.api.azure_locations`

- `azure_locations_list` GET `/api/azure-locations/` (5 query params)
- `azure_locations_count` HEAD `/api/azure-locations/` — Get number of items in the collection matching the request parameters (5 query params)
- `azure_locations_retrieve` GET `/api/azure-locations/{uuid}/` (path: uuid)

## azure-public-ips
Module: `waldur_api_client.api.azure_public_ips`

- `azure_public_ips_list` GET `/api/azure-public-ips/` (21 query params)
- `azure_public_ips_count` HEAD `/api/azure-public-ips/` — Get number of items in the collection matching the request parameters (20 query params)
- `azure_public_ips_create` POST `/api/azure-public-ips/` (request body)
- `azure_public_ips_retrieve` GET `/api/azure-public-ips/{uuid}/` (path: uuid | 1 query param)
- `azure_public_ips_update` PUT `/api/azure-public-ips/{uuid}/` (path: uuid | request body)
- `azure_public_ips_partial_update` PATCH `/api/azure-public-ips/{uuid}/` (path: uuid | request body)
- `azure_public_ips_destroy` DELETE `/api/azure-public-ips/{uuid}/` (path: uuid)
- `azure_public_ips_pull` POST `/api/azure-public-ips/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `azure_public_ips_set_erred` POST `/api/azure-public-ips/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `azure_public_ips_set_ok` POST `/api/azure-public-ips/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `azure_public_ips_unlink` POST `/api/azure-public-ips/{uuid}/unlink/` — Unlink resource (path: uuid)

## azure-resource-groups
Module: `waldur_api_client.api.azure_resource_groups`

- `azure_resource_groups_list` GET `/api/azure-resource-groups/` (1 query param)
- `azure_resource_groups_count` HEAD `/api/azure-resource-groups/` — Get number of items in the collection matching the request parameters (no params)
- `azure_resource_groups_retrieve` GET `/api/azure-resource-groups/{uuid}/` (path: uuid | 1 query param)

## azure-sizes
Module: `waldur_api_client.api.azure_sizes`

- `azure_sizes_list` GET `/api/azure-sizes/` (7 query params)
- `azure_sizes_count` HEAD `/api/azure-sizes/` — Get number of items in the collection matching the request parameters (7 query params)
- `azure_sizes_retrieve` GET `/api/azure-sizes/{uuid}/` (path: uuid)

## azure-sql-databases
Module: `waldur_api_client.api.azure_sql_databases`

- `azure_sql_databases_list` GET `/api/azure-sql-databases/` (23 query params)
- `azure_sql_databases_count` HEAD `/api/azure-sql-databases/` — Get number of items in the collection matching the request parameters (22 query params)
- `azure_sql_databases_create` POST `/api/azure-sql-databases/` (request body)
- `azure_sql_databases_retrieve` GET `/api/azure-sql-databases/{uuid}/` (path: uuid | 1 query param)
- `azure_sql_databases_update` PUT `/api/azure-sql-databases/{uuid}/` (path: uuid | request body)
- `azure_sql_databases_partial_update` PATCH `/api/azure-sql-databases/{uuid}/` (path: uuid | request body)
- `azure_sql_databases_destroy` DELETE `/api/azure-sql-databases/{uuid}/` (path: uuid)
- `azure_sql_databases_pull` POST `/api/azure-sql-databases/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `azure_sql_databases_set_erred` POST `/api/azure-sql-databases/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `azure_sql_databases_set_ok` POST `/api/azure-sql-databases/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `azure_sql_databases_unlink` POST `/api/azure-sql-databases/{uuid}/unlink/` — Unlink resource (path: uuid)

## azure-sql-servers
Module: `waldur_api_client.api.azure_sql_servers`

- `azure_sql_servers_list` GET `/api/azure-sql-servers/` (21 query params)
- `azure_sql_servers_count` HEAD `/api/azure-sql-servers/` — Get number of items in the collection matching the request parameters (20 query params)
- `azure_sql_servers_create` POST `/api/azure-sql-servers/` (request body)
- `azure_sql_servers_retrieve` GET `/api/azure-sql-servers/{uuid}/` (path: uuid | 1 query param)
- `azure_sql_servers_update` PUT `/api/azure-sql-servers/{uuid}/` (path: uuid | request body)
- `azure_sql_servers_partial_update` PATCH `/api/azure-sql-servers/{uuid}/` (path: uuid | request body)
- `azure_sql_servers_destroy` DELETE `/api/azure-sql-servers/{uuid}/` (path: uuid)
- `azure_sql_servers_create_database` POST `/api/azure-sql-servers/{uuid}/create_database/` (path: uuid | request body)
- `azure_sql_servers_pull` POST `/api/azure-sql-servers/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `azure_sql_servers_set_erred` POST `/api/azure-sql-servers/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `azure_sql_servers_set_ok` POST `/api/azure-sql-servers/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `azure_sql_servers_unlink` POST `/api/azure-sql-servers/{uuid}/unlink/` — Unlink resource (path: uuid)

## azure-virtualmachines
Module: `waldur_api_client.api.azure_virtualmachines`

- `azure_virtualmachines_list` GET `/api/azure-virtualmachines/` (21 query params)
- `azure_virtualmachines_count` HEAD `/api/azure-virtualmachines/` — Get number of items in the collection matching the request parameters (20 query params)
- `azure_virtualmachines_create` POST `/api/azure-virtualmachines/` (request body)
- `azure_virtualmachines_retrieve` GET `/api/azure-virtualmachines/{uuid}/` (path: uuid | 1 query param)
- `azure_virtualmachines_update` PUT `/api/azure-virtualmachines/{uuid}/` (path: uuid | request body)
- `azure_virtualmachines_partial_update` PATCH `/api/azure-virtualmachines/{uuid}/` (path: uuid | request body)
- `azure_virtualmachines_destroy` DELETE `/api/azure-virtualmachines/{uuid}/` (path: uuid)
- `azure_virtualmachines_pull` POST `/api/azure-virtualmachines/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `azure_virtualmachines_restart` POST `/api/azure-virtualmachines/{uuid}/restart/` (path: uuid)
- `azure_virtualmachines_set_erred` POST `/api/azure-virtualmachines/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `azure_virtualmachines_set_ok` POST `/api/azure-virtualmachines/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `azure_virtualmachines_start` POST `/api/azure-virtualmachines/{uuid}/start/` (path: uuid)
- `azure_virtualmachines_stop` POST `/api/azure-virtualmachines/{uuid}/stop/` (path: uuid)
- `azure_virtualmachines_unlink` POST `/api/azure-virtualmachines/{uuid}/unlink/` — Unlink resource (path: uuid)

## backend-resource-requests
Module: `waldur_api_client.api.backend_resource_requests`

- `backend_resource_requests_list` GET `/api/backend-resource-requests/` — List backend resource requests (7 query params)
- `backend_resource_requests_count` HEAD `/api/backend-resource-requests/` — List backend resource requests (7 query params)
- `backend_resource_requests_create` POST `/api/backend-resource-requests/` — Create a backend resource request (request body)
- `backend_resource_requests_retrieve` GET `/api/backend-resource-requests/{uuid}/` — Retrieve a backend resource request (path: uuid)
- `backend_resource_requests_set_done` POST `/api/backend-resource-requests/{uuid}/set_done/` — Mark a request as done (path: uuid)
- `backend_resource_requests_set_erred` POST `/api/backend-resource-requests/{uuid}/set_erred/` — Mark a request as erred (path: uuid | request body)
- `backend_resource_requests_start_processing` POST `/api/backend-resource-requests/{uuid}/start_processing/` — Start processing a request (path: uuid)

## backend-resources
Module: `waldur_api_client.api.backend_resources`

- `backend_resources_list` GET `/api/backend-resources/` — List backend resources (8 query params)
- `backend_resources_count` HEAD `/api/backend-resources/` — List backend resources (8 query params)
- `backend_resources_create` POST `/api/backend-resources/` — Create a backend resource (request body)
- `backend_resources_retrieve` GET `/api/backend-resources/{uuid}/` — Retrieve a backend resource (path: uuid)
- `backend_resources_destroy` DELETE `/api/backend-resources/{uuid}/` — Delete a backend resource (path: uuid)
- `backend_resources_import_resource` POST `/api/backend-resources/{uuid}/import_resource/` — Import a backend resource (staff only) (path: uuid | request body)

## billing-total-cost
Module: `waldur_api_client.api.billing_total_cost`

- `billing_total_cost_retrieve` GET `/api/billing-total-cost/` (5 query params)

## booking-offerings
Module: `waldur_api_client.api.booking_offerings`

- `booking_offerings_list` GET `/api/booking-offerings/` (1 query param)
- `booking_offerings_count` HEAD `/api/booking-offerings/` — Get number of items in the collection matching the request parameters (no params)
- `booking_offerings_retrieve` GET `/api/booking-offerings/{uuid}/` (path: uuid | 1 query param)
- `booking_offerings_google_calendar_sync` POST `/api/booking-offerings/{uuid}/google_calendar_sync/` (path: uuid)
- `booking_offerings_share_google_calendar` POST `/api/booking-offerings/{uuid}/share_google_calendar/` (path: uuid)
- `booking_offerings_unshare_google_calendar` POST `/api/booking-offerings/{uuid}/unshare_google_calendar/` (path: uuid)

## booking-resources
Module: `waldur_api_client.api.booking_resources`

- `booking_resources_list` GET `/api/booking-resources/` (41 query params)
- `booking_resources_count` HEAD `/api/booking-resources/` — Get number of items in the collection matching the request parameters (40 query params)
- `booking_resources_retrieve` GET `/api/booking-resources/{uuid}/` (path: uuid | 1 query param)
- `booking_resources_accept` POST `/api/booking-resources/{uuid}/accept/` (path: uuid)
- `booking_resources_reject` POST `/api/booking-resources/{uuid}/reject/` (path: uuid)

## broadcast-message-templates
Module: `waldur_api_client.api.broadcast_message_templates`

- `broadcast_message_templates_list` GET `/api/broadcast-message-templates/` (1 query param)
- `broadcast_message_templates_count` HEAD `/api/broadcast-message-templates/` — Get number of items in the collection matching the request parameters (1 query param)
- `broadcast_message_templates_create` POST `/api/broadcast-message-templates/` (request body)
- `broadcast_message_templates_retrieve` GET `/api/broadcast-message-templates/{uuid}/` (path: uuid)
- `broadcast_message_templates_update` PUT `/api/broadcast-message-templates/{uuid}/` (path: uuid | request body)
- `broadcast_message_templates_partial_update` PATCH `/api/broadcast-message-templates/{uuid}/` (path: uuid | request body)
- `broadcast_message_templates_destroy` DELETE `/api/broadcast-message-templates/{uuid}/` (path: uuid)

## broadcast-messages
Module: `waldur_api_client.api.broadcast_messages`

- `broadcast_messages_list` GET `/api/broadcast-messages/` (4 query params)
- `broadcast_messages_count` HEAD `/api/broadcast-messages/` — Get number of items in the collection matching the request parameters (3 query params)
- `broadcast_messages_create` POST `/api/broadcast-messages/` (request body)
- `broadcast_messages_recipients_retrieve` GET `/api/broadcast-messages/recipients/` (1 query param)
- `broadcast_messages_recipients_count` HEAD `/api/broadcast-messages/recipients/` — Get number of items in the collection matching the request parameters (no params)
- `broadcast_messages_retrieve` GET `/api/broadcast-messages/{uuid}/` (path: uuid | 1 query param)
- `broadcast_messages_update` PUT `/api/broadcast-messages/{uuid}/` (path: uuid | request body)
- `broadcast_messages_partial_update` PATCH `/api/broadcast-messages/{uuid}/` (path: uuid | request body)
- `broadcast_messages_destroy` DELETE `/api/broadcast-messages/{uuid}/` (path: uuid)
- `broadcast_messages_schedule` POST `/api/broadcast-messages/{uuid}/schedule/` (path: uuid)
- `broadcast_messages_send` POST `/api/broadcast-messages/{uuid}/send/` (path: uuid)

## call-assignment-configurations
Module: `waldur_api_client.api.call_assignment_configurations`

- `call_assignment_configurations_list` GET `/api/call-assignment-configurations/` (no params)
- `call_assignment_configurations_count` HEAD `/api/call-assignment-configurations/` — Get number of items in the collection matching the request parameters (no params)
- `call_assignment_configurations_create` POST `/api/call-assignment-configurations/` (request body)
- `call_assignment_configurations_retrieve` GET `/api/call-assignment-configurations/{uuid}/` (path: uuid)
- `call_assignment_configurations_update` PUT `/api/call-assignment-configurations/{uuid}/` (path: uuid | request body)
- `call_assignment_configurations_partial_update` PATCH `/api/call-assignment-configurations/{uuid}/` (path: uuid | request body)
- `call_assignment_configurations_destroy` DELETE `/api/call-assignment-configurations/{uuid}/` (path: uuid)

## call-managing-organisations
Module: `waldur_api_client.api.call_managing_organisations`

- `call_managing_organisations_list` GET `/api/call-managing-organisations/` (4 query params)
- `call_managing_organisations_count` HEAD `/api/call-managing-organisations/` — Get number of items in the collection matching the request parameters (4 query params)
- `call_managing_organisations_create` POST `/api/call-managing-organisations/` (request body)
- `call_managing_organisations_retrieve` GET `/api/call-managing-organisations/{uuid}/` (path: uuid)
- `call_managing_organisations_update` PUT `/api/call-managing-organisations/{uuid}/` (path: uuid | request body)
- `call_managing_organisations_partial_update` PATCH `/api/call-managing-organisations/{uuid}/` (path: uuid | request body)
- `call_managing_organisations_destroy` DELETE `/api/call-managing-organisations/{uuid}/` (path: uuid)
- `call_managing_organisations_add_user` POST `/api/call-managing-organisations/{uuid}/add_user/` — Grant a role to a user (path: uuid | request body)
- `call_managing_organisations_delete_user` POST `/api/call-managing-organisations/{uuid}/delete_user/` — Revoke a role from a user (path: uuid | request body)
- `call_managing_organisations_list_users_list` GET `/api/call-managing-organisations/{uuid}/list_users/` — List users and their roles in a scope (path: uuid | 10 query params)
- `call_managing_organisations_stats_retrieve` GET `/api/call-managing-organisations/{uuid}/stats/` — Return statistics for call managing organisation (path: uuid)
- `call_managing_organisations_update_user` POST `/api/call-managing-organisations/{uuid}/update_user/` — Update a user's role expiration (path: uuid | request body)

## call-proposal-project-role-mappings
Module: `waldur_api_client.api.call_proposal_project_role_mappings`

- `call_proposal_project_role_mappings_list` GET `/api/call-proposal-project-role-mappings/` (1 query param)
- `call_proposal_project_role_mappings_count` HEAD `/api/call-proposal-project-role-mappings/` — Get number of items in the collection matching the request parameters (1 query param)
- `call_proposal_project_role_mappings_create` POST `/api/call-proposal-project-role-mappings/` (request body)
- `call_proposal_project_role_mappings_retrieve` GET `/api/call-proposal-project-role-mappings/{uuid}/` (path: uuid)
- `call_proposal_project_role_mappings_update` PUT `/api/call-proposal-project-role-mappings/{uuid}/` (path: uuid | request body)
- `call_proposal_project_role_mappings_partial_update` PATCH `/api/call-proposal-project-role-mappings/{uuid}/` (path: uuid | request body)
- `call_proposal_project_role_mappings_destroy` DELETE `/api/call-proposal-project-role-mappings/{uuid}/` (path: uuid)

## call-reviewer-pools
Module: `waldur_api_client.api.call_reviewer_pools`

- `call_reviewer_pools_list` GET `/api/call-reviewer-pools/` (5 query params)
- `call_reviewer_pools_count` HEAD `/api/call-reviewer-pools/` — Get number of items in the collection matching the request parameters (5 query params)
- `call_reviewer_pools_retrieve` GET `/api/call-reviewer-pools/{uuid}/` (path: uuid)
- `call_reviewer_pools_partial_update` PATCH `/api/call-reviewer-pools/{uuid}/` (path: uuid | request body)
- `call_reviewer_pools_accept` POST `/api/call-reviewer-pools/{uuid}/accept/` — Accept a pool invitation (authenticated users only) (path: uuid | request body)
- `call_reviewer_pools_decline` POST `/api/call-reviewer-pools/{uuid}/decline/` — Decline a pool invitation (authenticated users only) (path: uuid | request body)

## call-rounds
Module: `waldur_api_client.api.call_rounds`

- `call_rounds_list` GET `/api/call-rounds/` (no params)
- `call_rounds_count` HEAD `/api/call-rounds/` — Get number of items in the collection matching the request parameters (no params)
- `call_rounds_retrieve` GET `/api/call-rounds/{uuid}/` (path: uuid)
- `call_rounds_reviewers_list` GET `/api/call-rounds/{uuid}/reviewers/` — Return list of reviewers for round (path: uuid)

## celery-stats
Module: `waldur_api_client.api.celery_stats`

- `celery_stats_retrieve` GET `/api/celery-stats/` — Get Celery worker statistics (no params)

## chat
Module: `waldur_api_client.api.chat`

- `chat_stream` POST `/api/chat/stream/` (request body)

## chat-messages
Module: `waldur_api_client.api.chat_messages`

- `chat_messages_list` GET `/api/chat-messages/` (2 query params)
- `chat_messages_edit` POST `/api/chat-messages/{uuid}/edit/` — Edit message (path: uuid | request body)

## chat-quota
Module: `waldur_api_client.api.chat_quota`

- `chat_quota_set_quota` POST `/api/chat-quota/set_quota/` — Set token quota for user (request body)
- `chat_quota_usage_retrieve` GET `/api/chat-quota/usage/` — Get current token quota and usage for the requesting user (1 query param)

## chat-sessions
Module: `waldur_api_client.api.chat_sessions`

- `chat_sessions_list` GET `/api/chat-sessions/` (1 query param)
- `chat_sessions_current_retrieve` GET `/api/chat-sessions/current/` — Get or create current user's chat session (no params)
- `chat_sessions_retrieve` GET `/api/chat-sessions/{uuid}/` (path: uuid | 1 query param)

## chat-threads
Module: `waldur_api_client.api.chat_threads`

- `chat_threads_list` GET `/api/chat-threads/` (7 query params)
- `chat_threads_retrieve` GET `/api/chat-threads/{uuid}/` (path: uuid | 1 query param)
- `chat_threads_archive` POST `/api/chat-threads/{uuid}/archive/` — Archive thread (path: uuid | request body)
- `chat_threads_unarchive` POST `/api/chat-threads/{uuid}/unarchive/` — Unarchive thread (path: uuid | request body)

## chat-tools
Module: `waldur_api_client.api.chat_tools`

- `chat_tools_execute` POST `/api/chat-tools/execute/` — Execute a tool and return the result (request body)

## checklists-admin
Module: `waldur_api_client.api.checklists_admin`

- `checklists_admin_list` GET `/api/checklists-admin/` (2 query params)
- `checklists_admin_count` HEAD `/api/checklists-admin/` — Get number of items in the collection matching the request parameters (2 query params)
- `checklists_admin_create` POST `/api/checklists-admin/` (request body)
- `checklists_admin_retrieve` GET `/api/checklists-admin/{uuid}/` (path: uuid)
- `checklists_admin_update` PUT `/api/checklists-admin/{uuid}/` (path: uuid | request body)
- `checklists_admin_partial_update` PATCH `/api/checklists-admin/{uuid}/` (path: uuid | request body)
- `checklists_admin_destroy` DELETE `/api/checklists-admin/{uuid}/` (path: uuid)
- `checklists_admin_checklist_questions` GET `/api/checklists-admin/{uuid}/questions/` — Return checklist questions (path: uuid | 2 query params)

## checklists-admin-question-dependencies
Module: `waldur_api_client.api.checklists_admin_question_dependencies`

- `checklists_admin_question_dependencies_list` GET `/api/checklists-admin-question-dependencies/` (2 query params)
- `checklists_admin_question_dependencies_count` HEAD `/api/checklists-admin-question-dependencies/` — Get number of items in the collection matching the request parameters (2 query params)
- `checklists_admin_question_dependencies_create` POST `/api/checklists-admin-question-dependencies/` (request body)
- `checklists_admin_question_dependencies_retrieve` GET `/api/checklists-admin-question-dependencies/{uuid}/` (path: uuid)
- `checklists_admin_question_dependencies_update` PUT `/api/checklists-admin-question-dependencies/{uuid}/` (path: uuid | request body)
- `checklists_admin_question_dependencies_partial_update` PATCH `/api/checklists-admin-question-dependencies/{uuid}/` (path: uuid | request body)
- `checklists_admin_question_dependencies_destroy` DELETE `/api/checklists-admin-question-dependencies/{uuid}/` (path: uuid)

## checklists-admin-question-options
Module: `waldur_api_client.api.checklists_admin_question_options`

- `checklists_admin_question_options_list` GET `/api/checklists-admin-question-options/` (1 query param)
- `checklists_admin_question_options_count` HEAD `/api/checklists-admin-question-options/` — Get number of items in the collection matching the request parameters (1 query param)
- `checklists_admin_question_options_create` POST `/api/checklists-admin-question-options/` (request body)
- `checklists_admin_question_options_retrieve` GET `/api/checklists-admin-question-options/{uuid}/` (path: uuid)
- `checklists_admin_question_options_update` PUT `/api/checklists-admin-question-options/{uuid}/` (path: uuid | request body)
- `checklists_admin_question_options_partial_update` PATCH `/api/checklists-admin-question-options/{uuid}/` (path: uuid | request body)
- `checklists_admin_question_options_destroy` DELETE `/api/checklists-admin-question-options/{uuid}/` (path: uuid)

## checklists-admin-questions
Module: `waldur_api_client.api.checklists_admin_questions`

- `checklists_admin_questions_list` GET `/api/checklists-admin-questions/` (3 query params)
- `checklists_admin_questions_count` HEAD `/api/checklists-admin-questions/` — Get number of items in the collection matching the request parameters (3 query params)
- `checklists_admin_questions_create` POST `/api/checklists-admin-questions/` (request body)
- `checklists_admin_questions_retrieve` GET `/api/checklists-admin-questions/{uuid}/` (path: uuid)
- `checklists_admin_questions_update` PUT `/api/checklists-admin-questions/{uuid}/` (path: uuid | request body)
- `checklists_admin_questions_partial_update` PATCH `/api/checklists-admin-questions/{uuid}/` (path: uuid | request body)
- `checklists_admin_questions_destroy` DELETE `/api/checklists-admin-questions/{uuid}/` (path: uuid)

## coi-detection-jobs
Module: `waldur_api_client.api.coi_detection_jobs`

- `coi_detection_jobs_list` GET `/api/coi-detection-jobs/` (4 query params)
- `coi_detection_jobs_count` HEAD `/api/coi-detection-jobs/` — Get number of items in the collection matching the request parameters (4 query params)
- `coi_detection_jobs_retrieve` GET `/api/coi-detection-jobs/{uuid}/` (path: uuid)

## coi-disclosures
Module: `waldur_api_client.api.coi_disclosures`

- `coi_disclosures_list` GET `/api/coi-disclosures/` (5 query params)
- `coi_disclosures_count` HEAD `/api/coi-disclosures/` — Get number of items in the collection matching the request parameters (5 query params)
- `coi_disclosures_create` POST `/api/coi-disclosures/` (request body)
- `coi_disclosures_retrieve` GET `/api/coi-disclosures/{uuid}/` (path: uuid)

## component-user-usage-limits
Module: `waldur_api_client.api.component_user_usage_limits`

- `component_user_usage_limits_list` GET `/api/component-user-usage-limits/` — List component usage limits for users (5 query params)
- `component_user_usage_limits_count` HEAD `/api/component-user-usage-limits/` — List component usage limits for users (5 query params)
- `component_user_usage_limits_create` POST `/api/component-user-usage-limits/` — Create a component usage limit for a user (request body)
- `component_user_usage_limits_retrieve` GET `/api/component-user-usage-limits/{uuid}/` — Retrieve a component usage limit (path: uuid)
- `component_user_usage_limits_update` PUT `/api/component-user-usage-limits/{uuid}/` — Update a component usage limit (path: uuid | request body)
- `component_user_usage_limits_partial_update` PATCH `/api/component-user-usage-limits/{uuid}/` — Partially update a component usage limit (path: uuid | request body)
- `component_user_usage_limits_destroy` DELETE `/api/component-user-usage-limits/{uuid}/` — Delete a component usage limit (path: uuid)

## configuration
Module: `waldur_api_client.api.configuration`

- `configuration_retrieve` GET `/api/configuration/` — Get public configuration (no params)

## conflicts-of-interest
Module: `waldur_api_client.api.conflicts_of_interest`

- `conflicts_of_interest_list` GET `/api/conflicts-of-interest/` (10 query params)
- `conflicts_of_interest_count` HEAD `/api/conflicts-of-interest/` — Get number of items in the collection matching the request parameters (10 query params)
- `conflicts_of_interest_retrieve` GET `/api/conflicts-of-interest/{uuid}/` (path: uuid)
- `conflicts_of_interest_update` PUT `/api/conflicts-of-interest/{uuid}/` (path: uuid | request body)
- `conflicts_of_interest_partial_update` PATCH `/api/conflicts-of-interest/{uuid}/` (path: uuid | request body)
- `conflicts_of_interest_dismiss` POST `/api/conflicts-of-interest/{uuid}/dismiss/` — Dismiss a conflict of interest (not a real conflict) (path: uuid | request body)
- `conflicts_of_interest_recuse` POST `/api/conflicts-of-interest/{uuid}/recuse/` — Recuse reviewer from the proposal (path: uuid | request body)
- `conflicts_of_interest_waive` POST `/api/conflicts-of-interest/{uuid}/waive/` — Waive a conflict with a management plan (path: uuid | request body)

## customer-credits
Module: `waldur_api_client.api.customer_credits`

- `customer_credits_list` GET `/api/customer-credits/` (5 query params)
- `customer_credits_count` HEAD `/api/customer-credits/` — Get number of items in the collection matching the request parameters (5 query params)
- `customer_credits_create` POST `/api/customer-credits/` (request body)
- `customer_credits_retrieve` GET `/api/customer-credits/{uuid}/` (path: uuid)
- `customer_credits_update` PUT `/api/customer-credits/{uuid}/` (path: uuid | request body)
- `customer_credits_partial_update` PATCH `/api/customer-credits/{uuid}/` (path: uuid | request body)
- `customer_credits_destroy` DELETE `/api/customer-credits/{uuid}/` (path: uuid)
- `customer_credits_apply_compensations` POST `/api/customer-credits/{uuid}/apply_compensations/` (path: uuid | request body)
- `customer_credits_clear_compensations` POST `/api/customer-credits/{uuid}/clear_compensations/` (path: uuid | request body)
- `customer_credits_consumptions_list` GET `/api/customer-credits/{uuid}/consumptions/` — Get credit consumption history grouped by month (path: uuid | 5 query params)

## customer-permissions-reviews
Module: `waldur_api_client.api.customer_permissions_reviews`

- `customer_permissions_reviews_list` GET `/api/customer-permissions-reviews/` (5 query params)
- `customer_permissions_reviews_count` HEAD `/api/customer-permissions-reviews/` — Get number of items in the collection matching the request parameters (5 query params)
- `customer_permissions_reviews_retrieve` GET `/api/customer-permissions-reviews/{uuid}/` (path: uuid)
- `customer_permissions_reviews_close` POST `/api/customer-permissions-reviews/{uuid}/close/` — Close customer permission review (path: uuid)

## customer-quotas
Module: `waldur_api_client.api.customer_quotas`

- `customer_quotas_list` GET `/api/customer-quotas/` — List customer quotas (no params)
- `customer_quotas_count` HEAD `/api/customer-quotas/` — Get number of items in the collection matching the request parameters (no params)

## customers
Module: `waldur_api_client.api.customers`

- `customers_list` GET `/api/customers/` — List customers (16 query params)
- `customers_count` HEAD `/api/customers/` — List customers (15 query params)
- `customers_create` POST `/api/customers/` — Create a new customer (request body)
- `customers_countries_list` GET `/api/customers/countries/` — Get list of available countries (15 query params)
- `customers_countries_count` HEAD `/api/customers/countries/` — Get list of available countries (15 query params)
- `customers_project_metadata_compliance_details_list` GET `/api/customers/{customer_uuid}/project-metadata-compliance-details/` — Get detailed project metadata compliance (path: customer_uuid)
- `customers_project_metadata_compliance_overview_list` GET `/api/customers/{customer_uuid}/project-metadata-compliance-overview/` — Get project metadata compliance overview (path: customer_uuid)
- `customers_project_metadata_compliance_projects_list` GET `/api/customers/{customer_uuid}/project-metadata-compliance-projects/` — List projects with compliance data (path: customer_uuid)
- `customers_project_metadata_question_answers_list` GET `/api/customers/{customer_uuid}/project-metadata-question-answers/` — List questions with project answers (path: customer_uuid)
- `customers_users_list` GET `/api/customers/{customer_uuid}/users/` — List users of a customer (path: customer_uuid | 19 query params)
- `customers_retrieve` GET `/api/customers/{uuid}/` — Retrieve customer details (path: uuid | 1 query param)
- `customers_update` PUT `/api/customers/{uuid}/` — Update a customer (path: uuid | request body)
- `customers_partial_update` PATCH `/api/customers/{uuid}/` — Partially update a customer (path: uuid | request body)
- `customers_destroy` DELETE `/api/customers/{uuid}/` — Delete a customer (path: uuid)
- `customers_add_user` POST `/api/customers/{uuid}/add_user/` — Grant a role to a user (path: uuid | request body)
- `customers_contact` POST `/api/customers/{uuid}/contact/` — Update customer contact details (path: uuid | request body)
- `customers_delete_user` POST `/api/customers/{uuid}/delete_user/` — Revoke a role from a user (path: uuid | request body)
- `customers_history_list` GET `/api/customers/{uuid}/history/` — Get version history (path: uuid | 17 query params)
- `customers_history_at_retrieve` GET `/api/customers/{uuid}/history/at/` — Get object state at a specific timestamp (path: uuid | 1 query param)
- `customers_list_users_list` GET `/api/customers/{uuid}/list_users/` — List users and their roles in a scope (path: uuid | 10 query params)
- `customers_project_digest_config_retrieve` GET `/api/customers/{uuid}/project-digest-config/` — Get project digest configuration (path: uuid)
- `customers_project_digest_config_preview` POST `/api/customers/{uuid}/project-digest-config/preview/` — Preview digest for a project (path: uuid | request body)
- `customers_project_digest_config_send_test` POST `/api/customers/{uuid}/project-digest-config/send-test/` — Send a test digest email (path: uuid)
- `customers_stats_retrieve` GET `/api/customers/{uuid}/stats/` — Get customer resource usage statistics (path: uuid | 1 query param)
- `customers_update_project_digest_config_update` PUT `/api/customers/{uuid}/update-project-digest-config/` — Update project digest configuration (path: uuid | request body)
- `customers_update_project_digest_config_partial_update` PATCH `/api/customers/{uuid}/update-project-digest-config/` — Update project digest configuration (path: uuid | request body)
- `customers_update_organization_groups` POST `/api/customers/{uuid}/update_organization_groups/` — Update organization groups for a customer (path: uuid | request body)
- `customers_update_user` POST `/api/customers/{uuid}/update_user/` — Update a user's role expiration (path: uuid | request body)

## daily-quotas
Module: `waldur_api_client.api.daily_quotas`

- `daily_quotas_retrieve` GET `/api/daily-quotas/` (4 query params)

## data-access-logs
Module: `waldur_api_client.api.data_access_logs`

- `data_access_logs_list` GET `/api/data-access-logs/` (7 query params)
- `data_access_logs_count` HEAD `/api/data-access-logs/` — Get number of items in the collection matching the request parameters (7 query params)
- `data_access_logs_retrieve` GET `/api/data-access-logs/{uuid}/` (path: uuid)
- `data_access_logs_destroy` DELETE `/api/data-access-logs/{uuid}/` (path: uuid)

## database-stats
Module: `waldur_api_client.api.database_stats`

- `database_stats_retrieve` GET `/api/database-stats/` — Get comprehensive database statistics (no params)

## debug
Module: `waldur_api_client.api.debug`

- `debug_pubsub_circuit_breaker_retrieve` GET `/api/debug/pubsub/circuit_breaker/` — Get circuit breaker state (no params)
- `debug_pubsub_circuit_breaker_reset` POST `/api/debug/pubsub/circuit_breaker_reset/` — Reset circuit breaker (no params)
- `debug_pubsub_dead_letter_queue_retrieve` GET `/api/debug/pubsub/dead_letter_queue/` — Get dead letter queue status (no params)
- `debug_pubsub_message_state_cache_retrieve` GET `/api/debug/pubsub/message_state_cache/` — Get message state cache statistics (no params)
- `debug_pubsub_metrics_retrieve` GET `/api/debug/pubsub/metrics/` — Get publishing metrics (no params)
- `debug_pubsub_metrics_reset` POST `/api/debug/pubsub/metrics_reset/` — Reset publishing metrics (no params)
- `debug_pubsub_overview_retrieve` GET `/api/debug/pubsub/overview/` — Get pubsub system health overview (no params)
- `debug_pubsub_queues_retrieve` GET `/api/debug/pubsub/queues/` — Get subscription queues overview (no params)

## digitalocean-droplets
Module: `waldur_api_client.api.digitalocean_droplets`

- `digitalocean_droplets_list` GET `/api/digitalocean-droplets/` (19 query params)
- `digitalocean_droplets_count` HEAD `/api/digitalocean-droplets/` — Get number of items in the collection matching the request parameters (18 query params)
- `digitalocean_droplets_create` POST `/api/digitalocean-droplets/` (request body)
- `digitalocean_droplets_retrieve` GET `/api/digitalocean-droplets/{uuid}/` (path: uuid | 1 query param)
- `digitalocean_droplets_update` PUT `/api/digitalocean-droplets/{uuid}/` (path: uuid | request body)
- `digitalocean_droplets_partial_update` PATCH `/api/digitalocean-droplets/{uuid}/` (path: uuid | request body)
- `digitalocean_droplets_destroy` DELETE `/api/digitalocean-droplets/{uuid}/` (path: uuid)
- `digitalocean_droplets_pull` POST `/api/digitalocean-droplets/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `digitalocean_droplets_resize` POST `/api/digitalocean-droplets/{uuid}/resize/` — To resize droplet, submit a POST request to the instance URL, specifying URI of a target size (path: uuid | request body)
- `digitalocean_droplets_restart` POST `/api/digitalocean-droplets/{uuid}/restart/` (path: uuid)
- `digitalocean_droplets_set_erred` POST `/api/digitalocean-droplets/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `digitalocean_droplets_set_ok` POST `/api/digitalocean-droplets/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `digitalocean_droplets_start` POST `/api/digitalocean-droplets/{uuid}/start/` (path: uuid)
- `digitalocean_droplets_stop` POST `/api/digitalocean-droplets/{uuid}/stop/` (path: uuid)
- `digitalocean_droplets_unlink` POST `/api/digitalocean-droplets/{uuid}/unlink/` — Unlink resource (path: uuid)

## digitalocean-images
Module: `waldur_api_client.api.digitalocean_images`

- `digitalocean_images_list` GET `/api/digitalocean-images/` (5 query params)
- `digitalocean_images_count` HEAD `/api/digitalocean-images/` — Get number of items in the collection matching the request parameters (5 query params)
- `digitalocean_images_retrieve` GET `/api/digitalocean-images/{uuid}/` (path: uuid)

## digitalocean-regions
Module: `waldur_api_client.api.digitalocean_regions`

- `digitalocean_regions_list` GET `/api/digitalocean-regions/` (2 query params)
- `digitalocean_regions_count` HEAD `/api/digitalocean-regions/` — Get number of items in the collection matching the request parameters (2 query params)
- `digitalocean_regions_retrieve` GET `/api/digitalocean-regions/{uuid}/` (path: uuid)

## digitalocean-sizes
Module: `waldur_api_client.api.digitalocean_sizes`

- `digitalocean_sizes_list` GET `/api/digitalocean-sizes/` (5 query params)
- `digitalocean_sizes_count` HEAD `/api/digitalocean-sizes/` — Get number of items in the collection matching the request parameters (5 query params)
- `digitalocean_sizes_retrieve` GET `/api/digitalocean-sizes/{uuid}/` (path: uuid)

## email-logs
Module: `waldur_api_client.api.email_logs`

- `email_logs_list` GET `/api/email-logs/` (5 query params)
- `email_logs_count` HEAD `/api/email-logs/` — Get number of items in the collection matching the request parameters (5 query params)
- `email_logs_retrieve` GET `/api/email-logs/{uuid}/` (path: uuid)

## event-subscription-queues
Module: `waldur_api_client.api.event_subscription_queues`

- `event_subscription_queues_list` GET `/api/event-subscription-queues/` (4 query params)
- `event_subscription_queues_count` HEAD `/api/event-subscription-queues/` — Get number of items in the collection matching the request parameters (4 query params)
- `event_subscription_queues_retrieve` GET `/api/event-subscription-queues/{uuid}/` (path: uuid)
- `event_subscription_queues_destroy` DELETE `/api/event-subscription-queues/{uuid}/` (path: uuid)

## event-subscriptions
Module: `waldur_api_client.api.event_subscriptions`

- `event_subscriptions_list` GET `/api/event-subscriptions/` (3 query params)
- `event_subscriptions_count` HEAD `/api/event-subscriptions/` — Get number of items in the collection matching the request parameters (3 query params)
- `event_subscriptions_create` POST `/api/event-subscriptions/` (request body)
- `event_subscriptions_retrieve` GET `/api/event-subscriptions/{uuid}/` (path: uuid)
- `event_subscriptions_destroy` DELETE `/api/event-subscriptions/{uuid}/` (path: uuid)
- `event_subscriptions_create_queue` POST `/api/event-subscriptions/{uuid}/create_queue/` — Create a RabbitMQ queue for receiving events for a specific offering and object type (path: uuid | request body)

## events
Module: `waldur_api_client.api.events`

- `events_list` GET `/api/events/` (8 query params)
- `events_count` HEAD `/api/events/` — Get number of items in the collection matching the request parameters (7 query params)
- `events_count_retrieve` GET `/api/events/count/` (1 query param)
- `events_count_count` HEAD `/api/events/count/` — Get number of items in the collection matching the request parameters (no params)
- `events_event_groups_retrieve` GET `/api/events/event_groups/` — Returns a list of groups with event types (1 query param)
- `events_event_groups_count` HEAD `/api/events/event_groups/` — Get number of items in the collection matching the request parameters (no params)
- `events_scope_types_retrieve` GET `/api/events/scope_types/` — Returns a list of scope types acceptable by events filter (1 query param)
- `events_scope_types_count` HEAD `/api/events/scope_types/` — Get number of items in the collection matching the request parameters (no params)
- `events_retrieve` GET `/api/events/{id}/` (path: id | 1 query param)

## events-stats
Module: `waldur_api_client.api.events_stats`

- `events_stats_list` GET `/api/events-stats/` (no params)
- `events_stats_count` HEAD `/api/events-stats/` — Get number of items in the collection matching the request parameters (no params)

## expertise-categories
Module: `waldur_api_client.api.expertise_categories`

- `expertise_categories_list` GET `/api/expertise-categories/` (5 query params)
- `expertise_categories_count` HEAD `/api/expertise-categories/` — Get number of items in the collection matching the request parameters (5 query params)
- `expertise_categories_retrieve` GET `/api/expertise-categories/{uuid}/` (path: uuid)

## external-links
Module: `waldur_api_client.api.external_links`

- `external_links_list` GET `/api/external-links/` — List external links (2 query params)
- `external_links_count` HEAD `/api/external-links/` — List external links (2 query params)
- `external_links_create` POST `/api/external-links/` — Create an external link (request body)
- `external_links_retrieve` GET `/api/external-links/{uuid}/` — Retrieve external link (path: uuid)
- `external_links_update` PUT `/api/external-links/{uuid}/` — Update an external link (path: uuid | request body)
- `external_links_partial_update` PATCH `/api/external-links/{uuid}/` — Partially update an external link (path: uuid | request body)
- `external_links_destroy` DELETE `/api/external-links/{uuid}/` — Delete an external link (path: uuid)

## feature-values
Module: `waldur_api_client.api.feature_values`

- `feature_values` POST `/api/feature-values/` — Update feature flags (request body)

## financial-reports
Module: `waldur_api_client.api.financial_reports`

- `financial_reports_list` GET `/api/financial-reports/` (15 query params)
- `financial_reports_count` HEAD `/api/financial-reports/` — Get number of items in the collection matching the request parameters (15 query params)
- `financial_reports_retrieve` GET `/api/financial-reports/{uuid}/` (path: uuid)

## freeipa-profiles
Module: `waldur_api_client.api.freeipa_profiles`

- `freeipa_profiles_list` GET `/api/freeipa-profiles/` (2 query params)
- `freeipa_profiles_count` HEAD `/api/freeipa-profiles/` — Get number of items in the collection matching the request parameters (2 query params)
- `freeipa_profiles_create` POST `/api/freeipa-profiles/` (request body)
- `freeipa_profiles_retrieve` GET `/api/freeipa-profiles/{uuid}/` (path: uuid)
- `freeipa_profiles_update` PUT `/api/freeipa-profiles/{uuid}/` (path: uuid | request body)
- `freeipa_profiles_partial_update` PATCH `/api/freeipa-profiles/{uuid}/` (path: uuid)
- `freeipa_profiles_update_ssh_keys` POST `/api/freeipa-profiles/{uuid}/update_ssh_keys/` — Update SSH keys for profile (path: uuid)

## google-auth
Module: `waldur_api_client.api.google_auth`

- `google_auth_list` GET `/api/google-auth/` (2 query params)
- `google_auth_count` HEAD `/api/google-auth/` — Get number of items in the collection matching the request parameters (1 query param)
- `google_auth_callback_retrieve` GET `/api/google-auth/callback/` — Callback endpoint for Google authorization (2 query params)
- `google_auth_callback_count` HEAD `/api/google-auth/callback/` — Get number of items in the collection matching the request parameters (2 query params)
- `google_auth_retrieve` GET `/api/google-auth/{uuid}/` (path: uuid | 1 query param)
- `google_auth_authorize_retrieve` GET `/api/google-auth/{uuid}/authorize/` (path: uuid | 1 query param)

## hooks
Module: `waldur_api_client.api.hooks`

- `hooks_list` GET `/api/hooks/` (no params)
- `hooks_count` HEAD `/api/hooks/` — Get number of items in the collection matching the request parameters (no params)

## hooks-email
Module: `waldur_api_client.api.hooks_email`

- `hooks_email_list` GET `/api/hooks-email/` (8 query params)
- `hooks_email_count` HEAD `/api/hooks-email/` — Get number of items in the collection matching the request parameters (8 query params)
- `hooks_email_create` POST `/api/hooks-email/` (request body)
- `hooks_email_retrieve` GET `/api/hooks-email/{uuid}/` (path: uuid)
- `hooks_email_update` PUT `/api/hooks-email/{uuid}/` (path: uuid | request body)
- `hooks_email_partial_update` PATCH `/api/hooks-email/{uuid}/` (path: uuid | request body)
- `hooks_email_destroy` DELETE `/api/hooks-email/{uuid}/` (path: uuid)

## hooks-web
Module: `waldur_api_client.api.hooks_web`

- `hooks_web_list` GET `/api/hooks-web/` (9 query params)
- `hooks_web_count` HEAD `/api/hooks-web/` — Get number of items in the collection matching the request parameters (9 query params)
- `hooks_web_create` POST `/api/hooks-web/` — When hook is activated, POST request is issued against destination URL with the following data: (request body)
- `hooks_web_retrieve` GET `/api/hooks-web/{uuid}/` (path: uuid)
- `hooks_web_update` PUT `/api/hooks-web/{uuid}/` (path: uuid | request body)
- `hooks_web_partial_update` PATCH `/api/hooks-web/{uuid}/` (path: uuid | request body)
- `hooks_web_destroy` DELETE `/api/hooks-web/{uuid}/` (path: uuid)

## identity-bridge
Module: `waldur_api_client.api.identity_bridge`

- `identity_bridge` POST `/api/identity-bridge/` — Push user attributes from an ISD (request body)
- `identity_bridge_remove` POST `/api/identity-bridge/remove/` — Remove a user from an ISD (request body)
- `identity_bridge_stats_retrieve` GET `/api/identity-bridge/stats/` — Get Identity Bridge statistics (no params)

## identity-providers
Module: `waldur_api_client.api.identity_providers`

- `identity_providers_list` GET `/api/identity-providers/` (no params)
- `identity_providers_count` HEAD `/api/identity-providers/` — Get number of items in the collection matching the request parameters (no params)
- `identity_providers_create` POST `/api/identity-providers/` (request body)
- `identity_providers_discover_metadata` POST `/api/identity-providers/discover_metadata/` — Discover OIDC provider metadata (request body)
- `identity_providers_generate_mapping` POST `/api/identity-providers/generate-mapping/` — Generate default attribute mapping (request body)
- `identity_providers_retrieve` GET `/api/identity-providers/{provider}/` (path: provider)
- `identity_providers_update` PUT `/api/identity-providers/{provider}/` (path: provider | request body)
- `identity_providers_partial_update` PATCH `/api/identity-providers/{provider}/` (path: provider | request body)
- `identity_providers_destroy` DELETE `/api/identity-providers/{provider}/` (path: provider)

## invoice
Module: `waldur_api_client.api.invoice`

- `invoice_send_financial_report_by_mail` POST `/api/invoice/send-financial-report-by-mail/` (request body)

## invoice-items
Module: `waldur_api_client.api.invoice_items`

- `invoice_items_list` GET `/api/invoice-items/` (9 query params)
- `invoice_items_count` HEAD `/api/invoice-items/` — Get number of items in the collection matching the request parameters (9 query params)
- `invoice_items_costs_list` GET `/api/invoice-items/costs/` — Get costs breakdown for a project by year and month (1 query param)
- `invoice_items_costs_count` HEAD `/api/invoice-items/costs/` — Get number of items in the collection matching the request parameters (1 query param)
- `invoice_items_customer_costs_for_period_retrieve` GET `/api/invoice-items/customer_costs_for_period/` (2 query params)
- `invoice_items_customer_costs_for_period_count` HEAD `/api/invoice-items/customer_costs_for_period/` — Get number of items in the collection matching the request parameters (2 query params)
- `invoice_items_project_costs_for_period_retrieve` GET `/api/invoice-items/project_costs_for_period/` — Get resource cost breakdown for a project over a specified period (2 query params)
- `invoice_items_project_costs_for_period_count` HEAD `/api/invoice-items/project_costs_for_period/` — Get number of items in the collection matching the request parameters (2 query params)
- `invoice_items_total_price_retrieve` GET `/api/invoice-items/total_price/` — Calculate total price for filtered invoice items (9 query params)
- `invoice_items_total_price_count` HEAD `/api/invoice-items/total_price/` — Get number of items in the collection matching the request parameters (9 query params)
- `invoice_items_retrieve` GET `/api/invoice-items/{uuid}/` (path: uuid)
- `invoice_items_update` PUT `/api/invoice-items/{uuid}/` (path: uuid | request body)
- `invoice_items_partial_update` PATCH `/api/invoice-items/{uuid}/` (path: uuid | request body)
- `invoice_items_destroy` DELETE `/api/invoice-items/{uuid}/` (path: uuid)
- `invoice_items_consumptions_retrieve` GET `/api/invoice-items/{uuid}/consumptions/` (path: uuid)
- `invoice_items_create_compensation` POST `/api/invoice-items/{uuid}/create_compensation/` — Create compensation invoice item for selected invoice item (path: uuid | request body)
- `invoice_items_migrate_to` POST `/api/invoice-items/{uuid}/migrate_to/` — Move invoice item from one invoice to another one (path: uuid | request body)

## invoices
Module: `waldur_api_client.api.invoices`

- `invoices_list` GET `/api/invoices/` (10 query params)
- `invoices_count` HEAD `/api/invoices/` — Get number of items in the collection matching the request parameters (9 query params)
- `invoices_growth_retrieve` GET `/api/invoices/growth/` — Analyze invoice trends over time by comparing monthly totals for major customers versus others over the past year (3 query params)
- `invoices_growth_count` HEAD `/api/invoices/growth/` — Get number of items in the collection matching the request parameters (3 query params)
- `invoices_import_usage` POST `/api/invoices/import_usage/` — Import usage data (request body)
- `invoices_retrieve` GET `/api/invoices/{uuid}/` (path: uuid | 1 query param)
- `invoices_history_list` GET `/api/invoices/{uuid}/history/` — Get version history (path: uuid | 11 query params)
- `invoices_history_at_retrieve` GET `/api/invoices/{uuid}/history/at/` — Get object state at a specific timestamp (path: uuid | 1 query param)
- `invoices_items_retrieve` GET `/api/invoices/{uuid}/items/` — Get invoice items (path: uuid | 6 query params)
- `invoices_paid` POST `/api/invoices/{uuid}/paid/` — Mark invoice as paid and optionally create payment record with proof of payment (path: uuid | request body)
- `invoices_send_notification` POST `/api/invoices/{uuid}/send_notification/` — Send invoice notification (path: uuid)
- `invoices_set_backend_id` POST `/api/invoices/{uuid}/set_backend_id/` — Set backend ID for invoice (path: uuid | request body)
- `invoices_set_payment_url` POST `/api/invoices/{uuid}/set_payment_url/` — Set payment URL for invoice (path: uuid | request body)
- `invoices_set_reference_number` POST `/api/invoices/{uuid}/set_reference_number/` — Set reference number for invoice (path: uuid | request body)
- `invoices_stats_list` GET `/api/invoices/{uuid}/stats/` — Spendings grouped by offerings and filtered by provider (path: uuid | 10 query params)

## keycloak-groups
Module: `waldur_api_client.api.keycloak_groups`

- `keycloak_groups_list` GET `/api/keycloak-groups/` (3 query params)
- `keycloak_groups_count` HEAD `/api/keycloak-groups/` — Get number of items in the collection matching the request parameters (3 query params)
- `keycloak_groups_retrieve` GET `/api/keycloak-groups/{uuid}/` (path: uuid)

## keycloak-user-group-memberships
Module: `waldur_api_client.api.keycloak_user_group_memberships`

- `keycloak_user_group_memberships_list` GET `/api/keycloak-user-group-memberships/` (9 query params)
- `keycloak_user_group_memberships_count` HEAD `/api/keycloak-user-group-memberships/` — Get number of items in the collection matching the request parameters (9 query params)
- `keycloak_user_group_memberships_create` POST `/api/keycloak-user-group-memberships/` (request body)
- `keycloak_user_group_memberships_retrieve` GET `/api/keycloak-user-group-memberships/{uuid}/` (path: uuid)
- `keycloak_user_group_memberships_update` PUT `/api/keycloak-user-group-memberships/{uuid}/` (path: uuid | request body)
- `keycloak_user_group_memberships_partial_update` PATCH `/api/keycloak-user-group-memberships/{uuid}/` (path: uuid | request body)
- `keycloak_user_group_memberships_destroy` DELETE `/api/keycloak-user-group-memberships/{uuid}/` (path: uuid)

## keys
Module: `waldur_api_client.api.keys`

- `keys_list` GET `/api/keys/` (12 query params)
- `keys_count` HEAD `/api/keys/` — Get number of items in the collection matching the request parameters (11 query params)
- `keys_create` POST `/api/keys/` (request body)
- `keys_retrieve` GET `/api/keys/{uuid}/` (path: uuid | 1 query param)
- `keys_destroy` DELETE `/api/keys/{uuid}/` (path: uuid)
- `keys_history_list` GET `/api/keys/{uuid}/history/` — Get version history (path: uuid | 13 query params)
- `keys_history_at_retrieve` GET `/api/keys/{uuid}/history/at/` — Get object state at a specific timestamp (path: uuid | 1 query param)

## lexis-links
Module: `waldur_api_client.api.lexis_links`

- `lexis_links_list` GET `/api/lexis-links/` (5 query params)
- `lexis_links_count` HEAD `/api/lexis-links/` — Get number of items in the collection matching the request parameters (5 query params)
- `lexis_links_create` POST `/api/lexis-links/` (request body)
- `lexis_links_retrieve` GET `/api/lexis-links/{uuid}/` (path: uuid)
- `lexis_links_update` PUT `/api/lexis-links/{uuid}/` (path: uuid | request body)
- `lexis_links_partial_update` PATCH `/api/lexis-links/{uuid}/` (path: uuid | request body)
- `lexis_links_destroy` DELETE `/api/lexis-links/{uuid}/` (path: uuid)

## maintenance-announcement-offerings
Module: `waldur_api_client.api.maintenance_announcement_offerings`

- `maintenance_announcement_offerings_list` GET `/api/maintenance-announcement-offerings/` — List affected offerings for maintenance (no params)
- `maintenance_announcement_offerings_count` HEAD `/api/maintenance-announcement-offerings/` — List affected offerings for maintenance (no params)
- `maintenance_announcement_offerings_create` POST `/api/maintenance-announcement-offerings/` — Link an offering to a maintenance announcement (request body)
- `maintenance_announcement_offerings_retrieve` GET `/api/maintenance-announcement-offerings/{uuid}/` — Retrieve an affected offering link (path: uuid)
- `maintenance_announcement_offerings_update` PUT `/api/maintenance-announcement-offerings/{uuid}/` — Update an affected offering link (path: uuid | request body)
- `maintenance_announcement_offerings_partial_update` PATCH `/api/maintenance-announcement-offerings/{uuid}/` — Partially update an affected offering link (path: uuid | request body)
- `maintenance_announcement_offerings_destroy` DELETE `/api/maintenance-announcement-offerings/{uuid}/` — Unlink an offering from a maintenance announcement (path: uuid)

## maintenance-announcement-template-offerings
Module: `waldur_api_client.api.maintenance_announcement_template_offerings`

- `maintenance_announcement_template_offerings_list` GET `/api/maintenance-announcement-template-offerings/` — List affected offering templates (5 query params)
- `maintenance_announcement_template_offerings_count` HEAD `/api/maintenance-announcement-template-offerings/` — List affected offering templates (5 query params)
- `maintenance_announcement_template_offerings_create` POST `/api/maintenance-announcement-template-offerings/` — Link an offering to a maintenance template (request body)
- `maintenance_announcement_template_offerings_retrieve` GET `/api/maintenance-announcement-template-offerings/{uuid}/` — Retrieve an affected offering template link (path: uuid)
- `maintenance_announcement_template_offerings_update` PUT `/api/maintenance-announcement-template-offerings/{uuid}/` — Update an affected offering template link (path: uuid | request body)
- `maintenance_announcement_template_offerings_partial_update` PATCH `/api/maintenance-announcement-template-offerings/{uuid}/` — Partially update an affected offering template link (path: uuid | request body)
- `maintenance_announcement_template_offerings_destroy` DELETE `/api/maintenance-announcement-template-offerings/{uuid}/` — Unlink an offering from a maintenance template (path: uuid)

## maintenance-announcements
Module: `waldur_api_client.api.maintenance_announcements`

- `maintenance_announcements_list` GET `/api/maintenance-announcements/` — List maintenance announcements (8 query params)
- `maintenance_announcements_count` HEAD `/api/maintenance-announcements/` — List maintenance announcements (8 query params)
- `maintenance_announcements_create` POST `/api/maintenance-announcements/` — Create a maintenance announcement (request body)
- `maintenance_announcements_maintenance_stats_retrieve` GET `/api/maintenance-announcements/maintenance_stats/` — Get maintenance announcement statistics (3 query params)
- `maintenance_announcements_maintenance_stats_count` HEAD `/api/maintenance-announcements/maintenance_stats/` — Get maintenance announcement statistics (3 query params)
- `maintenance_announcements_retrieve` GET `/api/maintenance-announcements/{uuid}/` — Retrieve a maintenance announcement (path: uuid)
- `maintenance_announcements_update` PUT `/api/maintenance-announcements/{uuid}/` — Update a maintenance announcement (path: uuid | request body)
- `maintenance_announcements_partial_update` PATCH `/api/maintenance-announcements/{uuid}/` — Partially update a maintenance announcement (path: uuid | request body)
- `maintenance_announcements_destroy` DELETE `/api/maintenance-announcements/{uuid}/` — Delete a maintenance announcement (path: uuid)
- `maintenance_announcements_cancel_maintenance` POST `/api/maintenance-announcements/{uuid}/cancel_maintenance/` — Cancel the maintenance announcement (path: uuid)
- `maintenance_announcements_complete_maintenance` POST `/api/maintenance-announcements/{uuid}/complete_maintenance/` — Complete the maintenance announcement (path: uuid)
- `maintenance_announcements_schedule` POST `/api/maintenance-announcements/{uuid}/schedule/` — Schedule/publish the maintenance announcement (path: uuid)
- `maintenance_announcements_start_maintenance` POST `/api/maintenance-announcements/{uuid}/start_maintenance/` — Start the maintenance announcement (path: uuid)
- `maintenance_announcements_unschedule` POST `/api/maintenance-announcements/{uuid}/unschedule/` — Unschedule/unpublish the maintenance announcement (path: uuid)

## maintenance-announcements-template
Module: `waldur_api_client.api.maintenance_announcements_template`

- `maintenance_announcements_template_list` GET `/api/maintenance-announcements-template/` — List maintenance announcement templates (3 query params)
- `maintenance_announcements_template_count` HEAD `/api/maintenance-announcements-template/` — List maintenance announcement templates (3 query params)
- `maintenance_announcements_template_create` POST `/api/maintenance-announcements-template/` — Create a maintenance announcement template (request body)
- `maintenance_announcements_template_retrieve` GET `/api/maintenance-announcements-template/{uuid}/` — Retrieve a maintenance announcement template (path: uuid)
- `maintenance_announcements_template_update` PUT `/api/maintenance-announcements-template/{uuid}/` — Update a maintenance announcement template (path: uuid | request body)
- `maintenance_announcements_template_partial_update` PATCH `/api/maintenance-announcements-template/{uuid}/` — Partially update a maintenance announcement template (path: uuid | request body)
- `maintenance_announcements_template_destroy` DELETE `/api/maintenance-announcements-template/{uuid}/` — Delete a maintenance announcement template (path: uuid)

## managed-rancher-cluster-resources
Module: `waldur_api_client.api.managed_rancher_cluster_resources`

- `managed_rancher_cluster_resources_list` GET `/api/managed-rancher-cluster-resources/` (1 query param)
- `managed_rancher_cluster_resources_count` HEAD `/api/managed-rancher-cluster-resources/` — Get number of items in the collection matching the request parameters (no params)
- `managed_rancher_cluster_resources_retrieve` GET `/api/managed-rancher-cluster-resources/{uuid}/` (path: uuid | 1 query param)
- `managed_rancher_cluster_resources_add_node` POST `/api/managed-rancher-cluster-resources/{uuid}/add_node/` (path: uuid | request body)

## marketplace-bookings
Module: `waldur_api_client.api.marketplace_bookings`

- `marketplace_bookings_list` GET `/api/marketplace-bookings/{uuid}/` (path: uuid)

## marketplace-categories
Module: `waldur_api_client.api.marketplace_categories`

- `marketplace_categories_list` GET `/api/marketplace-categories/` — List categories (9 query params)
- `marketplace_categories_count` HEAD `/api/marketplace-categories/` — List categories (8 query params)
- `marketplace_categories_create` POST `/api/marketplace-categories/` — Create a category (request body)
- `marketplace_categories_retrieve` GET `/api/marketplace-categories/{uuid}/` — Retrieve a category (path: uuid | 1 query param)
- `marketplace_categories_update` PUT `/api/marketplace-categories/{uuid}/` — Update a category (path: uuid | request body)
- `marketplace_categories_partial_update` PATCH `/api/marketplace-categories/{uuid}/` — Partially update a category (path: uuid | request body)
- `marketplace_categories_destroy` DELETE `/api/marketplace-categories/{uuid}/` — Delete a category (path: uuid)

## marketplace-category-columns
Module: `waldur_api_client.api.marketplace_category_columns`

- `marketplace_category_columns_list` GET `/api/marketplace-category-columns/` — List category columns (2 query params)
- `marketplace_category_columns_count` HEAD `/api/marketplace-category-columns/` — List category columns (2 query params)
- `marketplace_category_columns_create` POST `/api/marketplace-category-columns/` — Create a category column (request body)
- `marketplace_category_columns_retrieve` GET `/api/marketplace-category-columns/{uuid}/` — Retrieve a category column (path: uuid)
- `marketplace_category_columns_update` PUT `/api/marketplace-category-columns/{uuid}/` — Update a category column (path: uuid | request body)
- `marketplace_category_columns_partial_update` PATCH `/api/marketplace-category-columns/{uuid}/` — Partially update a category column (path: uuid | request body)
- `marketplace_category_columns_destroy` DELETE `/api/marketplace-category-columns/{uuid}/` — Delete a category column (path: uuid)

## marketplace-category-component-usages
Module: `waldur_api_client.api.marketplace_category_component_usages`

- `marketplace_category_component_usages_list` GET `/api/marketplace-category-component-usages/` — List aggregated category component usages (3 query params)
- `marketplace_category_component_usages_count` HEAD `/api/marketplace-category-component-usages/` — List aggregated category component usages (2 query params)
- `marketplace_category_component_usages_retrieve` GET `/api/marketplace-category-component-usages/{id}/` — Retrieve an aggregated category component usage record (path: id | 1 query param)

## marketplace-category-components
Module: `waldur_api_client.api.marketplace_category_components`

- `marketplace_category_components_list` GET `/api/marketplace-category-components/` — List category components (no params)
- `marketplace_category_components_count` HEAD `/api/marketplace-category-components/` — List category components (no params)
- `marketplace_category_components_create` POST `/api/marketplace-category-components/` — Create a category component (request body)
- `marketplace_category_components_retrieve` GET `/api/marketplace-category-components/{id}/` — Retrieve a category component (path: id)
- `marketplace_category_components_update` PUT `/api/marketplace-category-components/{id}/` — Update a category component (path: id | request body)
- `marketplace_category_components_partial_update` PATCH `/api/marketplace-category-components/{id}/` — Partially update a category component (path: id | request body)
- `marketplace_category_components_destroy` DELETE `/api/marketplace-category-components/{id}/` — Delete a category component (path: id)

## marketplace-category-groups
Module: `waldur_api_client.api.marketplace_category_groups`

- `marketplace_category_groups_list` GET `/api/marketplace-category-groups/` — List category groups (2 query params)
- `marketplace_category_groups_count` HEAD `/api/marketplace-category-groups/` — List category groups (1 query param)
- `marketplace_category_groups_create` POST `/api/marketplace-category-groups/` — Create a category group (request body)
- `marketplace_category_groups_retrieve` GET `/api/marketplace-category-groups/{uuid}/` — Retrieve a category group (path: uuid | 1 query param)
- `marketplace_category_groups_update` PUT `/api/marketplace-category-groups/{uuid}/` — Update a category group (path: uuid | request body)
- `marketplace_category_groups_partial_update` PATCH `/api/marketplace-category-groups/{uuid}/` — Partially update a category group (path: uuid | request body)
- `marketplace_category_groups_destroy` DELETE `/api/marketplace-category-groups/{uuid}/` — Delete a category group (path: uuid)

## marketplace-category-help-articles
Module: `waldur_api_client.api.marketplace_category_help_articles`

- `marketplace_category_help_articles_list` GET `/api/marketplace-category-help-articles/` — List category help articles (no params)
- `marketplace_category_help_articles_count` HEAD `/api/marketplace-category-help-articles/` — List category help articles (no params)
- `marketplace_category_help_articles_create` POST `/api/marketplace-category-help-articles/` — Create a category help article (request body)
- `marketplace_category_help_articles_retrieve` GET `/api/marketplace-category-help-articles/{id}/` — Retrieve a category help article (path: id)
- `marketplace_category_help_articles_update` PUT `/api/marketplace-category-help-articles/{id}/` — Update a category help article (path: id | request body)
- `marketplace_category_help_articles_partial_update` PATCH `/api/marketplace-category-help-articles/{id}/` — Partially update a category help article (path: id | request body)
- `marketplace_category_help_articles_destroy` DELETE `/api/marketplace-category-help-articles/{id}/` — Delete a category help article (path: id)

## marketplace-component-usages
Module: `waldur_api_client.api.marketplace_component_usages`

- `marketplace_component_usages_list` GET `/api/marketplace-component-usages/` — List component usage records (13 query params)
- `marketplace_component_usages_count` HEAD `/api/marketplace-component-usages/` — List component usage records (12 query params)
- `marketplace_component_usages_set_usage` POST `/api/marketplace-component-usages/set_usage/` — Set component usage for a resource (request body)
- `marketplace_component_usages_retrieve` GET `/api/marketplace-component-usages/{uuid}/` — Retrieve a component usage record (path: uuid | 1 query param)
- `marketplace_component_usages_set_user_usage` POST `/api/marketplace-component-usages/{uuid}/set_user_usage/` — Set user-specific component usage (path: uuid | request body)

## marketplace-component-user-usages
Module: `waldur_api_client.api.marketplace_component_user_usages`

- `marketplace_component_user_usages_list` GET `/api/marketplace-component-user-usages/` — List user-specific component usages (14 query params)
- `marketplace_component_user_usages_count` HEAD `/api/marketplace-component-user-usages/` — List user-specific component usages (13 query params)
- `marketplace_component_user_usages_retrieve` GET `/api/marketplace-component-user-usages/{uuid}/` — Retrieve a user-specific component usage record (path: uuid | 1 query param)

## marketplace-course-accounts
Module: `waldur_api_client.api.marketplace_course_accounts`

- `marketplace_course_accounts_list` GET `/api/marketplace-course-accounts/` — List course accounts (9 query params)
- `marketplace_course_accounts_count` HEAD `/api/marketplace-course-accounts/` — List course accounts (9 query params)
- `marketplace_course_accounts_create` POST `/api/marketplace-course-accounts/` — Create a course account (request body)
- `marketplace_course_accounts_create_bulk` POST `/api/marketplace-course-accounts/create_bulk/` — Bulk create course accounts (9 query params | request body)
- `marketplace_course_accounts_retrieve` GET `/api/marketplace-course-accounts/{uuid}/` — Retrieve a course account (path: uuid)
- `marketplace_course_accounts_destroy` DELETE `/api/marketplace-course-accounts/{uuid}/` — Delete (close) a course account (path: uuid)

## marketplace-customer-component-usage-policies
Module: `waldur_api_client.api.marketplace_customer_component_usage_policies`

- `marketplace_customer_component_usage_policies_list` GET `/api/marketplace-customer-component-usage-policies/` (4 query params)
- `marketplace_customer_component_usage_policies_count` HEAD `/api/marketplace-customer-component-usage-policies/` — Get number of items in the collection matching the request parameters (4 query params)
- `marketplace_customer_component_usage_policies_create` POST `/api/marketplace-customer-component-usage-policies/` (request body)
- `marketplace_customer_component_usage_policies_actions_retrieve` GET `/api/marketplace-customer-component-usage-policies/actions/` (no params)
- `marketplace_customer_component_usage_policies_actions_count` HEAD `/api/marketplace-customer-component-usage-policies/actions/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_customer_component_usage_policies_retrieve` GET `/api/marketplace-customer-component-usage-policies/{uuid}/` (path: uuid)
- `marketplace_customer_component_usage_policies_update` PUT `/api/marketplace-customer-component-usage-policies/{uuid}/` (path: uuid | request body)
- `marketplace_customer_component_usage_policies_partial_update` PATCH `/api/marketplace-customer-component-usage-policies/{uuid}/` (path: uuid | request body)
- `marketplace_customer_component_usage_policies_destroy` DELETE `/api/marketplace-customer-component-usage-policies/{uuid}/` (path: uuid)

## marketplace-customer-estimated-cost-policies
Module: `waldur_api_client.api.marketplace_customer_estimated_cost_policies`

- `marketplace_customer_estimated_cost_policies_list` GET `/api/marketplace-customer-estimated-cost-policies/` (4 query params)
- `marketplace_customer_estimated_cost_policies_count` HEAD `/api/marketplace-customer-estimated-cost-policies/` — Get number of items in the collection matching the request parameters (4 query params)
- `marketplace_customer_estimated_cost_policies_create` POST `/api/marketplace-customer-estimated-cost-policies/` (request body)
- `marketplace_customer_estimated_cost_policies_actions_retrieve` GET `/api/marketplace-customer-estimated-cost-policies/actions/` (no params)
- `marketplace_customer_estimated_cost_policies_actions_count` HEAD `/api/marketplace-customer-estimated-cost-policies/actions/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_customer_estimated_cost_policies_retrieve` GET `/api/marketplace-customer-estimated-cost-policies/{uuid}/` (path: uuid)
- `marketplace_customer_estimated_cost_policies_update` PUT `/api/marketplace-customer-estimated-cost-policies/{uuid}/` (path: uuid | request body)
- `marketplace_customer_estimated_cost_policies_partial_update` PATCH `/api/marketplace-customer-estimated-cost-policies/{uuid}/` (path: uuid | request body)
- `marketplace_customer_estimated_cost_policies_destroy` DELETE `/api/marketplace-customer-estimated-cost-policies/{uuid}/` (path: uuid)

## marketplace-customer-service-accounts
Module: `waldur_api_client.api.marketplace_customer_service_accounts`

- `marketplace_customer_service_accounts_list` GET `/api/marketplace-customer-service-accounts/` — List service accounts (5 query params)
- `marketplace_customer_service_accounts_count` HEAD `/api/marketplace-customer-service-accounts/` — List service accounts (5 query params)
- `marketplace_customer_service_accounts_create` POST `/api/marketplace-customer-service-accounts/` — Create a customer service account (request body)
- `marketplace_customer_service_accounts_retrieve` GET `/api/marketplace-customer-service-accounts/{uuid}/` — Retrieve a service account (path: uuid)
- `marketplace_customer_service_accounts_update` PUT `/api/marketplace-customer-service-accounts/{uuid}/` — Update a service account (path: uuid | request body)
- `marketplace_customer_service_accounts_partial_update` PATCH `/api/marketplace-customer-service-accounts/{uuid}/` — Partially update a service account (path: uuid | request body)
- `marketplace_customer_service_accounts_destroy` DELETE `/api/marketplace-customer-service-accounts/{uuid}/` — Close a customer service account (path: uuid)
- `marketplace_customer_service_accounts_rotate_api_key` POST `/api/marketplace-customer-service-accounts/{uuid}/rotate_api_key/` — Rotate API key for a customer service account (path: uuid)

## marketplace-demo-presets
Module: `waldur_api_client.api.marketplace_demo_presets`

- `marketplace_demo_presets_info_retrieve` GET `/api/marketplace-demo-presets/info/{name}/` — Get demo preset details (path: name)
- `marketplace_demo_presets_info_count` HEAD `/api/marketplace-demo-presets/info/{name}/` — Get demo preset details (path: name)
- `marketplace_demo_presets_list_list` GET `/api/marketplace-demo-presets/list/` — List demo presets (no params)
- `marketplace_demo_presets_list_count` HEAD `/api/marketplace-demo-presets/list/` — List demo presets (no params)
- `marketplace_demo_presets_load` POST `/api/marketplace-demo-presets/load/{name}/` — Load demo preset (path: name | request body)

## marketplace-global-categories
Module: `waldur_api_client.api.marketplace_global_categories`

- `marketplace_global_categories_retrieve` GET `/api/marketplace-global-categories/` — Get resource counts by category (2 query params)

## marketplace-integration-statuses
Module: `waldur_api_client.api.marketplace_integration_statuses`

- `marketplace_integration_statuses_list` GET `/api/marketplace-integration-statuses/` — List integration statuses (8 query params)
- `marketplace_integration_statuses_count` HEAD `/api/marketplace-integration-statuses/` — List integration statuses (8 query params)
- `marketplace_integration_statuses_retrieve` GET `/api/marketplace-integration-statuses/{uuid}/` — Retrieve an integration status (path: uuid)

## marketplace-offering-estimated-cost-policies
Module: `waldur_api_client.api.marketplace_offering_estimated_cost_policies`

- `marketplace_offering_estimated_cost_policies_list` GET `/api/marketplace-offering-estimated-cost-policies/` (2 query params)
- `marketplace_offering_estimated_cost_policies_count` HEAD `/api/marketplace-offering-estimated-cost-policies/` — Get number of items in the collection matching the request parameters (2 query params)
- `marketplace_offering_estimated_cost_policies_create` POST `/api/marketplace-offering-estimated-cost-policies/` (request body)
- `marketplace_offering_estimated_cost_policies_actions_retrieve` GET `/api/marketplace-offering-estimated-cost-policies/actions/` — List available actions for OfferingEstimatedCostPolicy (no params)
- `marketplace_offering_estimated_cost_policies_actions_count` HEAD `/api/marketplace-offering-estimated-cost-policies/actions/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_offering_estimated_cost_policies_retrieve` GET `/api/marketplace-offering-estimated-cost-policies/{uuid}/` (path: uuid)
- `marketplace_offering_estimated_cost_policies_update` PUT `/api/marketplace-offering-estimated-cost-policies/{uuid}/` (path: uuid | request body)
- `marketplace_offering_estimated_cost_policies_partial_update` PATCH `/api/marketplace-offering-estimated-cost-policies/{uuid}/` (path: uuid | request body)
- `marketplace_offering_estimated_cost_policies_destroy` DELETE `/api/marketplace-offering-estimated-cost-policies/{uuid}/` (path: uuid)

## marketplace-offering-files
Module: `waldur_api_client.api.marketplace_offering_files`

- `marketplace_offering_files_list` GET `/api/marketplace-offering-files/` (6 query params)
- `marketplace_offering_files_count` HEAD `/api/marketplace-offering-files/` — Get number of items in the collection matching the request parameters (5 query params)
- `marketplace_offering_files_create` POST `/api/marketplace-offering-files/` (request body)
- `marketplace_offering_files_retrieve` GET `/api/marketplace-offering-files/{uuid}/` (path: uuid | 1 query param)
- `marketplace_offering_files_destroy` DELETE `/api/marketplace-offering-files/{uuid}/` (path: uuid)

## marketplace-offering-permissions
Module: `waldur_api_client.api.marketplace_offering_permissions`

- `marketplace_offering_permissions_list` GET `/api/marketplace-offering-permissions/` (16 query params)
- `marketplace_offering_permissions_count` HEAD `/api/marketplace-offering-permissions/` — Get number of items in the collection matching the request parameters (16 query params)
- `marketplace_offering_permissions_retrieve` GET `/api/marketplace-offering-permissions/{id}/` (path: id)

## marketplace-offering-permissions-log
Module: `waldur_api_client.api.marketplace_offering_permissions_log`

- `marketplace_offering_permissions_log_list` GET `/api/marketplace-offering-permissions-log/` (16 query params)
- `marketplace_offering_permissions_log_count` HEAD `/api/marketplace-offering-permissions-log/` — Get number of items in the collection matching the request parameters (16 query params)
- `marketplace_offering_permissions_log_retrieve` GET `/api/marketplace-offering-permissions-log/{id}/` (path: id)

## marketplace-offering-referrals
Module: `waldur_api_client.api.marketplace_offering_referrals`

- `marketplace_offering_referrals_list` GET `/api/marketplace-offering-referrals/` — List Datacite referrals for offerings (1 query param)
- `marketplace_offering_referrals_count` HEAD `/api/marketplace-offering-referrals/` — List Datacite referrals for offerings (1 query param)
- `marketplace_offering_referrals_retrieve` GET `/api/marketplace-offering-referrals/{uuid}/` — Retrieve a specific Datacite referral (path: uuid)

## marketplace-offering-terms-of-service
Module: `waldur_api_client.api.marketplace_offering_terms_of_service`

- `marketplace_offering_terms_of_service_list` GET `/api/marketplace-offering-terms-of-service/` — List Terms of Service configurations (6 query params)
- `marketplace_offering_terms_of_service_count` HEAD `/api/marketplace-offering-terms-of-service/` — List Terms of Service configurations (6 query params)
- `marketplace_offering_terms_of_service_create` POST `/api/marketplace-offering-terms-of-service/` — Create a Terms of Service configuration (request body)
- `marketplace_offering_terms_of_service_retrieve` GET `/api/marketplace-offering-terms-of-service/{uuid}/` — Retrieve a Terms of Service configuration (path: uuid)
- `marketplace_offering_terms_of_service_update` PUT `/api/marketplace-offering-terms-of-service/{uuid}/` — Update a Terms of Service configuration (path: uuid | request body)
- `marketplace_offering_terms_of_service_partial_update` PATCH `/api/marketplace-offering-terms-of-service/{uuid}/` — Partially update a Terms of Service configuration (path: uuid | request body)
- `marketplace_offering_terms_of_service_destroy` DELETE `/api/marketplace-offering-terms-of-service/{uuid}/` — Delete a Terms of Service configuration (path: uuid)

## marketplace-offering-usage-policies
Module: `waldur_api_client.api.marketplace_offering_usage_policies`

- `marketplace_offering_usage_policies_list` GET `/api/marketplace-offering-usage-policies/` (2 query params)
- `marketplace_offering_usage_policies_count` HEAD `/api/marketplace-offering-usage-policies/` — Get number of items in the collection matching the request parameters (2 query params)
- `marketplace_offering_usage_policies_create` POST `/api/marketplace-offering-usage-policies/` (request body)
- `marketplace_offering_usage_policies_actions_retrieve` GET `/api/marketplace-offering-usage-policies/actions/` (no params)
- `marketplace_offering_usage_policies_actions_count` HEAD `/api/marketplace-offering-usage-policies/actions/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_offering_usage_policies_retrieve` GET `/api/marketplace-offering-usage-policies/{uuid}/` (path: uuid)
- `marketplace_offering_usage_policies_update` PUT `/api/marketplace-offering-usage-policies/{uuid}/` (path: uuid | request body)
- `marketplace_offering_usage_policies_partial_update` PATCH `/api/marketplace-offering-usage-policies/{uuid}/` (path: uuid | request body)
- `marketplace_offering_usage_policies_destroy` DELETE `/api/marketplace-offering-usage-policies/{uuid}/` (path: uuid)

## marketplace-offering-user-checklist-completions
Module: `waldur_api_client.api.marketplace_offering_user_checklist_completions`

- `marketplace_offering_user_checklist_completions_list` GET `/api/marketplace-offering-user-checklist-completions/` — List checklist completions for offering users (6 query params)
- `marketplace_offering_user_checklist_completions_count` HEAD `/api/marketplace-offering-user-checklist-completions/` — List checklist completions for offering users (6 query params)
- `marketplace_offering_user_checklist_completions_retrieve` GET `/api/marketplace-offering-user-checklist-completions/{id}/` — Retrieve a checklist completion (path: id)

## marketplace-offering-user-roles
Module: `waldur_api_client.api.marketplace_offering_user_roles`

- `marketplace_offering_user_roles_list` GET `/api/marketplace-offering-user-roles/` (4 query params)
- `marketplace_offering_user_roles_count` HEAD `/api/marketplace-offering-user-roles/` — Get number of items in the collection matching the request parameters (4 query params)
- `marketplace_offering_user_roles_create` POST `/api/marketplace-offering-user-roles/` (request body)
- `marketplace_offering_user_roles_retrieve` GET `/api/marketplace-offering-user-roles/{uuid}/` (path: uuid)
- `marketplace_offering_user_roles_update` PUT `/api/marketplace-offering-user-roles/{uuid}/` (path: uuid | request body)
- `marketplace_offering_user_roles_partial_update` PATCH `/api/marketplace-offering-user-roles/{uuid}/` (path: uuid | request body)
- `marketplace_offering_user_roles_destroy` DELETE `/api/marketplace-offering-user-roles/{uuid}/` (path: uuid)

## marketplace-offering-users
Module: `waldur_api_client.api.marketplace_offering_users`

- `marketplace_offering_users_list` GET `/api/marketplace-offering-users/` — List offering users (16 query params)
- `marketplace_offering_users_count` HEAD `/api/marketplace-offering-users/` — List offering users (15 query params)
- `marketplace_offering_users_create` POST `/api/marketplace-offering-users/` — Create an offering user (request body)
- `marketplace_offering_users_checklist_template_retrieve` GET `/api/marketplace-offering-users/checklist-template/` — Get checklist template for creating new objects (1 query param)
- `marketplace_offering_users_checklist_template_count` HEAD `/api/marketplace-offering-users/checklist-template/` — Get number of items in the collection matching the request parameters (1 query param)
- `marketplace_offering_users_profile_field_warnings_retrieve` GET `/api/marketplace-offering-users/profile_field_warnings/` — Get profile field warnings (no params)
- `marketplace_offering_users_profile_field_warnings_count` HEAD `/api/marketplace-offering-users/profile_field_warnings/` — Get profile field warnings (no params)
- `marketplace_offering_users_retrieve` GET `/api/marketplace-offering-users/{uuid}/` — Retrieve an offering user (path: uuid | 1 query param)
- `marketplace_offering_users_update` PUT `/api/marketplace-offering-users/{uuid}/` (path: uuid | request body)
- `marketplace_offering_users_partial_update` PATCH `/api/marketplace-offering-users/{uuid}/` (path: uuid | request body)
- `marketplace_offering_users_destroy` DELETE `/api/marketplace-offering-users/{uuid}/` — Delete an offering user (path: uuid)
- `marketplace_offering_users_begin_creating` POST `/api/marketplace-offering-users/{uuid}/begin_creating/` — Begin creation process (path: uuid)
- `marketplace_offering_users_checklist_retrieve` GET `/api/marketplace-offering-users/{uuid}/checklist/` — Get checklist with questions and existing answers (path: uuid | 1 query param)
- `marketplace_offering_users_checklist_review_retrieve` GET `/api/marketplace-offering-users/{uuid}/checklist_review/` — Get checklist with questions and existing answers including review logic (reviewers only) (path: uuid)
- `marketplace_offering_users_completion_review_status_retrieve` GET `/api/marketplace-offering-users/{uuid}/completion_review_status/` — Get checklist completion status with review triggers (reviewers only) (path: uuid)
- `marketplace_offering_users_completion_status_retrieve` GET `/api/marketplace-offering-users/{uuid}/completion_status/` — Get checklist completion status (path: uuid)
- `marketplace_offering_users_request_deletion` POST `/api/marketplace-offering-users/{uuid}/request_deletion/` — Request deletion of an offering user (path: uuid)
- `marketplace_offering_users_set_deleted` POST `/api/marketplace-offering-users/{uuid}/set_deleted/` — Set state to Deleted (path: uuid)
- `marketplace_offering_users_set_deleting` POST `/api/marketplace-offering-users/{uuid}/set_deleting/` — Begin deletion process (path: uuid)
- `marketplace_offering_users_set_error_creating` POST `/api/marketplace-offering-users/{uuid}/set_error_creating/` — Set state to Error Creating (path: uuid)
- `marketplace_offering_users_set_error_deleting` POST `/api/marketplace-offering-users/{uuid}/set_error_deleting/` — Set state to Error Deleting (path: uuid)
- `marketplace_offering_users_set_ok` POST `/api/marketplace-offering-users/{uuid}/set_ok/` — Set state to OK (path: uuid)
- `marketplace_offering_users_set_pending_account_linking` POST `/api/marketplace-offering-users/{uuid}/set_pending_account_linking/` — Set state to Pending Account Linking (path: uuid | request body)
- `marketplace_offering_users_set_pending_additional_validation` POST `/api/marketplace-offering-users/{uuid}/set_pending_additional_validation/` — Set state to Pending Additional Validation (path: uuid | request body)
- `marketplace_offering_users_set_validation_complete` POST `/api/marketplace-offering-users/{uuid}/set_validation_complete/` — Set state to Validation Complete (path: uuid)
- `marketplace_offering_users_submit_answers` POST `/api/marketplace-offering-users/{uuid}/submit_answers/` — Submit checklist answers (path: uuid | request body)
- `marketplace_offering_users_update_comments_partial_update` PATCH `/api/marketplace-offering-users/{uuid}/update_comments/` — Update service provider comments (path: uuid | request body)
- `marketplace_offering_users_update_restricted` POST `/api/marketplace-offering-users/{uuid}/update_restricted/` — Update restriction status (path: uuid | request body)

## marketplace-orders
Module: `waldur_api_client.api.marketplace_orders`

- `marketplace_orders_list` GET `/api/marketplace-orders/` — List orders (22 query params)
- `marketplace_orders_count` HEAD `/api/marketplace-orders/` — List orders (21 query params)
- `marketplace_orders_create` POST `/api/marketplace-orders/` — Create an order (request body)
- `marketplace_orders_retrieve` GET `/api/marketplace-orders/{uuid}/` — Retrieve an order (path: uuid | 1 query param)
- `marketplace_orders_update` PUT `/api/marketplace-orders/{uuid}/` (path: uuid | request body)
- `marketplace_orders_partial_update` PATCH `/api/marketplace-orders/{uuid}/` (path: uuid | request body)
- `marketplace_orders_destroy` DELETE `/api/marketplace-orders/{uuid}/` — Delete a pending order (path: uuid)
- `marketplace_orders_approve_by_consumer` POST `/api/marketplace-orders/{uuid}/approve_by_consumer/` — Approve an order (consumer) (path: uuid)
- `marketplace_orders_approve_by_provider` POST `/api/marketplace-orders/{uuid}/approve_by_provider/` — Approve an order (provider) (path: uuid | request body)
- `marketplace_orders_cancel` POST `/api/marketplace-orders/{uuid}/cancel/` — Cancel an order (path: uuid)
- `marketplace_orders_delete_attachment` POST `/api/marketplace-orders/{uuid}/delete_attachment/` — Delete order attachment (path: uuid)
- `marketplace_orders_offering_retrieve` GET `/api/marketplace-orders/{uuid}/offering/` — Get offering details (path: uuid)
- `marketplace_orders_reject_by_consumer` POST `/api/marketplace-orders/{uuid}/reject_by_consumer/` — Reject an order (consumer) (path: uuid | request body)
- `marketplace_orders_reject_by_provider` POST `/api/marketplace-orders/{uuid}/reject_by_provider/` — Reject an order (provider) (path: uuid | request body)
- `marketplace_orders_set_backend_id` POST `/api/marketplace-orders/{uuid}/set_backend_id/` — Set order backend ID (path: uuid | request body)
- `marketplace_orders_set_consumer_info` POST `/api/marketplace-orders/{uuid}/set_consumer_info/` — Set consumer info on order (path: uuid | request body)
- `marketplace_orders_set_provider_info` POST `/api/marketplace-orders/{uuid}/set_provider_info/` — Set provider info on order (path: uuid | request body)
- `marketplace_orders_set_state_done` POST `/api/marketplace-orders/{uuid}/set_state_done/` — Set order state to done (agent) (path: uuid)
- `marketplace_orders_set_state_erred` POST `/api/marketplace-orders/{uuid}/set_state_erred/` — Set order state to erred (agent) (path: uuid | request body)
- `marketplace_orders_set_state_executing` POST `/api/marketplace-orders/{uuid}/set_state_executing/` — Set order state to executing (agent) (path: uuid)
- `marketplace_orders_unlink` POST `/api/marketplace-orders/{uuid}/unlink/` — Unlink an order (staff only) (path: uuid)
- `marketplace_orders_update_attachment` POST `/api/marketplace-orders/{uuid}/update_attachment/` — Update order attachment (path: uuid | request body)

## marketplace-plan-components
Module: `waldur_api_client.api.marketplace_plan_components`

- `marketplace_plan_components_list` GET `/api/marketplace-plan-components/` — List plan components (4 query params)
- `marketplace_plan_components_count` HEAD `/api/marketplace-plan-components/` — List plan components (4 query params)
- `marketplace_plan_components_retrieve` GET `/api/marketplace-plan-components/{id}/` — Retrieve a plan component (path: id)

## marketplace-plans
Module: `waldur_api_client.api.marketplace_plans`

- `marketplace_plans_list` GET `/api/marketplace-plans/` — List provider plans (4 query params)
- `marketplace_plans_count` HEAD `/api/marketplace-plans/` — List provider plans (4 query params)
- `marketplace_plans_create` POST `/api/marketplace-plans/` — Create a provider plan (request body)
- `marketplace_plans_usage_stats_list` GET `/api/marketplace-plans/usage_stats/` — Get plan usage statistics (6 query params)
- `marketplace_plans_usage_stats_count` HEAD `/api/marketplace-plans/usage_stats/` — Get plan usage statistics (6 query params)
- `marketplace_plans_retrieve` GET `/api/marketplace-plans/{uuid}/` — Retrieve a provider plan (path: uuid)
- `marketplace_plans_update` PUT `/api/marketplace-plans/{uuid}/` — Update a provider plan (path: uuid | request body)
- `marketplace_plans_partial_update` PATCH `/api/marketplace-plans/{uuid}/` — Partially update a provider plan (path: uuid | request body)
- `marketplace_plans_destroy` DELETE `/api/marketplace-plans/{uuid}/` — Delete a provider plan (path: uuid)
- `marketplace_plans_archive` POST `/api/marketplace-plans/{uuid}/archive/` — Archive a plan (path: uuid)
- `marketplace_plans_delete_organization_groups` POST `/api/marketplace-plans/{uuid}/delete_organization_groups/` — Remove all organization groups from a plan (path: uuid)
- `marketplace_plans_history_list` GET `/api/marketplace-plans/{uuid}/history/` — Get version history (path: uuid | 6 query params)
- `marketplace_plans_history_at_retrieve` GET `/api/marketplace-plans/{uuid}/history/at/` — Get object state at a specific timestamp (path: uuid | 1 query param)
- `marketplace_plans_update_discounts` POST `/api/marketplace-plans/{uuid}/update_discounts/` — Update plan component discounts (path: uuid | request body)
- `marketplace_plans_update_organization_groups` POST `/api/marketplace-plans/{uuid}/update_organization_groups/` — Update organization groups for a plan (path: uuid | request body)
- `marketplace_plans_update_prices` POST `/api/marketplace-plans/{uuid}/update_prices/` — Update plan component prices (path: uuid | request body)
- `marketplace_plans_update_quotas` POST `/api/marketplace-plans/{uuid}/update_quotas/` — Update plan component quotas (path: uuid | request body)

## marketplace-plugins
Module: `waldur_api_client.api.marketplace_plugins`

- `marketplace_plugins_list` GET `/api/marketplace-plugins/` — List available marketplace plugins and their components (no params)

## marketplace-project-estimated-cost-policies
Module: `waldur_api_client.api.marketplace_project_estimated_cost_policies`

- `marketplace_project_estimated_cost_policies_list` GET `/api/marketplace-project-estimated-cost-policies/` (6 query params)
- `marketplace_project_estimated_cost_policies_count` HEAD `/api/marketplace-project-estimated-cost-policies/` — Get number of items in the collection matching the request parameters (6 query params)
- `marketplace_project_estimated_cost_policies_create` POST `/api/marketplace-project-estimated-cost-policies/` (request body)
- `marketplace_project_estimated_cost_policies_actions_retrieve` GET `/api/marketplace-project-estimated-cost-policies/actions/` (no params)
- `marketplace_project_estimated_cost_policies_actions_count` HEAD `/api/marketplace-project-estimated-cost-policies/actions/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_project_estimated_cost_policies_retrieve` GET `/api/marketplace-project-estimated-cost-policies/{uuid}/` (path: uuid)
- `marketplace_project_estimated_cost_policies_update` PUT `/api/marketplace-project-estimated-cost-policies/{uuid}/` (path: uuid | request body)
- `marketplace_project_estimated_cost_policies_partial_update` PATCH `/api/marketplace-project-estimated-cost-policies/{uuid}/` (path: uuid | request body)
- `marketplace_project_estimated_cost_policies_destroy` DELETE `/api/marketplace-project-estimated-cost-policies/{uuid}/` (path: uuid)

## marketplace-project-service-accounts
Module: `waldur_api_client.api.marketplace_project_service_accounts`

- `marketplace_project_service_accounts_list` GET `/api/marketplace-project-service-accounts/` — List service accounts (5 query params)
- `marketplace_project_service_accounts_count` HEAD `/api/marketplace-project-service-accounts/` — List service accounts (5 query params)
- `marketplace_project_service_accounts_create` POST `/api/marketplace-project-service-accounts/` — Create a project service account (request body)
- `marketplace_project_service_accounts_retrieve` GET `/api/marketplace-project-service-accounts/{uuid}/` — Retrieve a service account (path: uuid)
- `marketplace_project_service_accounts_update` PUT `/api/marketplace-project-service-accounts/{uuid}/` — Update a service account (path: uuid | request body)
- `marketplace_project_service_accounts_partial_update` PATCH `/api/marketplace-project-service-accounts/{uuid}/` — Partially update a service account (path: uuid | request body)
- `marketplace_project_service_accounts_destroy` DELETE `/api/marketplace-project-service-accounts/{uuid}/` — Close a project service account (path: uuid)
- `marketplace_project_service_accounts_rotate_api_key` POST `/api/marketplace-project-service-accounts/{uuid}/rotate_api_key/` — Rotate API key for a project service account (path: uuid)

## marketplace-project-update-requests
Module: `waldur_api_client.api.marketplace_project_update_requests`

- `marketplace_project_update_requests_list` GET `/api/marketplace-project-update-requests/` (5 query params)
- `marketplace_project_update_requests_count` HEAD `/api/marketplace-project-update-requests/` — Get number of items in the collection matching the request parameters (5 query params)
- `marketplace_project_update_requests_retrieve` GET `/api/marketplace-project-update-requests/{uuid}/` (path: uuid)
- `marketplace_project_update_requests_approve` POST `/api/marketplace-project-update-requests/{uuid}/approve/` — Approve project update request (path: uuid | request body)
- `marketplace_project_update_requests_reject` POST `/api/marketplace-project-update-requests/{uuid}/reject/` — Reject project update request (path: uuid | request body)

## marketplace-provider-offerings
Module: `waldur_api_client.api.marketplace_provider_offerings`

- `marketplace_provider_offerings_list` GET `/api/marketplace-provider-offerings/` — List provider offerings (37 query params)
- `marketplace_provider_offerings_count` HEAD `/api/marketplace-provider-offerings/` — List provider offerings (36 query params)
- `marketplace_provider_offerings_create` POST `/api/marketplace-provider-offerings/` — Create a provider offering (request body)
- `marketplace_provider_offerings_groups_list` GET `/api/marketplace-provider-offerings/groups/` — List offerings grouped by provider (36 query params)
- `marketplace_provider_offerings_groups_count` HEAD `/api/marketplace-provider-offerings/groups/` — List offerings grouped by provider (36 query params)
- `marketplace_provider_offerings_import_offering` POST `/api/marketplace-provider-offerings/import_offering/` — Import offering data (request body)
- `marketplace_provider_offerings_retrieve` GET `/api/marketplace-provider-offerings/{uuid}/` — Retrieve a provider offering (path: uuid | 1 query param)
- `marketplace_provider_offerings_destroy` DELETE `/api/marketplace-provider-offerings/{uuid}/` — Delete a provider offering (path: uuid)
- `marketplace_provider_offerings_activate` POST `/api/marketplace-provider-offerings/{uuid}/activate/` — Activate an offering (path: uuid)
- `marketplace_provider_offerings_add_endpoint` POST `/api/marketplace-provider-offerings/{uuid}/add_endpoint/` — Add an access endpoint to an offering (path: uuid | request body)
- `marketplace_provider_offerings_add_partition` POST `/api/marketplace-provider-offerings/{uuid}/add_partition/` — Add a partition to an offering (path: uuid | request body)
- `marketplace_provider_offerings_add_software_catalog` POST `/api/marketplace-provider-offerings/{uuid}/add_software_catalog/` — Add a software catalog to an offering (path: uuid | request body)
- `marketplace_provider_offerings_add_user` POST `/api/marketplace-provider-offerings/{uuid}/add_user/` — Grant a role to a user (path: uuid | request body)
- `marketplace_provider_offerings_archive` POST `/api/marketplace-provider-offerings/{uuid}/archive/` — Archive an offering (path: uuid)
- `marketplace_provider_offerings_check_unique_backend_id` POST `/api/marketplace-provider-offerings/{uuid}/check_unique_backend_id/` — Check if backend_id is unique (path: uuid | request body)
- `marketplace_provider_offerings_component_stats_list` GET `/api/marketplace-provider-offerings/{uuid}/component_stats/` — Get statistics for offering components (path: uuid | 38 query params)
- `marketplace_provider_offerings_costs_list` GET `/api/marketplace-provider-offerings/{uuid}/costs/` — Get costs for an offering (path: uuid | 39 query params)
- `marketplace_provider_offerings_create_offering_component` POST `/api/marketplace-provider-offerings/{uuid}/create_offering_component/` — Create an offering component (path: uuid | request body)
- `marketplace_provider_offerings_customers_list` GET `/api/marketplace-provider-offerings/{uuid}/customers/` — Get customers for an offering (path: uuid | 37 query params)
- `marketplace_provider_offerings_delete_user_attribute_config_destroy` DELETE `/api/marketplace-provider-offerings/{uuid}/delete-user-attribute-config/` — Delete user attribute config (path: uuid)
- `marketplace_provider_offerings_delete_endpoint` POST `/api/marketplace-provider-offerings/{uuid}/delete_endpoint/` — Delete an access endpoint from an offering (path: uuid | request body)
- `marketplace_provider_offerings_delete_image` POST `/api/marketplace-provider-offerings/{uuid}/delete_image/` — Delete offering image (path: uuid)
- `marketplace_provider_offerings_delete_organization_groups` POST `/api/marketplace-provider-offerings/{uuid}/delete_organization_groups/` — Delete organization groups for offering (path: uuid)
- `marketplace_provider_offerings_delete_tags` POST `/api/marketplace-provider-offerings/{uuid}/delete_tags/` — Delete tags for offering (path: uuid)
- `marketplace_provider_offerings_delete_thumbnail` POST `/api/marketplace-provider-offerings/{uuid}/delete_thumbnail/` — Delete offering thumbnail (path: uuid)
- `marketplace_provider_offerings_delete_user` POST `/api/marketplace-provider-offerings/{uuid}/delete_user/` — Revoke a role from a user (path: uuid | request body)
- `marketplace_provider_offerings_draft` POST `/api/marketplace-provider-offerings/{uuid}/draft/` — Move an offering to draft (path: uuid)
- `marketplace_provider_offerings_export_offering` POST `/api/marketplace-provider-offerings/{uuid}/export_offering/` — Export offering data (path: uuid | request body)
- `marketplace_provider_offerings_glauth_users_config_retrieve` GET `/api/marketplace-provider-offerings/{uuid}/glauth_users_config/` — Get GLauth user configuration (path: uuid)
- `marketplace_provider_offerings_history_list` GET `/api/marketplace-provider-offerings/{uuid}/history/` — Get version history (path: uuid | 38 query params)
- `marketplace_provider_offerings_history_at_retrieve` GET `/api/marketplace-provider-offerings/{uuid}/history/at/` — Get object state at a specific timestamp (path: uuid | 1 query param)
- `marketplace_provider_offerings_import_resource` POST `/api/marketplace-provider-offerings/{uuid}/import_resource/` — Import a resource (path: uuid | request body)
- `marketplace_provider_offerings_importable_resources_list` GET `/api/marketplace-provider-offerings/{uuid}/importable_resources/` — List importable resources (path: uuid)
- `marketplace_provider_offerings_list_course_accounts_list` GET `/api/marketplace-provider-offerings/{uuid}/list_course_accounts/` — List course accounts for an offering (path: uuid | 36 query params)
- `marketplace_provider_offerings_list_customer_projects_list` GET `/api/marketplace-provider-offerings/{uuid}/list_customer_projects/` — List customer projects for an offering (path: uuid | 1 query param)
- `marketplace_provider_offerings_list_customer_service_accounts_list` GET `/api/marketplace-provider-offerings/{uuid}/list_customer_service_accounts/` — List customer service accounts for an offering (path: uuid | 36 query params)
- `marketplace_provider_offerings_list_customer_users_list` GET `/api/marketplace-provider-offerings/{uuid}/list_customer_users/` — List customer users for an offering (path: uuid | 1 query param)
- `marketplace_provider_offerings_list_project_service_accounts_list` GET `/api/marketplace-provider-offerings/{uuid}/list_project_service_accounts/` — List project service accounts for an offering (path: uuid | 36 query params)
- `marketplace_provider_offerings_list_users_list` GET `/api/marketplace-provider-offerings/{uuid}/list_users/` — List users and their roles in a scope (path: uuid | 10 query params)
- `marketplace_provider_offerings_make_available` POST `/api/marketplace-provider-offerings/{uuid}/make_available/` — Mark an offering as available (path: uuid)
- `marketplace_provider_offerings_make_unavailable` POST `/api/marketplace-provider-offerings/{uuid}/make_unavailable/` — Mark an offering as unavailable (path: uuid)
- `marketplace_provider_offerings_move_offering` POST `/api/marketplace-provider-offerings/{uuid}/move_offering/` — Move an offering (path: uuid | request body)
- `marketplace_provider_offerings_orders_list` GET `/api/marketplace-provider-offerings/{uuid}/orders/` — List orders for an offering (path: uuid | 1 query param)
- `marketplace_provider_offerings_orders_retrieve` GET `/api/marketplace-provider-offerings/{uuid}/orders/{order_uuid}/` — Retrieve a specific order for an offering (path: order_uuid, uuid)
- `marketplace_provider_offerings_pause` POST `/api/marketplace-provider-offerings/{uuid}/pause/` — Pause an offering (path: uuid | request body)
- `marketplace_provider_offerings_refresh_offering_usernames` POST `/api/marketplace-provider-offerings/{uuid}/refresh_offering_usernames/` — Refresh offering user usernames (path: uuid)
- `marketplace_provider_offerings_remove_offering_component` POST `/api/marketplace-provider-offerings/{uuid}/remove_offering_component/` — Remove an offering component (path: uuid | request body)
- `marketplace_provider_offerings_remove_partition` POST `/api/marketplace-provider-offerings/{uuid}/remove_partition/` — Remove a partition from an offering (path: uuid | request body)
- `marketplace_provider_offerings_remove_software_catalog` POST `/api/marketplace-provider-offerings/{uuid}/remove_software_catalog/` — Remove a software catalog from an offering (path: uuid | request body)
- `marketplace_provider_offerings_set_backend_metadata` POST `/api/marketplace-provider-offerings/{uuid}/set_backend_metadata/` — Set offering backend metadata (path: uuid | request body)
- `marketplace_provider_offerings_stats_retrieve` GET `/api/marketplace-provider-offerings/{uuid}/stats/` — Get offering statistics (path: uuid)
- `marketplace_provider_offerings_sync` POST `/api/marketplace-provider-offerings/{uuid}/sync/` — Synchronize offering service settings (path: uuid)
- `marketplace_provider_offerings_tos_stats_retrieve` GET `/api/marketplace-provider-offerings/{uuid}/tos_stats/` — Get Terms of Service consent statistics (path: uuid)
- `marketplace_provider_offerings_unpause` POST `/api/marketplace-provider-offerings/{uuid}/unpause/` — Unpause an offering (path: uuid)
- `marketplace_provider_offerings_update_user_attribute_config` POST `/api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/` — Update user attribute config (path: uuid | request body)
- `marketplace_provider_offerings_update_user_attribute_config_update` PUT `/api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/` — Update user attribute config (path: uuid | request body)
- `marketplace_provider_offerings_update_user_attribute_config_partial_update` PATCH `/api/marketplace-provider-offerings/{uuid}/update-user-attribute-config/` — Update user attribute config (path: uuid | request body)
- `marketplace_provider_offerings_update_attributes` POST `/api/marketplace-provider-offerings/{uuid}/update_attributes/` — Update offering attributes (path: uuid | request body)
- `marketplace_provider_offerings_update_backend_id_rules` POST `/api/marketplace-provider-offerings/{uuid}/update_backend_id_rules/` — Update offering backend_id rules (path: uuid | request body)
- `marketplace_provider_offerings_update_compliance_checklist` POST `/api/marketplace-provider-offerings/{uuid}/update_compliance_checklist/` — Update offering compliance checklist (path: uuid | request body)
- `marketplace_provider_offerings_update_description` POST `/api/marketplace-provider-offerings/{uuid}/update_description/` — Update offering category (path: uuid | request body)
- `marketplace_provider_offerings_update_image` POST `/api/marketplace-provider-offerings/{uuid}/update_image/` — Update offering image (path: uuid | request body)
- `marketplace_provider_offerings_update_integration` POST `/api/marketplace-provider-offerings/{uuid}/update_integration/` — Update offering integration settings (path: uuid | request body)
- `marketplace_provider_offerings_update_location` POST `/api/marketplace-provider-offerings/{uuid}/update_location/` — Update offering location (path: uuid | request body)
- `marketplace_provider_offerings_update_offering_component` POST `/api/marketplace-provider-offerings/{uuid}/update_offering_component/` — Update an offering component (path: uuid | request body)
- `marketplace_provider_offerings_update_options` POST `/api/marketplace-provider-offerings/{uuid}/update_options/` — Update offering options (path: uuid | request body)
- `marketplace_provider_offerings_update_organization_groups` POST `/api/marketplace-provider-offerings/{uuid}/update_organization_groups/` — Update organization groups for offering (path: uuid | request body)
- `marketplace_provider_offerings_update_overview` POST `/api/marketplace-provider-offerings/{uuid}/update_overview/` — Update offering overview (path: uuid | request body)
- `marketplace_provider_offerings_update_partition_partial_update` PATCH `/api/marketplace-provider-offerings/{uuid}/update_partition/` — Update a partition of an offering (path: uuid | request body)
- `marketplace_provider_offerings_update_resource_options` POST `/api/marketplace-provider-offerings/{uuid}/update_resource_options/` — Update offering resource options (path: uuid | request body)
- `marketplace_provider_offerings_update_software_catalog_partial_update` PATCH `/api/marketplace-provider-offerings/{uuid}/update_software_catalog/` — Update software catalog configuration (path: uuid | request body)
- `marketplace_provider_offerings_update_tags` POST `/api/marketplace-provider-offerings/{uuid}/update_tags/` — Update tags for offering (path: uuid | request body)
- `marketplace_provider_offerings_update_thumbnail` POST `/api/marketplace-provider-offerings/{uuid}/update_thumbnail/` — Update offering thumbnail (path: uuid | request body)
- `marketplace_provider_offerings_update_user` POST `/api/marketplace-provider-offerings/{uuid}/update_user/` — Update a user's role expiration (path: uuid | request body)
- `marketplace_provider_offerings_user_attribute_config_retrieve` GET `/api/marketplace-provider-offerings/{uuid}/user-attribute-config/` — Get user attribute config (path: uuid)
- `marketplace_provider_offerings_user_has_resource_access_retrieve` GET `/api/marketplace-provider-offerings/{uuid}/user_has_resource_access/` — Check user access to offering resources (path: uuid | 2 query params)

## marketplace-provider-resources
Module: `waldur_api_client.api.marketplace_provider_resources`

- `marketplace_provider_resources_list` GET `/api/marketplace-provider-resources/` — List provider resources (40 query params)
- `marketplace_provider_resources_count` HEAD `/api/marketplace-provider-resources/` — List provider resources (39 query params)
- `marketplace_provider_resources_retrieve` GET `/api/marketplace-provider-resources/{uuid}/` — Retrieve a provider resource (path: uuid | 1 query param)
- `marketplace_provider_resources_update` PUT `/api/marketplace-provider-resources/{uuid}/` — Update a provider resource (path: uuid | request body)
- `marketplace_provider_resources_partial_update` PATCH `/api/marketplace-provider-resources/{uuid}/` — Partially update a provider resource (path: uuid | request body)
- `marketplace_provider_resources_details_retrieve` GET `/api/marketplace-provider-resources/{uuid}/details/` — Get resource details (path: uuid)
- `marketplace_provider_resources_glauth_users_config_retrieve` GET `/api/marketplace-provider-resources/{uuid}/glauth_users_config/` — Get GLauth user configuration for a resource (path: uuid)
- `marketplace_provider_resources_history_list` GET `/api/marketplace-provider-resources/{uuid}/history/` — Get version history (path: uuid | 41 query params)
- `marketplace_provider_resources_history_at_retrieve` GET `/api/marketplace-provider-resources/{uuid}/history/at/` — Get object state at a specific timestamp (path: uuid | 1 query param)
- `marketplace_provider_resources_move_resource` POST `/api/marketplace-provider-resources/{uuid}/move_resource/` — Move a resource to another project (path: uuid | request body)
- `marketplace_provider_resources_offering_retrieve` GET `/api/marketplace-provider-resources/{uuid}/offering/` — Get offering details (path: uuid)
- `marketplace_provider_resources_offering_for_subresources_list` GET `/api/marketplace-provider-resources/{uuid}/offering_for_subresources/` — List offerings for sub-resources (path: uuid)
- `marketplace_provider_resources_plan_periods_list` GET `/api/marketplace-provider-resources/{uuid}/plan_periods/` — List resource plan periods (path: uuid)
- `marketplace_provider_resources_pull` POST `/api/marketplace-provider-resources/{uuid}/pull/` — Pull resource data (path: uuid)
- `marketplace_provider_resources_refresh_last_sync` POST `/api/marketplace-provider-resources/{uuid}/refresh_last_sync/` — Refresh last sync time (path: uuid)
- `marketplace_provider_resources_restore` POST `/api/marketplace-provider-resources/{uuid}/restore/` (path: uuid | request body)
- `marketplace_provider_resources_set_as_erred` POST `/api/marketplace-provider-resources/{uuid}/set_as_erred/` — Set resource state to erred (path: uuid | request body)
- `marketplace_provider_resources_set_as_ok` POST `/api/marketplace-provider-resources/{uuid}/set_as_ok/` — Set resource state to OK (path: uuid)
- `marketplace_provider_resources_set_backend_id` POST `/api/marketplace-provider-resources/{uuid}/set_backend_id/` — Set resource backend ID (path: uuid | request body)
- `marketplace_provider_resources_set_backend_metadata` POST `/api/marketplace-provider-resources/{uuid}/set_backend_metadata/` — Set resource backend metadata (path: uuid | request body)
- `marketplace_provider_resources_set_downscaled` POST `/api/marketplace-provider-resources/{uuid}/set_downscaled/` — Set downscaled flag for resource (path: uuid | request body)
- `marketplace_provider_resources_set_end_date_by_provider` POST `/api/marketplace-provider-resources/{uuid}/set_end_date_by_provider/` — Set end date by provider (path: uuid | request body)
- `marketplace_provider_resources_set_end_date_by_staff` POST `/api/marketplace-provider-resources/{uuid}/set_end_date_by_staff/` — Set end date of the resource by staff (path: uuid | request body)
- `marketplace_provider_resources_set_limits` POST `/api/marketplace-provider-resources/{uuid}/set_limits/` — Set resource limits (path: uuid | request body)
- `marketplace_provider_resources_set_paused` POST `/api/marketplace-provider-resources/{uuid}/set_paused/` — Set paused flag for resource (path: uuid | request body)
- `marketplace_provider_resources_set_restrict_member_access` POST `/api/marketplace-provider-resources/{uuid}/set_restrict_member_access/` — Set restrict member access flag (path: uuid | request body)
- `marketplace_provider_resources_set_slug` POST `/api/marketplace-provider-resources/{uuid}/set_slug/` — Set resource slug (path: uuid | request body)
- `marketplace_provider_resources_set_state_ok` POST `/api/marketplace-provider-resources/{uuid}/set_state_ok/` — Set resource state to OK (path: uuid)
- `marketplace_provider_resources_submit_report` POST `/api/marketplace-provider-resources/{uuid}/submit_report/` — Submit a report for a resource (path: uuid | request body)
- `marketplace_provider_resources_team_list` GET `/api/marketplace-provider-resources/{uuid}/team/` — Get resource team (path: uuid)
- `marketplace_provider_resources_terminate` POST `/api/marketplace-provider-resources/{uuid}/terminate/` — Terminate a resource (path: uuid | request body)
- `marketplace_provider_resources_unlink` POST `/api/marketplace-provider-resources/{uuid}/unlink/` — Unlink a resource (staff only) (path: uuid)
- `marketplace_provider_resources_update_options` POST `/api/marketplace-provider-resources/{uuid}/update_options/` — Update resource options (path: uuid | request body)
- `marketplace_provider_resources_update_options_direct` POST `/api/marketplace-provider-resources/{uuid}/update_options_direct/` — Update resource options directly (path: uuid | request body)

## marketplace-public-api
Module: `waldur_api_client.api.marketplace_public_api`

- `marketplace_public_api_check_signature` POST `/api/marketplace-public-api/check_signature/` — Check service provider signature (request body)
- `marketplace_public_api_set_usage` POST `/api/marketplace-public-api/set_usage/` — Set component usage with signature (request body)

## marketplace-public-offerings
Module: `waldur_api_client.api.marketplace_public_offerings`

- `marketplace_public_offerings_list` GET `/api/marketplace-public-offerings/` — List public offerings (37 query params)
- `marketplace_public_offerings_count` HEAD `/api/marketplace-public-offerings/` — List public offerings (36 query params)
- `marketplace_public_offerings_retrieve` GET `/api/marketplace-public-offerings/{uuid}/` — Retrieve a public offering (path: uuid | 1 query param)
- `marketplace_public_offerings_plans_list` GET `/api/marketplace-public-offerings/{uuid}/plans/` — List plans for an offering (path: uuid)
- `marketplace_public_offerings_plans_retrieve` GET `/api/marketplace-public-offerings/{uuid}/plans/{plan_uuid}/` — Retrieve a specific plan for an offering (path: plan_uuid, uuid)

## marketplace-related-customers
Module: `waldur_api_client.api.marketplace_related_customers`

- `marketplace_related_customers_list` GET `/api/marketplace-related-customers/{customer_uuid}/` (path: customer_uuid | 2 query params)

## marketplace-remote-synchronisations
Module: `waldur_api_client.api.marketplace_remote_synchronisations`

- `marketplace_remote_synchronisations_list` GET `/api/marketplace-remote-synchronisations/` (no params)
- `marketplace_remote_synchronisations_count` HEAD `/api/marketplace-remote-synchronisations/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_remote_synchronisations_create` POST `/api/marketplace-remote-synchronisations/` (request body)
- `marketplace_remote_synchronisations_retrieve` GET `/api/marketplace-remote-synchronisations/{uuid}/` (path: uuid)
- `marketplace_remote_synchronisations_update` PUT `/api/marketplace-remote-synchronisations/{uuid}/` (path: uuid | request body)
- `marketplace_remote_synchronisations_partial_update` PATCH `/api/marketplace-remote-synchronisations/{uuid}/` (path: uuid | request body)
- `marketplace_remote_synchronisations_destroy` DELETE `/api/marketplace-remote-synchronisations/{uuid}/` (path: uuid)
- `marketplace_remote_synchronisations_run_synchronisation` POST `/api/marketplace-remote-synchronisations/{uuid}/run_synchronisation/` (path: uuid)

## marketplace-resource-offerings
Module: `waldur_api_client.api.marketplace_resource_offerings`

- `marketplace_resource_offerings_list` GET `/api/marketplace-resource-offerings/{category_uuid}/` (path: category_uuid | 2 query params)

## marketplace-resource-users
Module: `waldur_api_client.api.marketplace_resource_users`

- `marketplace_resource_users_list` GET `/api/marketplace-resource-users/` — List resource users (5 query params)
- `marketplace_resource_users_count` HEAD `/api/marketplace-resource-users/` — List resource users (5 query params)
- `marketplace_resource_users_create` POST `/api/marketplace-resource-users/` — Link a user to a resource (request body)
- `marketplace_resource_users_retrieve` GET `/api/marketplace-resource-users/{uuid}/` — Retrieve a resource-user link (path: uuid)
- `marketplace_resource_users_destroy` DELETE `/api/marketplace-resource-users/{uuid}/` — Unlink a user from a resource (path: uuid)

## marketplace-resources
Module: `waldur_api_client.api.marketplace_resources`

- `marketplace_resources_list` GET `/api/marketplace-resources/` — List consumer resources (40 query params)
- `marketplace_resources_count` HEAD `/api/marketplace-resources/` — List consumer resources (39 query params)
- `marketplace_resources_suggest_name` POST `/api/marketplace-resources/suggest_name/` — Suggest a resource name (request body)
- `marketplace_resources_retrieve` GET `/api/marketplace-resources/{uuid}/` — Retrieve a consumer resource (path: uuid | 1 query param)
- `marketplace_resources_update` PUT `/api/marketplace-resources/{uuid}/` — Update a consumer resource (path: uuid | request body)
- `marketplace_resources_partial_update` PATCH `/api/marketplace-resources/{uuid}/` — Partially update a consumer resource (path: uuid | request body)
- `marketplace_resources_details_retrieve` GET `/api/marketplace-resources/{uuid}/details/` — Get resource details (path: uuid)
- `marketplace_resources_estimate_renewal` POST `/api/marketplace-resources/{uuid}/estimate_renewal/` — Estimate renewal cost breakdown (path: uuid | request body)
- `marketplace_resources_glauth_users_config_retrieve` GET `/api/marketplace-resources/{uuid}/glauth_users_config/` — Get GLauth user configuration for a resource (path: uuid)
- `marketplace_resources_history_list` GET `/api/marketplace-resources/{uuid}/history/` — Get version history (path: uuid | 41 query params)
- `marketplace_resources_history_at_retrieve` GET `/api/marketplace-resources/{uuid}/history/at/` — Get object state at a specific timestamp (path: uuid | 1 query param)
- `marketplace_resources_move_resource` POST `/api/marketplace-resources/{uuid}/move_resource/` — Move a resource to another project (path: uuid | request body)
- `marketplace_resources_offering_retrieve` GET `/api/marketplace-resources/{uuid}/offering/` — Get offering details (path: uuid)
- `marketplace_resources_offering_for_subresources_list` GET `/api/marketplace-resources/{uuid}/offering_for_subresources/` — List offerings for sub-resources (path: uuid)
- `marketplace_resources_plan_periods_list` GET `/api/marketplace-resources/{uuid}/plan_periods/` — List resource plan periods (path: uuid)
- `marketplace_resources_pull` POST `/api/marketplace-resources/{uuid}/pull/` — Pull resource data (path: uuid)
- `marketplace_resources_reallocate_limits` POST `/api/marketplace-resources/{uuid}/reallocate_limits/` — Reallocate resource limits (path: uuid | request body)
- `marketplace_resources_renew` POST `/api/marketplace-resources/{uuid}/renew/` — Renew a prepaid resource (path: uuid | request body)
- `marketplace_resources_restore` POST `/api/marketplace-resources/{uuid}/restore/` (path: uuid | request body)
- `marketplace_resources_set_downscaled` POST `/api/marketplace-resources/{uuid}/set_downscaled/` — Set downscaled flag for resource (path: uuid | request body)
- `marketplace_resources_set_end_date_by_staff` POST `/api/marketplace-resources/{uuid}/set_end_date_by_staff/` — Set end date of the resource by staff (path: uuid | request body)
- `marketplace_resources_set_paused` POST `/api/marketplace-resources/{uuid}/set_paused/` — Set paused flag for resource (path: uuid | request body)
- `marketplace_resources_set_restrict_member_access` POST `/api/marketplace-resources/{uuid}/set_restrict_member_access/` — Set restrict member access flag (path: uuid | request body)
- `marketplace_resources_set_slug` POST `/api/marketplace-resources/{uuid}/set_slug/` — Set resource slug (path: uuid | request body)
- `marketplace_resources_switch_plan` POST `/api/marketplace-resources/{uuid}/switch_plan/` — Switch resource plan (path: uuid | request body)
- `marketplace_resources_team_list` GET `/api/marketplace-resources/{uuid}/team/` — Get resource team (path: uuid)
- `marketplace_resources_terminate` POST `/api/marketplace-resources/{uuid}/terminate/` — Terminate a resource (path: uuid | request body)
- `marketplace_resources_unlink` POST `/api/marketplace-resources/{uuid}/unlink/` — Unlink a resource (staff only) (path: uuid)
- `marketplace_resources_update_limits` POST `/api/marketplace-resources/{uuid}/update_limits/` — Update resource limits (path: uuid | request body)
- `marketplace_resources_update_options` POST `/api/marketplace-resources/{uuid}/update_options/` — Update resource options (path: uuid | request body)

## marketplace-robot-accounts
Module: `waldur_api_client.api.marketplace_robot_accounts`

- `marketplace_robot_accounts_list` GET `/api/marketplace-robot-accounts/` — List robot accounts (10 query params)
- `marketplace_robot_accounts_count` HEAD `/api/marketplace-robot-accounts/` — List robot accounts (9 query params)
- `marketplace_robot_accounts_create` POST `/api/marketplace-robot-accounts/` — Create a robot account (request body)
- `marketplace_robot_accounts_retrieve` GET `/api/marketplace-robot-accounts/{uuid}/` — Retrieve a robot account (path: uuid | 1 query param)
- `marketplace_robot_accounts_update` PUT `/api/marketplace-robot-accounts/{uuid}/` — Update a robot account (path: uuid | request body)
- `marketplace_robot_accounts_partial_update` PATCH `/api/marketplace-robot-accounts/{uuid}/` — Partially update a robot account (path: uuid | request body)
- `marketplace_robot_accounts_destroy` DELETE `/api/marketplace-robot-accounts/{uuid}/` — Delete a robot account (path: uuid)
- `marketplace_robot_accounts_set_state_creating` POST `/api/marketplace-robot-accounts/{uuid}/set_state_creating/` — Set robot account state to creating (path: uuid)
- `marketplace_robot_accounts_set_state_deleted` POST `/api/marketplace-robot-accounts/{uuid}/set_state_deleted/` — Set robot account state to deleted (path: uuid)
- `marketplace_robot_accounts_set_state_erred` POST `/api/marketplace-robot-accounts/{uuid}/set_state_erred/` — Set robot account state to erred (path: uuid | request body)
- `marketplace_robot_accounts_set_state_ok` POST `/api/marketplace-robot-accounts/{uuid}/set_state_ok/` — Set robot account state to OK (path: uuid)
- `marketplace_robot_accounts_set_state_request_deletion` POST `/api/marketplace-robot-accounts/{uuid}/set_state_request_deletion/` — Request deletion of a robot account (path: uuid)

## marketplace-runtime-states
Module: `waldur_api_client.api.marketplace_runtime_states`

- `marketplace_runtime_states_list` GET `/api/marketplace-runtime-states/` — List available runtime states for resources (2 query params)

## marketplace-screenshots
Module: `waldur_api_client.api.marketplace_screenshots`

- `marketplace_screenshots_list` GET `/api/marketplace-screenshots/` (5 query params)
- `marketplace_screenshots_count` HEAD `/api/marketplace-screenshots/` — Get number of items in the collection matching the request parameters (5 query params)
- `marketplace_screenshots_create` POST `/api/marketplace-screenshots/` (request body)
- `marketplace_screenshots_retrieve` GET `/api/marketplace-screenshots/{uuid}/` (path: uuid)
- `marketplace_screenshots_update` PUT `/api/marketplace-screenshots/{uuid}/` (path: uuid | request body)
- `marketplace_screenshots_partial_update` PATCH `/api/marketplace-screenshots/{uuid}/` (path: uuid | request body)
- `marketplace_screenshots_destroy` DELETE `/api/marketplace-screenshots/{uuid}/` (path: uuid)

## marketplace-script-async-dry-run
Module: `waldur_api_client.api.marketplace_script_async_dry_run`

- `marketplace_script_async_dry_run_list` GET `/api/marketplace-script-async-dry-run/` (no params)
- `marketplace_script_async_dry_run_count` HEAD `/api/marketplace-script-async-dry-run/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_script_async_dry_run_retrieve` GET `/api/marketplace-script-async-dry-run/{uuid}/` (path: uuid)

## marketplace-script-dry-run
Module: `waldur_api_client.api.marketplace_script_dry_run`

- `marketplace_script_dry_run_async_run` POST `/api/marketplace-script-dry-run/{uuid}/async_run/` (path: uuid | request body)
- `marketplace_script_dry_run_run` POST `/api/marketplace-script-dry-run/{uuid}/run/` (path: uuid | request body)

## marketplace-script-sync-resource
Module: `waldur_api_client.api.marketplace_script_sync_resource`

- `marketplace_script_sync_resource` POST `/api/marketplace-script-sync-resource/` — This view allows a user to trigger a pull operation for a marketplace script resource.
        The user must be a service consumer and have access to the resource.
        The pull operation is performed asynchronously using Celery. (request body)

## marketplace-sections
Module: `waldur_api_client.api.marketplace_sections`

- `marketplace_sections_list` GET `/api/marketplace-sections/` — List sections (no params)
- `marketplace_sections_count` HEAD `/api/marketplace-sections/` — List sections (no params)
- `marketplace_sections_create` POST `/api/marketplace-sections/` — Create a section (request body)
- `marketplace_sections_retrieve` GET `/api/marketplace-sections/{key}/` — Retrieve a section (path: key)
- `marketplace_sections_update` PUT `/api/marketplace-sections/{key}/` — Update a section (path: key | request body)
- `marketplace_sections_partial_update` PATCH `/api/marketplace-sections/{key}/` — Partially update a section (path: key | request body)
- `marketplace_sections_destroy` DELETE `/api/marketplace-sections/{key}/` — Delete a section (path: key)

## marketplace-service-providers
Module: `waldur_api_client.api.marketplace_service_providers`

- `marketplace_service_providers_list` GET `/api/marketplace-service-providers/` — List service providers (5 query params)
- `marketplace_service_providers_count` HEAD `/api/marketplace-service-providers/` — List service providers (4 query params)
- `marketplace_service_providers_create` POST `/api/marketplace-service-providers/` — Create a service provider (request body)
- `service_provider_checklists_summary` GET `/api/marketplace-service-providers/{service_provider_uuid}/compliance/checklists_summary/` — Get summary of compliance checklists (path: service_provider_uuid)
- `service_provider_compliance_overview` GET `/api/marketplace-service-providers/{service_provider_uuid}/compliance/compliance_overview/` — Get compliance overview for a service provider (path: service_provider_uuid)
- `service_provider_offering_users_compliance` GET `/api/marketplace-service-providers/{service_provider_uuid}/compliance/offering_users/` — List offering users' compliance status (path: service_provider_uuid | 2 query params)
- `marketplace_service_providers_course_accounts_list` GET `/api/marketplace-service-providers/{service_provider_uuid}/course_accounts/` — List course project accounts for a service provider (path: service_provider_uuid | 9 query params)
- `marketplace_service_providers_customer_projects_list` GET `/api/marketplace-service-providers/{service_provider_uuid}/customer_projects/` — List customer projects of a service provider (path: service_provider_uuid | 19 query params)
- `marketplace_service_providers_customers_list` GET `/api/marketplace-service-providers/{service_provider_uuid}/customers/` — List customers of a service provider (path: service_provider_uuid | 15 query params)
- `marketplace_service_providers_keys_list` GET `/api/marketplace-service-providers/{service_provider_uuid}/keys/` — List SSH keys of a service provider (path: service_provider_uuid | 12 query params)
- `marketplace_service_providers_offerings_list` GET `/api/marketplace-service-providers/{service_provider_uuid}/offerings/` — List offerings of a service provider (path: service_provider_uuid | 37 query params)
- `marketplace_service_providers_project_permissions_list` GET `/api/marketplace-service-providers/{service_provider_uuid}/project_permissions/` — List project permissions of a service provider (path: service_provider_uuid | 16 query params)
- `marketplace_service_providers_project_service_accounts_list` GET `/api/marketplace-service-providers/{service_provider_uuid}/project_service_accounts/` — List project service accounts for a service provider (path: service_provider_uuid | 5 query params)
- `marketplace_service_providers_projects_list` GET `/api/marketplace-service-providers/{service_provider_uuid}/projects/` — List projects of a service provider (path: service_provider_uuid | 18 query params)
- `marketplace_service_providers_user_customers_list` GET `/api/marketplace-service-providers/{service_provider_uuid}/user_customers/` — List customers of a specific user within a service provider's scope (path: service_provider_uuid | 16 query params)
- `marketplace_service_providers_users_list` GET `/api/marketplace-service-providers/{service_provider_uuid}/users/` — List users of a service provider (path: service_provider_uuid | 25 query params)
- `marketplace_service_providers_retrieve` GET `/api/marketplace-service-providers/{uuid}/` — Retrieve a service provider (path: uuid | 1 query param)
- `marketplace_service_providers_update` PUT `/api/marketplace-service-providers/{uuid}/` — Update a service provider (path: uuid | request body)
- `marketplace_service_providers_partial_update` PATCH `/api/marketplace-service-providers/{uuid}/` — Partially update a service provider (path: uuid | request body)
- `marketplace_service_providers_destroy` DELETE `/api/marketplace-service-providers/{uuid}/` — Delete a service provider (path: uuid)
- `marketplace_service_providers_add_user` POST `/api/marketplace-service-providers/{uuid}/add_user/` — Grant a role to a user (path: uuid | request body)
- `service_provider_api_secret_code_retrieve` GET `/api/marketplace-service-providers/{uuid}/api_secret_code/` — Get service provider API secret code (path: uuid)
- `service_provider_api_secret_code_generate` POST `/api/marketplace-service-providers/{uuid}/api_secret_code/` — Generate new service provider API secret code (path: uuid)
- `marketplace_service_providers_delete_user` POST `/api/marketplace-service-providers/{uuid}/delete_user/` — Revoke a role from a user (path: uuid | request body)
- `marketplace_service_providers_generate_site_agent_config` POST `/api/marketplace-service-providers/{uuid}/generate_site_agent_config/` — Generate site agent configuration (path: uuid | request body)
- `marketplace_service_providers_list_users_list` GET `/api/marketplace-service-providers/{uuid}/list_users/` — List users and their roles in a scope (path: uuid | 10 query params)
- `marketplace_service_providers_revenue_list` GET `/api/marketplace-service-providers/{uuid}/revenue/` — Get service provider revenue (path: uuid)
- `marketplace_service_providers_robot_account_customers_list` GET `/api/marketplace-service-providers/{uuid}/robot_account_customers/` — List customers with robot accounts (path: uuid | 1 query param)
- `marketplace_service_providers_robot_account_projects_list` GET `/api/marketplace-service-providers/{uuid}/robot_account_projects/` — List projects with robot accounts (path: uuid | 1 query param)
- `marketplace_service_providers_set_offerings_username` POST `/api/marketplace-service-providers/{uuid}/set_offerings_username/` — Set offering username for a user (path: uuid | request body)
- `marketplace_service_providers_stat_retrieve` GET `/api/marketplace-service-providers/{uuid}/stat/` — Get service provider statistics (path: uuid)
- `marketplace_service_providers_update_user` POST `/api/marketplace-service-providers/{uuid}/update_user/` — Update a user's role expiration (path: uuid | request body)

## marketplace-site-agent-connection-stats
Module: `waldur_api_client.api.marketplace_site_agent_connection_stats`

- `marketplace_site_agent_connection_stats_retrieve` GET `/api/marketplace-site-agent-connection-stats/` — Get agent connection statistics (no params)

## marketplace-site-agent-identities
Module: `waldur_api_client.api.marketplace_site_agent_identities`

- `marketplace_site_agent_identities_list` GET `/api/marketplace-site-agent-identities/` (5 query params)
- `marketplace_site_agent_identities_count` HEAD `/api/marketplace-site-agent-identities/` — Get number of items in the collection matching the request parameters (5 query params)
- `marketplace_site_agent_identities_create` POST `/api/marketplace-site-agent-identities/` (request body)
- `marketplace_site_agent_identities_cleanup_orphaned` POST `/api/marketplace-site-agent-identities/cleanup_orphaned/` — Remove agent identities that have no active services (request body)
- `marketplace_site_agent_identities_retrieve` GET `/api/marketplace-site-agent-identities/{uuid}/` (path: uuid)
- `marketplace_site_agent_identities_update` PUT `/api/marketplace-site-agent-identities/{uuid}/` (path: uuid | request body)
- `marketplace_site_agent_identities_destroy` DELETE `/api/marketplace-site-agent-identities/{uuid}/` (path: uuid)
- `marketplace_site_agent_identities_register_event_subscription` POST `/api/marketplace-site-agent-identities/{uuid}/register_event_subscription/` — Register an event subscription for the specified agent identity and observable object type (path: uuid | request body)
- `marketplace_site_agent_identities_register_service` POST `/api/marketplace-site-agent-identities/{uuid}/register_service/` — Register a new processor or get the existing one for the agent service (path: uuid | request body)

## marketplace-site-agent-processors
Module: `waldur_api_client.api.marketplace_site_agent_processors`

- `marketplace_site_agent_processors_list` GET `/api/marketplace-site-agent-processors/` (6 query params)
- `marketplace_site_agent_processors_count` HEAD `/api/marketplace-site-agent-processors/` — Get number of items in the collection matching the request parameters (6 query params)
- `marketplace_site_agent_processors_retrieve` GET `/api/marketplace-site-agent-processors/{uuid}/` (path: uuid)
- `marketplace_site_agent_processors_destroy` DELETE `/api/marketplace-site-agent-processors/{uuid}/` (path: uuid)

## marketplace-site-agent-services
Module: `waldur_api_client.api.marketplace_site_agent_services`

- `marketplace_site_agent_services_list` GET `/api/marketplace-site-agent-services/` (6 query params)
- `marketplace_site_agent_services_count` HEAD `/api/marketplace-site-agent-services/` — Get number of items in the collection matching the request parameters (6 query params)
- `marketplace_site_agent_services_cleanup_stale` POST `/api/marketplace-site-agent-services/cleanup_stale/` — Remove agent services that have been inactive for a specified time (request body)
- `marketplace_site_agent_services_retrieve` GET `/api/marketplace-site-agent-services/{uuid}/` (path: uuid)
- `marketplace_site_agent_services_destroy` DELETE `/api/marketplace-site-agent-services/{uuid}/` (path: uuid)
- `marketplace_site_agent_services_register_processor` POST `/api/marketplace-site-agent-services/{uuid}/register_processor/` — Register a new processor for the agent service (path: uuid | request body)
- `marketplace_site_agent_services_set_statistics` POST `/api/marketplace-site-agent-services/{uuid}/set_statistics/` — Update statistics for the agent service (path: uuid | request body)

## marketplace-site-agent-stats
Module: `waldur_api_client.api.marketplace_site_agent_stats`

- `marketplace_site_agent_stats_retrieve` GET `/api/marketplace-site-agent-stats/` — Get aggregated statistics about agent identities, services, and processors (no params)

## marketplace-site-agent-task-stats
Module: `waldur_api_client.api.marketplace_site_agent_task_stats`

- `marketplace_site_agent_task_stats_retrieve` GET `/api/marketplace-site-agent-task-stats/` — Get Celery task status for agent-related tasks (no params)

## marketplace-slurm-periodic-usage-policies
Module: `waldur_api_client.api.marketplace_slurm_periodic_usage_policies`

- `marketplace_slurm_periodic_usage_policies_list` GET `/api/marketplace-slurm-periodic-usage-policies/` (2 query params)
- `marketplace_slurm_periodic_usage_policies_count` HEAD `/api/marketplace-slurm-periodic-usage-policies/` — Get number of items in the collection matching the request parameters (2 query params)
- `marketplace_slurm_periodic_usage_policies_create` POST `/api/marketplace-slurm-periodic-usage-policies/` (request body)
- `marketplace_slurm_periodic_usage_policies_actions_retrieve` GET `/api/marketplace-slurm-periodic-usage-policies/actions/` (no params)
- `marketplace_slurm_periodic_usage_policies_actions_count` HEAD `/api/marketplace-slurm-periodic-usage-policies/actions/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_slurm_periodic_usage_policies_preview_impact` POST `/api/marketplace-slurm-periodic-usage-policies/preview_impact/` — Preview policy impact without saving (request body)
- `marketplace_slurm_periodic_usage_policies_retrieve` GET `/api/marketplace-slurm-periodic-usage-policies/{uuid}/` (path: uuid)
- `marketplace_slurm_periodic_usage_policies_update` PUT `/api/marketplace-slurm-periodic-usage-policies/{uuid}/` (path: uuid | request body)
- `marketplace_slurm_periodic_usage_policies_partial_update` PATCH `/api/marketplace-slurm-periodic-usage-policies/{uuid}/` (path: uuid | request body)
- `marketplace_slurm_periodic_usage_policies_destroy` DELETE `/api/marketplace-slurm-periodic-usage-policies/{uuid}/` (path: uuid)
- `marketplace_slurm_periodic_usage_policies_command_history_list` GET `/api/marketplace-slurm-periodic-usage-policies/{uuid}/command-history/` — List command history for this policy (path: uuid | 2 query params)
- `marketplace_slurm_periodic_usage_policies_dry_run` POST `/api/marketplace-slurm-periodic-usage-policies/{uuid}/dry-run/` — Staff-only (path: uuid | request body)
- `marketplace_slurm_periodic_usage_policies_evaluate` POST `/api/marketplace-slurm-periodic-usage-policies/{uuid}/evaluate/` — Staff-only (path: uuid | request body)
- `marketplace_slurm_periodic_usage_policies_evaluation_logs_list` GET `/api/marketplace-slurm-periodic-usage-policies/{uuid}/evaluation-logs/` — List evaluation logs for this policy (path: uuid | 2 query params)
- `marketplace_slurm_periodic_usage_policies_report_command_result` POST `/api/marketplace-slurm-periodic-usage-policies/{uuid}/report-command-result/` — Report command execution result from site agent (path: uuid | request body)

## marketplace-software-catalogs
Module: `waldur_api_client.api.marketplace_software_catalogs`

- `marketplace_software_catalogs_list` GET `/api/marketplace-software-catalogs/` — List software catalogs (3 query params)
- `marketplace_software_catalogs_count` HEAD `/api/marketplace-software-catalogs/` — List software catalogs (3 query params)
- `marketplace_software_catalogs_create` POST `/api/marketplace-software-catalogs/` — Create a software catalog (request body)
- `marketplace_software_catalogs_discover_list` GET `/api/marketplace-software-catalogs/discover/` — Discover available software catalog versions (3 query params)
- `marketplace_software_catalogs_discover_count` HEAD `/api/marketplace-software-catalogs/discover/` — Discover available software catalog versions (3 query params)
- `marketplace_software_catalogs_import_catalog` POST `/api/marketplace-software-catalogs/import_catalog/` — Import a new software catalog (request body)
- `marketplace_software_catalogs_retrieve` GET `/api/marketplace-software-catalogs/{uuid}/` — Retrieve a software catalog (path: uuid)
- `marketplace_software_catalogs_update` PUT `/api/marketplace-software-catalogs/{uuid}/` — Update a software catalog (path: uuid | request body)
- `marketplace_software_catalogs_partial_update` PATCH `/api/marketplace-software-catalogs/{uuid}/` — Partially update a software catalog (path: uuid | request body)
- `marketplace_software_catalogs_destroy` DELETE `/api/marketplace-software-catalogs/{uuid}/` — Delete a software catalog (path: uuid)
- `marketplace_software_catalogs_update_catalog` POST `/api/marketplace-software-catalogs/{uuid}/update_catalog/` — Trigger async update for an existing catalog (path: uuid | request body)

## marketplace-software-packages
Module: `waldur_api_client.api.marketplace_software_packages`

- `marketplace_software_packages_list` GET `/api/marketplace-software-packages/` — List software packages (14 query params)
- `marketplace_software_packages_count` HEAD `/api/marketplace-software-packages/` — List software packages (14 query params)
- `marketplace_software_packages_create` POST `/api/marketplace-software-packages/` — Create a software package (request body)
- `marketplace_software_packages_retrieve` GET `/api/marketplace-software-packages/{uuid}/` — Retrieve a software package (path: uuid)
- `marketplace_software_packages_update` PUT `/api/marketplace-software-packages/{uuid}/` — Update a software package (path: uuid | request body)
- `marketplace_software_packages_partial_update` PATCH `/api/marketplace-software-packages/{uuid}/` — Partially update a software package (path: uuid | request body)
- `marketplace_software_packages_destroy` DELETE `/api/marketplace-software-packages/{uuid}/` — Delete a software package (path: uuid)

## marketplace-software-targets
Module: `waldur_api_client.api.marketplace_software_targets`

- `marketplace_software_targets_list` GET `/api/marketplace-software-targets/` — List software targets (8 query params)
- `marketplace_software_targets_count` HEAD `/api/marketplace-software-targets/` — List software targets (8 query params)
- `marketplace_software_targets_create` POST `/api/marketplace-software-targets/` — Create a software target (no params)
- `marketplace_software_targets_retrieve` GET `/api/marketplace-software-targets/{uuid}/` — Retrieve a software target (path: uuid)
- `marketplace_software_targets_update` PUT `/api/marketplace-software-targets/{uuid}/` — Update a software target (path: uuid)
- `marketplace_software_targets_partial_update` PATCH `/api/marketplace-software-targets/{uuid}/` — Partially update a software target (path: uuid)
- `marketplace_software_targets_destroy` DELETE `/api/marketplace-software-targets/{uuid}/` — Delete a software target (path: uuid)

## marketplace-software-versions
Module: `waldur_api_client.api.marketplace_software_versions`

- `marketplace_software_versions_list` GET `/api/marketplace-software-versions/` — List software versions (8 query params)
- `marketplace_software_versions_count` HEAD `/api/marketplace-software-versions/` — List software versions (8 query params)
- `marketplace_software_versions_create` POST `/api/marketplace-software-versions/` — Create a software version (no params)
- `marketplace_software_versions_retrieve` GET `/api/marketplace-software-versions/{uuid}/` — Retrieve a software version (path: uuid)
- `marketplace_software_versions_update` PUT `/api/marketplace-software-versions/{uuid}/` — Update a software version (path: uuid)
- `marketplace_software_versions_partial_update` PATCH `/api/marketplace-software-versions/{uuid}/` — Partially update a software version (path: uuid)
- `marketplace_software_versions_destroy` DELETE `/api/marketplace-software-versions/{uuid}/` — Delete a software version (path: uuid)

## marketplace-stats
Module: `waldur_api_client.api.marketplace_stats`

- `marketplace_stats_aggregated_usage_trends_list` GET `/api/marketplace-stats/aggregated_usage_trends/` — Return aggregated usage trends per month (no params)
- `marketplace_stats_aggregated_usage_trends_count` HEAD `/api/marketplace-stats/aggregated_usage_trends/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_component_usages_list` GET `/api/marketplace-stats/component_usages/` — Return component usages for current month (no params)
- `marketplace_stats_component_usages_count` HEAD `/api/marketplace-stats/component_usages/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_component_usages_per_month_list` GET `/api/marketplace-stats/component_usages_per_month/` — Return component usages per month (no params)
- `marketplace_stats_component_usages_per_month_count` HEAD `/api/marketplace-stats/component_usages_per_month/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_component_usages_per_project_list` GET `/api/marketplace-stats/component_usages_per_project/` — Return component usages per project (no params)
- `marketplace_stats_component_usages_per_project_count` HEAD `/api/marketplace-stats/component_usages_per_project/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_count_active_resources_grouped_by_offering_list` GET `/api/marketplace-stats/count_active_resources_grouped_by_offering/` — Count active resources grouped by offering (no params)
- `marketplace_stats_count_active_resources_grouped_by_offering_count` HEAD `/api/marketplace-stats/count_active_resources_grouped_by_offering/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_count_active_resources_grouped_by_offering_country_list` GET `/api/marketplace-stats/count_active_resources_grouped_by_offering_country/` — Count active resources grouped by offering country (no params)
- `marketplace_stats_count_active_resources_grouped_by_offering_country_count` HEAD `/api/marketplace-stats/count_active_resources_grouped_by_offering_country/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_count_active_resources_grouped_by_organization_group_list` GET `/api/marketplace-stats/count_active_resources_grouped_by_organization_group/` — Count active resources grouped by organization group (no params)
- `marketplace_stats_count_active_resources_grouped_by_organization_group_count` HEAD `/api/marketplace-stats/count_active_resources_grouped_by_organization_group/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_count_projects_grouped_by_provider_and_industry_flag_list` GET `/api/marketplace-stats/count_projects_grouped_by_provider_and_industry_flag/` — Count projects grouped by provider and industry flag (no params)
- `marketplace_stats_count_projects_grouped_by_provider_and_industry_flag_count` HEAD `/api/marketplace-stats/count_projects_grouped_by_provider_and_industry_flag/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_count_projects_grouped_by_provider_and_oecd_list` GET `/api/marketplace-stats/count_projects_grouped_by_provider_and_oecd/` — Count projects grouped by provider and OECD code (no params)
- `marketplace_stats_count_projects_grouped_by_provider_and_oecd_count` HEAD `/api/marketplace-stats/count_projects_grouped_by_provider_and_oecd/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_count_projects_of_service_providers_list` GET `/api/marketplace-stats/count_projects_of_service_providers/` — Count projects of service providers (no params)
- `marketplace_stats_count_projects_of_service_providers_count` HEAD `/api/marketplace-stats/count_projects_of_service_providers/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_count_projects_of_service_providers_grouped_by_oecd_list` GET `/api/marketplace-stats/count_projects_of_service_providers_grouped_by_oecd/` — Count projects of service providers grouped by OECD (no params)
- `marketplace_stats_count_projects_of_service_providers_grouped_by_oecd_count` HEAD `/api/marketplace-stats/count_projects_of_service_providers_grouped_by_oecd/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_count_unique_users_connected_with_active_resources_of_service_provider_list` GET `/api/marketplace-stats/count_unique_users_connected_with_active_resources_of_service_provider/` — Count unique users connected with active resources of service provider (no params)
- `marketplace_stats_count_unique_users_connected_with_active_resources_of_service_provider_count` HEAD `/api/marketplace-stats/count_unique_users_connected_with_active_resources_of_service_provider/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_count_users_of_service_providers_list` GET `/api/marketplace-stats/count_users_of_service_providers/` — Count users of service providers (no params)
- `marketplace_stats_count_users_of_service_providers_count` HEAD `/api/marketplace-stats/count_users_of_service_providers/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_customer_member_count_list` GET `/api/marketplace-stats/customer_member_count/` — Return count of customer members (no params)
- `marketplace_stats_customer_member_count_count` HEAD `/api/marketplace-stats/customer_member_count/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_customer_member_summary_retrieve` GET `/api/marketplace-stats/customer_member_summary/` — Return summary statistics for customer members (no params)
- `marketplace_stats_customer_member_summary_count` HEAD `/api/marketplace-stats/customer_member_summary/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_offering_costs_summary_retrieve` GET `/api/marketplace-stats/offering_costs_summary/` — Return summary statistics for offering costs (no params)
- `marketplace_stats_offering_costs_summary_count` HEAD `/api/marketplace-stats/offering_costs_summary/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_offerings_counter_stats_list` GET `/api/marketplace-stats/offerings_counter_stats/` — Retrieve statistics about the number of offerings, grouped by category and service provider (no params)
- `marketplace_stats_offerings_counter_stats_count` HEAD `/api/marketplace-stats/offerings_counter_stats/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_order_stats_retrieve` GET `/api/marketplace-stats/order_stats/` — Return comprehensive order statistics including daily breakdown, state/type aggregations, and summary stats (4 query params)
- `marketplace_stats_order_stats_count` HEAD `/api/marketplace-stats/order_stats/` — Get number of items in the collection matching the request parameters (4 query params)
- `marketplace_stats_organization_project_count_list` GET `/api/marketplace-stats/organization_project_count/` — Return project count per organization (no params)
- `marketplace_stats_organization_project_count_count` HEAD `/api/marketplace-stats/organization_project_count/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_organization_resource_count_list` GET `/api/marketplace-stats/organization_resource_count/` — Return resource count per organization (no params)
- `marketplace_stats_organization_resource_count_count` HEAD `/api/marketplace-stats/organization_resource_count/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_project_classification_summary_retrieve` GET `/api/marketplace-stats/project_classification_summary/` — Return summary statistics for project classification (no params)
- `marketplace_stats_project_classification_summary_count` HEAD `/api/marketplace-stats/project_classification_summary/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_projects_limits_grouped_by_industry_flag_retrieve` GET `/api/marketplace-stats/projects_limits_grouped_by_industry_flag/` — Group project limits by industry flag (no params)
- `marketplace_stats_projects_limits_grouped_by_industry_flag_count` HEAD `/api/marketplace-stats/projects_limits_grouped_by_industry_flag/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_projects_limits_grouped_by_oecd_retrieve` GET `/api/marketplace-stats/projects_limits_grouped_by_oecd/` — Group project limits by OECD code (no params)
- `marketplace_stats_projects_limits_grouped_by_oecd_count` HEAD `/api/marketplace-stats/projects_limits_grouped_by_oecd/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_projects_usages_grouped_by_industry_flag_retrieve` GET `/api/marketplace-stats/projects_usages_grouped_by_industry_flag/` — Group project usages by industry flag (no params)
- `marketplace_stats_projects_usages_grouped_by_industry_flag_count` HEAD `/api/marketplace-stats/projects_usages_grouped_by_industry_flag/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_projects_usages_grouped_by_oecd_retrieve` GET `/api/marketplace-stats/projects_usages_grouped_by_oecd/` — Group project usages by OECD code (no params)
- `marketplace_stats_projects_usages_grouped_by_oecd_count` HEAD `/api/marketplace-stats/projects_usages_grouped_by_oecd/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_provider_customers_retrieve` GET `/api/marketplace-stats/provider_customers/` — Return customer statistics for a service provider (1 query param)
- `marketplace_stats_provider_customers_count` HEAD `/api/marketplace-stats/provider_customers/` — Get number of items in the collection matching the request parameters (1 query param)
- `marketplace_stats_provider_offerings_retrieve` GET `/api/marketplace-stats/provider_offerings/` — Return offering performance statistics for a service provider (1 query param)
- `marketplace_stats_provider_offerings_count` HEAD `/api/marketplace-stats/provider_offerings/` — Get number of items in the collection matching the request parameters (1 query param)
- `marketplace_stats_provider_resources_retrieve` GET `/api/marketplace-stats/provider_resources/` — Return resource statistics for a service provider (1 query param)
- `marketplace_stats_provider_resources_count` HEAD `/api/marketplace-stats/provider_resources/` — Get number of items in the collection matching the request parameters (1 query param)
- `marketplace_stats_resource_provisioning_stats_list` GET `/api/marketplace-stats/resource_provisioning_stats/` — Get resource provisioning statistics (1 query param)
- `marketplace_stats_resource_provisioning_stats_count` HEAD `/api/marketplace-stats/resource_provisioning_stats/` — Get number of items in the collection matching the request parameters (1 query param)
- `marketplace_stats_resource_usage_by_creator_affiliation_list` GET `/api/marketplace-stats/resource_usage_by_creator_affiliation/` — Return resource usage grouped by creator's affiliation (no params)
- `marketplace_stats_resource_usage_by_creator_affiliation_count` HEAD `/api/marketplace-stats/resource_usage_by_creator_affiliation/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_resource_usage_by_customer_list` GET `/api/marketplace-stats/resource_usage_by_customer/` — Return resource usage statistics grouped by customer (no params)
- `marketplace_stats_resource_usage_by_customer_count` HEAD `/api/marketplace-stats/resource_usage_by_customer/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_resource_usage_by_organization_type_list` GET `/api/marketplace-stats/resource_usage_by_organization_type/` — Return component usages grouped by project members' organization type (no params)
- `marketplace_stats_resource_usage_by_organization_type_count` HEAD `/api/marketplace-stats/resource_usage_by_organization_type/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_resources_geography_summary_retrieve` GET `/api/marketplace-stats/resources_geography_summary/` — Return summary statistics for resource geographic distribution (no params)
- `marketplace_stats_resources_geography_summary_count` HEAD `/api/marketplace-stats/resources_geography_summary/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_resources_limits_list` GET `/api/marketplace-stats/resources_limits/` — Return resources limits per offering (no params)
- `marketplace_stats_resources_limits_count` HEAD `/api/marketplace-stats/resources_limits/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_resources_missing_usage_list` GET `/api/marketplace-stats/resources_missing_usage/` — Return usage-based resources with no usage reported in the specified billing period (2 query params)
- `marketplace_stats_resources_missing_usage_count` HEAD `/api/marketplace-stats/resources_missing_usage/` — Get number of items in the collection matching the request parameters (2 query params)
- `marketplace_stats_total_cost_of_active_resources_per_offering_list` GET `/api/marketplace-stats/total_cost_of_active_resources_per_offering/` — Total cost of active resources per offering (no params)
- `marketplace_stats_total_cost_of_active_resources_per_offering_count` HEAD `/api/marketplace-stats/total_cost_of_active_resources_per_offering/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_user_affiliation_count_list` GET `/api/marketplace-stats/user_affiliation_count/` — Return user count grouped by affiliation (no params)
- `marketplace_stats_user_affiliation_count_count` HEAD `/api/marketplace-stats/user_affiliation_count/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_user_auth_method_count_list` GET `/api/marketplace-stats/user_auth_method_count/` — Return user count grouped by authentication method (no params)
- `marketplace_stats_user_auth_method_count_count` HEAD `/api/marketplace-stats/user_auth_method_count/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_user_identity_source_count_list` GET `/api/marketplace-stats/user_identity_source_count/` — Return user count grouped by identity source (no params)
- `marketplace_stats_user_identity_source_count_count` HEAD `/api/marketplace-stats/user_identity_source_count/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_user_job_title_count_list` GET `/api/marketplace-stats/user_job_title_count/` — Return user count grouped by job title (no params)
- `marketplace_stats_user_job_title_count_count` HEAD `/api/marketplace-stats/user_job_title_count/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_user_organization_count_list` GET `/api/marketplace-stats/user_organization_count/` — Return user count grouped by organization (no params)
- `marketplace_stats_user_organization_count_count` HEAD `/api/marketplace-stats/user_organization_count/` — Get number of items in the collection matching the request parameters (no params)
- `marketplace_stats_user_organization_type_count_list` GET `/api/marketplace-stats/user_organization_type_count/` — Return user count grouped by organization type (SCHAC URN) (no params)
- `marketplace_stats_user_organization_type_count_count` HEAD `/api/marketplace-stats/user_organization_type_count/` — Get number of items in the collection matching the request parameters (no params)

## marketplace-tags
Module: `waldur_api_client.api.marketplace_tags`

- `marketplace_tags_list` GET `/api/marketplace-tags/` (2 query params)
- `marketplace_tags_count` HEAD `/api/marketplace-tags/` — Get number of items in the collection matching the request parameters (2 query params)
- `marketplace_tags_create` POST `/api/marketplace-tags/` (request body)
- `marketplace_tags_retrieve` GET `/api/marketplace-tags/{uuid}/` (path: uuid)
- `marketplace_tags_update` PUT `/api/marketplace-tags/{uuid}/` (path: uuid | request body)
- `marketplace_tags_partial_update` PATCH `/api/marketplace-tags/{uuid}/` (path: uuid | request body)
- `marketplace_tags_destroy` DELETE `/api/marketplace-tags/{uuid}/` (path: uuid)

## marketplace-user-offering-consents
Module: `waldur_api_client.api.marketplace_user_offering_consents`

- `marketplace_user_offering_consents_list` GET `/api/marketplace-user-offering-consents/` — List user offering consents (8 query params)
- `marketplace_user_offering_consents_count` HEAD `/api/marketplace-user-offering-consents/` — List user offering consents (8 query params)
- `marketplace_user_offering_consents_create` POST `/api/marketplace-user-offering-consents/` — Grant consent to an offering's Terms of Service (request body)
- `marketplace_user_offering_consents_retrieve` GET `/api/marketplace-user-offering-consents/{uuid}/` — Retrieve a user offering consent (path: uuid)
- `marketplace_user_offering_consents_update` PUT `/api/marketplace-user-offering-consents/{uuid}/` (path: uuid | request body)
- `marketplace_user_offering_consents_partial_update` PATCH `/api/marketplace-user-offering-consents/{uuid}/` (path: uuid | request body)
- `marketplace_user_offering_consents_destroy` DELETE `/api/marketplace-user-offering-consents/{uuid}/` (path: uuid)
- `marketplace_user_offering_consents_revoke` POST `/api/marketplace-user-offering-consents/{uuid}/revoke/` — Revoke consent to Terms of Service (path: uuid)

## media
Module: `waldur_api_client.api.media`

- `media_retrieve` GET `/api/media/{uuid}/` — Get media file (path: uuid)

## metadata
Module: `waldur_api_client.api.metadata`

- `metadata_events_retrieve` GET `/api/metadata/events/` — Get event metadata (no params)
- `metadata_features_retrieve` GET `/api/metadata/features/` — Get feature flag metadata (no params)
- `metadata_permissions_retrieve` GET `/api/metadata/permissions/` — Get permission metadata (no params)
- `metadata_settings_retrieve` GET `/api/metadata/settings/` — Get overridable settings metadata (no params)

## my-assignment-batches
Module: `waldur_api_client.api.my_assignment_batches`

- `my_assignment_batches_list` GET `/api/my-assignment-batches/` — List all pending assignment batches for the authenticated reviewer (no params)
- `my_assignment_batches_count` HEAD `/api/my-assignment-batches/` — Get number of items in the collection matching the request parameters (no params)
- `my_assignment_batches_retrieve` GET `/api/my-assignment-batches/{uuid}/` — Get details of a specific assignment batch with items (path: uuid)

## notification-messages
Module: `waldur_api_client.api.notification_messages`

- `notification_messages_list` GET `/api/notification-messages/` (6 query params)
- `notification_messages_count` HEAD `/api/notification-messages/` — Get number of items in the collection matching the request parameters (6 query params)
- `notification_messages_create` POST `/api/notification-messages/` (request body)
- `notification_messages_retrieve` GET `/api/notification-messages/{uuid}/` (path: uuid)
- `notification_messages_update` PUT `/api/notification-messages/{uuid}/` (path: uuid | request body)
- `notification_messages_partial_update` PATCH `/api/notification-messages/{uuid}/` (path: uuid | request body)
- `notification_messages_destroy` DELETE `/api/notification-messages/{uuid}/` (path: uuid)
- `notification_messages_disable` POST `/api/notification-messages/{uuid}/disable/` — Disable a notification (path: uuid)
- `notification_messages_enable` POST `/api/notification-messages/{uuid}/enable/` — Enable a notification (path: uuid)

## notification-messages-templates
Module: `waldur_api_client.api.notification_messages_templates`

- `notification_messages_templates_list` GET `/api/notification-messages-templates/` (5 query params)
- `notification_messages_templates_count` HEAD `/api/notification-messages-templates/` — Get number of items in the collection matching the request parameters (5 query params)
- `notification_messages_templates_create` POST `/api/notification-messages-templates/` (request body)
- `notification_messages_templates_retrieve` GET `/api/notification-messages-templates/{uuid}/` (path: uuid)
- `notification_messages_templates_update` PUT `/api/notification-messages-templates/{uuid}/` (path: uuid | request body)
- `notification_messages_templates_partial_update` PATCH `/api/notification-messages-templates/{uuid}/` (path: uuid | request body)
- `notification_messages_templates_destroy` DELETE `/api/notification-messages-templates/{uuid}/` (path: uuid)
- `notification_messages_templates_override` POST `/api/notification-messages-templates/{uuid}/override/` — Override notification template content (path: uuid | request body)

## onboarding
Module: `waldur_api_client.api.onboarding`

- `onboarding_person_identifier_fields_retrieve` GET `/api/onboarding/person-identifier-fields/` — Return person identifier field specification for a specific validation method (1 query param)
- `onboarding_supported_countries_retrieve` GET `/api/onboarding/supported-countries/` — Return list of supported countries for validation (no params)

## onboarding-justifications
Module: `waldur_api_client.api.onboarding_justifications`

- `onboarding_justifications_list` GET `/api/onboarding-justifications/` (5 query params)
- `onboarding_justifications_count` HEAD `/api/onboarding-justifications/` — Get number of items in the collection matching the request parameters (5 query params)
- `onboarding_justifications_create` POST `/api/onboarding-justifications/` (request body)
- `onboarding_justifications_create_justification` POST `/api/onboarding-justifications/create_justification/` — Create justification for failed verification (request body)
- `onboarding_justifications_retrieve` GET `/api/onboarding-justifications/{uuid}/` (path: uuid)
- `onboarding_justifications_update` PUT `/api/onboarding-justifications/{uuid}/` (path: uuid | request body)
- `onboarding_justifications_partial_update` PATCH `/api/onboarding-justifications/{uuid}/` (path: uuid | request body)
- `onboarding_justifications_destroy` DELETE `/api/onboarding-justifications/{uuid}/` (path: uuid)
- `onboarding_justifications_approve` POST `/api/onboarding-justifications/{uuid}/approve/` — Approve justification and mark verification as VERIFIED (path: uuid | request body)
- `onboarding_justifications_attach_document` POST `/api/onboarding-justifications/{uuid}/attach_document/` — Attach supporting document to justification (path: uuid | request body)
- `onboarding_justifications_reject` POST `/api/onboarding-justifications/{uuid}/reject/` — Reject justification and mark verification as FAILED (path: uuid | request body)

## onboarding-question-metadata
Module: `waldur_api_client.api.onboarding_question_metadata`

- `onboarding_question_metadata_list` GET `/api/onboarding-question-metadata/` (5 query params)
- `onboarding_question_metadata_count` HEAD `/api/onboarding-question-metadata/` — Get number of items in the collection matching the request parameters (5 query params)
- `onboarding_question_metadata_create` POST `/api/onboarding-question-metadata/` (request body)
- `onboarding_question_metadata_retrieve` GET `/api/onboarding-question-metadata/{uuid}/` (path: uuid)
- `onboarding_question_metadata_update` PUT `/api/onboarding-question-metadata/{uuid}/` (path: uuid | request body)
- `onboarding_question_metadata_partial_update` PATCH `/api/onboarding-question-metadata/{uuid}/` (path: uuid | request body)
- `onboarding_question_metadata_destroy` DELETE `/api/onboarding-question-metadata/{uuid}/` (path: uuid)

## onboarding-verifications
Module: `waldur_api_client.api.onboarding_verifications`

- `onboarding_verifications_list` GET `/api/onboarding-verifications/` (8 query params)
- `onboarding_verifications_count` HEAD `/api/onboarding-verifications/` — Get number of items in the collection matching the request parameters (8 query params)
- `onboarding_verifications_create` POST `/api/onboarding-verifications/` (request body)
- `onboarding_verifications_available_checklists_retrieve` GET `/api/onboarding-verifications/available_checklists/` — Get available onboarding checklists (customer and intent) for preview (1 query param)
- `onboarding_verifications_available_checklists_count` HEAD `/api/onboarding-verifications/available_checklists/` — Get number of items in the collection matching the request parameters (1 query param)
- `onboarding_verifications_checklist_template_retrieve` GET `/api/onboarding-verifications/checklist-template/` — Get checklist template for creating new objects (1 query param)
- `onboarding_verifications_checklist_template_count` HEAD `/api/onboarding-verifications/checklist-template/` — Get number of items in the collection matching the request parameters (1 query param)
- `onboarding_verifications_start_verification` POST `/api/onboarding-verifications/start_verification/` — Start company validation process by creating a verification record (request body)
- `onboarding_verifications_retrieve` GET `/api/onboarding-verifications/{uuid}/` (path: uuid)
- `onboarding_verifications_update` PUT `/api/onboarding-verifications/{uuid}/` (path: uuid | request body)
- `onboarding_verifications_partial_update` PATCH `/api/onboarding-verifications/{uuid}/` (path: uuid | request body)
- `onboarding_verifications_destroy` DELETE `/api/onboarding-verifications/{uuid}/` (path: uuid)
- `onboarding_verifications_checklist_retrieve` GET `/api/onboarding-verifications/{uuid}/checklist/` — Get checklist with questions and existing answers (path: uuid | 2 query params)
- `onboarding_verifications_completion_status_retrieve` GET `/api/onboarding-verifications/{uuid}/completion_status/` — Get checklist completion status (path: uuid | 1 query param)
- `onboarding_verifications_create_customer` POST `/api/onboarding-verifications/{uuid}/create_customer/` — Create customer from successful verification (path: uuid)
- `onboarding_verifications_run_validation` POST `/api/onboarding-verifications/{uuid}/run_validation/` — Run automatic validation using the required fields provided during verification creation (path: uuid | request body)
- `onboarding_verifications_submit_answers` POST `/api/onboarding-verifications/{uuid}/submit_answers/` — Submit answers to checklist questions (path: uuid | request body)

## openportal-allocation-user-usage
Module: `waldur_api_client.api.openportal_allocation_user_usage`

- `openportal_allocation_user_usage_list` GET `/api/openportal-allocation-user-usage/` (6 query params)
- `openportal_allocation_user_usage_count` HEAD `/api/openportal-allocation-user-usage/` — Get number of items in the collection matching the request parameters (6 query params)
- `openportal_allocation_user_usage_retrieve` GET `/api/openportal-allocation-user-usage/{id}/` (path: id)

## openportal-allocations
Module: `waldur_api_client.api.openportal_allocations`

- `openportal_allocations_list` GET `/api/openportal-allocations/` (20 query params)
- `openportal_allocations_count` HEAD `/api/openportal-allocations/` — Get number of items in the collection matching the request parameters (19 query params)
- `openportal_allocations_create` POST `/api/openportal-allocations/` (request body)
- `openportal_allocations_retrieve` GET `/api/openportal-allocations/{uuid}/` (path: uuid | 1 query param)
- `openportal_allocations_update` PUT `/api/openportal-allocations/{uuid}/` (path: uuid | request body)
- `openportal_allocations_partial_update` PATCH `/api/openportal-allocations/{uuid}/` (path: uuid | request body)
- `openportal_allocations_destroy` DELETE `/api/openportal-allocations/{uuid}/` (path: uuid)
- `openportal_allocations_pull` POST `/api/openportal-allocations/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `openportal_allocations_set_erred` POST `/api/openportal-allocations/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `openportal_allocations_set_limits` POST `/api/openportal-allocations/{uuid}/set_limits/` (path: uuid | request body)
- `openportal_allocations_set_ok` POST `/api/openportal-allocations/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `openportal_allocations_unlink` POST `/api/openportal-allocations/{uuid}/unlink/` — Unlink resource (path: uuid)

## openportal-associations
Module: `waldur_api_client.api.openportal_associations`

- `openportal_associations_list` GET `/api/openportal-associations/` (2 query params)
- `openportal_associations_count` HEAD `/api/openportal-associations/` — Get number of items in the collection matching the request parameters (2 query params)
- `openportal_associations_retrieve` GET `/api/openportal-associations/{uuid}/` (path: uuid)

## openportal-managed-projects
Module: `waldur_api_client.api.openportal_managed_projects`

- `openportal_managed_projects_list` GET `/api/openportal-managed-projects/` — List all managed projects (7 query params)
- `openportal_managed_projects_count` HEAD `/api/openportal-managed-projects/` — Get number of items in the collection matching the request parameters (7 query params)
- `openportal_managed_projects_retrieve_get` GET `/api/openportal-managed-projects/{identifier}/{destination}/` — Retrieve a managed project (path: destination, identifier)
- `openportal_managed_projects_retrieve_head` HEAD `/api/openportal-managed-projects/{identifier}/{destination}/` — Get number of items in the collection matching the request parameters (path: destination, identifier)
- `openportal_managed_projects_approve` POST `/api/openportal-managed-projects/{identifier}/{destination}/approve/` — Approve managed project request (path: destination, identifier | request body)
- `openportal_managed_projects_attach` POST `/api/openportal-managed-projects/{identifier}/{destination}/attach/` — Attach a project to this managed project (path: destination, identifier | request body)
- `openportal_managed_projects_delete_destroy` DELETE `/api/openportal-managed-projects/{identifier}/{destination}/delete/` — Delete ManagedProject object (path: destination, identifier)
- `openportal_managed_projects_detach` POST `/api/openportal-managed-projects/{identifier}/{destination}/detach/` — Detach the project from this managed project (path: destination, identifier)
- `openportal_managed_projects_reject` POST `/api/openportal-managed-projects/{identifier}/{destination}/reject/` — Reject managed project request (path: destination, identifier | request body)

## openportal-project-template
Module: `waldur_api_client.api.openportal_project_template`

- `openportal_project_template_list` GET `/api/openportal-project-template/` (3 query params)
- `openportal_project_template_count` HEAD `/api/openportal-project-template/` — Get number of items in the collection matching the request parameters (3 query params)
- `openportal_project_template_create` POST `/api/openportal-project-template/` — Create ProjectTemplate object (request body)
- `openportal_project_template_retrieve` GET `/api/openportal-project-template/{uuid}/` (path: uuid)
- `openportal_project_template_update` PUT `/api/openportal-project-template/{uuid}/` — Update ProjectTemplate object (full update) (path: uuid | request body)
- `openportal_project_template_partial_update` PATCH `/api/openportal-project-template/{uuid}/` — Partially update ProjectTemplate object (path: uuid | request body)
- `openportal_project_template_destroy` DELETE `/api/openportal-project-template/{uuid}/` (path: uuid)
- `openportal_project_template_delete_destroy` DELETE `/api/openportal-project-template/{uuid}/delete/` — Delete ProjectTemplate object (path: uuid)

## openportal-projectinfo
Module: `waldur_api_client.api.openportal_projectinfo`

- `openportal_projectinfo_list` GET `/api/openportal-projectinfo/` (2 query params)
- `openportal_projectinfo_count` HEAD `/api/openportal-projectinfo/` — Get number of items in the collection matching the request parameters (2 query params)
- `openportal_projectinfo_create` POST `/api/openportal-projectinfo/` (request body)
- `openportal_projectinfo_retrieve` GET `/api/openportal-projectinfo/{project}/` (path: project)
- `openportal_projectinfo_update` PUT `/api/openportal-projectinfo/{project}/` (path: project | request body)
- `openportal_projectinfo_partial_update` PATCH `/api/openportal-projectinfo/{project}/` (path: project | request body)
- `openportal_projectinfo_destroy` DELETE `/api/openportal-projectinfo/{project}/` (path: project)
- `openportal_projectinfo_set_allowed_destinations_update` PUT `/api/openportal-projectinfo/{project}/set_allowed_destinations/` (path: project | request body)
- `openportal_projectinfo_set_shortname_update` PUT `/api/openportal-projectinfo/{project}/set_shortname/` (path: project | request body)

## openportal-remote-allocations
Module: `waldur_api_client.api.openportal_remote_allocations`

- `openportal_remote_allocations_list` GET `/api/openportal-remote-allocations/` (20 query params)
- `openportal_remote_allocations_count` HEAD `/api/openportal-remote-allocations/` — Get number of items in the collection matching the request parameters (19 query params)
- `openportal_remote_allocations_create` POST `/api/openportal-remote-allocations/` (request body)
- `openportal_remote_allocations_retrieve` GET `/api/openportal-remote-allocations/{uuid}/` (path: uuid | 1 query param)
- `openportal_remote_allocations_update` PUT `/api/openportal-remote-allocations/{uuid}/` (path: uuid | request body)
- `openportal_remote_allocations_partial_update` PATCH `/api/openportal-remote-allocations/{uuid}/` (path: uuid | request body)
- `openportal_remote_allocations_destroy` DELETE `/api/openportal-remote-allocations/{uuid}/` (path: uuid)
- `openportal_remote_allocations_pull` POST `/api/openportal-remote-allocations/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `openportal_remote_allocations_set_erred` POST `/api/openportal-remote-allocations/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `openportal_remote_allocations_set_limits` POST `/api/openportal-remote-allocations/{uuid}/set_limits/` (path: uuid | request body)
- `openportal_remote_allocations_set_ok` POST `/api/openportal-remote-allocations/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `openportal_remote_allocations_unlink` POST `/api/openportal-remote-allocations/{uuid}/unlink/` — Unlink resource (path: uuid)

## openportal-remote-associations
Module: `waldur_api_client.api.openportal_remote_associations`

- `openportal_remote_associations_list` GET `/api/openportal-remote-associations/` (2 query params)
- `openportal_remote_associations_count` HEAD `/api/openportal-remote-associations/` — Get number of items in the collection matching the request parameters (2 query params)
- `openportal_remote_associations_retrieve` GET `/api/openportal-remote-associations/{uuid}/` (path: uuid)

## openportal-unmanaged-projects
Module: `waldur_api_client.api.openportal_unmanaged_projects`

- `openportal_unmanaged_projects_list` GET `/api/openportal-unmanaged-projects/` — List projects (19 query params)
- `openportal_unmanaged_projects_count` HEAD `/api/openportal-unmanaged-projects/` — List projects (18 query params)
- `openportal_unmanaged_projects_create` POST `/api/openportal-unmanaged-projects/` — Create a new project (request body)
- `openportal_unmanaged_projects_checklist_template_retrieve` GET `/api/openportal-unmanaged-projects/checklist-template/` — Get checklist template for creating new objects (1 query param)
- `openportal_unmanaged_projects_checklist_template_count` HEAD `/api/openportal-unmanaged-projects/checklist-template/` — Get number of items in the collection matching the request parameters (1 query param)
- `openportal_unmanaged_projects_retrieve` GET `/api/openportal-unmanaged-projects/{uuid}/` — Retrieve project details (path: uuid | 1 query param)
- `openportal_unmanaged_projects_update` PUT `/api/openportal-unmanaged-projects/{uuid}/` — Update project details (path: uuid | request body)
- `openportal_unmanaged_projects_partial_update` PATCH `/api/openportal-unmanaged-projects/{uuid}/` — Partially update project details (path: uuid | request body)
- `openportal_unmanaged_projects_destroy` DELETE `/api/openportal-unmanaged-projects/{uuid}/` — Delete a project (path: uuid)
- `openportal_unmanaged_projects_add_user` POST `/api/openportal-unmanaged-projects/{uuid}/add_user/` — Grant a role to a user (path: uuid | request body)
- `openportal_unmanaged_projects_checklist_retrieve` GET `/api/openportal-unmanaged-projects/{uuid}/checklist/` — Get checklist with questions and existing answers (path: uuid | 1 query param)
- `openportal_unmanaged_projects_completion_status_retrieve` GET `/api/openportal-unmanaged-projects/{uuid}/completion_status/` — Get checklist completion status (path: uuid)
- `openportal_unmanaged_projects_delete_user` POST `/api/openportal-unmanaged-projects/{uuid}/delete_user/` — Revoke a role from a user (path: uuid | request body)
- `openportal_unmanaged_projects_list_users_list` GET `/api/openportal-unmanaged-projects/{uuid}/list_users/` — List users and their roles in a scope (path: uuid | 10 query params)
- `openportal_unmanaged_projects_move_project` POST `/api/openportal-unmanaged-projects/{uuid}/move_project/` — Move project to another customer (path: uuid | request body)
- `openportal_unmanaged_projects_recover` POST `/api/openportal-unmanaged-projects/{uuid}/recover/` — Recover a soft-deleted project (path: uuid | request body)
- `openportal_unmanaged_projects_stats_retrieve` GET `/api/openportal-unmanaged-projects/{uuid}/stats/` — Get project resource usage statistics (path: uuid | 1 query param)
- `openportal_unmanaged_projects_submit_answers` POST `/api/openportal-unmanaged-projects/{uuid}/submit_answers/` — Submit checklist answers (path: uuid | request body)
- `openportal_unmanaged_projects_update_user` POST `/api/openportal-unmanaged-projects/{uuid}/update_user/` — Update a user's role expiration (path: uuid | request body)

## openportal-userinfo
Module: `waldur_api_client.api.openportal_userinfo`

- `openportal_userinfo_list` GET `/api/openportal-userinfo/` (2 query params)
- `openportal_userinfo_count` HEAD `/api/openportal-userinfo/` — Get number of items in the collection matching the request parameters (2 query params)
- `openportal_userinfo_create` POST `/api/openportal-userinfo/` (request body)
- `openportal_userinfo_me_retrieve` GET `/api/openportal-userinfo/me/` (no params)
- `openportal_userinfo_me_count` HEAD `/api/openportal-userinfo/me/` — Get number of items in the collection matching the request parameters (no params)
- `openportal_userinfo_retrieve` GET `/api/openportal-userinfo/{user}/` (path: user)
- `openportal_userinfo_update` PUT `/api/openportal-userinfo/{user}/` (path: user | request body)
- `openportal_userinfo_partial_update` PATCH `/api/openportal-userinfo/{user}/` (path: user | request body)
- `openportal_userinfo_destroy` DELETE `/api/openportal-userinfo/{user}/` (path: user)
- `openportal_userinfo_set_shortname_update` PUT `/api/openportal-userinfo/{user}/set_shortname/` (path: user | request body)

## openstack
Module: `waldur_api_client.api.openstack`

- `openstack_discovery_list` GET `/api/openstack/discovery/` (no params)
- `openstack_discovery_create` POST `/api/openstack/discovery/` (no params)
- `openstack_discovery_discover_external_networks` POST `/api/openstack/discovery/discover_external_networks/` — Discover available external networks (request body)
- `openstack_discovery_discover_flavors` POST `/api/openstack/discovery/discover_flavors/` — Discover available flavors (request body)
- `openstack_discovery_discover_instance_availability_zones` POST `/api/openstack/discovery/discover_instance_availability_zones/` — Discover available Nova instance availability zones (request body)
- `openstack_discovery_discover_volume_availability_zones` POST `/api/openstack/discovery/discover_volume_availability_zones/` — Discover available Cinder volume availability zones (request body)
- `openstack_discovery_discover_volume_types` POST `/api/openstack/discovery/discover_volume_types/` — Discover available volume types (request body)
- `openstack_discovery_preview_service_attributes` POST `/api/openstack/discovery/preview_service_attributes/` — Build service_attributes and plugin_options from selected values (request body)
- `openstack_discovery_validate_credentials` POST `/api/openstack/discovery/validate_credentials/` — Validate OpenStack credentials without saving them (request body)
- `openstack_discovery_retrieve` GET `/api/openstack/discovery/{id}/` (path: id)
- `openstack_discovery_update` PUT `/api/openstack/discovery/{id}/` (path: id)
- `openstack_discovery_partial_update` PATCH `/api/openstack/discovery/{id}/` (path: id)
- `openstack_discovery_destroy` DELETE `/api/openstack/discovery/{id}/` (path: id)

## openstack-backups
Module: `waldur_api_client.api.openstack_backups`

- `openstack_backups_list` GET `/api/openstack-backups/` — List backups (23 query params)
- `openstack_backups_count` HEAD `/api/openstack-backups/` — List backups (22 query params)
- `openstack_backups_retrieve` GET `/api/openstack-backups/{uuid}/` — Get backup details (path: uuid | 1 query param)
- `openstack_backups_update` PUT `/api/openstack-backups/{uuid}/` — Update backup (path: uuid | request body)
- `openstack_backups_partial_update` PATCH `/api/openstack-backups/{uuid}/` — Partially update backup (path: uuid | request body)
- `openstack_backups_destroy` DELETE `/api/openstack-backups/{uuid}/` — Delete backup (path: uuid)
- `openstack_backups_pull` POST `/api/openstack-backups/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `openstack_backups_restore` POST `/api/openstack-backups/{uuid}/restore/` — Restore instance from backup (path: uuid | request body)
- `openstack_backups_set_erred` POST `/api/openstack-backups/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `openstack_backups_set_ok` POST `/api/openstack-backups/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `openstack_backups_unlink` POST `/api/openstack-backups/{uuid}/unlink/` — Unlink resource (path: uuid)

## openstack-external-networks
Module: `waldur_api_client.api.openstack_external_networks`

- `openstack_external_networks_list` GET `/api/openstack-external-networks/` — List external networks (5 query params)
- `openstack_external_networks_count` HEAD `/api/openstack-external-networks/` — List external networks (4 query params)
- `openstack_external_networks_retrieve` GET `/api/openstack-external-networks/{uuid}/` — Get external network details (path: uuid | 1 query param)

## openstack-flavors
Module: `waldur_api_client.api.openstack_flavors`

- `openstack_flavors_list` GET `/api/openstack-flavors/` — List flavors (19 query params)
- `openstack_flavors_count` HEAD `/api/openstack-flavors/` — List flavors (18 query params)
- `openstack_flavors_usage_stats_retrieve` GET `/api/openstack-flavors/usage_stats/` — Get flavor usage statistics (1 query param)
- `openstack_flavors_usage_stats_count` HEAD `/api/openstack-flavors/usage_stats/` — Get flavor usage statistics (no params)
- `openstack_flavors_retrieve` GET `/api/openstack-flavors/{uuid}/` — Get flavor details (path: uuid | 1 query param)

## openstack-floating-ips
Module: `waldur_api_client.api.openstack_floating_ips`

- `openstack_floating_ips_list` GET `/api/openstack-floating-ips/` — List floating IPs (24 query params)
- `openstack_floating_ips_count` HEAD `/api/openstack-floating-ips/` — List floating IPs (23 query params)
- `openstack_floating_ips_retrieve` GET `/api/openstack-floating-ips/{uuid}/` — Get floating IP details (path: uuid | 1 query param)
- `openstack_floating_ips_destroy` DELETE `/api/openstack-floating-ips/{uuid}/` — Delete floating IP (path: uuid)
- `openstack_floating_ips_attach_to_port` POST `/api/openstack-floating-ips/{uuid}/attach_to_port/` — Attach floating IP to a port (path: uuid | request body)
- `openstack_floating_ips_detach_from_port` POST `/api/openstack-floating-ips/{uuid}/detach_from_port/` — Detach floating IP from port (path: uuid)
- `openstack_floating_ips_pull` POST `/api/openstack-floating-ips/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `openstack_floating_ips_set_erred` POST `/api/openstack-floating-ips/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `openstack_floating_ips_set_ok` POST `/api/openstack-floating-ips/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `openstack_floating_ips_unlink` POST `/api/openstack-floating-ips/{uuid}/unlink/` — Unlink resource (path: uuid)
- `openstack_floating_ips_update_description` POST `/api/openstack-floating-ips/{uuid}/update_description/` — Update floating IP description (path: uuid | request body)

## openstack-images
Module: `waldur_api_client.api.openstack_images`

- `openstack_images_list` GET `/api/openstack-images/` — List images (8 query params)
- `openstack_images_count` HEAD `/api/openstack-images/` — List images (8 query params)
- `openstack_images_usage_stats_retrieve` GET `/api/openstack-images/usage_stats/` — Get image usage statistics (no params)
- `openstack_images_usage_stats_count` HEAD `/api/openstack-images/usage_stats/` — Get image usage statistics (no params)
- `openstack_images_retrieve` GET `/api/openstack-images/{uuid}/` — Get image details (path: uuid)

## openstack-instance-availability-zones
Module: `waldur_api_client.api.openstack_instance_availability_zones`

- `openstack_instance_availability_zones_list` GET `/api/openstack-instance-availability-zones/` — List instance availability zones (6 query params)
- `openstack_instance_availability_zones_count` HEAD `/api/openstack-instance-availability-zones/` — List instance availability zones (6 query params)
- `openstack_instance_availability_zones_retrieve` GET `/api/openstack-instance-availability-zones/{uuid}/` — Get instance availability zone details (path: uuid)

## openstack-instances
Module: `waldur_api_client.api.openstack_instances`

- `openstack_instances_list` GET `/api/openstack-instances/` — List instances (25 query params)
- `openstack_instances_count` HEAD `/api/openstack-instances/` — List instances (24 query params)
- `openstack_instances_retrieve` GET `/api/openstack-instances/{uuid}/` — Get instance details (path: uuid | 1 query param)
- `openstack_instances_update` PUT `/api/openstack-instances/{uuid}/` — Update instance (path: uuid | request body)
- `openstack_instances_partial_update` PATCH `/api/openstack-instances/{uuid}/` — Partially update instance (path: uuid | request body)
- `openstack_instances_backup` POST `/api/openstack-instances/{uuid}/backup/` — Create instance backup (path: uuid | request body)
- `openstack_instances_change_flavor` POST `/api/openstack-instances/{uuid}/change_flavor/` — Change instance flavor (path: uuid | request body)
- `openstack_instances_console_retrieve` GET `/api/openstack-instances/{uuid}/console/` — Get console URL (path: uuid)
- `openstack_instances_console_log_retrieve` GET `/api/openstack-instances/{uuid}/console_log/` — Get console log (path: uuid | 1 query param)
- `openstack_instances_floating_ips_list` GET `/api/openstack-instances/{uuid}/floating_ips/` — List instance floating IPs (path: uuid)
- `openstack_instances_ports_list` GET `/api/openstack-instances/{uuid}/ports/` — List instance ports (path: uuid)
- `openstack_instances_pull` POST `/api/openstack-instances/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `openstack_instances_restart` POST `/api/openstack-instances/{uuid}/restart/` — Restart instance (path: uuid)
- `openstack_instances_set_erred` POST `/api/openstack-instances/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `openstack_instances_set_ok` POST `/api/openstack-instances/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `openstack_instances_start` POST `/api/openstack-instances/{uuid}/start/` — Start instance (path: uuid)
- `openstack_instances_stop` POST `/api/openstack-instances/{uuid}/stop/` — Stop instance (path: uuid)
- `openstack_instances_unlink` POST `/api/openstack-instances/{uuid}/unlink/` — Unlink resource (path: uuid)
- `openstack_instances_update_allowed_address_pairs` POST `/api/openstack-instances/{uuid}/update_allowed_address_pairs/` — Update instance allowed address pairs (path: uuid | request body)
- `openstack_instances_update_floating_ips` POST `/api/openstack-instances/{uuid}/update_floating_ips/` — Update instance floating IPs (path: uuid | request body)
- `openstack_instances_update_ports` POST `/api/openstack-instances/{uuid}/update_ports/` — Update instance ports (path: uuid | request body)
- `openstack_instances_update_security_groups` POST `/api/openstack-instances/{uuid}/update_security_groups/` — Update instance security groups (path: uuid | request body)

## openstack-marketplace-tenants
Module: `waldur_api_client.api.openstack_marketplace_tenants`

- `openstack_marketplace_tenants_list` GET `/api/openstack-marketplace-tenants/` (18 query params)
- `openstack_marketplace_tenants_count` HEAD `/api/openstack-marketplace-tenants/` — Get number of items in the collection matching the request parameters (18 query params)
- `openstack_marketplace_tenants_retrieve` GET `/api/openstack-marketplace-tenants/{uuid}/` (path: uuid)
- `openstack_marketplace_tenants_create_image` POST `/api/openstack-marketplace-tenants/{uuid}/create_image/` (path: uuid | request body)
- `openstack_marketplace_tenants_upload_image_data` POST `/api/openstack-marketplace-tenants/{uuid}/upload_image_data/{image_id}/` (path: image_id, uuid | request body)

## openstack-migrations
Module: `waldur_api_client.api.openstack_migrations`

- `openstack_migrations_list` GET `/api/openstack-migrations/` (2 query params)
- `openstack_migrations_count` HEAD `/api/openstack-migrations/` — Get number of items in the collection matching the request parameters (2 query params)
- `openstack_migrations_create` POST `/api/openstack-migrations/` (request body)
- `openstack_migrations_retrieve` GET `/api/openstack-migrations/{uuid}/` (path: uuid)
- `openstack_migrations_update` PUT `/api/openstack-migrations/{uuid}/` (path: uuid | request body)
- `openstack_migrations_partial_update` PATCH `/api/openstack-migrations/{uuid}/` (path: uuid | request body)
- `openstack_migrations_destroy` DELETE `/api/openstack-migrations/{uuid}/` (path: uuid)

## openstack-network-rbac-policies
Module: `waldur_api_client.api.openstack_network_rbac_policies`

- `openstack_network_rbac_policies_list` GET `/api/openstack-network-rbac-policies/` — List network RBAC policies (7 query params)
- `openstack_network_rbac_policies_count` HEAD `/api/openstack-network-rbac-policies/` — List network RBAC policies (7 query params)
- `openstack_network_rbac_policies_create` POST `/api/openstack-network-rbac-policies/` — Create RBAC policy (request body)
- `openstack_network_rbac_policies_retrieve` GET `/api/openstack-network-rbac-policies/{uuid}/` — Get network RBAC policy details (path: uuid)
- `openstack_network_rbac_policies_update` PUT `/api/openstack-network-rbac-policies/{uuid}/` (path: uuid | request body)
- `openstack_network_rbac_policies_partial_update` PATCH `/api/openstack-network-rbac-policies/{uuid}/` (path: uuid | request body)
- `openstack_network_rbac_policies_destroy` DELETE `/api/openstack-network-rbac-policies/{uuid}/` — Delete RBAC policy (path: uuid)

## openstack-networks
Module: `waldur_api_client.api.openstack_networks`

- `openstack_networks_list` GET `/api/openstack-networks/` — List networks (25 query params)
- `openstack_networks_count` HEAD `/api/openstack-networks/` — List networks (24 query params)
- `openstack_networks_retrieve` GET `/api/openstack-networks/{uuid}/` — Get network details (path: uuid | 1 query param)
- `openstack_networks_update` PUT `/api/openstack-networks/{uuid}/` — Update network (path: uuid | request body)
- `openstack_networks_partial_update` PATCH `/api/openstack-networks/{uuid}/` — Partially update network (path: uuid | request body)
- `openstack_networks_destroy` DELETE `/api/openstack-networks/{uuid}/` — Delete network (path: uuid)
- `openstack_networks_create_subnet` POST `/api/openstack-networks/{uuid}/create_subnet/` — Create subnet (path: uuid | request body)
- `openstack_networks_pull` POST `/api/openstack-networks/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `openstack_networks_rbac_policy_create` POST `/api/openstack-networks/{uuid}/rbac_policy_create/` — Create RBAC policy (path: uuid | request body)
- `openstack_networks_rbac_policy_delete_destroy` DELETE `/api/openstack-networks/{uuid}/rbac_policy_delete/{rbac_policy_uuid}/` — Delete RBAC policy (path: rbac_policy_uuid, uuid)
- `openstack_networks_set_erred` POST `/api/openstack-networks/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `openstack_networks_set_mtu` POST `/api/openstack-networks/{uuid}/set_mtu/` — Set network MTU (path: uuid | request body)
- `openstack_networks_set_ok` POST `/api/openstack-networks/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `openstack_networks_unlink` POST `/api/openstack-networks/{uuid}/unlink/` — Unlink resource (path: uuid)

## openstack-ports
Module: `waldur_api_client.api.openstack_ports`

- `openstack_ports_list` GET `/api/openstack-ports/` — List ports (18 query params)
- `openstack_ports_count` HEAD `/api/openstack-ports/` — List ports (17 query params)
- `openstack_ports_create` POST `/api/openstack-ports/` — Create port (request body)
- `openstack_ports_retrieve` GET `/api/openstack-ports/{uuid}/` — Get port details (path: uuid | 1 query param)
- `openstack_ports_update` PUT `/api/openstack-ports/{uuid}/` — Update port (path: uuid | request body)
- `openstack_ports_partial_update` PATCH `/api/openstack-ports/{uuid}/` — Partially update port (path: uuid | request body)
- `openstack_ports_destroy` DELETE `/api/openstack-ports/{uuid}/` — Delete port (path: uuid)
- `openstack_ports_disable_port` POST `/api/openstack-ports/{uuid}/disable_port/` — Disable port (path: uuid)
- `openstack_ports_disable_port_security` POST `/api/openstack-ports/{uuid}/disable_port_security/` — Disable port security (path: uuid)
- `openstack_ports_enable_port` POST `/api/openstack-ports/{uuid}/enable_port/` — Enable port (path: uuid)
- `openstack_ports_enable_port_security` POST `/api/openstack-ports/{uuid}/enable_port_security/` — Enable port security (path: uuid)
- `openstack_ports_pull` POST `/api/openstack-ports/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `openstack_ports_set_erred` POST `/api/openstack-ports/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `openstack_ports_set_ok` POST `/api/openstack-ports/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `openstack_ports_unlink` POST `/api/openstack-ports/{uuid}/unlink/` — Unlink resource (path: uuid)
- `openstack_ports_update_port_ip` POST `/api/openstack-ports/{uuid}/update_port_ip/` — Update port IP address (path: uuid | request body)
- `openstack_ports_update_security_groups` POST `/api/openstack-ports/{uuid}/update_security_groups/` — Update port security groups (path: uuid | request body)

## openstack-routers
Module: `waldur_api_client.api.openstack_routers`

- `openstack_routers_list` GET `/api/openstack-routers/` — List routers (6 query params)
- `openstack_routers_count` HEAD `/api/openstack-routers/` — List routers (5 query params)
- `openstack_routers_create` POST `/api/openstack-routers/` — Create router (request body)
- `openstack_routers_retrieve` GET `/api/openstack-routers/{uuid}/` — Get router details (path: uuid | 1 query param)
- `openstack_routers_destroy` DELETE `/api/openstack-routers/{uuid}/` — Delete router (path: uuid)
- `openstack_routers_add_router_interface` POST `/api/openstack-routers/{uuid}/add_router_interface/` — Add router interface (path: uuid | request body)
- `openstack_routers_remove_router_interface` POST `/api/openstack-routers/{uuid}/remove_router_interface/` — Remove router interface (path: uuid | request body)
- `openstack_routers_set_erred` POST `/api/openstack-routers/{uuid}/set_erred/` — Mark router as ERRED (path: uuid | request body)
- `openstack_routers_set_ok` POST `/api/openstack-routers/{uuid}/set_ok/` — Mark router as OK (path: uuid)
- `openstack_routers_set_routes` POST `/api/openstack-routers/{uuid}/set_routes/` — Set static routes (path: uuid | request body)

## openstack-security-groups
Module: `waldur_api_client.api.openstack_security_groups`

- `openstack_security_groups_list` GET `/api/openstack-security-groups/` — List security groups (22 query params)
- `openstack_security_groups_count` HEAD `/api/openstack-security-groups/` — List security groups (21 query params)
- `openstack_security_groups_retrieve` GET `/api/openstack-security-groups/{uuid}/` — Get security group details (path: uuid | 1 query param)
- `openstack_security_groups_update` PUT `/api/openstack-security-groups/{uuid}/` (path: uuid | request body)
- `openstack_security_groups_partial_update` PATCH `/api/openstack-security-groups/{uuid}/` — Partially update security group (path: uuid | request body)
- `openstack_security_groups_destroy` DELETE `/api/openstack-security-groups/{uuid}/` — Delete security group (path: uuid)
- `openstack_security_groups_pull` POST `/api/openstack-security-groups/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `openstack_security_groups_set_erred` POST `/api/openstack-security-groups/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `openstack_security_groups_set_ok` POST `/api/openstack-security-groups/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `openstack_security_groups_set_rules` POST `/api/openstack-security-groups/{uuid}/set_rules/` — Set security group rules (path: uuid | request body)
- `openstack_security_groups_unlink` POST `/api/openstack-security-groups/{uuid}/unlink/` — Unlink resource (path: uuid)

## openstack-server-groups
Module: `waldur_api_client.api.openstack_server_groups`

- `openstack_server_groups_list` GET `/api/openstack-server-groups/` — List server groups (21 query params)
- `openstack_server_groups_count` HEAD `/api/openstack-server-groups/` — List server groups (20 query params)
- `openstack_server_groups_create` POST `/api/openstack-server-groups/` (request body)
- `openstack_server_groups_retrieve` GET `/api/openstack-server-groups/{uuid}/` — Get server group details (path: uuid | 1 query param)
- `openstack_server_groups_destroy` DELETE `/api/openstack-server-groups/{uuid}/` — Delete server group (path: uuid)
- `openstack_server_groups_pull` POST `/api/openstack-server-groups/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `openstack_server_groups_set_erred` POST `/api/openstack-server-groups/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `openstack_server_groups_set_ok` POST `/api/openstack-server-groups/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `openstack_server_groups_unlink` POST `/api/openstack-server-groups/{uuid}/unlink/` — Unlink resource (path: uuid)

## openstack-snapshots
Module: `waldur_api_client.api.openstack_snapshots`

- `openstack_snapshots_list` GET `/api/openstack-snapshots/` — List snapshots (26 query params)
- `openstack_snapshots_count` HEAD `/api/openstack-snapshots/` — List snapshots (25 query params)
- `openstack_snapshots_retrieve` GET `/api/openstack-snapshots/{uuid}/` — Get snapshot details (path: uuid | 1 query param)
- `openstack_snapshots_update` PUT `/api/openstack-snapshots/{uuid}/` — Update snapshot (path: uuid | request body)
- `openstack_snapshots_partial_update` PATCH `/api/openstack-snapshots/{uuid}/` — Partially update snapshot (path: uuid | request body)
- `openstack_snapshots_destroy` DELETE `/api/openstack-snapshots/{uuid}/` — Delete snapshot (path: uuid)
- `openstack_snapshots_pull` POST `/api/openstack-snapshots/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `openstack_snapshots_restorations_list` GET `/api/openstack-snapshots/{uuid}/restorations/` — List snapshot restorations (path: uuid)
- `openstack_snapshots_restore` POST `/api/openstack-snapshots/{uuid}/restore/` — Restore volume from snapshot (path: uuid | request body)
- `openstack_snapshots_set_erred` POST `/api/openstack-snapshots/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `openstack_snapshots_set_ok` POST `/api/openstack-snapshots/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `openstack_snapshots_unlink` POST `/api/openstack-snapshots/{uuid}/unlink/` — Unlink resource (path: uuid)

## openstack-subnets
Module: `waldur_api_client.api.openstack_subnets`

- `openstack_subnets_list` GET `/api/openstack-subnets/` — List subnets (27 query params)
- `openstack_subnets_count` HEAD `/api/openstack-subnets/` — List subnets (26 query params)
- `openstack_subnets_retrieve` GET `/api/openstack-subnets/{uuid}/` — Get subnet details (path: uuid | 1 query param)
- `openstack_subnets_update` PUT `/api/openstack-subnets/{uuid}/` — Update subnet (path: uuid | request body)
- `openstack_subnets_partial_update` PATCH `/api/openstack-subnets/{uuid}/` — Partially update subnet (path: uuid | request body)
- `openstack_subnets_destroy` DELETE `/api/openstack-subnets/{uuid}/` — Delete subnet (path: uuid)
- `openstack_subnets_connect` POST `/api/openstack-subnets/{uuid}/connect/` — Connect subnet to router (path: uuid)
- `openstack_subnets_disconnect` POST `/api/openstack-subnets/{uuid}/disconnect/` — Disconnect subnet from router (path: uuid)
- `openstack_subnets_pull` POST `/api/openstack-subnets/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `openstack_subnets_set_erred` POST `/api/openstack-subnets/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `openstack_subnets_set_ok` POST `/api/openstack-subnets/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `openstack_subnets_unlink` POST `/api/openstack-subnets/{uuid}/unlink/` — Unlink resource (path: uuid)

## openstack-tenants
Module: `waldur_api_client.api.openstack_tenants`

- `openstack_tenants_list` GET `/api/openstack-tenants/` — List tenants (19 query params)
- `openstack_tenants_count` HEAD `/api/openstack-tenants/` — List tenants (18 query params)
- `openstack_tenants_retrieve` GET `/api/openstack-tenants/{uuid}/` — Get tenant details (path: uuid | 1 query param)
- `openstack_tenants_update` PUT `/api/openstack-tenants/{uuid}/` — Update tenant (path: uuid | request body)
- `openstack_tenants_partial_update` PATCH `/api/openstack-tenants/{uuid}/` — Partially update tenant (path: uuid | request body)
- `openstack_tenants_backend_instances_list` GET `/api/openstack-tenants/{uuid}/backend_instances/` — List backend instances (path: uuid | 18 query params)
- `openstack_tenants_backend_volumes_list` GET `/api/openstack-tenants/{uuid}/backend_volumes/` — List backend volumes (path: uuid | 18 query params)
- `openstack_tenants_change_password` POST `/api/openstack-tenants/{uuid}/change_password/` — Change tenant user password (path: uuid | request body)
- `openstack_tenants_create_floating_ip` POST `/api/openstack-tenants/{uuid}/create_floating_ip/` — Create floating IP for tenant (path: uuid | request body)
- `openstack_tenants_create_network` POST `/api/openstack-tenants/{uuid}/create_network/` — Create network for tenant (path: uuid | request body)
- `openstack_tenants_create_security_group` POST `/api/openstack-tenants/{uuid}/create_security_group/` — Create security group (path: uuid | request body)
- `openstack_tenants_create_server_group` POST `/api/openstack-tenants/{uuid}/create_server_group/` — Create server group (path: uuid | request body)
- `openstack_tenants_pull` POST `/api/openstack-tenants/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `openstack_tenants_pull_floating_ips` POST `/api/openstack-tenants/{uuid}/pull_floating_ips/` — Pull floating IPs (path: uuid)
- `openstack_tenants_pull_quotas` POST `/api/openstack-tenants/{uuid}/pull_quotas/` — Pull tenant quotas (path: uuid)
- `openstack_tenants_pull_security_groups` POST `/api/openstack-tenants/{uuid}/pull_security_groups/` — Pull security groups (path: uuid)
- `openstack_tenants_pull_server_groups` POST `/api/openstack-tenants/{uuid}/pull_server_groups/` — Pull server groups (path: uuid)
- `openstack_tenants_push_security_groups` POST `/api/openstack-tenants/{uuid}/push_security_groups/` — Batch update security groups for a tenant. (path: uuid | request body)
- `openstack_tenants_set_erred` POST `/api/openstack-tenants/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `openstack_tenants_set_ok` POST `/api/openstack-tenants/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `openstack_tenants_set_quotas` POST `/api/openstack-tenants/{uuid}/set_quotas/` — Set tenant quotas (path: uuid | request body)
- `openstack_tenants_unlink` POST `/api/openstack-tenants/{uuid}/unlink/` — Unlink resource (path: uuid)

## openstack-volume-availability-zones
Module: `waldur_api_client.api.openstack_volume_availability_zones`

- `openstack_volume_availability_zones_list` GET `/api/openstack-volume-availability-zones/` — List volume availability zones (6 query params)
- `openstack_volume_availability_zones_count` HEAD `/api/openstack-volume-availability-zones/` — List volume availability zones (6 query params)
- `openstack_volume_availability_zones_retrieve` GET `/api/openstack-volume-availability-zones/{uuid}/` — Get volume availability zone details (path: uuid)

## openstack-volume-types
Module: `waldur_api_client.api.openstack_volume_types`

- `openstack_volume_types_list` GET `/api/openstack-volume-types/` — List volume types (7 query params)
- `openstack_volume_types_count` HEAD `/api/openstack-volume-types/` — List volume types (7 query params)
- `openstack_volume_types_names_retrieve` GET `/api/openstack-volume-types/names/` — List unique volume type names (no params)
- `openstack_volume_types_names_count` HEAD `/api/openstack-volume-types/names/` — List unique volume type names (no params)
- `openstack_volume_types_retrieve` GET `/api/openstack-volume-types/{uuid}/` — Get volume type details (path: uuid)

## openstack-volumes
Module: `waldur_api_client.api.openstack_volumes`

- `openstack_volumes_list` GET `/api/openstack-volumes/` — List volumes (28 query params)
- `openstack_volumes_count` HEAD `/api/openstack-volumes/` — List volumes (27 query params)
- `openstack_volumes_retrieve` GET `/api/openstack-volumes/{uuid}/` — Get volume details (path: uuid | 1 query param)
- `openstack_volumes_update` PUT `/api/openstack-volumes/{uuid}/` — Update volume (path: uuid | request body)
- `openstack_volumes_partial_update` PATCH `/api/openstack-volumes/{uuid}/` — Partially update volume (path: uuid | request body)
- `openstack_volumes_attach` POST `/api/openstack-volumes/{uuid}/attach/` — Attach volume to instance (path: uuid | request body)
- `openstack_volumes_detach` POST `/api/openstack-volumes/{uuid}/detach/` — Detach volume from instance (path: uuid)
- `openstack_volumes_extend` POST `/api/openstack-volumes/{uuid}/extend/` — Extend volume size (path: uuid | request body)
- `openstack_volumes_pull` POST `/api/openstack-volumes/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `openstack_volumes_retype` POST `/api/openstack-volumes/{uuid}/retype/` — Change volume type (path: uuid | request body)
- `openstack_volumes_set_erred` POST `/api/openstack-volumes/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `openstack_volumes_set_ok` POST `/api/openstack-volumes/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `openstack_volumes_snapshot` POST `/api/openstack-volumes/{uuid}/snapshot/` — Create volume snapshot (path: uuid | request body)
- `openstack_volumes_unlink` POST `/api/openstack-volumes/{uuid}/unlink/` — Unlink resource (path: uuid)

## organization-groups
Module: `waldur_api_client.api.organization_groups`

- `organization_groups_list` GET `/api/organization-groups/` (4 query params)
- `organization_groups_count` HEAD `/api/organization-groups/` — Get number of items in the collection matching the request parameters (4 query params)
- `organization_groups_create` POST `/api/organization-groups/` (request body)
- `organization_groups_retrieve` GET `/api/organization-groups/{uuid}/` (path: uuid)
- `organization_groups_update` PUT `/api/organization-groups/{uuid}/` (path: uuid | request body)
- `organization_groups_partial_update` PATCH `/api/organization-groups/{uuid}/` (path: uuid | request body)
- `organization_groups_destroy` DELETE `/api/organization-groups/{uuid}/` (path: uuid)

## override-settings
Module: `waldur_api_client.api.override_settings`

- `override_settings_retrieve` GET `/api/override-settings/` — Get all overridable settings (no params)
- `override_settings` POST `/api/override-settings/` — Update overridable settings (request body)

## payment-profiles
Module: `waldur_api_client.api.payment_profiles`

- `payment_profiles_list` GET `/api/payment-profiles/` (5 query params)
- `payment_profiles_count` HEAD `/api/payment-profiles/` — Get number of items in the collection matching the request parameters (5 query params)
- `payment_profiles_create` POST `/api/payment-profiles/` (request body)
- `payment_profiles_retrieve` GET `/api/payment-profiles/{uuid}/` (path: uuid)
- `payment_profiles_update` PUT `/api/payment-profiles/{uuid}/` (path: uuid | request body)
- `payment_profiles_partial_update` PATCH `/api/payment-profiles/{uuid}/` (path: uuid | request body)
- `payment_profiles_destroy` DELETE `/api/payment-profiles/{uuid}/` (path: uuid)
- `payment_profiles_enable` POST `/api/payment-profiles/{uuid}/enable/` (path: uuid)

## payments
Module: `waldur_api_client.api.payments`

- `payments_list` GET `/api/payments/` (3 query params)
- `payments_count` HEAD `/api/payments/` — Get number of items in the collection matching the request parameters (3 query params)
- `payments_create` POST `/api/payments/` (request body)
- `payments_retrieve` GET `/api/payments/{uuid}/` (path: uuid)
- `payments_update` PUT `/api/payments/{uuid}/` (path: uuid | request body)
- `payments_partial_update` PATCH `/api/payments/{uuid}/` (path: uuid | request body)
- `payments_destroy` DELETE `/api/payments/{uuid}/` (path: uuid)
- `payments_link_to_invoice` POST `/api/payments/{uuid}/link_to_invoice/` — Link a payment to an invoice (path: uuid | request body)
- `payments_unlink_from_invoice` POST `/api/payments/{uuid}/unlink_from_invoice/` — Unlink a payment from an invoice (path: uuid)

## project-credits
Module: `waldur_api_client.api.project_credits`

- `project_credits_list` GET `/api/project-credits/` (7 query params)
- `project_credits_count` HEAD `/api/project-credits/` — Get number of items in the collection matching the request parameters (7 query params)
- `project_credits_create` POST `/api/project-credits/` (request body)
- `project_credits_retrieve` GET `/api/project-credits/{uuid}/` (path: uuid)
- `project_credits_update` PUT `/api/project-credits/{uuid}/` (path: uuid | request body)
- `project_credits_partial_update` PATCH `/api/project-credits/{uuid}/` (path: uuid | request body)
- `project_credits_destroy` DELETE `/api/project-credits/{uuid}/` (path: uuid)

## project-permissions-reviews
Module: `waldur_api_client.api.project_permissions_reviews`

- `project_permissions_reviews_list` GET `/api/project-permissions-reviews/` (5 query params)
- `project_permissions_reviews_count` HEAD `/api/project-permissions-reviews/` — Get number of items in the collection matching the request parameters (5 query params)
- `project_permissions_reviews_retrieve` GET `/api/project-permissions-reviews/{uuid}/` (path: uuid)
- `project_permissions_reviews_close` POST `/api/project-permissions-reviews/{uuid}/close/` — Close project permission review (path: uuid)

## project-quotas
Module: `waldur_api_client.api.project_quotas`

- `project_quotas_list` GET `/api/project-quotas/` — List project quotas (no params)
- `project_quotas_count` HEAD `/api/project-quotas/` — Get number of items in the collection matching the request parameters (no params)

## project-types
Module: `waldur_api_client.api.project_types`

- `project_types_list` GET `/api/project-types/` — List project types (2 query params)
- `project_types_count` HEAD `/api/project-types/` — List project types (2 query params)
- `project_types_retrieve` GET `/api/project-types/{uuid}/` — Retrieve project type details (path: uuid)

## projects
Module: `waldur_api_client.api.projects`

- `projects_list` GET `/api/projects/` — List projects (19 query params)
- `projects_count` HEAD `/api/projects/` — List projects (18 query params)
- `projects_create` POST `/api/projects/` — Create a new project (request body)
- `projects_checklist_template_retrieve` GET `/api/projects/checklist-template/` — Get checklist template for creating new objects (1 query param)
- `projects_checklist_template_count` HEAD `/api/projects/checklist-template/` — Get number of items in the collection matching the request parameters (1 query param)
- `projects_other_users_list` GET `/api/projects/{project_uuid}/other_users/` — A list of users which can be added to the current project from other projects of the same customer (path: project_uuid | 16 query params)
- `projects_retrieve` GET `/api/projects/{uuid}/` — Retrieve project details (path: uuid | 1 query param)
- `projects_update` PUT `/api/projects/{uuid}/` — Update project details (path: uuid | request body)
- `projects_partial_update` PATCH `/api/projects/{uuid}/` — Partially update project details (path: uuid | request body)
- `projects_destroy` DELETE `/api/projects/{uuid}/` — Delete a project (path: uuid)
- `projects_add_user` POST `/api/projects/{uuid}/add_user/` — Grant a role to a user (path: uuid | request body)
- `projects_checklist_retrieve` GET `/api/projects/{uuid}/checklist/` — Get checklist with questions and existing answers (path: uuid | 1 query param)
- `projects_completion_status_retrieve` GET `/api/projects/{uuid}/completion_status/` — Get checklist completion status (path: uuid)
- `projects_delete_user` POST `/api/projects/{uuid}/delete_user/` — Revoke a role from a user (path: uuid | request body)
- `projects_list_users_list` GET `/api/projects/{uuid}/list_users/` — List users and their roles in a scope (path: uuid | 10 query params)
- `projects_move_project` POST `/api/projects/{uuid}/move_project/` — Move project to another customer (path: uuid | request body)
- `projects_recover` POST `/api/projects/{uuid}/recover/` — Recover a soft-deleted project (path: uuid | request body)
- `projects_stats_retrieve` GET `/api/projects/{uuid}/stats/` — Get project resource usage statistics (path: uuid | 1 query param)
- `projects_submit_answers` POST `/api/projects/{uuid}/submit_answers/` — Submit checklist answers (path: uuid | request body)
- `projects_sync_user_roles` POST `/api/projects/{uuid}/sync_user_roles/` — Trigger user role sync for this project (path: uuid)
- `projects_update_user` POST `/api/projects/{uuid}/update_user/` — Update a user's role expiration (path: uuid | request body)

## promotions-campaigns
Module: `waldur_api_client.api.promotions_campaigns`

- `promotions_campaigns_list` GET `/api/promotions-campaigns/` (9 query params)
- `promotions_campaigns_count` HEAD `/api/promotions-campaigns/` — Get number of items in the collection matching the request parameters (9 query params)
- `promotions_campaigns_create` POST `/api/promotions-campaigns/` (request body)
- `promotions_campaigns_retrieve` GET `/api/promotions-campaigns/{uuid}/` (path: uuid)
- `promotions_campaigns_update` PUT `/api/promotions-campaigns/{uuid}/` (path: uuid | request body)
- `promotions_campaigns_destroy` DELETE `/api/promotions-campaigns/{uuid}/` (path: uuid)
- `promotions_campaigns_activate` POST `/api/promotions-campaigns/{uuid}/activate/` — Activate campaign (path: uuid)
- `promotions_campaigns_orders_list` GET `/api/promotions-campaigns/{uuid}/orders/` — Return a list of orders for which the campaign is applied (path: uuid | 1 query param)
- `promotions_campaigns_resources_list` GET `/api/promotions-campaigns/{uuid}/resources/` — Return a list of resources for which the campaign is applied (path: uuid | 1 query param)
- `promotions_campaigns_terminate` POST `/api/promotions-campaigns/{uuid}/terminate/` — Terminate campaign (path: uuid)

## proposal-proposals
Module: `waldur_api_client.api.proposal_proposals`

- `proposal_proposals_list` GET `/api/proposal-proposals/` (9 query params)
- `proposal_proposals_count` HEAD `/api/proposal-proposals/` — Get number of items in the collection matching the request parameters (9 query params)
- `proposal_proposals_create` POST `/api/proposal-proposals/` (request body)
- `proposal_proposals_checklist_template_retrieve` GET `/api/proposal-proposals/checklist-template/` — Get checklist template for creating new objects (1 query param)
- `proposal_proposals_checklist_template_count` HEAD `/api/proposal-proposals/checklist-template/` — Get number of items in the collection matching the request parameters (1 query param)
- `proposal_proposals_retrieve` GET `/api/proposal-proposals/{uuid}/` (path: uuid)
- `proposal_proposals_destroy` DELETE `/api/proposal-proposals/{uuid}/` (path: uuid)
- `proposal_proposals_add_user` POST `/api/proposal-proposals/{uuid}/add_user/` — Grant a role to a user (path: uuid | request body)
- `proposal_proposals_approve` POST `/api/proposal-proposals/{uuid}/approve/` — Approve a proposal (path: uuid | request body)
- `proposal_proposals_attach_document` POST `/api/proposal-proposals/{uuid}/attach_document/` — Attach document to proposal (path: uuid | request body)
- `proposal_proposals_checklist_retrieve` GET `/api/proposal-proposals/{uuid}/checklist/` — Get checklist with questions and existing answers (path: uuid | 1 query param)
- `proposal_proposals_checklist_review_retrieve` GET `/api/proposal-proposals/{uuid}/checklist_review/` — Get checklist with questions and existing answers including review logic (reviewers only) (path: uuid)
- `proposal_proposals_completion_review_status_retrieve` GET `/api/proposal-proposals/{uuid}/completion_review_status/` — Get checklist completion status with review triggers (reviewers only) (path: uuid)
- `proposal_proposals_completion_status_retrieve` GET `/api/proposal-proposals/{uuid}/completion_status/` — Get checklist completion status (path: uuid)
- `proposal_proposals_delete_user` POST `/api/proposal-proposals/{uuid}/delete_user/` — Revoke a role from a user (path: uuid | request body)
- `proposal_proposals_detach_documents` POST `/api/proposal-proposals/{uuid}/detach_documents/` — Detach documents from proposal (path: uuid | request body)
- `proposal_proposals_list_users_list` GET `/api/proposal-proposals/{uuid}/list_users/` — List users and their roles in a scope (path: uuid | 10 query params)
- `proposal_proposals_reject` POST `/api/proposal-proposals/{uuid}/reject/` — Reject a proposal (path: uuid | request body)
- `proposal_proposals_resources_list` GET `/api/proposal-proposals/{uuid}/resources/` — List resources for a proposal (path: uuid)
- `proposal_proposals_resources_set` POST `/api/proposal-proposals/{uuid}/resources/` — Create resource for a proposal (path: uuid | request body)
- `proposal_proposals_resources_retrieve` GET `/api/proposal-proposals/{uuid}/resources/{obj_uuid}/` (path: obj_uuid, uuid)
- `proposal_proposals_resources_update` PUT `/api/proposal-proposals/{uuid}/resources/{obj_uuid}/` (path: obj_uuid, uuid | request body)
- `proposal_proposals_resources_partial_update` PATCH `/api/proposal-proposals/{uuid}/resources/{obj_uuid}/` (path: obj_uuid, uuid | request body)
- `proposal_proposals_resources_destroy` DELETE `/api/proposal-proposals/{uuid}/resources/{obj_uuid}/` (path: obj_uuid, uuid)
- `proposal_proposals_submit` POST `/api/proposal-proposals/{uuid}/submit/` — Submit a proposal (path: uuid)
- `proposal_proposals_submit_answers` POST `/api/proposal-proposals/{uuid}/submit_answers/` — Submit checklist answers (path: uuid | request body)
- `proposal_proposals_update_project_details` POST `/api/proposal-proposals/{uuid}/update_project_details/` — Update project details of a proposal (path: uuid | request body)
- `proposal_proposals_update_user` POST `/api/proposal-proposals/{uuid}/update_user/` — Update a user's role expiration (path: uuid | request body)

## proposal-protected-calls
Module: `waldur_api_client.api.proposal_protected_calls`

- `proposal_protected_calls_list` GET `/api/proposal-protected-calls/` (10 query params)
- `proposal_protected_calls_count` HEAD `/api/proposal-protected-calls/` — Get number of items in the collection matching the request parameters (9 query params)
- `proposal_protected_calls_create` POST `/api/proposal-protected-calls/` (request body)
- `proposal_protected_calls_available_compliance_checklists_list` GET `/api/proposal-protected-calls/available_compliance_checklists/` — Get available compliance checklists for call creation/editing (10 query params)
- `proposal_protected_calls_available_compliance_checklists_count` HEAD `/api/proposal-protected-calls/available_compliance_checklists/` — Get number of items in the collection matching the request parameters (10 query params)
- `proposal_protected_calls_retrieve` GET `/api/proposal-protected-calls/{uuid}/` (path: uuid | 1 query param)
- `proposal_protected_calls_update` PUT `/api/proposal-protected-calls/{uuid}/` (path: uuid | request body)
- `proposal_protected_calls_partial_update` PATCH `/api/proposal-protected-calls/{uuid}/` (path: uuid | request body)
- `proposal_protected_calls_destroy` DELETE `/api/proposal-protected-calls/{uuid}/` (path: uuid)
- `proposal_protected_calls_activate` POST `/api/proposal-protected-calls/{uuid}/activate/` — Activate a call (path: uuid)
- `proposal_protected_calls_add_user` POST `/api/proposal-protected-calls/{uuid}/add_user/` — Grant a role to a user (path: uuid | request body)
- `proposal_protected_calls_affinity_matrix_retrieve` GET `/api/proposal-protected-calls/{uuid}/affinity-matrix/` — Get affinity matrix for reviewer-proposal matching (path: uuid | 1 query param)
- `proposal_protected_calls_applicant_attribute_config_retrieve` GET `/api/proposal-protected-calls/{uuid}/applicant_attribute_config/` — Get applicant attribute exposure configuration for this call (path: uuid)
- `proposal_protected_calls_archive` POST `/api/proposal-protected-calls/{uuid}/archive/` — Archive a call (path: uuid)
- `proposal_protected_calls_attach_documents` POST `/api/proposal-protected-calls/{uuid}/attach_documents/` — Attach documents to call (path: uuid | request body)
- `proposal_protected_calls_coi_configuration_retrieve` GET `/api/proposal-protected-calls/{uuid}/coi-configuration/` — Get COI configuration for this call (path: uuid)
- `proposal_protected_calls_coi_configuration_partial_update` PATCH `/api/proposal-protected-calls/{uuid}/coi-configuration/` — Get COI configuration for this call (path: uuid | request body)
- `proposal_protected_calls_compliance_overview_retrieve` GET `/api/proposal-protected-calls/{uuid}/compliance_overview/` — Get compliance overview for call manager showing all proposals and their compliance status (path: uuid)
- `proposal_protected_calls_compute_affinities` POST `/api/proposal-protected-calls/{uuid}/compute-affinities/` — Compute affinity scores for all reviewer-proposal pairs (path: uuid | request body)
- `proposal_protected_calls_conflict_summary_retrieve` GET `/api/proposal-protected-calls/{uuid}/conflict-summary/` — Get summary statistics of conflicts for this call (path: uuid)
- `proposal_protected_calls_conflicts_list` GET `/api/proposal-protected-calls/{uuid}/conflicts/` — List all conflicts of interest detected for this call (path: uuid | 9 query params)
- `proposal_protected_calls_create_manual_assignment` POST `/api/proposal-protected-calls/{uuid}/create-manual-assignment/` — Create a manual assignment batch for a specific reviewer (path: uuid | request body)
- `proposal_protected_calls_delete_applicant_attribute_config_destroy` DELETE `/api/proposal-protected-calls/{uuid}/delete_applicant_attribute_config/` — Delete custom applicant attribute config, reverting to system defaults (path: uuid)
- `proposal_protected_calls_delete_user` POST `/api/proposal-protected-calls/{uuid}/delete_user/` — Revoke a role from a user (path: uuid | request body)
- `proposal_protected_calls_detach_documents` POST `/api/proposal-protected-calls/{uuid}/detach_documents/` — Detach documents from call (path: uuid | request body)
- `proposal_protected_calls_detect_conflicts` POST `/api/proposal-protected-calls/{uuid}/detect-conflicts/` — Trigger automated COI detection for all reviewer-proposal pairs (path: uuid | request body)
- `proposal_protected_calls_generate_assignments` POST `/api/proposal-protected-calls/{uuid}/generate-assignments/` — Generate assignment batches for reviewers (path: uuid | request body)
- `proposal_protected_calls_generate_suggestions` POST `/api/proposal-protected-calls/{uuid}/generate-suggestions/` — Generate reviewer suggestions with configurable matching source (path: uuid | request body)
- `proposal_protected_calls_invite_by_email` POST `/api/proposal-protected-calls/{uuid}/invite-by-email/` — Invite a reviewer by email address (path: uuid | request body)
- `proposal_protected_calls_list_users_list` GET `/api/proposal-protected-calls/{uuid}/list_users/` — List users and their roles in a scope (path: uuid | 10 query params)
- `proposal_protected_calls_matching_configuration_retrieve` GET `/api/proposal-protected-calls/{uuid}/matching-configuration/` — Get or update matching configuration for this call (path: uuid)
- `proposal_protected_calls_matching_configuration_partial_update` PATCH `/api/proposal-protected-calls/{uuid}/matching-configuration/` — Get or update matching configuration for this call (path: uuid | request body)
- `proposal_protected_calls_offerings_list` GET `/api/proposal-protected-calls/{uuid}/offerings/` — List offerings for a call (path: uuid | 1 query param)
- `proposal_protected_calls_offerings_set` POST `/api/proposal-protected-calls/{uuid}/offerings/` — Create offering for a call (path: uuid | request body)
- `proposal_protected_calls_offerings_retrieve` GET `/api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/` (path: obj_uuid, uuid)
- `proposal_protected_calls_offerings_update` PUT `/api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/` (path: obj_uuid, uuid | request body)
- `proposal_protected_calls_offerings_partial_update` PATCH `/api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/` (path: obj_uuid, uuid | request body)
- `proposal_protected_calls_offerings_destroy` DELETE `/api/proposal-protected-calls/{uuid}/offerings/{obj_uuid}/` (path: obj_uuid, uuid)
- `proposal_protected_calls_proposals_compliance_answers_list` GET `/api/proposal-protected-calls/{uuid}/proposals/{proposal_uuid}/compliance-answers/` — Get detailed compliance answers for a specific proposal (call managers only) (path: proposal_uuid, uuid | 9 query params)
- `proposal_protected_calls_proposed_assignments_list` GET `/api/proposal-protected-calls/{uuid}/proposed-assignments/` — Get proposed reviewer-proposal assignments (path: uuid | 9 query params)
- `proposal_protected_calls_resource_templates_list` GET `/api/proposal-protected-calls/{uuid}/resource_templates/` — List resource templates for a call (path: uuid)
- `proposal_protected_calls_resource_templates_set` POST `/api/proposal-protected-calls/{uuid}/resource_templates/` — Create resource template for a call (path: uuid | request body)
- `proposal_protected_calls_resource_templates_retrieve` GET `/api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/` (path: obj_uuid, uuid)
- `proposal_protected_calls_resource_templates_update` PUT `/api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/` (path: obj_uuid, uuid | request body)
- `proposal_protected_calls_resource_templates_partial_update` PATCH `/api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/` (path: obj_uuid, uuid | request body)
- `proposal_protected_calls_resource_templates_destroy` DELETE `/api/proposal-protected-calls/{uuid}/resource_templates/{obj_uuid}/` (path: obj_uuid, uuid)
- `proposal_protected_calls_review_proposal_compliance` POST `/api/proposal-protected-calls/{uuid}/review_proposal_compliance/` — Mark proposal compliance as reviewed by call manager (path: uuid | request body)
- `proposal_protected_calls_reviewer_pool_list` GET `/api/proposal-protected-calls/{uuid}/reviewer-pool/` — List reviewer pool members for a call (path: uuid)
- `proposal_protected_calls_invite_reviewers` POST `/api/proposal-protected-calls/{uuid}/reviewer-pool/` — Invite reviewers to join the call's reviewer pool (path: uuid | 9 query params | request body)
- `proposal_protected_calls_rounds_list` GET `/api/proposal-protected-calls/{uuid}/rounds/` — List rounds for a call (path: uuid)
- `proposal_protected_calls_rounds_set` POST `/api/proposal-protected-calls/{uuid}/rounds/` — Create a round for a call (path: uuid | request body)
- `proposal_protected_calls_rounds_retrieve` GET `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/` (path: obj_uuid, uuid)
- `proposal_protected_calls_rounds_update` PUT `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/` (path: obj_uuid, uuid | request body)
- `proposal_protected_calls_rounds_partial_update` PATCH `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/` (path: obj_uuid, uuid | request body)
- `proposal_protected_calls_rounds_destroy` DELETE `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/` (path: obj_uuid, uuid)
- `proposal_protected_calls_rounds_close` POST `/api/proposal-protected-calls/{uuid}/rounds/{obj_uuid}/close/` (path: obj_uuid, uuid | request body)
- `proposal_protected_calls_send_all_assignments` POST `/api/proposal-protected-calls/{uuid}/send-all-assignments/` — Send all draft assignment batches for this call (path: uuid | request body)
- `proposal_protected_calls_send_invitations` POST `/api/proposal-protected-calls/{uuid}/send-invitations/` — Send invitations to all confirmed suggestions (path: uuid)
- `proposal_protected_calls_suggestions_list` GET `/api/proposal-protected-calls/{uuid}/suggestions/` — List all reviewer suggestions for this call with affinity scores (path: uuid | 9 query params)
- `proposal_protected_calls_update_applicant_attribute_config` POST `/api/proposal-protected-calls/{uuid}/update_applicant_attribute_config/` — Create or update applicant attribute exposure configuration (path: uuid | request body)
- `proposal_protected_calls_update_applicant_attribute_config_partial_update` PATCH `/api/proposal-protected-calls/{uuid}/update_applicant_attribute_config/` — Create or update applicant attribute exposure configuration (path: uuid | request body)
- `proposal_protected_calls_update_user` POST `/api/proposal-protected-calls/{uuid}/update_user/` — Update a user's role expiration (path: uuid | request body)

## proposal-public-calls
Module: `waldur_api_client.api.proposal_public_calls`

- `proposal_public_calls_list` GET `/api/proposal-public-calls/` (10 query params)
- `proposal_public_calls_count` HEAD `/api/proposal-public-calls/` — Get number of items in the collection matching the request parameters (9 query params)
- `proposal_public_calls_retrieve` GET `/api/proposal-public-calls/{uuid}/` (path: uuid | 1 query param)
- `proposal_public_calls_check_eligibility_retrieve` GET `/api/proposal-public-calls/{uuid}/check_eligibility/` — Check if the current user is eligible to submit proposals to this call (path: uuid)

## proposal-requested-offerings
Module: `waldur_api_client.api.proposal_requested_offerings`

- `proposal_requested_offerings_list` GET `/api/proposal-requested-offerings/` (8 query params)
- `proposal_requested_offerings_count` HEAD `/api/proposal-requested-offerings/` — Get number of items in the collection matching the request parameters (8 query params)
- `proposal_requested_offerings_retrieve` GET `/api/proposal-requested-offerings/{uuid}/` (path: uuid)
- `proposal_requested_offerings_accept` POST `/api/proposal-requested-offerings/{uuid}/accept/` — Accept a requested offering (path: uuid)
- `proposal_requested_offerings_cancel` POST `/api/proposal-requested-offerings/{uuid}/cancel/` — Cancel a requested offering (path: uuid)

## proposal-requested-resources
Module: `waldur_api_client.api.proposal_requested_resources`

- `proposal_requested_resources_list` GET `/api/proposal-requested-resources/` (8 query params)
- `proposal_requested_resources_count` HEAD `/api/proposal-requested-resources/` — Get number of items in the collection matching the request parameters (8 query params)
- `proposal_requested_resources_retrieve` GET `/api/proposal-requested-resources/{uuid}/` (path: uuid)

## proposal-reviews
Module: `waldur_api_client.api.proposal_reviews`

- `proposal_reviews_list` GET `/api/proposal-reviews/` (9 query params)
- `proposal_reviews_count` HEAD `/api/proposal-reviews/` — Get number of items in the collection matching the request parameters (9 query params)
- `proposal_reviews_create` POST `/api/proposal-reviews/` (request body)
- `proposal_reviews_retrieve` GET `/api/proposal-reviews/{uuid}/` (path: uuid)
- `proposal_reviews_update` PUT `/api/proposal-reviews/{uuid}/` (path: uuid | request body)
- `proposal_reviews_partial_update` PATCH `/api/proposal-reviews/{uuid}/` (path: uuid | request body)
- `proposal_reviews_destroy` DELETE `/api/proposal-reviews/{uuid}/` (path: uuid)
- `proposal_reviews_reject` POST `/api/proposal-reviews/{uuid}/reject/` — Reject a review, changing its state to REJECTED (path: uuid)
- `proposal_reviews_submit` POST `/api/proposal-reviews/{uuid}/submit/` — Submit a review, changing its state to SUBMITTED (path: uuid | request body)

## provider-invoice-items
Module: `waldur_api_client.api.provider_invoice_items`

- `provider_invoice_items_list` GET `/api/provider-invoice-items/` (6 query params)
- `provider_invoice_items_count` HEAD `/api/provider-invoice-items/` — Get number of items in the collection matching the request parameters (6 query params)
- `provider_invoice_items_retrieve` GET `/api/provider-invoice-items/{id}/` (path: id)

## public-maintenance-announcements
Module: `waldur_api_client.api.public_maintenance_announcements`

- `public_maintenance_announcements_list` GET `/api/public-maintenance-announcements/` — List public maintenance announcements (8 query params)
- `public_maintenance_announcements_count` HEAD `/api/public-maintenance-announcements/` — List public maintenance announcements (8 query params)
- `public_maintenance_announcements_retrieve` GET `/api/public-maintenance-announcements/{uuid}/` — Retrieve a public maintenance announcement (path: uuid)

## query
Module: `waldur_api_client.api.query`

- `query` POST `/api/query/` — Execute read-only SQL query (request body)

## rabbitmq-overview
Module: `waldur_api_client.api.rabbitmq_overview`

- `rabbitmq_overview_retrieve` GET `/api/rabbitmq-overview/` — Get RabbitMQ cluster overview statistics (no params)

## rabbitmq-stats
Module: `waldur_api_client.api.rabbitmq_stats`

- `rabbitmq_stats_retrieve` GET `/api/rabbitmq-stats/` — Get RabbitMQ subscription queue statistics (no params)
- `rabbitmq_stats` POST `/api/rabbitmq-stats/` — Purge or delete RabbitMQ subscription queues (request body)

## rabbitmq-user-stats
Module: `waldur_api_client.api.rabbitmq_user_stats`

- `rabbitmq_user_stats_list` GET `/api/rabbitmq-user-stats/` — Get RabbitMQ user connection statistics (no params)

## rabbitmq-vhost-stats
Module: `waldur_api_client.api.rabbitmq_vhost_stats`

- `rabbitmq_vhost_stats_list` GET `/api/rabbitmq-vhost-stats/` (no params)

## rancher-apps
Module: `waldur_api_client.api.rancher_apps`

- `rancher_apps_list` GET `/api/rancher-apps/` (22 query params)
- `rancher_apps_count` HEAD `/api/rancher-apps/` — Get number of items in the collection matching the request parameters (21 query params)
- `rancher_apps_create` POST `/api/rancher-apps/` (request body)
- `rancher_apps_retrieve` GET `/api/rancher-apps/{uuid}/` (path: uuid | 1 query param)
- `rancher_apps_update` PUT `/api/rancher-apps/{uuid}/` (path: uuid | request body)
- `rancher_apps_partial_update` PATCH `/api/rancher-apps/{uuid}/` (path: uuid | request body)
- `rancher_apps_destroy` DELETE `/api/rancher-apps/{uuid}/` (path: uuid)
- `rancher_apps_pull` POST `/api/rancher-apps/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `rancher_apps_set_erred` POST `/api/rancher-apps/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `rancher_apps_set_ok` POST `/api/rancher-apps/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `rancher_apps_unlink` POST `/api/rancher-apps/{uuid}/unlink/` — Unlink resource (path: uuid)

## rancher-catalogs
Module: `waldur_api_client.api.rancher_catalogs`

- `rancher_catalogs_list` GET `/api/rancher-catalogs/` (no params)
- `rancher_catalogs_count` HEAD `/api/rancher-catalogs/` — Get number of items in the collection matching the request parameters (no params)
- `rancher_catalogs_create` POST `/api/rancher-catalogs/` (request body)
- `rancher_catalogs_retrieve` GET `/api/rancher-catalogs/{uuid}/` (path: uuid)
- `rancher_catalogs_update` PUT `/api/rancher-catalogs/{uuid}/` (path: uuid | request body)
- `rancher_catalogs_partial_update` PATCH `/api/rancher-catalogs/{uuid}/` (path: uuid | request body)
- `rancher_catalogs_destroy` DELETE `/api/rancher-catalogs/{uuid}/` (path: uuid)
- `rancher_catalogs_refresh` POST `/api/rancher-catalogs/{uuid}/refresh/` (path: uuid | request body)

## rancher-cluster-security-groups
Module: `waldur_api_client.api.rancher_cluster_security_groups`

- `rancher_cluster_security_groups_list` GET `/api/rancher-cluster-security-groups/` (3 query params)
- `rancher_cluster_security_groups_count` HEAD `/api/rancher-cluster-security-groups/` — Get number of items in the collection matching the request parameters (3 query params)
- `rancher_cluster_security_groups_retrieve` GET `/api/rancher-cluster-security-groups/{uuid}/` (path: uuid)
- `rancher_cluster_security_groups_update` PUT `/api/rancher-cluster-security-groups/{uuid}/` (path: uuid | request body)
- `rancher_cluster_security_groups_partial_update` PATCH `/api/rancher-cluster-security-groups/{uuid}/` (path: uuid | request body)

## rancher-cluster-templates
Module: `waldur_api_client.api.rancher_cluster_templates`

- `rancher_cluster_templates_list` GET `/api/rancher-cluster-templates/` (no params)
- `rancher_cluster_templates_count` HEAD `/api/rancher-cluster-templates/` — Get number of items in the collection matching the request parameters (no params)
- `rancher_cluster_templates_retrieve` GET `/api/rancher-cluster-templates/{uuid}/` (path: uuid)

## rancher-clusters
Module: `waldur_api_client.api.rancher_clusters`

- `rancher_clusters_list` GET `/api/rancher-clusters/` (19 query params)
- `rancher_clusters_count` HEAD `/api/rancher-clusters/` — Get number of items in the collection matching the request parameters (18 query params)
- `rancher_clusters_retrieve` GET `/api/rancher-clusters/{uuid}/` (path: uuid | 1 query param)
- `rancher_clusters_update` PUT `/api/rancher-clusters/{uuid}/` (path: uuid | request body)
- `rancher_clusters_partial_update` PATCH `/api/rancher-clusters/{uuid}/` (path: uuid | request body)
- `rancher_clusters_create_management_security_group` POST `/api/rancher-clusters/{uuid}/create_management_security_group/` (path: uuid | request body)
- `rancher_clusters_import_yaml` POST `/api/rancher-clusters/{uuid}/import_yaml/` (path: uuid | request body)
- `rancher_clusters_pull` POST `/api/rancher-clusters/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `rancher_clusters_set_erred` POST `/api/rancher-clusters/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `rancher_clusters_set_ok` POST `/api/rancher-clusters/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `rancher_clusters_unlink` POST `/api/rancher-clusters/{uuid}/unlink/` — Unlink resource (path: uuid)

## rancher-hpas
Module: `waldur_api_client.api.rancher_hpas`

- `rancher_hpas_list` GET `/api/rancher-hpas/` (8 query params)
- `rancher_hpas_count` HEAD `/api/rancher-hpas/` — Get number of items in the collection matching the request parameters (8 query params)
- `rancher_hpas_create` POST `/api/rancher-hpas/` (request body)
- `rancher_hpas_retrieve` GET `/api/rancher-hpas/{uuid}/` (path: uuid)
- `rancher_hpas_update` PUT `/api/rancher-hpas/{uuid}/` (path: uuid | request body)
- `rancher_hpas_partial_update` PATCH `/api/rancher-hpas/{uuid}/` (path: uuid | request body)
- `rancher_hpas_destroy` DELETE `/api/rancher-hpas/{uuid}/` (path: uuid)
- `rancher_hpas_pull` POST `/api/rancher-hpas/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `rancher_hpas_set_erred` POST `/api/rancher-hpas/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `rancher_hpas_set_ok` POST `/api/rancher-hpas/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `rancher_hpas_unlink` POST `/api/rancher-hpas/{uuid}/unlink/` — Unlink resource (path: uuid)
- `rancher_hpas_yaml_retrieve` GET `/api/rancher-hpas/{uuid}/yaml/` (path: uuid)
- `rancher_hpas_yaml_update` PUT `/api/rancher-hpas/{uuid}/yaml/` (path: uuid | request body)

## rancher-ingresses
Module: `waldur_api_client.api.rancher_ingresses`

- `rancher_ingresses_list` GET `/api/rancher-ingresses/` (22 query params)
- `rancher_ingresses_count` HEAD `/api/rancher-ingresses/` — Get number of items in the collection matching the request parameters (21 query params)
- `rancher_ingresses_create` POST `/api/rancher-ingresses/` (request body)
- `rancher_ingresses_retrieve` GET `/api/rancher-ingresses/{uuid}/` (path: uuid | 1 query param)
- `rancher_ingresses_update` PUT `/api/rancher-ingresses/{uuid}/` (path: uuid | request body)
- `rancher_ingresses_partial_update` PATCH `/api/rancher-ingresses/{uuid}/` (path: uuid | request body)
- `rancher_ingresses_destroy` DELETE `/api/rancher-ingresses/{uuid}/` (path: uuid)
- `rancher_ingresses_pull` POST `/api/rancher-ingresses/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `rancher_ingresses_set_erred` POST `/api/rancher-ingresses/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `rancher_ingresses_set_ok` POST `/api/rancher-ingresses/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `rancher_ingresses_unlink` POST `/api/rancher-ingresses/{uuid}/unlink/` — Unlink resource (path: uuid)
- `rancher_ingresses_yaml_retrieve` GET `/api/rancher-ingresses/{uuid}/yaml/` (path: uuid | 1 query param)
- `rancher_ingresses_yaml_update` PUT `/api/rancher-ingresses/{uuid}/yaml/` (path: uuid | request body)

## rancher-namespaces
Module: `waldur_api_client.api.rancher_namespaces`

- `rancher_namespaces_list` GET `/api/rancher-namespaces/` (7 query params)
- `rancher_namespaces_count` HEAD `/api/rancher-namespaces/` — Get number of items in the collection matching the request parameters (7 query params)
- `rancher_namespaces_retrieve` GET `/api/rancher-namespaces/{uuid}/` (path: uuid)

## rancher-nodes
Module: `waldur_api_client.api.rancher_nodes`

- `rancher_nodes_list` GET `/api/rancher-nodes/` (1 query param)
- `rancher_nodes_count` HEAD `/api/rancher-nodes/` — Get number of items in the collection matching the request parameters (1 query param)
- `rancher_nodes_create` POST `/api/rancher-nodes/` (request body)
- `rancher_nodes_retrieve` GET `/api/rancher-nodes/{uuid}/` (path: uuid)
- `rancher_nodes_destroy` DELETE `/api/rancher-nodes/{uuid}/` (path: uuid)
- `rancher_nodes_console_retrieve` GET `/api/rancher-nodes/{uuid}/console/` — Returns console URL for the node (path: uuid)
- `rancher_nodes_console_log_retrieve` GET `/api/rancher-nodes/{uuid}/console_log/` — Returns console log for the node (path: uuid | 1 query param)
- `rancher_nodes_link_openstack` POST `/api/rancher-nodes/{uuid}/link_openstack/` — Links node to OpenStack instance (path: uuid | request body)
- `rancher_nodes_pull` POST `/api/rancher-nodes/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `rancher_nodes_set_erred` POST `/api/rancher-nodes/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `rancher_nodes_set_ok` POST `/api/rancher-nodes/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `rancher_nodes_unlink` POST `/api/rancher-nodes/{uuid}/unlink/` — Unlink resource (path: uuid)
- `rancher_nodes_unlink_openstack` POST `/api/rancher-nodes/{uuid}/unlink_openstack/` — Unlinks node from OpenStack instance (path: uuid)

## rancher-projects
Module: `waldur_api_client.api.rancher_projects`

- `rancher_projects_list` GET `/api/rancher-projects/` (5 query params)
- `rancher_projects_count` HEAD `/api/rancher-projects/` — Get number of items in the collection matching the request parameters (5 query params)
- `rancher_projects_retrieve` GET `/api/rancher-projects/{uuid}/` (path: uuid)
- `rancher_projects_secrets_retrieve` GET `/api/rancher-projects/{uuid}/secrets/` — Returns project's secrets (path: uuid)

## rancher-role-templates
Module: `waldur_api_client.api.rancher_role_templates`

- `rancher_role_templates_list` GET `/api/rancher-role-templates/` (4 query params)
- `rancher_role_templates_count` HEAD `/api/rancher-role-templates/` — Get number of items in the collection matching the request parameters (4 query params)
- `rancher_role_templates_retrieve` GET `/api/rancher-role-templates/{uuid}/` (path: uuid)

## rancher-services
Module: `waldur_api_client.api.rancher_services`

- `rancher_services_list` GET `/api/rancher-services/` (22 query params)
- `rancher_services_count` HEAD `/api/rancher-services/` — Get number of items in the collection matching the request parameters (21 query params)
- `rancher_services_create` POST `/api/rancher-services/` (request body)
- `rancher_services_retrieve` GET `/api/rancher-services/{uuid}/` (path: uuid | 1 query param)
- `rancher_services_update` PUT `/api/rancher-services/{uuid}/` (path: uuid | request body)
- `rancher_services_partial_update` PATCH `/api/rancher-services/{uuid}/` (path: uuid | request body)
- `rancher_services_destroy` DELETE `/api/rancher-services/{uuid}/` (path: uuid)
- `rancher_services_pull` POST `/api/rancher-services/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `rancher_services_set_erred` POST `/api/rancher-services/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `rancher_services_set_ok` POST `/api/rancher-services/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `rancher_services_unlink` POST `/api/rancher-services/{uuid}/unlink/` — Unlink resource (path: uuid)
- `rancher_services_yaml_retrieve` GET `/api/rancher-services/{uuid}/yaml/` (path: uuid | 1 query param)
- `rancher_services_yaml_update` PUT `/api/rancher-services/{uuid}/yaml/` (path: uuid | request body)

## rancher-template-versions
Module: `waldur_api_client.api.rancher_template_versions`

- `rancher_template_versions_retrieve` GET `/api/rancher-template-versions/{template_uuid}/{version}/` (path: template_uuid, version)

## rancher-templates
Module: `waldur_api_client.api.rancher_templates`

- `rancher_templates_list` GET `/api/rancher-templates/` (8 query params)
- `rancher_templates_count` HEAD `/api/rancher-templates/` — Get number of items in the collection matching the request parameters (8 query params)
- `rancher_templates_retrieve` GET `/api/rancher-templates/{uuid}/` (path: uuid)

## rancher-users
Module: `waldur_api_client.api.rancher_users`

- `rancher_users_list` GET `/api/rancher-users/` (6 query params)
- `rancher_users_count` HEAD `/api/rancher-users/` — Get number of items in the collection matching the request parameters (6 query params)
- `rancher_users_retrieve` GET `/api/rancher-users/{uuid}/` (path: uuid)

## rancher-workloads
Module: `waldur_api_client.api.rancher_workloads`

- `rancher_workloads_list` GET `/api/rancher-workloads/` (8 query params)
- `rancher_workloads_count` HEAD `/api/rancher-workloads/` — Get number of items in the collection matching the request parameters (8 query params)
- `rancher_workloads_create` POST `/api/rancher-workloads/` (request body)
- `rancher_workloads_retrieve` GET `/api/rancher-workloads/{uuid}/` (path: uuid)
- `rancher_workloads_update` PUT `/api/rancher-workloads/{uuid}/` (path: uuid | request body)
- `rancher_workloads_partial_update` PATCH `/api/rancher-workloads/{uuid}/` (path: uuid | request body)
- `rancher_workloads_destroy` DELETE `/api/rancher-workloads/{uuid}/` (path: uuid)
- `rancher_workloads_redeploy` POST `/api/rancher-workloads/{uuid}/redeploy/` (path: uuid)
- `rancher_workloads_yaml_retrieve` GET `/api/rancher-workloads/{uuid}/yaml/` (path: uuid)
- `rancher_workloads_yaml_update` PUT `/api/rancher-workloads/{uuid}/yaml/` (path: uuid | request body)

## remote-eduteams
Module: `waldur_api_client.api.remote_eduteams`

- `remote_eduteams` POST `/api/remote-eduteams/` — Allows to pull user details from remote eduTEAMS instance (request body)

## remote-waldur-api
Module: `waldur_api_client.api.remote_waldur_api`

- `remote_waldur_api_cancel_termination` POST `/api/remote-waldur-api/cancel_termination/{uuid}` — Cancel termination order (path: uuid)
- `remote_waldur_api_import_offering` POST `/api/remote-waldur-api/import_offering/` — Create local offering from remote (request body)
- `remote_waldur_api_pull_offering_details` POST `/api/remote-waldur-api/pull_offering_details/{uuid}/` (path: uuid)
- `remote_waldur_api_pull_offering_invoices` POST `/api/remote-waldur-api/pull_offering_invoices/{uuid}/` (path: uuid)
- `remote_waldur_api_pull_offering_orders` POST `/api/remote-waldur-api/pull_offering_orders/{uuid}/` (path: uuid)
- `remote_waldur_api_pull_offering_resources` POST `/api/remote-waldur-api/pull_offering_resources/{uuid}/` (path: uuid)
- `remote_waldur_api_pull_offering_robot_accounts` POST `/api/remote-waldur-api/pull_offering_robot_accounts/{uuid}/` (path: uuid)
- `remote_waldur_api_pull_offering_usage` POST `/api/remote-waldur-api/pull_offering_usage/{uuid}/` (path: uuid)
- `remote_waldur_api_pull_offering_users` POST `/api/remote-waldur-api/pull_offering_users/{uuid}/` (path: uuid)
- `remote_waldur_api_pull_order` POST `/api/remote-waldur-api/pull_order/{uuid}` — Schedule order pull task (path: uuid)
- `remote_waldur_api_pull_resource_robot_accounts` POST `/api/remote-waldur-api/pull_resource_robot_accounts/{uuid}/` (path: uuid)
- `remote_waldur_api_push_project_data` POST `/api/remote-waldur-api/push_project_data/{uuid}/` (path: uuid)
- `remote_waldur_api_remote_categories` POST `/api/remote-waldur-api/remote_categories/` — List remote marketplace categories (request body)
- `remote_waldur_api_remote_customers` POST `/api/remote-waldur-api/remote_customers/` — List remote customers owned by current user (request body)
- `remote_waldur_api_remote_resource_order_status_retrieve` GET `/api/remote-waldur-api/remote_resource_order_status/{resource_uuid}/` — Get remote order details (path: resource_uuid)
- `remote_waldur_api_remote_resource_status_retrieve` GET `/api/remote-waldur-api/remote_resource_status/{resource_uuid}/` — Get remote resource sync status (path: resource_uuid)
- `remote_waldur_api_remote_resource_team_status_list` GET `/api/remote-waldur-api/remote_resource_team_status/{resource_uuid}/` — Get remote resource team members (path: resource_uuid)
- `remote_waldur_api_shared_offerings` POST `/api/remote-waldur-api/shared_offerings/` — List remote importable offerings for particular customer (1 query param | request body)
- `remote_waldur_api_sync_resource` POST `/api/remote-waldur-api/sync_resource/{uuid}/` (path: uuid)
- `remote_waldur_api_sync_resource_project_permissions` POST `/api/remote-waldur-api/sync_resource_project_permissions/{uuid}/` (path: uuid)

## reviewer-bids
Module: `waldur_api_client.api.reviewer_bids`

- `reviewer_bids_list` GET `/api/reviewer-bids/` (5 query params)
- `reviewer_bids_count` HEAD `/api/reviewer-bids/` — Get number of items in the collection matching the request parameters (5 query params)
- `reviewer_bids_create` POST `/api/reviewer-bids/` (request body)
- `reviewer_bids_bulk_submit` POST `/api/reviewer-bids/bulk-submit/` — Submit multiple bids at once (request body)
- `reviewer_bids_my_bids_list` GET `/api/reviewer-bids/my-bids/` — Get my bids for a specific call (5 query params)
- `reviewer_bids_my_bids_count` HEAD `/api/reviewer-bids/my-bids/` — Get number of items in the collection matching the request parameters (5 query params)
- `reviewer_bids_submit` POST `/api/reviewer-bids/submit/` — Submit a bid on a proposal (request body)
- `reviewer_bids_retrieve` GET `/api/reviewer-bids/{uuid}/` (path: uuid)
- `reviewer_bids_update` PUT `/api/reviewer-bids/{uuid}/` (path: uuid | request body)
- `reviewer_bids_partial_update` PATCH `/api/reviewer-bids/{uuid}/` (path: uuid | request body)
- `reviewer_bids_destroy` DELETE `/api/reviewer-bids/{uuid}/` (path: uuid)

## reviewer-invitations
Module: `waldur_api_client.api.reviewer_invitations`

- `reviewer_invitations_retrieve` GET `/api/reviewer-invitations/{token}/` — Get invitation details by token (path: token)
- `reviewer_invitations_accept` POST `/api/reviewer-invitations/{token}/accept/` — Accept a reviewer invitation (path: token | request body)
- `reviewer_invitations_decline` POST `/api/reviewer-invitations/{token}/decline/` — Decline a reviewer invitation (path: token | request body)

## reviewer-profiles
Module: `waldur_api_client.api.reviewer_profiles`

- `reviewer_profiles_list` GET `/api/reviewer-profiles/` (8 query params)
- `reviewer_profiles_count` HEAD `/api/reviewer-profiles/` — Get number of items in the collection matching the request parameters (8 query params)
- `reviewer_profiles_create` POST `/api/reviewer-profiles/` (request body)
- `reviewer_profiles_me_retrieve` GET `/api/reviewer-profiles/me/` — Get or create reviewer profile for the current user (no params)
- `reviewer_profiles_me_count` HEAD `/api/reviewer-profiles/me/` — Get number of items in the collection matching the request parameters (no params)
- `reviewer_profiles_me` POST `/api/reviewer-profiles/me/` — Get or create reviewer profile for the current user (request body)
- `reviewer_profiles_me_partial_update` PATCH `/api/reviewer-profiles/me/` — Get or create reviewer profile for the current user (request body)
- `reviewer_profiles_publish` POST `/api/reviewer-profiles/publish/` — Publish reviewer profile for discovery by call managers (request body)
- `reviewer_profiles_unpublish` POST `/api/reviewer-profiles/unpublish/` — Unpublish reviewer profile to remove it from discovery (request body)
- `nested_reviewer_profile_affiliations_list` GET `/api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/` (path: reviewer_profile_uuid)
- `nested_reviewer_profile_affiliations_create` POST `/api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/` (path: reviewer_profile_uuid | request body)
- `nested_reviewer_profile_affiliations_retrieve` GET `/api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/` (path: reviewer_profile_uuid, uuid)
- `nested_reviewer_profile_affiliations_update` PUT `/api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/` (path: reviewer_profile_uuid, uuid | request body)
- `nested_reviewer_profile_affiliations_partial_update` PATCH `/api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/` (path: reviewer_profile_uuid, uuid | request body)
- `nested_reviewer_profile_affiliations_destroy` DELETE `/api/reviewer-profiles/{reviewer_profile_uuid}/affiliations/{uuid}/` (path: reviewer_profile_uuid, uuid)
- `nested_reviewer_profile_expertise_list` GET `/api/reviewer-profiles/{reviewer_profile_uuid}/expertise/` (path: reviewer_profile_uuid)
- `nested_reviewer_profile_expertise_create` POST `/api/reviewer-profiles/{reviewer_profile_uuid}/expertise/` (path: reviewer_profile_uuid | request body)
- `nested_reviewer_profile_expertise_retrieve` GET `/api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/` (path: reviewer_profile_uuid, uuid)
- `nested_reviewer_profile_expertise_update` PUT `/api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/` (path: reviewer_profile_uuid, uuid | request body)
- `nested_reviewer_profile_expertise_partial_update` PATCH `/api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/` (path: reviewer_profile_uuid, uuid | request body)
- `nested_reviewer_profile_expertise_destroy` DELETE `/api/reviewer-profiles/{reviewer_profile_uuid}/expertise/{uuid}/` (path: reviewer_profile_uuid, uuid)
- `nested_reviewer_profile_publications_list` GET `/api/reviewer-profiles/{reviewer_profile_uuid}/publications/` (path: reviewer_profile_uuid)
- `nested_reviewer_profile_publications_create` POST `/api/reviewer-profiles/{reviewer_profile_uuid}/publications/` (path: reviewer_profile_uuid | request body)
- `nested_reviewer_profile_publications_retrieve` GET `/api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/` (path: reviewer_profile_uuid, uuid)
- `nested_reviewer_profile_publications_update` PUT `/api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/` (path: reviewer_profile_uuid, uuid | request body)
- `nested_reviewer_profile_publications_partial_update` PATCH `/api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/` (path: reviewer_profile_uuid, uuid | request body)
- `nested_reviewer_profile_publications_destroy` DELETE `/api/reviewer-profiles/{reviewer_profile_uuid}/publications/{uuid}/` (path: reviewer_profile_uuid, uuid)
- `reviewer_profiles_retrieve` GET `/api/reviewer-profiles/{uuid}/` (path: uuid)
- `reviewer_profiles_update` PUT `/api/reviewer-profiles/{uuid}/` (path: uuid | request body)
- `reviewer_profiles_partial_update` PATCH `/api/reviewer-profiles/{uuid}/` (path: uuid | request body)
- `reviewer_profiles_destroy` DELETE `/api/reviewer-profiles/{uuid}/` (path: uuid)
- `reviewer_profiles_affiliations_list` GET `/api/reviewer-profiles/{uuid}/affiliations/` — List affiliations for a reviewer profile (path: uuid)
- `reviewer_profiles_affiliations_create` POST `/api/reviewer-profiles/{uuid}/affiliations/` — Create affiliation for a reviewer profile (path: uuid | request body)
- `reviewer_profiles_connect_orcid_retrieve` GET `/api/reviewer-profiles/{uuid}/connect-orcid/` — Get ORCID OAuth authorization URL (path: uuid)
- `reviewer_profiles_connect_orcid_callback` POST `/api/reviewer-profiles/{uuid}/connect-orcid/callback/` — Complete ORCID OAuth connection with authorization code (path: uuid | request body)
- `reviewer_profiles_disconnect_orcid` POST `/api/reviewer-profiles/{uuid}/disconnect-orcid/` — Disconnect ORCID from profile (path: uuid | request body)
- `reviewer_profiles_expertise_list` GET `/api/reviewer-profiles/{uuid}/expertise/` — List expertise keywords for a reviewer profile (path: uuid)
- `reviewer_profiles_expertise_create` POST `/api/reviewer-profiles/{uuid}/expertise/` — Create expertise entry for a reviewer profile (path: uuid | request body)
- `reviewer_profiles_import_publications` POST `/api/reviewer-profiles/{uuid}/import-publications/` — Import publications from ORCID or other sources (path: uuid | request body)
- `reviewer_profiles_publications_list` GET `/api/reviewer-profiles/{uuid}/publications/` — List publications for a reviewer profile (path: uuid)
- `reviewer_profiles_publications_create` POST `/api/reviewer-profiles/{uuid}/publications/` — Create publication for a reviewer profile (path: uuid | request body)
- `reviewer_profiles_sync_orcid` POST `/api/reviewer-profiles/{uuid}/sync-orcid/` — Sync profile data from ORCID (path: uuid | request body)

## reviewer-suggestions
Module: `waldur_api_client.api.reviewer_suggestions`

- `reviewer_suggestions_list` GET `/api/reviewer-suggestions/` (5 query params)
- `reviewer_suggestions_count` HEAD `/api/reviewer-suggestions/` — Get number of items in the collection matching the request parameters (5 query params)
- `reviewer_suggestions_retrieve` GET `/api/reviewer-suggestions/{uuid}/` (path: uuid)
- `reviewer_suggestions_destroy` DELETE `/api/reviewer-suggestions/{uuid}/` — Delete a reviewer suggestion (path: uuid)
- `reviewer_suggestions_confirm` POST `/api/reviewer-suggestions/{uuid}/confirm/` — Confirm a reviewer suggestion (path: uuid | request body)
- `reviewer_suggestions_reject` POST `/api/reviewer-suggestions/{uuid}/reject/` — Reject a reviewer suggestion (path: uuid | request body)

## roles
Module: `waldur_api_client.api.roles`

- `roles_list` GET `/api/roles/` — List roles (4 query params)
- `roles_count` HEAD `/api/roles/` — List roles (3 query params)
- `roles_create` POST `/api/roles/` — Create a new role (request body)
- `roles_retrieve` GET `/api/roles/{uuid}/` — Get role details (path: uuid | 1 query param)
- `roles_update` PUT `/api/roles/{uuid}/` — Update a role (path: uuid | request body)
- `roles_partial_update` PATCH `/api/roles/{uuid}/` (path: uuid | request body)
- `roles_destroy` DELETE `/api/roles/{uuid}/` — Delete a role (path: uuid)
- `roles_disable` POST `/api/roles/{uuid}/disable/` — Disable a role (path: uuid)
- `roles_enable` POST `/api/roles/{uuid}/enable/` — Enable a role (path: uuid)
- `roles_update_descriptions_update` PUT `/api/roles/{uuid}/update_descriptions/` — Update role descriptions (path: uuid | request body)

## service-settings
Module: `waldur_api_client.api.service_settings`

- `service_settings_list` GET `/api/service-settings/` (10 query params)
- `service_settings_count` HEAD `/api/service-settings/` — Get number of items in the collection matching the request parameters (9 query params)
- `service_settings_retrieve` GET `/api/service-settings/{uuid}/` (path: uuid | 1 query param)

## slurm-allocation-user-usage
Module: `waldur_api_client.api.slurm_allocation_user_usage`

- `slurm_allocation_user_usage_list` GET `/api/slurm-allocation-user-usage/` (6 query params)
- `slurm_allocation_user_usage_count` HEAD `/api/slurm-allocation-user-usage/` — Get number of items in the collection matching the request parameters (6 query params)
- `slurm_allocation_user_usage_retrieve` GET `/api/slurm-allocation-user-usage/{id}/` (path: id)

## slurm-allocations
Module: `waldur_api_client.api.slurm_allocations`

- `slurm_allocations_list` GET `/api/slurm-allocations/` (20 query params)
- `slurm_allocations_count` HEAD `/api/slurm-allocations/` — Get number of items in the collection matching the request parameters (19 query params)
- `slurm_allocations_create` POST `/api/slurm-allocations/` (request body)
- `slurm_allocations_retrieve` GET `/api/slurm-allocations/{uuid}/` (path: uuid | 1 query param)
- `slurm_allocations_update` PUT `/api/slurm-allocations/{uuid}/` (path: uuid | request body)
- `slurm_allocations_partial_update` PATCH `/api/slurm-allocations/{uuid}/` (path: uuid | request body)
- `slurm_allocations_destroy` DELETE `/api/slurm-allocations/{uuid}/` (path: uuid)
- `slurm_allocations_pull` POST `/api/slurm-allocations/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `slurm_allocations_set_erred` POST `/api/slurm-allocations/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `slurm_allocations_set_limits` POST `/api/slurm-allocations/{uuid}/set_limits/` (path: uuid | request body)
- `slurm_allocations_set_ok` POST `/api/slurm-allocations/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `slurm_allocations_unlink` POST `/api/slurm-allocations/{uuid}/unlink/` — Unlink resource (path: uuid)

## slurm-associations
Module: `waldur_api_client.api.slurm_associations`

- `slurm_associations_list` GET `/api/slurm-associations/` (2 query params)
- `slurm_associations_count` HEAD `/api/slurm-associations/` — Get number of items in the collection matching the request parameters (2 query params)
- `slurm_associations_retrieve` GET `/api/slurm-associations/{uuid}/` (path: uuid)

## slurm-jobs
Module: `waldur_api_client.api.slurm_jobs`

- `slurm_jobs_list` GET `/api/slurm-jobs/` (1 query param)
- `slurm_jobs_count` HEAD `/api/slurm-jobs/` — Get number of items in the collection matching the request parameters (no params)
- `slurm_jobs_create` POST `/api/slurm-jobs/` (request body)
- `slurm_jobs_retrieve` GET `/api/slurm-jobs/{uuid}/` (path: uuid | 1 query param)
- `slurm_jobs_update` PUT `/api/slurm-jobs/{uuid}/` (path: uuid | request body)
- `slurm_jobs_partial_update` PATCH `/api/slurm-jobs/{uuid}/` (path: uuid | request body)
- `slurm_jobs_destroy` DELETE `/api/slurm-jobs/{uuid}/` (path: uuid)
- `slurm_jobs_pull` POST `/api/slurm-jobs/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `slurm_jobs_set_erred` POST `/api/slurm-jobs/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `slurm_jobs_set_ok` POST `/api/slurm-jobs/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `slurm_jobs_unlink` POST `/api/slurm-jobs/{uuid}/unlink/` — Unlink resource (path: uuid)

## stats
Module: `waldur_api_client.api.stats`

- `stats_celery_retrieve` GET `/api/stats/celery/` — Get Celery worker statistics (no params)
- `stats_database_retrieve` GET `/api/stats/database/` — Get comprehensive database statistics (no params)
- `stats_query` POST `/api/stats/query/` — Execute read-only SQL query (request body)
- `stats_table_growth_retrieve` GET `/api/stats/table-growth/` — Get table growth statistics (no params)

## support
Module: `waldur_api_client.api.support`

- `support_settings_atlassian_list` GET `/api/support/settings/atlassian/` (no params)
- `support_settings_atlassian_create` POST `/api/support/settings/atlassian/` (no params)
- `support_settings_atlassian_current_settings_retrieve` GET `/api/support/settings/atlassian/current_settings/` — Get current Atlassian settings (masked secrets) (no params)
- `support_settings_atlassian_discover_custom_fields` POST `/api/support/settings/atlassian/discover_custom_fields/` — Discover available custom fields (request body)
- `support_settings_atlassian_discover_priorities` POST `/api/support/settings/atlassian/discover_priorities/` — Discover available priorities (request body)
- `support_settings_atlassian_discover_projects` POST `/api/support/settings/atlassian/discover_projects/` — Discover available Service Desk projects (request body)
- `support_settings_atlassian_discover_request_types` POST `/api/support/settings/atlassian/discover_request_types/` — Discover request types for a selected project (request body)
- `support_settings_atlassian_preview_settings` POST `/api/support/settings/atlassian/preview_settings/` — Generate preview of settings to be saved (request body)
- `support_settings_atlassian_save_settings` POST `/api/support/settings/atlassian/save_settings/` — Save selected settings to constance (request body)
- `support_settings_atlassian_validate_credentials` POST `/api/support/settings/atlassian/validate_credentials/` — Validate Atlassian credentials without saving them (request body)
- `support_settings_atlassian_retrieve` GET `/api/support/settings/atlassian/{id}/` (path: id)
- `support_settings_atlassian_update` PUT `/api/support/settings/atlassian/{id}/` (path: id)
- `support_settings_atlassian_partial_update` PATCH `/api/support/settings/atlassian/{id}/` (path: id)
- `support_settings_atlassian_destroy` DELETE `/api/support/settings/atlassian/{id}/` (path: id)

## support-attachments
Module: `waldur_api_client.api.support_attachments`

- `support_attachments_list` GET `/api/support-attachments/` (3 query params)
- `support_attachments_count` HEAD `/api/support-attachments/` — Get number of items in the collection matching the request parameters (2 query params)
- `support_attachments_create` POST `/api/support-attachments/` (request body)
- `support_attachments_retrieve` GET `/api/support-attachments/{uuid}/` (path: uuid | 1 query param)
- `support_attachments_destroy` DELETE `/api/support-attachments/{uuid}/` (path: uuid)

## support-comments
Module: `waldur_api_client.api.support_comments`

- `support_comments_list` GET `/api/support-comments/` (8 query params)
- `support_comments_count` HEAD `/api/support-comments/` — Get number of items in the collection matching the request parameters (8 query params)
- `support_comments_retrieve` GET `/api/support-comments/{uuid}/` (path: uuid)
- `support_comments_update` PUT `/api/support-comments/{uuid}/` (path: uuid | request body)
- `support_comments_partial_update` PATCH `/api/support-comments/{uuid}/` (path: uuid | request body)
- `support_comments_destroy` DELETE `/api/support-comments/{uuid}/` (path: uuid)

## support-feedback-average-report
Module: `waldur_api_client.api.support_feedback_average_report`

- `support_feedback_average_report_retrieve` GET `/api/support-feedback-average-report/` (no params)

## support-feedback-report
Module: `waldur_api_client.api.support_feedback_report`

- `support_feedback_report_retrieve` GET `/api/support-feedback-report/` (no params)

## support-feedbacks
Module: `waldur_api_client.api.support_feedbacks`

- `support_feedbacks_list` GET `/api/support-feedbacks/` (9 query params)
- `support_feedbacks_count` HEAD `/api/support-feedbacks/` — Get number of items in the collection matching the request parameters (9 query params)
- `support_feedbacks_create` POST `/api/support-feedbacks/` (request body)
- `support_feedbacks_retrieve` GET `/api/support-feedbacks/{uuid}/` (path: uuid)

## support-issue-statuses
Module: `waldur_api_client.api.support_issue_statuses`

- `support_issue_statuses_list` GET `/api/support-issue-statuses/` (no params)
- `support_issue_statuses_count` HEAD `/api/support-issue-statuses/` — Get number of items in the collection matching the request parameters (no params)
- `support_issue_statuses_create` POST `/api/support-issue-statuses/` (request body)
- `support_issue_statuses_retrieve` GET `/api/support-issue-statuses/{uuid}/` (path: uuid)
- `support_issue_statuses_update` PUT `/api/support-issue-statuses/{uuid}/` (path: uuid | request body)
- `support_issue_statuses_partial_update` PATCH `/api/support-issue-statuses/{uuid}/` (path: uuid | request body)
- `support_issue_statuses_destroy` DELETE `/api/support-issue-statuses/{uuid}/` (path: uuid)

## support-issues
Module: `waldur_api_client.api.support_issues`

- `support_issues_list` GET `/api/support-issues/` (21 query params)
- `support_issues_count` HEAD `/api/support-issues/` — Get number of items in the collection matching the request parameters (21 query params)
- `support_issues_create` POST `/api/support-issues/` (request body)
- `support_issues_retrieve` GET `/api/support-issues/{uuid}/` (path: uuid)
- `support_issues_update` PUT `/api/support-issues/{uuid}/` (path: uuid | request body)
- `support_issues_partial_update` PATCH `/api/support-issues/{uuid}/` (path: uuid | request body)
- `support_issues_destroy` DELETE `/api/support-issues/{uuid}/` (path: uuid)
- `support_issues_comment` POST `/api/support-issues/{uuid}/comment/` (path: uuid | request body)
- `support_issues_sync` POST `/api/support-issues/{uuid}/sync/` (path: uuid | request body)

## support-jira-webhook
Module: `waldur_api_client.api.support_jira_webhook`

- `support_jira_webhook` POST `/api/support-jira-webhook/` (request body)

## support-priorities
Module: `waldur_api_client.api.support_priorities`

- `support_priorities_list` GET `/api/support-priorities/` (2 query params)
- `support_priorities_count` HEAD `/api/support-priorities/` — Get number of items in the collection matching the request parameters (2 query params)
- `support_priorities_retrieve` GET `/api/support-priorities/{uuid}/` (path: uuid)

## support-request-types
Module: `waldur_api_client.api.support_request_types`

- `support_request_types_list` GET `/api/support-request-types/` (no params)
- `support_request_types_count` HEAD `/api/support-request-types/` — Get number of items in the collection matching the request parameters (no params)
- `support_request_types_retrieve` GET `/api/support-request-types/{uuid}/` (path: uuid)

## support-request-types-admin
Module: `waldur_api_client.api.support_request_types_admin`

- `support_request_types_admin_list` GET `/api/support-request-types-admin/` (2 query params)
- `support_request_types_admin_count` HEAD `/api/support-request-types-admin/` — Get number of items in the collection matching the request parameters (2 query params)
- `support_request_types_admin_create` POST `/api/support-request-types-admin/` (request body)
- `support_request_types_admin_reorder` POST `/api/support-request-types-admin/reorder/` — Bulk update order for multiple request types (request body)
- `support_request_types_admin_retrieve` GET `/api/support-request-types-admin/{uuid}/` (path: uuid)
- `support_request_types_admin_update` PUT `/api/support-request-types-admin/{uuid}/` (path: uuid | request body)
- `support_request_types_admin_partial_update` PATCH `/api/support-request-types-admin/{uuid}/` (path: uuid | request body)
- `support_request_types_admin_destroy` DELETE `/api/support-request-types-admin/{uuid}/` (path: uuid)
- `support_request_types_admin_activate` POST `/api/support-request-types-admin/{uuid}/activate/` — Activate a request type so it appears in issue creation (path: uuid | request body)
- `support_request_types_admin_deactivate` POST `/api/support-request-types-admin/{uuid}/deactivate/` — Deactivate a request type so it no longer appears in issue creation (path: uuid | request body)

## support-smax-webhook
Module: `waldur_api_client.api.support_smax_webhook`

- `support_smax_webhook` POST `/api/support-smax-webhook/` (request body)

## support-statistics
Module: `waldur_api_client.api.support_statistics`

- `support_statistics_retrieve` GET `/api/support-statistics/` (no params)

## support-templates
Module: `waldur_api_client.api.support_templates`

- `support_templates_list` GET `/api/support-templates/` (no params)
- `support_templates_count` HEAD `/api/support-templates/` — Get number of items in the collection matching the request parameters (no params)
- `support_templates_create` POST `/api/support-templates/` (request body)
- `support_templates_retrieve` GET `/api/support-templates/{uuid}/` (path: uuid)
- `support_templates_update` PUT `/api/support-templates/{uuid}/` (path: uuid | request body)
- `support_templates_partial_update` PATCH `/api/support-templates/{uuid}/` (path: uuid | request body)
- `support_templates_destroy` DELETE `/api/support-templates/{uuid}/` (path: uuid)
- `support_templates_create_attachments` POST `/api/support-templates/{uuid}/create_attachments/` — This view attaches documents to template (path: uuid | request body)
- `support_templates_delete_attachments` POST `/api/support-templates/{uuid}/delete_attachments/` (path: uuid | request body)

## support-users
Module: `waldur_api_client.api.support_users`

- `support_users_list` GET `/api/support-users/` (3 query params)
- `support_users_count` HEAD `/api/support-users/` — Get number of items in the collection matching the request parameters (3 query params)
- `support_users_retrieve` GET `/api/support-users/{uuid}/` (path: uuid)

## support-zammad-webhook
Module: `waldur_api_client.api.support_zammad_webhook`

- `support_zammad_webhook` POST `/api/support-zammad-webhook/` (no params)

## sync-issues
Module: `waldur_api_client.api.sync_issues`

- `sync_issues_retrieve` GET `/api/sync-issues/` — This view triggers synchronization of issues from backend (no params)
- `sync_issues` POST `/api/sync-issues/` — This view triggers synchronization of issues from backend (no params)

## system-logs
Module: `waldur_api_client.api.system_logs`

- `system_logs_list` GET `/api/system-logs/` (9 query params)
- `system_logs_count` HEAD `/api/system-logs/` — Get number of items in the collection matching the request parameters (9 query params)
- `system_logs_instances_list` GET `/api/system-logs/instances/` — List system log instances (9 query params)
- `system_logs_instances_count` HEAD `/api/system-logs/instances/` — List system log instances (9 query params)
- `system_logs_stats_retrieve` GET `/api/system-logs/stats/` — Get system log statistics (no params)
- `system_logs_stats_count` HEAD `/api/system-logs/stats/` — Get system log statistics (no params)
- `system_logs_retrieve` GET `/api/system-logs/{id}/` (path: id)

## user-action-executions
Module: `waldur_api_client.api.user_action_executions`

- `user_action_executions_list` GET `/api/user-action-executions/` (1 query param)
- `user_action_executions_count` HEAD `/api/user-action-executions/` — Get number of items in the collection matching the request parameters (1 query param)
- `user_action_executions_retrieve` GET `/api/user-action-executions/{id}/` (path: id)

## user-action-providers
Module: `waldur_api_client.api.user_action_providers`

- `user_action_providers_list` GET `/api/user-action-providers/` (no params)
- `user_action_providers_count` HEAD `/api/user-action-providers/` — Get number of items in the collection matching the request parameters (no params)
- `user_action_providers_retrieve` GET `/api/user-action-providers/{id}/` (path: id)

## user-actions
Module: `waldur_api_client.api.user_actions`

- `user_actions_list` GET `/api/user-actions/` (10 query params)
- `user_actions_count` HEAD `/api/user-actions/` — Get number of items in the collection matching the request parameters (10 query params)
- `user_actions_bulk_silence` POST `/api/user-actions/bulk_silence/` — Bulk silence actions by filters (request body)
- `user_actions_summary_retrieve` GET `/api/user-actions/summary/` — Get action summary counts (no params)
- `user_actions_summary_count` HEAD `/api/user-actions/summary/` — Get number of items in the collection matching the request parameters (no params)
- `user_actions_update_actions` POST `/api/user-actions/update_actions/` — Trigger update of user actions (request body)
- `user_actions_retrieve` GET `/api/user-actions/{uuid}/` (path: uuid)
- `user_actions_execute_action` POST `/api/user-actions/{uuid}/execute_action/` — Execute a corrective action (path: uuid | request body)
- `user_actions_silence` POST `/api/user-actions/{uuid}/silence/` — Silence an action temporarily or permanently (path: uuid | request body)
- `user_actions_unsilence` POST `/api/user-actions/{uuid}/unsilence/` — Remove silence from an action (path: uuid)

## user-agreements
Module: `waldur_api_client.api.user_agreements`

- `user_agreements_list` GET `/api/user-agreements/` — List user agreements (2 query params)
- `user_agreements_count` HEAD `/api/user-agreements/` — List user agreements (2 query params)
- `user_agreements_create` POST `/api/user-agreements/` (request body)
- `user_agreements_retrieve` GET `/api/user-agreements/{uuid}/` — Retrieve user agreement (path: uuid)
- `user_agreements_update` PUT `/api/user-agreements/{uuid}/` (path: uuid | request body)
- `user_agreements_partial_update` PATCH `/api/user-agreements/{uuid}/` (path: uuid | request body)
- `user_agreements_destroy` DELETE `/api/user-agreements/{uuid}/` (path: uuid)

## user-group-invitations
Module: `waldur_api_client.api.user_group_invitations`

- `user_group_invitations_list` GET `/api/user-group-invitations/` — List group invitations (7 query params)
- `user_group_invitations_count` HEAD `/api/user-group-invitations/` — List group invitations (7 query params)
- `user_group_invitations_create` POST `/api/user-group-invitations/` — Create group invitation (request body)
- `user_group_invitations_retrieve` GET `/api/user-group-invitations/{uuid}/` — Retrieve group invitation (path: uuid)
- `user_group_invitations_update` PUT `/api/user-group-invitations/{uuid}/` — Update a group invitation (path: uuid | request body)
- `user_group_invitations_partial_update` PATCH `/api/user-group-invitations/{uuid}/` — Partially update a group invitation (path: uuid | request body)
- `user_group_invitations_destroy` DELETE `/api/user-group-invitations/{uuid}/` — Delete a group invitation (path: uuid)
- `user_group_invitations_cancel` POST `/api/user-group-invitations/{uuid}/cancel/` — Cancel a group invitation (path: uuid)
- `user_group_invitations_projects_list` GET `/api/user-group-invitations/{uuid}/projects/` — List projects for a customer-scoped group invitation (path: uuid)
- `user_group_invitations_submit_request` POST `/api/user-group-invitations/{uuid}/submit_request/` — Submit a permission request (path: uuid)

## user-invitations
Module: `waldur_api_client.api.user_invitations`

- `user_invitations_list` GET `/api/user-invitations/` — List user invitations (11 query params)
- `user_invitations_count` HEAD `/api/user-invitations/` — List user invitations (11 query params)
- `user_invitations_create` POST `/api/user-invitations/` — Create user invitation (request body)
- `user_invitations_approve` POST `/api/user-invitations/approve/` — Approve a requested invitation (request body)
- `user_invitations_check_duplicates` POST `/api/user-invitations/check-duplicates/` — Check for duplicate invitations (request body)
- `user_invitations_reject` POST `/api/user-invitations/reject/` — Reject a requested invitation (request body)
- `user_invitations_retrieve` GET `/api/user-invitations/{uuid}/` — Retrieve user invitation (path: uuid)
- `user_invitations_update` PUT `/api/user-invitations/{uuid}/` — Update user invitation (path: uuid | request body)
- `user_invitations_partial_update` PATCH `/api/user-invitations/{uuid}/` — Partially update user invitation (path: uuid | request body)
- `user_invitations_destroy` DELETE `/api/user-invitations/{uuid}/` — Delete user invitation (path: uuid)
- `user_invitations_accept` POST `/api/user-invitations/{uuid}/accept/` — Accept an invitation (path: uuid)
- `user_invitations_cancel` POST `/api/user-invitations/{uuid}/cancel/` — Cancel an invitation (path: uuid)
- `user_invitations_check` POST `/api/user-invitations/{uuid}/check/` — Check invitation validity (path: uuid)
- `user_invitations_delete` POST `/api/user-invitations/{uuid}/delete/` — Delete an invitation (staff only) (path: uuid)
- `user_invitations_details_retrieve` GET `/api/user-invitations/{uuid}/details/` — Get public invitation details (path: uuid)
- `user_invitations_send` POST `/api/user-invitations/{uuid}/send/` — Resend an invitation (path: uuid)

## user-permission-requests
Module: `waldur_api_client.api.user_permission_requests`

- `user_permission_requests_list` GET `/api/user-permission-requests/` — List permission requests (5 query params)
- `user_permission_requests_count` HEAD `/api/user-permission-requests/` — List permission requests (5 query params)
- `user_permission_requests_retrieve` GET `/api/user-permission-requests/{uuid}/` — Retrieve permission request (path: uuid)
- `user_permission_requests_approve` POST `/api/user-permission-requests/{uuid}/approve/` — Approve a permission request (path: uuid | request body)
- `user_permission_requests_cancel_request` POST `/api/user-permission-requests/{uuid}/cancel_request/` — Cancel a permission request (path: uuid)
- `user_permission_requests_reject` POST `/api/user-permission-requests/{uuid}/reject/` — Reject a permission request (path: uuid | request body)

## user-permissions
Module: `waldur_api_client.api.user_permissions`

- `user_permissions_list` GET `/api/user-permissions/` — List user permissions (15 query params)
- `user_permissions_count` HEAD `/api/user-permissions/` — List user permissions (15 query params)
- `user_permissions_retrieve` GET `/api/user-permissions/{uuid}/` — Get permission details (path: uuid)

## users
Module: `waldur_api_client.api.users`

- `users_list` GET `/api/users/` (25 query params)
- `users_count` HEAD `/api/users/` — Get number of items in the collection matching the request parameters (24 query params)
- `users_create` POST `/api/users/` (request body)
- `users_confirm_email` POST `/api/users/confirm_email/` — Confirm email change (request body)
- `users_me_retrieve` GET `/api/users/me/` — Get current user details (1 query param)
- `users_me_count` HEAD `/api/users/me/` — Get current user details (no params)
- `users_profile_completeness_retrieve` GET `/api/users/profile_completeness/` — Check profile completeness (no params)
- `users_profile_completeness_count` HEAD `/api/users/profile_completeness/` — Check profile completeness (no params)
- `users_scim_sync_all` POST `/api/users/scim_sync_all/` — Trigger SCIM synchronization for all users (no params)
- `users_user_active_status_count_list` GET `/api/users/user_active_status_count/` — Get user counts by active status (24 query params)
- `users_user_active_status_count_count` HEAD `/api/users/user_active_status_count/` — Get user counts by active status (24 query params)
- `users_user_language_count_list` GET `/api/users/user_language_count/` — Get user counts by preferred language (24 query params)
- `users_user_language_count_count` HEAD `/api/users/user_language_count/` — Get user counts by preferred language (24 query params)
- `users_user_registration_trend_list` GET `/api/users/user_registration_trend/` — Get user registration trends by month (24 query params)
- `users_user_registration_trend_count` HEAD `/api/users/user_registration_trend/` — Get user registration trends by month (24 query params)
- `users_retrieve` GET `/api/users/{uuid}/` (path: uuid | 1 query param)
- `users_update` PUT `/api/users/{uuid}/` (path: uuid | request body)
- `users_partial_update` PATCH `/api/users/{uuid}/` (path: uuid | request body)
- `users_destroy` DELETE `/api/users/{uuid}/` (path: uuid)
- `users_cancel_change_email` POST `/api/users/{uuid}/cancel_change_email/` — Cancel email change request (path: uuid)
- `users_change_email` POST `/api/users/{uuid}/change_email/` — Request email change (path: uuid | request body)
- `users_change_password` POST `/api/users/{uuid}/change_password/` — Change user password (path: uuid | request body)
- `users_data_access_retrieve` GET `/api/users/{uuid}/data_access/` — Get user data access visibility (path: uuid)
- `users_data_access_history_list` GET `/api/users/{uuid}/data_access_history/` — Get user data access history (path: uuid | 27 query params)
- `users_history_list` GET `/api/users/{uuid}/history/` — Get version history (path: uuid | 26 query params)
- `users_history_at_retrieve` GET `/api/users/{uuid}/history/at/` — Get object state at a specific timestamp (path: uuid | 1 query param)
- `users_identity_bridge_status_retrieve` GET `/api/users/{uuid}/identity_bridge_status/` — Get identity bridge status for a user (path: uuid)
- `users_pull_remote_user` POST `/api/users/{uuid}/pull_remote_user/` — Synchronize user details from eduTEAMS (path: uuid)
- `users_refresh_token` POST `/api/users/{uuid}/refresh_token/` — Refresh user auth token (path: uuid)
- `users_send_notification` POST `/api/users/{uuid}/send_notification/` — Send action notification to a specific user (path: uuid)
- `users_token_retrieve` GET `/api/users/{uuid}/token/` — Get user auth token (path: uuid)
- `users_update_actions` POST `/api/users/{uuid}/update_actions/` — Recalculate user actions for a specific user (path: uuid | request body)

## version
Module: `waldur_api_client.api.version`

- `version_retrieve` GET `/api/version/` — Get application version (no params)

## vmware-clusters
Module: `waldur_api_client.api.vmware_clusters`

- `vmware_clusters_list` GET `/api/vmware-clusters/` (5 query params)
- `vmware_clusters_count` HEAD `/api/vmware-clusters/` — Get number of items in the collection matching the request parameters (5 query params)
- `vmware_clusters_retrieve` GET `/api/vmware-clusters/{uuid}/` (path: uuid)

## vmware-datastores
Module: `waldur_api_client.api.vmware_datastores`

- `vmware_datastores_list` GET `/api/vmware-datastores/` (5 query params)
- `vmware_datastores_count` HEAD `/api/vmware-datastores/` — Get number of items in the collection matching the request parameters (5 query params)
- `vmware_datastores_retrieve` GET `/api/vmware-datastores/{uuid}/` (path: uuid)

## vmware-disks
Module: `waldur_api_client.api.vmware_disks`

- `vmware_disks_list` GET `/api/vmware-disks/` (21 query params)
- `vmware_disks_count` HEAD `/api/vmware-disks/` — Get number of items in the collection matching the request parameters (20 query params)
- `vmware_disks_retrieve` GET `/api/vmware-disks/{uuid}/` (path: uuid | 1 query param)
- `vmware_disks_destroy` DELETE `/api/vmware-disks/{uuid}/` (path: uuid)
- `vmware_disks_extend` POST `/api/vmware-disks/{uuid}/extend/` — Increase disk capacity (path: uuid | request body)
- `vmware_disks_pull` POST `/api/vmware-disks/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `vmware_disks_set_erred` POST `/api/vmware-disks/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `vmware_disks_set_ok` POST `/api/vmware-disks/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `vmware_disks_unlink` POST `/api/vmware-disks/{uuid}/unlink/` — Unlink resource (path: uuid)

## vmware-folders
Module: `waldur_api_client.api.vmware_folders`

- `vmware_folders_list` GET `/api/vmware-folders/` (5 query params)
- `vmware_folders_count` HEAD `/api/vmware-folders/` — Get number of items in the collection matching the request parameters (5 query params)
- `vmware_folders_retrieve` GET `/api/vmware-folders/{uuid}/` (path: uuid)

## vmware-limits
Module: `waldur_api_client.api.vmware_limits`

- `vmware_limits_retrieve` GET `/api/vmware-limits/{uuid}/` (path: uuid)

## vmware-networks
Module: `waldur_api_client.api.vmware_networks`

- `vmware_networks_list` GET `/api/vmware-networks/` (6 query params)
- `vmware_networks_count` HEAD `/api/vmware-networks/` — Get number of items in the collection matching the request parameters (6 query params)
- `vmware_networks_retrieve` GET `/api/vmware-networks/{uuid}/` (path: uuid)

## vmware-ports
Module: `waldur_api_client.api.vmware_ports`

- `vmware_ports_list` GET `/api/vmware-ports/` (23 query params)
- `vmware_ports_count` HEAD `/api/vmware-ports/` — Get number of items in the collection matching the request parameters (22 query params)
- `vmware_ports_retrieve` GET `/api/vmware-ports/{uuid}/` (path: uuid | 1 query param)
- `vmware_ports_destroy` DELETE `/api/vmware-ports/{uuid}/` (path: uuid)
- `vmware_ports_pull` POST `/api/vmware-ports/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `vmware_ports_set_erred` POST `/api/vmware-ports/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `vmware_ports_set_ok` POST `/api/vmware-ports/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `vmware_ports_unlink` POST `/api/vmware-ports/{uuid}/unlink/` — Unlink resource (path: uuid)

## vmware-templates
Module: `waldur_api_client.api.vmware_templates`

- `vmware_templates_list` GET `/api/vmware-templates/` (4 query params)
- `vmware_templates_count` HEAD `/api/vmware-templates/` — Get number of items in the collection matching the request parameters (4 query params)
- `vmware_templates_retrieve` GET `/api/vmware-templates/{uuid}/` (path: uuid)

## vmware-virtual-machine
Module: `waldur_api_client.api.vmware_virtual_machine`

- `vmware_virtual_machine_list` GET `/api/vmware-virtual-machine/` (20 query params)
- `vmware_virtual_machine_count` HEAD `/api/vmware-virtual-machine/` — Get number of items in the collection matching the request parameters (19 query params)
- `vmware_virtual_machine_create` POST `/api/vmware-virtual-machine/` (request body)
- `vmware_virtual_machine_retrieve` GET `/api/vmware-virtual-machine/{uuid}/` (path: uuid | 1 query param)
- `vmware_virtual_machine_update` PUT `/api/vmware-virtual-machine/{uuid}/` (path: uuid | request body)
- `vmware_virtual_machine_partial_update` PATCH `/api/vmware-virtual-machine/{uuid}/` (path: uuid | request body)
- `vmware_virtual_machine_destroy` DELETE `/api/vmware-virtual-machine/{uuid}/` (path: uuid)
- `vmware_virtual_machine_console_retrieve` GET `/api/vmware-virtual-machine/{uuid}/console/` — This endpoint provides access to Virtual Machine Remote Console aka VMRC (path: uuid)
- `vmware_virtual_machine_create_disk` POST `/api/vmware-virtual-machine/{uuid}/create_disk/` (path: uuid | request body)
- `vmware_virtual_machine_create_port` POST `/api/vmware-virtual-machine/{uuid}/create_port/` (path: uuid | request body)
- `vmware_virtual_machine_pull` POST `/api/vmware-virtual-machine/{uuid}/pull/` — Synchronize resource state (path: uuid)
- `vmware_virtual_machine_reboot_guest` POST `/api/vmware-virtual-machine/{uuid}/reboot_guest/` (path: uuid)
- `vmware_virtual_machine_reset` POST `/api/vmware-virtual-machine/{uuid}/reset/` (path: uuid)
- `vmware_virtual_machine_set_erred` POST `/api/vmware-virtual-machine/{uuid}/set_erred/` — Mark resource as ERRED (path: uuid | request body)
- `vmware_virtual_machine_set_ok` POST `/api/vmware-virtual-machine/{uuid}/set_ok/` — Mark resource as OK (path: uuid)
- `vmware_virtual_machine_shutdown_guest` POST `/api/vmware-virtual-machine/{uuid}/shutdown_guest/` (path: uuid)
- `vmware_virtual_machine_start` POST `/api/vmware-virtual-machine/{uuid}/start/` (path: uuid)
- `vmware_virtual_machine_stop` POST `/api/vmware-virtual-machine/{uuid}/stop/` (path: uuid)
- `vmware_virtual_machine_suspend` POST `/api/vmware-virtual-machine/{uuid}/suspend/` (path: uuid)
- `vmware_virtual_machine_unlink` POST `/api/vmware-virtual-machine/{uuid}/unlink/` — Unlink resource (path: uuid)
- `vmware_virtual_machine_web_console_retrieve` GET `/api/vmware-virtual-machine/{uuid}/web_console/` — This endpoint provides access to HTML Console aka WMKS (path: uuid)
