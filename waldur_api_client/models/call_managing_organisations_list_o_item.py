from enum import Enum


class CallManagingOrganisationsListOItem(str, Enum):
    CUSTOMER_NAME = "customer_name"
    VALUE_0 = "-customer_name"

    def __str__(self) -> str:
        return str(self.value)
