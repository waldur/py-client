from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.budget_enforcement_enum import BudgetEnforcementEnum

if TYPE_CHECKING:
    from ..models.proposal_budget_entry import ProposalBudgetEntry


T = TypeVar("T", bound="ProposalBudget")


@_attrs_define
class ProposalBudget:
    """
    Attributes:
        budget_enforcement (BudgetEnforcementEnum):
        entries (list['ProposalBudgetEntry']):
    """

    budget_enforcement: BudgetEnforcementEnum
    entries: list["ProposalBudgetEntry"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget_enforcement = self.budget_enforcement.value

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "budget_enforcement": budget_enforcement,
                "entries": entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_budget_entry import ProposalBudgetEntry

        d = dict(src_dict)
        budget_enforcement = BudgetEnforcementEnum(d.pop("budget_enforcement"))

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = ProposalBudgetEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        proposal_budget = cls(
            budget_enforcement=budget_enforcement,
            entries=entries,
        )

        proposal_budget.additional_properties = d
        return proposal_budget

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
