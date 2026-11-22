from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.requirement_enum import RequirementEnum

T = TypeVar("T", bound="SiteAgentConfigSecret")


@_attrs_define
class SiteAgentConfigSecret:
    """
    Attributes:
        offering_uuid (UUID):
        offering_name (str):
        field (str): Where the secret goes in the offering, such as waldur_api_token or
            backend_settings.ldap.bind_password.
        backend (Union[None, str]): The backend that reads it; null for the offering's own fields.
        requirement (RequirementEnum):
        in_file (bool): Whether the file has a placeholder for it; otherwise it is only listed, to be added where it
            applies.
        env_var (Union[None, str]): The variable the placeholder names, with secret_format=env.
    """

    offering_uuid: UUID
    offering_name: str
    field: str
    backend: Union[None, str]
    requirement: RequirementEnum
    in_file: bool
    env_var: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offering_uuid = str(self.offering_uuid)

        offering_name = self.offering_name

        field = self.field

        backend: Union[None, str]
        backend = self.backend

        requirement = self.requirement.value

        in_file = self.in_file

        env_var: Union[None, str]
        env_var = self.env_var

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offering_uuid": offering_uuid,
                "offering_name": offering_name,
                "field": field,
                "backend": backend,
                "requirement": requirement,
                "in_file": in_file,
                "env_var": env_var,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offering_uuid = UUID(d.pop("offering_uuid"))

        offering_name = d.pop("offering_name")

        field = d.pop("field")

        def _parse_backend(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        backend = _parse_backend(d.pop("backend"))

        requirement = RequirementEnum(d.pop("requirement"))

        in_file = d.pop("in_file")

        def _parse_env_var(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        env_var = _parse_env_var(d.pop("env_var"))

        site_agent_config_secret = cls(
            offering_uuid=offering_uuid,
            offering_name=offering_name,
            field=field,
            backend=backend,
            requirement=requirement,
            in_file=in_file,
            env_var=env_var,
        )

        site_agent_config_secret.additional_properties = d
        return site_agent_config_secret

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
