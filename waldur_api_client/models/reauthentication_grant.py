import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reauthentication_action_enum import ReauthenticationActionEnum

T = TypeVar("T", bound="ReauthenticationGrant")


@_attrs_define
class ReauthenticationGrant:
    """
    Attributes:
        grant (str): Send it in the X-Reauthentication-Grant header of the change it is for. It is single-use and is not
            shown again.
        action (ReauthenticationActionEnum):
        expires_at (datetime.datetime): When the grant stops being usable.
    """

    grant: str
    action: ReauthenticationActionEnum
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant = self.grant

        action = self.action.value

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant": grant,
                "action": action,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant = d.pop("grant")

        action = ReauthenticationActionEnum(d.pop("action"))

        expires_at = isoparse(d.pop("expires_at"))

        reauthentication_grant = cls(
            grant=grant,
            action=action,
            expires_at=expires_at,
        )

        reauthentication_grant.additional_properties = d
        return reauthentication_grant

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
