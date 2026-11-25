import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_rule_user_claims import FeatureRuleUserClaims
    from ..models.named_summary import NamedSummary
    from ..models.user_summary import UserSummary


T = TypeVar("T", bound="FeatureRule")


@_attrs_define
class FeatureRule:
    """
    Attributes:
        url (str):
        uuid (UUID):
        feature_key (str): Dotted key of a user-scoped feature flag, or micro_apps.<name> for a micro-app.
        is_orphaned (bool): True when the rule targets a feature that is no longer user-scoped, or a micro-app without a
            setting: it then has no effect.
        users_summary (list['UserSummary']):
        customers_summary (list['NamedSummary']):
        organization_groups_summary (list['NamedSummary']):
        created_by (Union[None, UUID]):
        created_by_username (Union[None, str]):
        created (datetime.datetime):
        modified (datetime.datetime):
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
        user_claims (Union[Unset, FeatureRuleUserClaims]): Identity provider claims the user must carry, as {"claim":
            ["accepted", "values"]}. All claims must match; within one claim any value matches. A value ending in '*'
            matches by prefix.
    """

    url: str
    uuid: UUID
    feature_key: str
    is_orphaned: bool
    users_summary: list["UserSummary"]
    customers_summary: list["NamedSummary"]
    organization_groups_summary: list["NamedSummary"]
    created_by: Union[None, UUID]
    created_by_username: Union[None, str]
    created: datetime.datetime
    modified: datetime.datetime
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
    user_claims: Union[Unset, "FeatureRuleUserClaims"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        feature_key = self.feature_key

        is_orphaned = self.is_orphaned

        users_summary = []
        for users_summary_item_data in self.users_summary:
            users_summary_item = users_summary_item_data.to_dict()
            users_summary.append(users_summary_item)

        customers_summary = []
        for customers_summary_item_data in self.customers_summary:
            customers_summary_item = customers_summary_item_data.to_dict()
            customers_summary.append(customers_summary_item)

        organization_groups_summary = []
        for organization_groups_summary_item_data in self.organization_groups_summary:
            organization_groups_summary_item = organization_groups_summary_item_data.to_dict()
            organization_groups_summary.append(organization_groups_summary_item)

        created_by: Union[None, str]
        if isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        created_by_username: Union[None, str]
        created_by_username = self.created_by_username

        created = self.created.isoformat()

        modified = self.modified.isoformat()

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
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "feature_key": feature_key,
                "is_orphaned": is_orphaned,
                "users_summary": users_summary,
                "customers_summary": customers_summary,
                "organization_groups_summary": organization_groups_summary,
                "created_by": created_by,
                "created_by_username": created_by_username,
                "created": created,
                "modified": modified,
            }
        )
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
        from ..models.feature_rule_user_claims import FeatureRuleUserClaims
        from ..models.named_summary import NamedSummary
        from ..models.user_summary import UserSummary

        d = dict(src_dict)
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        feature_key = d.pop("feature_key")

        is_orphaned = d.pop("is_orphaned")

        users_summary = []
        _users_summary = d.pop("users_summary")
        for users_summary_item_data in _users_summary:
            users_summary_item = UserSummary.from_dict(users_summary_item_data)

            users_summary.append(users_summary_item)

        customers_summary = []
        _customers_summary = d.pop("customers_summary")
        for customers_summary_item_data in _customers_summary:
            customers_summary_item = NamedSummary.from_dict(customers_summary_item_data)

            customers_summary.append(customers_summary_item)

        organization_groups_summary = []
        _organization_groups_summary = d.pop("organization_groups_summary")
        for organization_groups_summary_item_data in _organization_groups_summary:
            organization_groups_summary_item = NamedSummary.from_dict(organization_groups_summary_item_data)

            organization_groups_summary.append(organization_groups_summary_item)

        def _parse_created_by(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        created_by = _parse_created_by(d.pop("created_by"))

        def _parse_created_by_username(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by_username = _parse_created_by_username(d.pop("created_by_username"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

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
        user_claims: Union[Unset, FeatureRuleUserClaims]
        if isinstance(_user_claims, Unset):
            user_claims = UNSET
        else:
            user_claims = FeatureRuleUserClaims.from_dict(_user_claims)

        feature_rule = cls(
            url=url,
            uuid=uuid,
            feature_key=feature_key,
            is_orphaned=is_orphaned,
            users_summary=users_summary,
            customers_summary=customers_summary,
            organization_groups_summary=organization_groups_summary,
            created_by=created_by,
            created_by_username=created_by_username,
            created=created,
            modified=modified,
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

        feature_rule.additional_properties = d
        return feature_rule

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
