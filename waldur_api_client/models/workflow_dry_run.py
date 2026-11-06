from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dry_run_coverage import DryRunCoverage
    from ..models.dry_run_log_entry import DryRunLogEntry
    from ..models.dry_run_message import DryRunMessage
    from ..models.dry_run_next import DryRunNext
    from ..models.dry_run_requested_offering import DryRunRequestedOffering
    from ..models.dry_run_step_state import DryRunStepState
    from ..models.dry_run_view_as_result import DryRunViewAsResult
    from ..models.workflow_dry_run_scenario_draft import WorkflowDryRunScenarioDraft


T = TypeVar("T", bound="WorkflowDryRun")


@_attrs_define
class WorkflowDryRun:
    """
    Attributes:
        proposal_state (str):
        decision_held (bool):
        day (int):
        requested_offerings (list['DryRunRequestedOffering']):
        steps (list['DryRunStepState']):
        next_ (DryRunNext):
        log (list['DryRunLogEntry']):
        messages (list['DryRunMessage']):
        coverage (DryRunCoverage):
        view_as (Union['DryRunViewAsResult', None]):
        scenario_draft (Union[Unset, WorkflowDryRunScenarioDraft]): The path as a scenario: its request and assertions
            on where it ended, to name and save on the call's template.
    """

    proposal_state: str
    decision_held: bool
    day: int
    requested_offerings: list["DryRunRequestedOffering"]
    steps: list["DryRunStepState"]
    next_: "DryRunNext"
    log: list["DryRunLogEntry"]
    messages: list["DryRunMessage"]
    coverage: "DryRunCoverage"
    view_as: Union["DryRunViewAsResult", None]
    scenario_draft: Union[Unset, "WorkflowDryRunScenarioDraft"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dry_run_view_as_result import DryRunViewAsResult

        proposal_state = self.proposal_state

        decision_held = self.decision_held

        day = self.day

        requested_offerings = []
        for requested_offerings_item_data in self.requested_offerings:
            requested_offerings_item = requested_offerings_item_data.to_dict()
            requested_offerings.append(requested_offerings_item)

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        next_ = self.next_.to_dict()

        log = []
        for log_item_data in self.log:
            log_item = log_item_data.to_dict()
            log.append(log_item)

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        coverage = self.coverage.to_dict()

        view_as: Union[None, dict[str, Any]]
        if isinstance(self.view_as, DryRunViewAsResult):
            view_as = self.view_as.to_dict()
        else:
            view_as = self.view_as

        scenario_draft: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.scenario_draft, Unset):
            scenario_draft = self.scenario_draft.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposal_state": proposal_state,
                "decision_held": decision_held,
                "day": day,
                "requested_offerings": requested_offerings,
                "steps": steps,
                "next": next_,
                "log": log,
                "messages": messages,
                "coverage": coverage,
                "view_as": view_as,
            }
        )
        if scenario_draft is not UNSET:
            field_dict["scenario_draft"] = scenario_draft

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dry_run_coverage import DryRunCoverage
        from ..models.dry_run_log_entry import DryRunLogEntry
        from ..models.dry_run_message import DryRunMessage
        from ..models.dry_run_next import DryRunNext
        from ..models.dry_run_requested_offering import DryRunRequestedOffering
        from ..models.dry_run_step_state import DryRunStepState
        from ..models.dry_run_view_as_result import DryRunViewAsResult
        from ..models.workflow_dry_run_scenario_draft import WorkflowDryRunScenarioDraft

        d = dict(src_dict)
        proposal_state = d.pop("proposal_state")

        decision_held = d.pop("decision_held")

        day = d.pop("day")

        requested_offerings = []
        _requested_offerings = d.pop("requested_offerings")
        for requested_offerings_item_data in _requested_offerings:
            requested_offerings_item = DryRunRequestedOffering.from_dict(requested_offerings_item_data)

            requested_offerings.append(requested_offerings_item)

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = DryRunStepState.from_dict(steps_item_data)

            steps.append(steps_item)

        next_ = DryRunNext.from_dict(d.pop("next"))

        log = []
        _log = d.pop("log")
        for log_item_data in _log:
            log_item = DryRunLogEntry.from_dict(log_item_data)

            log.append(log_item)

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = DryRunMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        coverage = DryRunCoverage.from_dict(d.pop("coverage"))

        def _parse_view_as(data: object) -> Union["DryRunViewAsResult", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                view_as_type_1 = DryRunViewAsResult.from_dict(data)

                return view_as_type_1
            except:  # noqa: E722
                pass
            return cast(Union["DryRunViewAsResult", None], data)

        view_as = _parse_view_as(d.pop("view_as"))

        _scenario_draft = d.pop("scenario_draft", UNSET)
        scenario_draft: Union[Unset, WorkflowDryRunScenarioDraft]
        if isinstance(_scenario_draft, Unset):
            scenario_draft = UNSET
        else:
            scenario_draft = WorkflowDryRunScenarioDraft.from_dict(_scenario_draft)

        workflow_dry_run = cls(
            proposal_state=proposal_state,
            decision_held=decision_held,
            day=day,
            requested_offerings=requested_offerings,
            steps=steps,
            next_=next_,
            log=log,
            messages=messages,
            coverage=coverage,
            view_as=view_as,
            scenario_draft=scenario_draft,
        )

        workflow_dry_run.additional_properties = d
        return workflow_dry_run

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
