from enum import Enum


class ObservableObjectTypeEnum(str, Enum):
    COURSE_ACCOUNT = "course_account"
    IMPORTABLE_RESOURCES = "importable_resources"
    OFFERING_RESOURCES_SYNC = "offering_resources_sync"
    OFFERING_USER = "offering_user"
    ORDER = "order"
    RESOURCE = "resource"
    RESOURCE_PERIODIC_LIMITS = "resource_periodic_limits"
    SERVICE_ACCOUNT = "service_account"
    USER_LIFECYCLE = "user_lifecycle"
    USER_PROFILE = "user_profile"
    USER_ROLE = "user_role"
    USER_SSH_KEY = "user_ssh_key"

    def __str__(self) -> str:
        return str(self.value)
