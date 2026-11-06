from enum import Enum


class ReviewerRegistryOEnum(str, Enum):
    CREATED = "created"
    STANDING_CHANGED_AT = "standing_changed_at"
    USER_EMAIL = "user_email"
    USER_NAME = "user_name"
    VALUE_0 = "-created"
    VALUE_1 = "-standing_changed_at"
    VALUE_2 = "-user_email"
    VALUE_3 = "-user_name"

    def __str__(self) -> str:
        return str(self.value)
