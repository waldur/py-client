from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rule_request_plan_attributes import RuleRequestPlanAttributes
    from ..models.rule_request_plan_limits import RuleRequestPlanLimits


T = TypeVar("T", bound="RuleRequest")


@_attrs_define
class RuleRequest:
    """
    Attributes:
        name (str):
        customer (str):
        user_affiliations (Union[Unset, list[str]]):
        user_email_patterns (Union[Unset, list[str]]):
        project_role (Union[None, Unset, str]):
        project_role_name (Union[None, Unset, str]):
        plan (Union[None, Unset, str]):
        plan_attributes (Union[Unset, RuleRequestPlanAttributes]):
        plan_limits (Union[Unset, RuleRequestPlanLimits]):
    """

    name: str
    customer: str
    user_affiliations: Union[Unset, list[str]] = UNSET
    user_email_patterns: Union[Unset, list[str]] = UNSET
    project_role: Union[None, Unset, str] = UNSET
    project_role_name: Union[None, Unset, str] = UNSET
    plan: Union[None, Unset, str] = UNSET
    plan_attributes: Union[Unset, "RuleRequestPlanAttributes"] = UNSET
    plan_limits: Union[Unset, "RuleRequestPlanLimits"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        customer = self.customer

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

        project_role_name: Union[None, Unset, str]
        if isinstance(self.project_role_name, Unset):
            project_role_name = UNSET
        else:
            project_role_name = self.project_role_name

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
                "customer": customer,
            }
        )
        if user_affiliations is not UNSET:
            field_dict["user_affiliations"] = user_affiliations
        if user_email_patterns is not UNSET:
            field_dict["user_email_patterns"] = user_email_patterns
        if project_role is not UNSET:
            field_dict["project_role"] = project_role
        if project_role_name is not UNSET:
            field_dict["project_role_name"] = project_role_name
        if plan is not UNSET:
            field_dict["plan"] = plan
        if plan_attributes is not UNSET:
            field_dict["plan_attributes"] = plan_attributes
        if plan_limits is not UNSET:
            field_dict["plan_limits"] = plan_limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rule_request_plan_attributes import RuleRequestPlanAttributes
        from ..models.rule_request_plan_limits import RuleRequestPlanLimits

        d = dict(src_dict)
        name = d.pop("name")

        customer = d.pop("customer")

        user_affiliations = cast(list[str], d.pop("user_affiliations", UNSET))

        user_email_patterns = cast(list[str], d.pop("user_email_patterns", UNSET))

        def _parse_project_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        project_role = _parse_project_role(d.pop("project_role", UNSET))

        def _parse_project_role_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        project_role_name = _parse_project_role_name(d.pop("project_role_name", UNSET))

        def _parse_plan(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        plan = _parse_plan(d.pop("plan", UNSET))

        _plan_attributes = d.pop("plan_attributes", UNSET)
        plan_attributes: Union[Unset, RuleRequestPlanAttributes]
        if isinstance(_plan_attributes, Unset):
            plan_attributes = UNSET
        else:
            plan_attributes = RuleRequestPlanAttributes.from_dict(_plan_attributes)

        _plan_limits = d.pop("plan_limits", UNSET)
        plan_limits: Union[Unset, RuleRequestPlanLimits]
        if isinstance(_plan_limits, Unset):
            plan_limits = UNSET
        else:
            plan_limits = RuleRequestPlanLimits.from_dict(_plan_limits)

        rule_request = cls(
            name=name,
            customer=customer,
            user_affiliations=user_affiliations,
            user_email_patterns=user_email_patterns,
            project_role=project_role,
            project_role_name=project_role_name,
            plan=plan,
            plan_attributes=plan_attributes,
            plan_limits=plan_limits,
        )

        rule_request.additional_properties = d
        return rule_request

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
