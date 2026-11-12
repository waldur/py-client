from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reauthentication_action_enum import ReauthenticationActionEnum

if TYPE_CHECKING:
    from ..models.passkey_reauthentication_finish_request_credential import (
        PasskeyReauthenticationFinishRequestCredential,
    )


T = TypeVar("T", bound="PasskeyReauthenticationFinishRequest")


@_attrs_define
class PasskeyReauthenticationFinishRequest:
    """
    Attributes:
        action (ReauthenticationActionEnum):
        ceremony (UUID):
        credential (PasskeyReauthenticationFinishRequestCredential):
    """

    action: ReauthenticationActionEnum
    ceremony: UUID
    credential: "PasskeyReauthenticationFinishRequestCredential"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        ceremony = str(self.ceremony)

        credential = self.credential.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "ceremony": ceremony,
                "credential": credential,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.passkey_reauthentication_finish_request_credential import (
            PasskeyReauthenticationFinishRequestCredential,
        )

        d = dict(src_dict)
        action = ReauthenticationActionEnum(d.pop("action"))

        ceremony = UUID(d.pop("ceremony"))

        credential = PasskeyReauthenticationFinishRequestCredential.from_dict(d.pop("credential"))

        passkey_reauthentication_finish_request = cls(
            action=action,
            ceremony=ceremony,
            credential=credential,
        )

        passkey_reauthentication_finish_request.additional_properties = d
        return passkey_reauthentication_finish_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
