from enum import Enum


class ProposalPublicCallsListFieldItem(str, Enum):
    BACKEND_ID = "backend_id"
    CREATED = "created"
    CUSTOMER_NAME = "customer_name"
    CUSTOMER_UUID = "customer_uuid"
    DESCRIPTION = "description"
    DOCUMENTS = "documents"
    END_DATE = "end_date"
    EXTERNAL_URL = "external_url"
    MANAGER = "manager"
    NAME = "name"
    OFFERINGS = "offerings"
    ROUNDS = "rounds"
    SLUG = "slug"
    START_DATE = "start_date"
    STATE = "state"
    URL = "url"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
