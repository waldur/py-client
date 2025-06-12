from enum import Enum


class ProposalProtectedCallsRetrieveFieldItem(str, Enum):
    BACKEND_ID = "backend_id"
    CREATED = "created"
    CREATED_BY = "created_by"
    CUSTOMER_NAME = "customer_name"
    CUSTOMER_UUID = "customer_uuid"
    DEFAULT_PROJECT_ROLE = "default_project_role"
    DEFAULT_PROJECT_ROLE_DESCRIPTION = "default_project_role_description"
    DEFAULT_PROJECT_ROLE_NAME = "default_project_role_name"
    DESCRIPTION = "description"
    DOCUMENTS = "documents"
    END_DATE = "end_date"
    EXTERNAL_URL = "external_url"
    FIXED_DURATION_IN_DAYS = "fixed_duration_in_days"
    MANAGER = "manager"
    NAME = "name"
    OFFERINGS = "offerings"
    REFERENCE_CODE = "reference_code"
    RESOURCE_TEMPLATES = "resource_templates"
    REVIEWER_IDENTITY_VISIBLE_TO_SUBMITTERS = "reviewer_identity_visible_to_submitters"
    REVIEWS_VISIBLE_TO_SUBMITTERS = "reviews_visible_to_submitters"
    ROUNDS = "rounds"
    SLUG = "slug"
    START_DATE = "start_date"
    STATE = "state"
    URL = "url"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
