import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.workflow_version_reason import WorkflowVersionReason

if TYPE_CHECKING:
    from ..models.workflow_version_detail_document import WorkflowVersionDetailDocument
    from ..models.workflow_version_summary import WorkflowVersionSummary


T = TypeVar("T", bound="WorkflowVersionDetail")


@_attrs_define
class WorkflowVersionDetail:
    """
    Attributes:
        number (int):
        created (datetime.datetime):
        modified (datetime.datetime):
        created_by_name (Union[None, str]):
        reason (WorkflowVersionReason):
        summary (WorkflowVersionSummary):
        document_hash (str):
        document (WorkflowVersionDetailDocument): The settings and workflow, in the call-transfer format.
    """

    number: int
    created: datetime.datetime
    modified: datetime.datetime
    created_by_name: Union[None, str]
    reason: WorkflowVersionReason
    summary: "WorkflowVersionSummary"
    document_hash: str
    document: "WorkflowVersionDetailDocument"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        created_by_name: Union[None, str]
        created_by_name = self.created_by_name

        reason = self.reason.value

        summary = self.summary.to_dict()

        document_hash = self.document_hash

        document = self.document.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "created": created,
                "modified": modified,
                "created_by_name": created_by_name,
                "reason": reason,
                "summary": summary,
                "document_hash": document_hash,
                "document": document,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_version_detail_document import WorkflowVersionDetailDocument
        from ..models.workflow_version_summary import WorkflowVersionSummary

        d = dict(src_dict)
        number = d.pop("number")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        def _parse_created_by_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by_name = _parse_created_by_name(d.pop("created_by_name"))

        reason = WorkflowVersionReason(d.pop("reason"))

        summary = WorkflowVersionSummary.from_dict(d.pop("summary"))

        document_hash = d.pop("document_hash")

        document = WorkflowVersionDetailDocument.from_dict(d.pop("document"))

        workflow_version_detail = cls(
            number=number,
            created=created,
            modified=modified,
            created_by_name=created_by_name,
            reason=reason,
            summary=summary,
            document_hash=document_hash,
            document=document,
        )

        workflow_version_detail.additional_properties = d
        return workflow_version_detail

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
