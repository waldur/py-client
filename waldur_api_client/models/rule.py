from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rule_plan_attributes import RulePlanAttributes
    from ..models.rule_plan_limits import RulePlanLimits


T = TypeVar("T", bound="Rule")


@_attrs_define
class Rule:
    """
    Attributes:
        name (str):
        uuid (UUID):
        url (str):
        customer (str):
        customer_name (str):
        customer_uuid (str):
        project_role_dispay_name (str):
        project_role_description (str):
        user_affiliations (Union[Unset, list[str]]):
        user_email_patterns (Union[Unset, list[str]]):
        project_role (Union[None, Unset, str]):
        plan (Union[None, Unset, str]):
        plan_attributes (Union[Unset, RulePlanAttributes]):
        plan_limits (Union[Unset, RulePlanLimits]):
    """

    name: str
    uuid: UUID
    url: str
    customer: str
    customer_name: str
    customer_uuid: str
    project_role_dispay_name: str
    project_role_description: str
    user_affiliations: Union[Unset, list[str]] = UNSET
    user_email_patterns: Union[Unset, list[str]] = UNSET
    project_role: Union[None, Unset, str] = UNSET
    plan: Union[None, Unset, str] = UNSET
    plan_attributes: Union[Unset, "RulePlanAttributes"] = UNSET
    plan_limits: Union[Unset, "RulePlanLimits"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        uuid = str(self.uuid)

        url = self.url

        customer = self.customer

        customer_name = self.customer_name

        customer_uuid = self.customer_uuid

        project_role_dispay_name = self.project_role_dispay_name

        project_role_description = self.project_role_description

        user_affiliations: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_affiliations, Unset):
            user_affiliations = self.user_affiliations

        user_email_patterns: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_email_patterns, Unset):
            user_email_patterns = self.user_email_patterns

        project_role: Union[None, Unset, str]
        if isinstance(self.project_role, Unset):
            project_role = UNSET
        else:
            project_role = self.project_role

        plan: Union[None, Unset, str]
        if isinstance(self.plan, Unset):
            plan = UNSET
        else:
            plan = self.plan

        plan_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.plan_attributes, Unset):
            plan_attributes = self.plan_attributes.to_dict()

        plan_limits: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.plan_limits, Unset):
            plan_limits = self.plan_limits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uuid": uuid,
                "url": url,
                "customer": customer,
                "customer_name": customer_name,
                "customer_uuid": customer_uuid,
                "project_role_dispay_name": project_role_dispay_name,
                "project_role_description": project_role_description,
            }
        )
        if user_affiliations is not UNSET:
            field_dict["user_affiliations"] = user_affiliations
        if user_email_patterns is not UNSET:
            field_dict["user_email_patterns"] = user_email_patterns
        if project_role is not UNSET:
            field_dict["project_role"] = project_role
        if plan is not UNSET:
            field_dict["plan"] = plan
        if plan_attributes is not UNSET:
            field_dict["plan_attributes"] = plan_attributes
        if plan_limits is not UNSET:
            field_dict["plan_limits"] = plan_limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rule_plan_attributes import RulePlanAttributes
        from ..models.rule_plan_limits import RulePlanLimits

        d = dict(src_dict)
        name = d.pop("name")

        uuid = UUID(d.pop("uuid"))

        url = d.pop("url")

        customer = d.pop("customer")

        customer_name = d.pop("customer_name")

        customer_uuid = d.pop("customer_uuid")

        project_role_dispay_name = d.pop("project_role_dispay_name")

        project_role_description = d.pop("project_role_description")

        user_affiliations = cast(list[str], d.pop("user_affiliations", UNSET))

        user_email_patterns = cast(list[str], d.pop("user_email_patterns", UNSET))

        def _parse_project_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        project_role = _parse_project_role(d.pop("project_role", UNSET))

        def _parse_plan(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        plan = _parse_plan(d.pop("plan", UNSET))

        _plan_attributes = d.pop("plan_attributes", UNSET)
        plan_attributes: Union[Unset, RulePlanAttributes]
        if isinstance(_plan_attributes, Unset):
            plan_attributes = UNSET
        else:
            plan_attributes = RulePlanAttributes.from_dict(_plan_attributes)

        _plan_limits = d.pop("plan_limits", UNSET)
        plan_limits: Union[Unset, RulePlanLimits]
        if isinstance(_plan_limits, Unset):
            plan_limits = UNSET
        else:
            plan_limits = RulePlanLimits.from_dict(_plan_limits)

        rule = cls(
            name=name,
            uuid=uuid,
            url=url,
            customer=customer,
            customer_name=customer_name,
            customer_uuid=customer_uuid,
            project_role_dispay_name=project_role_dispay_name,
            project_role_description=project_role_description,
            user_affiliations=user_affiliations,
            user_email_patterns=user_email_patterns,
            project_role=project_role,
            plan=plan,
            plan_attributes=plan_attributes,
            plan_limits=plan_limits,
        )

        rule.additional_properties = d
        return rule

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
