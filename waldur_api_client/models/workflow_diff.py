from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_changes import WorkflowChanges
    from ..models.workflow_diff_template import WorkflowDiffTemplate


T = TypeVar("T", bound="WorkflowDiff")


@_attrs_define
class WorkflowDiff:
    """
    Attributes:
        from_version (str):
        to_version (str):
        template (Union['WorkflowDiffTemplate', None]):
        changes (WorkflowChanges):
    """

    from_version: str
    to_version: str
    template: Union["WorkflowDiffTemplate", None]
    changes: "WorkflowChanges"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_diff_template import WorkflowDiffTemplate

        from_version = self.from_version

        to_version = self.to_version

        template: Union[None, dict[str, Any]]
        if isinstance(self.template, WorkflowDiffTemplate):
            template = self.template.to_dict()
        else:
            template = self.template

        changes = self.changes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_version": from_version,
                "to_version": to_version,
                "template": template,
                "changes": changes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_changes import WorkflowChanges
        from ..models.workflow_diff_template import WorkflowDiffTemplate

        d = dict(src_dict)
        from_version = d.pop("from_version")

        to_version = d.pop("to_version")

        def _parse_template(data: object) -> Union["WorkflowDiffTemplate", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                template_type_1 = WorkflowDiffTemplate.from_dict(data)

                return template_type_1
            except:  # noqa: E722
                pass
            return cast(Union["WorkflowDiffTemplate", None], data)

        template = _parse_template(d.pop("template"))

        changes = WorkflowChanges.from_dict(d.pop("changes"))

        workflow_diff = cls(
            from_version=from_version,
            to_version=to_version,
            template=template,
            changes=changes,
        )

        workflow_diff.additional_properties = d
        return workflow_diff

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
