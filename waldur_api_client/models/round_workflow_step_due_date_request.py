import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoundWorkflowStepDueDateRequest")


@_attrs_define
class RoundWorkflowStepDueDateRequest:
    """
    Attributes:
        due_at (Union[None, datetime.datetime]): When the step is due for every proposal of the round; null to count the
            step's duration again.
        step_uuid (Union[Unset, UUID]): UUID of the step. Either this or step.
        step (Union[Unset, str]): Key of the step. Either this or step_uuid.
    """

    due_at: Union[None, datetime.datetime]
    step_uuid: Union[Unset, UUID] = UNSET
    step: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        due_at: Union[None, str]
        if isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        step_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.step_uuid, Unset):
            step_uuid = str(self.step_uuid)

        step = self.step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "due_at": due_at,
            }
        )
        if step_uuid is not UNSET:
            field_dict["step_uuid"] = step_uuid
        if step is not UNSET:
            field_dict["step"] = step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_due_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = isoparse(data)

                return due_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        due_at = _parse_due_at(d.pop("due_at"))

        _step_uuid = d.pop("step_uuid", UNSET)
        step_uuid: Union[Unset, UUID]
        if isinstance(_step_uuid, Unset):
            step_uuid = UNSET
        else:
            step_uuid = UUID(_step_uuid)

        step = d.pop("step", UNSET)

        round_workflow_step_due_date_request = cls(
            due_at=due_at,
            step_uuid=step_uuid,
            step=step,
        )

        round_workflow_step_due_date_request.additional_properties = d
        return round_workflow_step_due_date_request

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
