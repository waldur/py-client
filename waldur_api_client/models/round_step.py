import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.round_step_discussion import RoundStepDiscussion


T = TypeVar("T", bound="RoundStep")


@_attrs_define
class RoundStep:
    """
    Attributes:
        round_step_uuid (Union[None, UUID]): The step's record in the round, once it has a due date or was opened there;
            null before.
        has_discussion (bool):
        discussions (list['RoundStepDiscussion']): For a round step with a discussion, its discussion per panel (one on
            a call without panels) that the viewer takes part in or oversees; empty otherwise.
        step_uuid (UUID):
        step_key (str):
        step_name (str):
        step_kind (str):
        order (int):
        round_scoped (bool):
        has_reports (bool):
        due_at (Union[None, datetime.datetime]):
        opened_at (Union[None, datetime.datetime]):
        proposals_at_step (int): Proposals of the round standing at the step now.
        proposals_before_step (int): Proposals of the round still to reach the step.
        proposals_awaiting_advance (int): Proposals parked on the step once completed, waiting to be moved on.
        reports_total (int):
        reports_submitted (int):
    """

    round_step_uuid: Union[None, UUID]
    has_discussion: bool
    discussions: list["RoundStepDiscussion"]
    step_uuid: UUID
    step_key: str
    step_name: str
    step_kind: str
    order: int
    round_scoped: bool
    has_reports: bool
    due_at: Union[None, datetime.datetime]
    opened_at: Union[None, datetime.datetime]
    proposals_at_step: int
    proposals_before_step: int
    proposals_awaiting_advance: int
    reports_total: int
    reports_submitted: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        round_step_uuid: Union[None, str]
        if isinstance(self.round_step_uuid, UUID):
            round_step_uuid = str(self.round_step_uuid)
        else:
            round_step_uuid = self.round_step_uuid

        has_discussion = self.has_discussion

        discussions = []
        for discussions_item_data in self.discussions:
            discussions_item = discussions_item_data.to_dict()
            discussions.append(discussions_item)

        step_uuid = str(self.step_uuid)

        step_key = self.step_key

        step_name = self.step_name

        step_kind = self.step_kind

        order = self.order

        round_scoped = self.round_scoped

        has_reports = self.has_reports

        due_at: Union[None, str]
        if isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        opened_at: Union[None, str]
        if isinstance(self.opened_at, datetime.datetime):
            opened_at = self.opened_at.isoformat()
        else:
            opened_at = self.opened_at

        proposals_at_step = self.proposals_at_step

        proposals_before_step = self.proposals_before_step

        proposals_awaiting_advance = self.proposals_awaiting_advance

        reports_total = self.reports_total

        reports_submitted = self.reports_submitted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "round_step_uuid": round_step_uuid,
                "has_discussion": has_discussion,
                "discussions": discussions,
                "step_uuid": step_uuid,
                "step_key": step_key,
                "step_name": step_name,
                "step_kind": step_kind,
                "order": order,
                "round_scoped": round_scoped,
                "has_reports": has_reports,
                "due_at": due_at,
                "opened_at": opened_at,
                "proposals_at_step": proposals_at_step,
                "proposals_before_step": proposals_before_step,
                "proposals_awaiting_advance": proposals_awaiting_advance,
                "reports_total": reports_total,
                "reports_submitted": reports_submitted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.round_step_discussion import RoundStepDiscussion

        d = dict(src_dict)

        def _parse_round_step_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_step_uuid_type_0 = UUID(data)

                return round_step_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        round_step_uuid = _parse_round_step_uuid(d.pop("round_step_uuid"))

        has_discussion = d.pop("has_discussion")

        discussions = []
        _discussions = d.pop("discussions")
        for discussions_item_data in _discussions:
            discussions_item = RoundStepDiscussion.from_dict(discussions_item_data)

            discussions.append(discussions_item)

        step_uuid = UUID(d.pop("step_uuid"))

        step_key = d.pop("step_key")

        step_name = d.pop("step_name")

        step_kind = d.pop("step_kind")

        order = d.pop("order")

        round_scoped = d.pop("round_scoped")

        has_reports = d.pop("has_reports")

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

        def _parse_opened_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opened_at_type_0 = isoparse(data)

                return opened_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        opened_at = _parse_opened_at(d.pop("opened_at"))

        proposals_at_step = d.pop("proposals_at_step")

        proposals_before_step = d.pop("proposals_before_step")

        proposals_awaiting_advance = d.pop("proposals_awaiting_advance")

        reports_total = d.pop("reports_total")

        reports_submitted = d.pop("reports_submitted")

        round_step = cls(
            round_step_uuid=round_step_uuid,
            has_discussion=has_discussion,
            discussions=discussions,
            step_uuid=step_uuid,
            step_key=step_key,
            step_name=step_name,
            step_kind=step_kind,
            order=order,
            round_scoped=round_scoped,
            has_reports=has_reports,
            due_at=due_at,
            opened_at=opened_at,
            proposals_at_step=proposals_at_step,
            proposals_before_step=proposals_before_step,
            proposals_awaiting_advance=proposals_awaiting_advance,
            reports_total=reports_total,
            reports_submitted=reports_submitted,
        )

        round_step.additional_properties = d
        return round_step

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
