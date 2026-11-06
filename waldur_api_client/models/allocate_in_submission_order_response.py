from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.allocation_plan_budget import AllocationPlanBudget
    from ..models.allocation_plan_row import AllocationPlanRow
    from ..models.round_step_proposal_result import RoundStepProposalResult


T = TypeVar("T", bound="AllocateInSubmissionOrderResponse")


@_attrs_define
class AllocateInSubmissionOrderResponse:
    """
    Attributes:
        preview (bool):
        has_budget (bool): False when no resource pool of the call covers this round.
        plan (list['AllocationPlanRow']):
        budgets (list['AllocationPlanBudget']):
        completed (list['RoundStepProposalResult']):
        skipped (list['RoundStepProposalResult']):
        failed (list['RoundStepProposalResult']):
    """

    preview: bool
    has_budget: bool
    plan: list["AllocationPlanRow"]
    budgets: list["AllocationPlanBudget"]
    completed: list["RoundStepProposalResult"]
    skipped: list["RoundStepProposalResult"]
    failed: list["RoundStepProposalResult"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preview = self.preview

        has_budget = self.has_budget

        plan = []
        for plan_item_data in self.plan:
            plan_item = plan_item_data.to_dict()
            plan.append(plan_item)

        budgets = []
        for budgets_item_data in self.budgets:
            budgets_item = budgets_item_data.to_dict()
            budgets.append(budgets_item)

        completed = []
        for completed_item_data in self.completed:
            completed_item = completed_item_data.to_dict()
            completed.append(completed_item)

        skipped = []
        for skipped_item_data in self.skipped:
            skipped_item = skipped_item_data.to_dict()
            skipped.append(skipped_item)

        failed = []
        for failed_item_data in self.failed:
            failed_item = failed_item_data.to_dict()
            failed.append(failed_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "preview": preview,
                "has_budget": has_budget,
                "plan": plan,
                "budgets": budgets,
                "completed": completed,
                "skipped": skipped,
                "failed": failed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allocation_plan_budget import AllocationPlanBudget
        from ..models.allocation_plan_row import AllocationPlanRow
        from ..models.round_step_proposal_result import RoundStepProposalResult

        d = dict(src_dict)
        preview = d.pop("preview")

        has_budget = d.pop("has_budget")

        plan = []
        _plan = d.pop("plan")
        for plan_item_data in _plan:
            plan_item = AllocationPlanRow.from_dict(plan_item_data)

            plan.append(plan_item)

        budgets = []
        _budgets = d.pop("budgets")
        for budgets_item_data in _budgets:
            budgets_item = AllocationPlanBudget.from_dict(budgets_item_data)

            budgets.append(budgets_item)

        completed = []
        _completed = d.pop("completed")
        for completed_item_data in _completed:
            completed_item = RoundStepProposalResult.from_dict(completed_item_data)

            completed.append(completed_item)

        skipped = []
        _skipped = d.pop("skipped")
        for skipped_item_data in _skipped:
            skipped_item = RoundStepProposalResult.from_dict(skipped_item_data)

            skipped.append(skipped_item)

        failed = []
        _failed = d.pop("failed")
        for failed_item_data in _failed:
            failed_item = RoundStepProposalResult.from_dict(failed_item_data)

            failed.append(failed_item)

        allocate_in_submission_order_response = cls(
            preview=preview,
            has_budget=has_budget,
            plan=plan,
            budgets=budgets,
            completed=completed,
            skipped=skipped,
            failed=failed,
        )

        allocate_in_submission_order_response.additional_properties = d
        return allocate_in_submission_order_response

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
