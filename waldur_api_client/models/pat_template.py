from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pat_template_feature import PatTemplateFeature


T = TypeVar("T", bound="PatTemplate")


@_attrs_define
class PatTemplate:
    """
    Attributes:
        key (str):
        name (str):
        description (str):
        required_scopes (list[str]):
        optional_features (list['PatTemplateFeature']):
        binding_types (list[str]): Entity types a token from this template is bound to.
        default_lifetime_days (int): Suggested lifetime, capped by the site's maximum token lifetime.
        dedicated_user_types (list[str]): Target types staff can create a dedicated user for, whose token is restricted
            to the target (agent_user).
    """

    key: str
    name: str
    description: str
    required_scopes: list[str]
    optional_features: list["PatTemplateFeature"]
    binding_types: list[str]
    default_lifetime_days: int
    dedicated_user_types: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        description = self.description

        required_scopes = self.required_scopes

        optional_features = []
        for optional_features_item_data in self.optional_features:
            optional_features_item = optional_features_item_data.to_dict()
            optional_features.append(optional_features_item)

        binding_types = self.binding_types

        default_lifetime_days = self.default_lifetime_days

        dedicated_user_types = self.dedicated_user_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "description": description,
                "required_scopes": required_scopes,
                "optional_features": optional_features,
                "binding_types": binding_types,
                "default_lifetime_days": default_lifetime_days,
                "dedicated_user_types": dedicated_user_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pat_template_feature import PatTemplateFeature

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        description = d.pop("description")

        required_scopes = cast(list[str], d.pop("required_scopes"))

        optional_features = []
        _optional_features = d.pop("optional_features")
        for optional_features_item_data in _optional_features:
            optional_features_item = PatTemplateFeature.from_dict(optional_features_item_data)

            optional_features.append(optional_features_item)

        binding_types = cast(list[str], d.pop("binding_types"))

        default_lifetime_days = d.pop("default_lifetime_days")

        dedicated_user_types = cast(list[str], d.pop("dedicated_user_types"))

        pat_template = cls(
            key=key,
            name=name,
            description=description,
            required_scopes=required_scopes,
            optional_features=optional_features,
            binding_types=binding_types,
            default_lifetime_days=default_lifetime_days,
            dedicated_user_types=dedicated_user_types,
        )

        pat_template.additional_properties = d
        return pat_template

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
