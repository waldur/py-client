from enum import Enum


class ChatThreadsListFieldItem(str, Enum):
    CHAT_SESSION = "chat_session"
    CREATED = "created"
    FLAGS = "flags"
    IS_ARCHIVED = "is_archived"
    MESSAGE_COUNT = "message_count"
    NAME = "name"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
