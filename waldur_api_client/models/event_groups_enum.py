from enum import Enum


class EventGroupsEnum(str, Enum):
    ACCESS_SUBNETS = "access_subnets"
    AUTH = "auth"
    CALL = "call"
    CREDITS = "credits"
    CUSTOMERS = "customers"
    INVOICES = "invoices"
    PERMISSIONS = "permissions"
    PROJECTS = "projects"
    PROPOSAL = "proposal"
    PROVIDERS = "providers"
    RESOURCES = "resources"
    REVIEW = "review"
    SSH = "ssh"
    SUPPORT = "support"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
