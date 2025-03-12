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
    MANAGER = "manager"
    NAME = "name"
    OFFERINGS = "offerings"
    REFERENCE_CODE = "reference_code"
    ROUNDS = "rounds"
    SLUG = "slug"
    START_DATE = "start_date"
    STATE = "state"
    URL = "url"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
