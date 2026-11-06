import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestChangesRequest")


@_attrs_define
class RequestChangesRequest:
    """
    Attributes:
        step_uuid (UUID): UUID of the active workflow step instance the changes are asked at.
        message (str): What the applicant is to change. The applicant reads it.
        parts (list[str]): The parts the applicant may edit until the changes are submitted: field:<name> for a Project
            details field, documents, resources, team or compliance; at a step of an extension request or final report,
            run_form (its applicant step's answers) and, for an extension, run_request (the end date and limits asked for).
            unlockable_parts on the proposal lists them.
        due_at (Union[None, Unset, datetime.datetime]): When the changes are due. Past it, the request lapses and the
            step returns to its actor; nothing is decided for them.
    """

    step_uuid: UUID
    message: str
    parts: list[str]
    due_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step_uuid = str(self.step_uuid)

        message = self.message

        parts = self.parts

        due_at: Union[None, Unset, str]
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step_uuid": step_uuid,
                "message": message,
                "parts": parts,
            }
        )
        if due_at is not UNSET:
            field_dict["due_at"] = due_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        step_uuid = UUID(d.pop("step_uuid"))

        message = d.pop("message")

        parts = cast(list[str], d.pop("parts"))

        def _parse_due_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = isoparse(data)

                return due_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        due_at = _parse_due_at(d.pop("due_at", UNSET))

        request_changes_request = cls(
            step_uuid=step_uuid,
            message=message,
            parts=parts,
            due_at=due_at,
        )

        request_changes_request.additional_properties = d
        return request_changes_request

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
