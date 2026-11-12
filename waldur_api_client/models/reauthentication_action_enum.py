from enum import Enum


class ReauthenticationActionEnum(str, Enum):
    CHANGE_EMAIL = "change_email"
    CHANGE_PASSWORD = "change_password"
    CREATE_PERSONAL_ACCESS_TOKEN = "create_personal_access_token"
    REGISTER_PASSKEY = "register_passkey"
    REVOKE_PASSKEY = "revoke_passkey"
    TOKEN_LIFETIME = "token_lifetime"

    def __str__(self) -> str:
        return str(self.value)
