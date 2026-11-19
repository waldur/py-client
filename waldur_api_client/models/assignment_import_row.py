from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assignment_import_row_status_enum import AssignmentImportRowStatusEnum

T = TypeVar("T", bound="AssignmentImportRow")


@_attrs_define
class AssignmentImportRow:
    """
    Attributes:
        row (int): Line of the file, the header is 1
        proposal_uuid (Union[None, UUID]): The proposal the row names, when found
        proposal_slug (str):
        proposal_name (str):
        reviewer_email (str):
        status (AssignmentImportRowStatusEnum):
        reason (str):
    """

    row: int
    proposal_uuid: Union[None, UUID]
    proposal_slug: str
    proposal_name: str
    reviewer_email: str
    status: AssignmentImportRowStatusEnum
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        row = self.row

        proposal_uuid: Union[None, str]
        if isinstance(self.proposal_uuid, UUID):
            proposal_uuid = str(self.proposal_uuid)
        else:
            proposal_uuid = self.proposal_uuid

        proposal_slug = self.proposal_slug

        proposal_name = self.proposal_name

        reviewer_email = self.reviewer_email

        status = self.status.value

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "row": row,
                "proposal_uuid": proposal_uuid,
                "proposal_slug": proposal_slug,
                "proposal_name": proposal_name,
                "reviewer_email": reviewer_email,
                "status": status,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        row = d.pop("row")

        def _parse_proposal_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proposal_uuid_type_0 = UUID(data)

                return proposal_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        proposal_uuid = _parse_proposal_uuid(d.pop("proposal_uuid"))

        proposal_slug = d.pop("proposal_slug")

        proposal_name = d.pop("proposal_name")

        reviewer_email = d.pop("reviewer_email")

        status = AssignmentImportRowStatusEnum(d.pop("status"))

        reason = d.pop("reason")

        assignment_import_row = cls(
            row=row,
            proposal_uuid=proposal_uuid,
            proposal_slug=proposal_slug,
            proposal_name=proposal_name,
            reviewer_email=reviewer_email,
            status=status,
            reason=reason,
        )

        assignment_import_row.additional_properties = d
        return assignment_import_row

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
