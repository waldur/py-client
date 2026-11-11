from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.demo_preset_preview_role import DemoPresetPreviewRole


T = TypeVar("T", bound="DemoPresetPreviewUser")


@_attrs_define
class DemoPresetPreviewUser:
    """
    Attributes:
        username (str):
        email (str):
        full_name (str):
        is_staff (bool):
        is_support (bool):
        is_active (bool): An inactive user is imported but cannot log in.
        password (Union[None, str]): The preset's password for this user. Never given for staff, support or inactive
            users, or for the overlay's users.
        roles (list['DemoPresetPreviewRole']):
    """

    username: str
    email: str
    full_name: str
    is_staff: bool
    is_support: bool
    is_active: bool
    password: Union[None, str]
    roles: list["DemoPresetPreviewRole"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        email = self.email

        full_name = self.full_name

        is_staff = self.is_staff

        is_support = self.is_support

        is_active = self.is_active

        password: Union[None, str]
        password = self.password

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "email": email,
                "full_name": full_name,
                "is_staff": is_staff,
                "is_support": is_support,
                "is_active": is_active,
                "password": password,
                "roles": roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.demo_preset_preview_role import DemoPresetPreviewRole

        d = dict(src_dict)
        username = d.pop("username")

        email = d.pop("email")

        full_name = d.pop("full_name")

        is_staff = d.pop("is_staff")

        is_support = d.pop("is_support")

        is_active = d.pop("is_active")

        def _parse_password(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        password = _parse_password(d.pop("password"))

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = DemoPresetPreviewRole.from_dict(roles_item_data)

            roles.append(roles_item)

        demo_preset_preview_user = cls(
            username=username,
            email=email,
            full_name=full_name,
            is_staff=is_staff,
            is_support=is_support,
            is_active=is_active,
            password=password,
            roles=roles,
        )

        demo_preset_preview_user.additional_properties = d
        return demo_preset_preview_user

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
