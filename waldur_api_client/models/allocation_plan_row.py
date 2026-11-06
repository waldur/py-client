import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.planned_outcome_enum import PlannedOutcomeEnum

if TYPE_CHECKING:
    from ..models.allocation_plan_award import AllocationPlanAward


T = TypeVar("T", bound="AllocationPlanRow")


@_attrs_define
class AllocationPlanRow:
    """
    Attributes:
        order (int):
        proposal_uuid (UUID):
        proposal_name (str):
        proposal_slug (str):
        submitted_at (Union[None, datetime.datetime]):
        score (Union[None, float]):
        threshold (Union[None, float]):
        award (list['AllocationPlanAward']):
        planned_outcome (PlannedOutcomeEnum):
        reason (str):
    """

    order: int
    proposal_uuid: UUID
    proposal_name: str
    proposal_slug: str
    submitted_at: Union[None, datetime.datetime]
    score: Union[None, float]
    threshold: Union[None, float]
    award: list["AllocationPlanAward"]
    planned_outcome: PlannedOutcomeEnum
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order = self.order

        proposal_uuid = str(self.proposal_uuid)

        proposal_name = self.proposal_name

        proposal_slug = self.proposal_slug

        submitted_at: Union[None, str]
        if isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        score: Union[None, float]
        score = self.score

        threshold: Union[None, float]
        threshold = self.threshold

        award = []
        for award_item_data in self.award:
            award_item = award_item_data.to_dict()
            award.append(award_item)

        planned_outcome = self.planned_outcome.value

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order": order,
                "proposal_uuid": proposal_uuid,
                "proposal_name": proposal_name,
                "proposal_slug": proposal_slug,
                "submitted_at": submitted_at,
                "score": score,
                "threshold": threshold,
                "award": award,
                "planned_outcome": planned_outcome,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allocation_plan_award import AllocationPlanAward

        d = dict(src_dict)
        order = d.pop("order")

        proposal_uuid = UUID(d.pop("proposal_uuid"))

        proposal_name = d.pop("proposal_name")

        proposal_slug = d.pop("proposal_slug")

        def _parse_submitted_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = isoparse(data)

                return submitted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at"))

        def _parse_score(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        score = _parse_score(d.pop("score"))

        def _parse_threshold(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        threshold = _parse_threshold(d.pop("threshold"))

        award = []
        _award = d.pop("award")
        for award_item_data in _award:
            award_item = AllocationPlanAward.from_dict(award_item_data)

            award.append(award_item)

        planned_outcome = PlannedOutcomeEnum(d.pop("planned_outcome"))

        reason = d.pop("reason")

        allocation_plan_row = cls(
            order=order,
            proposal_uuid=proposal_uuid,
            proposal_name=proposal_name,
            proposal_slug=proposal_slug,
            submitted_at=submitted_at,
            score=score,
            threshold=threshold,
            award=award,
            planned_outcome=planned_outcome,
            reason=reason,
        )

        allocation_plan_row.additional_properties = d
        return allocation_plan_row

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
