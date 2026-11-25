from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_feature_rule_request_user_claims import PatchedFeatureRuleRequestUserClaims


T = TypeVar("T", bound="PatchedFeatureRuleRequest")


@_attrs_define
class PatchedFeatureRuleRequest:
    """
    Attributes:
        feature_key (Union[Unset, str]): Dotted key of a user-scoped feature flag, or micro_apps.<name> for a micro-app.
        description (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        users (Union[Unset, list[UUID]]): UUIDs of the users the rule lists.
        customers (Union[Unset, list[UUID]]): UUIDs of organizations; a member of any of them matches.
        organization_groups (Union[Unset, list[UUID]]): UUIDs of organization groups; a member of an organization in any
            of them matches.
        roles (Union[Unset, list[str]]): Role names; the user must hold one of them in any scope.
        user_affiliations (Union[Unset, list[str]]):
        user_email_patterns (Union[Unset, list[str]]):
        user_identity_sources (Union[Unset, list[str]]):
        user_nationalities (Union[Unset, list[str]]):
        user_organization_types (Union[Unset, list[str]]):
        user_assurance_levels (Union[Unset, list[str]]):
        user_claims (Union[Unset, PatchedFeatureRuleRequestUserClaims]): Identity provider claims the user must carry,
            as {"claim": ["accepted", "values"]}. All claims must match; within one claim any value matches. A value ending
            in '*' matches by prefix.
    """

    feature_key: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    users: Union[Unset, list[UUID]] = UNSET
    customers: Union[Unset, list[UUID]] = UNSET
    organization_groups: Union[Unset, list[UUID]] = UNSET
    roles: Union[Unset, list[str]] = UNSET
    user_affiliations: Union[Unset, list[str]] = UNSET
    user_email_patterns: Union[Unset, list[str]] = UNSET
    user_identity_sources: Union[Unset, list[str]] = UNSET
    user_nationalities: Union[Unset, list[str]] = UNSET
    user_organization_types: Union[Unset, list[str]] = UNSET
    user_assurance_levels: Union[Unset, list[str]] = UNSET
    user_claims: Union[Unset, "PatchedFeatureRuleRequestUserClaims"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_key = self.feature_key

        description = self.description

        is_active = self.is_active

        users: Union[Unset, list[str]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = str(users_item_data)
                users.append(users_item)

        customers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.customers, Unset):
            customers = []
            for customers_item_data in self.customers:
                customers_item = str(customers_item_data)
                customers.append(customers_item)

        organization_groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.organization_groups, Unset):
            organization_groups = []
            for organization_groups_item_data in self.organization_groups:
                organization_groups_item = str(organization_groups_item_data)
                organization_groups.append(organization_groups_item)

        roles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        user_affiliations: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_affiliations, Unset):
            user_affiliations = self.user_affiliations

        user_email_patterns: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_email_patterns, Unset):
            user_email_patterns = self.user_email_patterns

        user_identity_sources: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_identity_sources, Unset):
            user_identity_sources = self.user_identity_sources

        user_nationalities: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_nationalities, Unset):
            user_nationalities = self.user_nationalities

        user_organization_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_organization_types, Unset):
            user_organization_types = self.user_organization_types

        user_assurance_levels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_assurance_levels, Unset):
            user_assurance_levels = self.user_assurance_levels

        user_claims: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user_claims, Unset):
            user_claims = self.user_claims.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feature_key is not UNSET:
            field_dict["feature_key"] = feature_key
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if users is not UNSET:
            field_dict["users"] = users
        if customers is not UNSET:
            field_dict["customers"] = customers
        if organization_groups is not UNSET:
            field_dict["organization_groups"] = organization_groups
        if roles is not UNSET:
            field_dict["roles"] = roles
        if user_affiliations is not UNSET:
            field_dict["user_affiliations"] = user_affiliations
        if user_email_patterns is not UNSET:
            field_dict["user_email_patterns"] = user_email_patterns
        if user_identity_sources is not UNSET:
            field_dict["user_identity_sources"] = user_identity_sources
        if user_nationalities is not UNSET:
            field_dict["user_nationalities"] = user_nationalities
        if user_organization_types is not UNSET:
            field_dict["user_organization_types"] = user_organization_types
        if user_assurance_levels is not UNSET:
            field_dict["user_assurance_levels"] = user_assurance_levels
        if user_claims is not UNSET:
            field_dict["user_claims"] = user_claims

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patched_feature_rule_request_user_claims import PatchedFeatureRuleRequestUserClaims

        d = dict(src_dict)
        feature_key = d.pop("feature_key", UNSET)

        description = d.pop("description", UNSET)

        is_active = d.pop("is_active", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = UUID(users_item_data)

            users.append(users_item)

        customers = []
        _customers = d.pop("customers", UNSET)
        for customers_item_data in _customers or []:
            customers_item = UUID(customers_item_data)

            customers.append(customers_item)

        organization_groups = []
        _organization_groups = d.pop("organization_groups", UNSET)
        for organization_groups_item_data in _organization_groups or []:
            organization_groups_item = UUID(organization_groups_item_data)

            organization_groups.append(organization_groups_item)

        roles = cast(list[str], d.pop("roles", UNSET))

        user_affiliations = cast(list[str], d.pop("user_affiliations", UNSET))

        user_email_patterns = cast(list[str], d.pop("user_email_patterns", UNSET))

        user_identity_sources = cast(list[str], d.pop("user_identity_sources", UNSET))

        user_nationalities = cast(list[str], d.pop("user_nationalities", UNSET))

        user_organization_types = cast(list[str], d.pop("user_organization_types", UNSET))

        user_assurance_levels = cast(list[str], d.pop("user_assurance_levels", UNSET))

        _user_claims = d.pop("user_claims", UNSET)
        user_claims: Union[Unset, PatchedFeatureRuleRequestUserClaims]
        if isinstance(_user_claims, Unset):
            user_claims = UNSET
        else:
            user_claims = PatchedFeatureRuleRequestUserClaims.from_dict(_user_claims)

        patched_feature_rule_request = cls(
            feature_key=feature_key,
            description=description,
            is_active=is_active,
            users=users,
            customers=customers,
            organization_groups=organization_groups,
            roles=roles,
            user_affiliations=user_affiliations,
            user_email_patterns=user_email_patterns,
            user_identity_sources=user_identity_sources,
            user_nationalities=user_nationalities,
            user_organization_types=user_organization_types,
            user_assurance_levels=user_assurance_levels,
            user_claims=user_claims,
        )

        patched_feature_rule_request.additional_properties = d
        return patched_feature_rule_request

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
