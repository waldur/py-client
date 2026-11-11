from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.demo_preset_preview_offering_group import DemoPresetPreviewOfferingGroup
    from ..models.demo_preset_preview_organization import DemoPresetPreviewOrganization
    from ..models.demo_preset_preview_user import DemoPresetPreviewUser


T = TypeVar("T", bound="DemoPresetPreviewOverlayContents")


@_attrs_define
class DemoPresetPreviewOverlayContents:
    """
    Attributes:
        users (list['DemoPresetPreviewUser']):
        organizations (list['DemoPresetPreviewOrganization']):
        offerings (list['DemoPresetPreviewOfferingGroup']):
    """

    users: list["DemoPresetPreviewUser"]
    organizations: list["DemoPresetPreviewOrganization"]
    offerings: list["DemoPresetPreviewOfferingGroup"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        organizations = []
        for organizations_item_data in self.organizations:
            organizations_item = organizations_item_data.to_dict()
            organizations.append(organizations_item)

        offerings = []
        for offerings_item_data in self.offerings:
            offerings_item = offerings_item_data.to_dict()
            offerings.append(offerings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
                "organizations": organizations,
                "offerings": offerings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.demo_preset_preview_offering_group import DemoPresetPreviewOfferingGroup
        from ..models.demo_preset_preview_organization import DemoPresetPreviewOrganization
        from ..models.demo_preset_preview_user import DemoPresetPreviewUser

        d = dict(src_dict)
        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = DemoPresetPreviewUser.from_dict(users_item_data)

            users.append(users_item)

        organizations = []
        _organizations = d.pop("organizations")
        for organizations_item_data in _organizations:
            organizations_item = DemoPresetPreviewOrganization.from_dict(organizations_item_data)

            organizations.append(organizations_item)

        offerings = []
        _offerings = d.pop("offerings")
        for offerings_item_data in _offerings:
            offerings_item = DemoPresetPreviewOfferingGroup.from_dict(offerings_item_data)

            offerings.append(offerings_item)

        demo_preset_preview_overlay_contents = cls(
            users=users,
            organizations=organizations,
            offerings=offerings,
        )

        demo_preset_preview_overlay_contents.additional_properties = d
        return demo_preset_preview_overlay_contents

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
