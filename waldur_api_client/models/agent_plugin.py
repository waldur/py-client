from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.roles_enum import RolesEnum

if TYPE_CHECKING:
    from ..models.agent_plugin_component_schema_type_0 import AgentPluginComponentSchemaType0
    from ..models.agent_plugin_settings_schema_type_0 import AgentPluginSettingsSchemaType0


T = TypeVar("T", bound="AgentPlugin")


@_attrs_define
class AgentPlugin:
    """
    Attributes:
        name (str): Entry point name, as used in the agent configuration
        package (str):
        version (str): Version of the package the catalog was built from
        roles (list[RolesEnum]):
        settings_schema (Union['AgentPluginSettingsSchemaType0', None]): JSON Schema of the backend settings
        component_schema (Union['AgentPluginComponentSchemaType0', None]): JSON Schema of the plugin's component fields
        secret_settings (list[str]): Dotted paths of settings that stay in the agent configuration file
    """

    name: str
    package: str
    version: str
    roles: list[RolesEnum]
    settings_schema: Union["AgentPluginSettingsSchemaType0", None]
    component_schema: Union["AgentPluginComponentSchemaType0", None]
    secret_settings: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_plugin_component_schema_type_0 import AgentPluginComponentSchemaType0
        from ..models.agent_plugin_settings_schema_type_0 import AgentPluginSettingsSchemaType0

        name = self.name

        package = self.package

        version = self.version

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.value
            roles.append(roles_item)

        settings_schema: Union[None, dict[str, Any]]
        if isinstance(self.settings_schema, AgentPluginSettingsSchemaType0):
            settings_schema = self.settings_schema.to_dict()
        else:
            settings_schema = self.settings_schema

        component_schema: Union[None, dict[str, Any]]
        if isinstance(self.component_schema, AgentPluginComponentSchemaType0):
            component_schema = self.component_schema.to_dict()
        else:
            component_schema = self.component_schema

        secret_settings = self.secret_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "package": package,
                "version": version,
                "roles": roles,
                "settings_schema": settings_schema,
                "component_schema": component_schema,
                "secret_settings": secret_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_plugin_component_schema_type_0 import AgentPluginComponentSchemaType0
        from ..models.agent_plugin_settings_schema_type_0 import AgentPluginSettingsSchemaType0

        d = dict(src_dict)
        name = d.pop("name")

        package = d.pop("package")

        version = d.pop("version")

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = RolesEnum(roles_item_data)

            roles.append(roles_item)

        def _parse_settings_schema(data: object) -> Union["AgentPluginSettingsSchemaType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_schema_type_0 = AgentPluginSettingsSchemaType0.from_dict(data)

                return settings_schema_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AgentPluginSettingsSchemaType0", None], data)

        settings_schema = _parse_settings_schema(d.pop("settings_schema"))

        def _parse_component_schema(data: object) -> Union["AgentPluginComponentSchemaType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                component_schema_type_0 = AgentPluginComponentSchemaType0.from_dict(data)

                return component_schema_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AgentPluginComponentSchemaType0", None], data)

        component_schema = _parse_component_schema(d.pop("component_schema"))

        secret_settings = cast(list[str], d.pop("secret_settings"))

        agent_plugin = cls(
            name=name,
            package=package,
            version=version,
            roles=roles,
            settings_schema=settings_schema,
            component_schema=component_schema,
            secret_settings=secret_settings,
        )

        agent_plugin.additional_properties = d
        return agent_plugin

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
