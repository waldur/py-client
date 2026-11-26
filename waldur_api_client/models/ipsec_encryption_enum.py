from enum import Enum


class IpsecEncryptionEnum(str, Enum):
    AES128 = "aes128"
    AES128GCM16 = "aes128gcm16"
    AES192 = "aes192"
    AES256 = "aes256"
    AES256GCM16 = "aes256gcm16"
    CHACHA20POLY1305 = "chacha20poly1305"

    def __str__(self) -> str:
        return str(self.value)
