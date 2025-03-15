from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.jira_issue_fields import JiraIssueFields


T = TypeVar("T", bound="JiraIssue")


@_attrs_define
class JiraIssue:
    """
    Attributes:
        key (str):
        fields (JiraIssueFields):
    """

    key: str
    fields: "JiraIssueFields"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        fields = self.fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "fields": fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jira_issue_fields import JiraIssueFields

        d = dict(src_dict)
        key = d.pop("key")

        fields = JiraIssueFields.from_dict(d.pop("fields"))

        jira_issue = cls(
            key=key,
            fields=fields,
        )

        jira_issue.additional_properties = d
        return jira_issue

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
