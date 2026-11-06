from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dry_run_viewer_permissions_item import DryRunViewerPermissionsItem


T = TypeVar("T", bound="DryRunViewer")


@_attrs_define
class DryRunViewer:
    """
    Attributes:
        uuid (UUID):
        username (str):
        full_name (str):
        is_staff (bool):
        is_support (bool):
        permissions (list['DryRunViewerPermissionsItem']):
    """

    uuid: UUID
    username: str
    full_name: str
    is_staff: bool
    is_support: bool
    permissions: list["DryRunViewerPermissionsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        username = self.username

        full_name = self.full_name

        is_staff = self.is_staff

        is_support = self.is_support

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.to_dict()
            permissions.append(permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "username": username,
                "full_name": full_name,
                "is_staff": is_staff,
                "is_support": is_support,
                "permissions": permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dry_run_viewer_permissions_item import DryRunViewerPermissionsItem

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        username = d.pop("username")

        full_name = d.pop("full_name")

        is_staff = d.pop("is_staff")

        is_support = d.pop("is_support")

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = DryRunViewerPermissionsItem.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        dry_run_viewer = cls(
            uuid=uuid,
            username=username,
            full_name=full_name,
            is_staff=is_staff,
            is_support=is_support,
            permissions=permissions,
        )

        dry_run_viewer.additional_properties = d
        return dry_run_viewer

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
