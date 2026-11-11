from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.demo_preset_preview_entity_counts import DemoPresetPreviewEntityCounts
    from ..models.demo_preset_preview_feature_change import DemoPresetPreviewFeatureChange
    from ..models.demo_preset_preview_offering_group import DemoPresetPreviewOfferingGroup
    from ..models.demo_preset_preview_organization import DemoPresetPreviewOrganization
    from ..models.demo_preset_preview_overlay_contents import DemoPresetPreviewOverlayContents
    from ..models.demo_preset_preview_setting_change import DemoPresetPreviewSettingChange
    from ..models.demo_preset_preview_user import DemoPresetPreviewUser


T = TypeVar("T", bound="DemoPresetPreview")


@_attrs_define
class DemoPresetPreview:
    """
    Attributes:
        name (str):
        title (str):
        description (str):
        version (str):
        entity_counts (DemoPresetPreviewEntityCounts):
        scenarios (list[str]):
        overlay (Union[None, str]): The deployment's overlay preset imported after this one, if any.
        users (list['DemoPresetPreviewUser']):
        organizations (list['DemoPresetPreviewOrganization']):
        offerings (list['DemoPresetPreviewOfferingGroup']): The preset's offerings, grouped by type and category.
        overlay_contents (Union['DemoPresetPreviewOverlayContents', None]): What the deployment's overlay preset adds
            after this one.
        settings_changes (list['DemoPresetPreviewSettingChange']): Settings the load changes, and every setting the
            preset sets.
        feature_changes (list['DemoPresetPreviewFeatureChange']): Features the load changes, and every feature the
            preset sets.
        warnings (list[str]): What would not work after the load, such as a feature whose deployment configuration is
            missing.
    """

    name: str
    title: str
    description: str
    version: str
    entity_counts: "DemoPresetPreviewEntityCounts"
    scenarios: list[str]
    overlay: Union[None, str]
    users: list["DemoPresetPreviewUser"]
    organizations: list["DemoPresetPreviewOrganization"]
    offerings: list["DemoPresetPreviewOfferingGroup"]
    overlay_contents: Union["DemoPresetPreviewOverlayContents", None]
    settings_changes: list["DemoPresetPreviewSettingChange"]
    feature_changes: list["DemoPresetPreviewFeatureChange"]
    warnings: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.demo_preset_preview_overlay_contents import DemoPresetPreviewOverlayContents

        name = self.name

        title = self.title

        description = self.description

        version = self.version

        entity_counts = self.entity_counts.to_dict()

        scenarios = self.scenarios

        overlay: Union[None, str]
        overlay = self.overlay

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

        overlay_contents: Union[None, dict[str, Any]]
        if isinstance(self.overlay_contents, DemoPresetPreviewOverlayContents):
            overlay_contents = self.overlay_contents.to_dict()
        else:
            overlay_contents = self.overlay_contents

        settings_changes = []
        for settings_changes_item_data in self.settings_changes:
            settings_changes_item = settings_changes_item_data.to_dict()
            settings_changes.append(settings_changes_item)

        feature_changes = []
        for feature_changes_item_data in self.feature_changes:
            feature_changes_item = feature_changes_item_data.to_dict()
            feature_changes.append(feature_changes_item)

        warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "title": title,
                "description": description,
                "version": version,
                "entity_counts": entity_counts,
                "scenarios": scenarios,
                "overlay": overlay,
                "users": users,
                "organizations": organizations,
                "offerings": offerings,
                "overlay_contents": overlay_contents,
                "settings_changes": settings_changes,
                "feature_changes": feature_changes,
                "warnings": warnings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.demo_preset_preview_entity_counts import DemoPresetPreviewEntityCounts
        from ..models.demo_preset_preview_feature_change import DemoPresetPreviewFeatureChange
        from ..models.demo_preset_preview_offering_group import DemoPresetPreviewOfferingGroup
        from ..models.demo_preset_preview_organization import DemoPresetPreviewOrganization
        from ..models.demo_preset_preview_overlay_contents import DemoPresetPreviewOverlayContents
        from ..models.demo_preset_preview_setting_change import DemoPresetPreviewSettingChange
        from ..models.demo_preset_preview_user import DemoPresetPreviewUser

        d = dict(src_dict)
        name = d.pop("name")

        title = d.pop("title")

        description = d.pop("description")

        version = d.pop("version")

        entity_counts = DemoPresetPreviewEntityCounts.from_dict(d.pop("entity_counts"))

        scenarios = cast(list[str], d.pop("scenarios"))

        def _parse_overlay(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        overlay = _parse_overlay(d.pop("overlay"))

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

        def _parse_overlay_contents(data: object) -> Union["DemoPresetPreviewOverlayContents", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                overlay_contents_type_1 = DemoPresetPreviewOverlayContents.from_dict(data)

                return overlay_contents_type_1
            except:  # noqa: E722
                pass
            return cast(Union["DemoPresetPreviewOverlayContents", None], data)

        overlay_contents = _parse_overlay_contents(d.pop("overlay_contents"))

        settings_changes = []
        _settings_changes = d.pop("settings_changes")
        for settings_changes_item_data in _settings_changes:
            settings_changes_item = DemoPresetPreviewSettingChange.from_dict(settings_changes_item_data)

            settings_changes.append(settings_changes_item)

        feature_changes = []
        _feature_changes = d.pop("feature_changes")
        for feature_changes_item_data in _feature_changes:
            feature_changes_item = DemoPresetPreviewFeatureChange.from_dict(feature_changes_item_data)

            feature_changes.append(feature_changes_item)

        warnings = cast(list[str], d.pop("warnings"))

        demo_preset_preview = cls(
            name=name,
            title=title,
            description=description,
            version=version,
            entity_counts=entity_counts,
            scenarios=scenarios,
            overlay=overlay,
            users=users,
            organizations=organizations,
            offerings=offerings,
            overlay_contents=overlay_contents,
            settings_changes=settings_changes,
            feature_changes=feature_changes,
            warnings=warnings,
        )

        demo_preset_preview.additional_properties = d
        return demo_preset_preview

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
