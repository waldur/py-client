from enum import Enum


class ChatThreadsListFieldItem(str, Enum):
    CHAT_SESSION = "chat_session"
    CREATED = "created"
    FLAGS = "flags"
    IS_ARCHIVED = "is_archived"
    MESSAGE_COUNT = "message_count"
    MODIFIED = "modified"
    NAME = "name"
    USER_FULL_NAME = "user_full_name"
    USER_USERNAME = "user_username"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
