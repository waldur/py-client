from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_me_features_additional_property import UserMeFeaturesAdditionalProperty


T = TypeVar("T", bound="UserMeFeatures")


@_attrs_define
class UserMeFeatures:
    """Effective values of the user-scoped feature flags for this user: the global value, or on when a feature rule matches
    the user. Same section -> key -> bool shape as FEATURES in the configuration.

    """

    additional_properties: dict[str, "UserMeFeaturesAdditionalProperty"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_me_features_additional_property import UserMeFeaturesAdditionalProperty

        d = dict(src_dict)
        user_me_features = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = UserMeFeaturesAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        user_me_features.additional_properties = additional_properties
        return user_me_features

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "UserMeFeaturesAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "UserMeFeaturesAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
