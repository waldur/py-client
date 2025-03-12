from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.issue_type_enum import IssueTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueRequest")


@_attrs_define
class IssueRequest:
    """
    Attributes:
        summary (str):
        type_ (Union[Unset, IssueTypeEnum]):  Default: IssueTypeEnum.INFORMATIONAL.
        remote_id (Union[None, Unset, str]):
        description (Union[Unset, str]):
        priority (Union[Unset, str]):
        caller (Union[None, Unset, str]):
        assignee (Union[None, Unset, str]):
        customer (Union[None, Unset, str]):
        project (Union[None, Unset, str]):
        resource (Union[Unset, str]):
        is_reported_manually (Union[Unset, bool]): Set true if issue is created by regular user via portal. Default:
            False.
        template (Union[None, Unset, str]):
    """

    summary: str
    type_: Union[Unset, IssueTypeEnum] = IssueTypeEnum.INFORMATIONAL
    remote_id: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    priority: Union[Unset, str] = UNSET
    caller: Union[None, Unset, str] = UNSET
    assignee: Union[None, Unset, str] = UNSET
    customer: Union[None, Unset, str] = UNSET
    project: Union[None, Unset, str] = UNSET
    resource: Union[Unset, str] = UNSET
    is_reported_manually: Union[Unset, bool] = False
    template: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        remote_id: Union[None, Unset, str]
        if isinstance(self.remote_id, Unset):
            remote_id = UNSET
        else:
            remote_id = self.remote_id

        description = self.description

        priority = self.priority

        caller: Union[None, Unset, str]
        if isinstance(self.caller, Unset):
            caller = UNSET
        else:
            caller = self.caller

        assignee: Union[None, Unset, str]
        if isinstance(self.assignee, Unset):
            assignee = UNSET
        else:
            assignee = self.assignee

        customer: Union[None, Unset, str]
        if isinstance(self.customer, Unset):
            customer = UNSET
        else:
            customer = self.customer

        project: Union[None, Unset, str]
        if isinstance(self.project, Unset):
            project = UNSET
        else:
            project = self.project

        resource = self.resource

        is_reported_manually = self.is_reported_manually

        template: Union[None, Unset, str]
        if isinstance(self.template, Unset):
            template = UNSET
        else:
            template = self.template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if remote_id is not UNSET:
            field_dict["remote_id"] = remote_id
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if caller is not UNSET:
            field_dict["caller"] = caller
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if customer is not UNSET:
            field_dict["customer"] = customer
        if project is not UNSET:
            field_dict["project"] = project
        if resource is not UNSET:
            field_dict["resource"] = resource
        if is_reported_manually is not UNSET:
            field_dict["is_reported_manually"] = is_reported_manually
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        summary = (None, str(self.summary).encode(), "text/plain")

        type_: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = (None, str(self.type_.value).encode(), "text/plain")

        remote_id: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.remote_id, Unset):
            remote_id = UNSET
        elif isinstance(self.remote_id, str):
            remote_id = (None, str(self.remote_id).encode(), "text/plain")
        else:
            remote_id = (None, str(self.remote_id).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        priority = (
            self.priority if isinstance(self.priority, Unset) else (None, str(self.priority).encode(), "text/plain")
        )

        caller: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.caller, Unset):
            caller = UNSET
        elif isinstance(self.caller, str):
            caller = (None, str(self.caller).encode(), "text/plain")
        else:
            caller = (None, str(self.caller).encode(), "text/plain")

        assignee: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.assignee, Unset):
            assignee = UNSET
        elif isinstance(self.assignee, str):
            assignee = (None, str(self.assignee).encode(), "text/plain")
        else:
            assignee = (None, str(self.assignee).encode(), "text/plain")

        customer: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.customer, Unset):
            customer = UNSET
        elif isinstance(self.customer, str):
            customer = (None, str(self.customer).encode(), "text/plain")
        else:
            customer = (None, str(self.customer).encode(), "text/plain")

        project: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.project, Unset):
            project = UNSET
        elif isinstance(self.project, str):
            project = (None, str(self.project).encode(), "text/plain")
        else:
            project = (None, str(self.project).encode(), "text/plain")

        resource = (
            self.resource if isinstance(self.resource, Unset) else (None, str(self.resource).encode(), "text/plain")
        )

        is_reported_manually = (
            self.is_reported_manually
            if isinstance(self.is_reported_manually, Unset)
            else (None, str(self.is_reported_manually).encode(), "text/plain")
        )

        template: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.template, Unset):
            template = UNSET
        elif isinstance(self.template, str):
            template = (None, str(self.template).encode(), "text/plain")
        else:
            template = (None, str(self.template).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "summary": summary,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if remote_id is not UNSET:
            field_dict["remote_id"] = remote_id
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if caller is not UNSET:
            field_dict["caller"] = caller
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if customer is not UNSET:
            field_dict["customer"] = customer
        if project is not UNSET:
            field_dict["project"] = project
        if resource is not UNSET:
            field_dict["resource"] = resource
        if is_reported_manually is not UNSET:
            field_dict["is_reported_manually"] = is_reported_manually
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        summary = d.pop("summary")

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, IssueTypeEnum]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = IssueTypeEnum(_type_)

        def _parse_remote_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remote_id = _parse_remote_id(d.pop("remote_id", UNSET))

        description = d.pop("description", UNSET)

        priority = d.pop("priority", UNSET)

        def _parse_caller(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        caller = _parse_caller(d.pop("caller", UNSET))

        def _parse_assignee(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assignee = _parse_assignee(d.pop("assignee", UNSET))

        def _parse_customer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        customer = _parse_customer(d.pop("customer", UNSET))

        def _parse_project(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        project = _parse_project(d.pop("project", UNSET))

        resource = d.pop("resource", UNSET)

        is_reported_manually = d.pop("is_reported_manually", UNSET)

        def _parse_template(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        template = _parse_template(d.pop("template", UNSET))

        issue_request = cls(
            summary=summary,
            type_=type_,
            remote_id=remote_id,
            description=description,
            priority=priority,
            caller=caller,
            assignee=assignee,
            customer=customer,
            project=project,
            resource=resource,
            is_reported_manually=is_reported_manually,
            template=template,
        )

        issue_request.additional_properties = d
        return issue_request

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
