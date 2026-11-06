from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dry_run_contribution_request import DryRunContributionRequest
    from ..models.dry_run_slot_request import DryRunSlotRequest


T = TypeVar("T", bound="DryRunActionRequest")


@_attrs_define
class DryRunActionRequest:
    """
    Attributes:
        step (Union[Unset, str]):
        outcome (Union[Unset, str]):
        reason (Union[Unset, str]):
        message (Union[Unset, str]):
        contributions (Union[Unset, list['DryRunContributionRequest']]):
        parts (Union[Unset, list[str]]):
        reject (Union[Unset, bool]):
        expire (Union[Unset, bool]):
        request_changes (Union[Unset, bool]):
        submit_changes (Union[Unset, bool]):
        cancel_changes (Union[Unset, bool]):
        advance (Union[Unset, bool]):
        publish (Union[Unset, bool]):
        release (Union[Unset, bool]):
        round_step (Union[Unset, bool]): Open the step run once per round for the round, have its round reports written
            and complete it: with ``outcome`` for a decision.
        extend (Union[Unset, bool]): The applicant team asks to extend the accepted proposal.
        final_report (Union[Unset, bool]): Open the accepted proposal's final report.
        exhaust_budget (Union[Unset, bool]): Take the budgets the proposal draws on as spent, so its award no longer
            fits.
        override_budget (Union[Unset, str]): With an outcome: approve past the budget, for this reason.
        scores (Union[Unset, list[int]]): With an outcome on a step its assigned reviewers review: the score of each
            review, in order, one review per score; each passes the step's threshold by default.
        delegate (Union[Unset, DryRunSlotRequest]):
        reopen (Union[Unset, DryRunSlotRequest]):
    """

    step: Union[Unset, str] = UNSET
    outcome: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    contributions: Union[Unset, list["DryRunContributionRequest"]] = UNSET
    parts: Union[Unset, list[str]] = UNSET
    reject: Union[Unset, bool] = UNSET
    expire: Union[Unset, bool] = UNSET
    request_changes: Union[Unset, bool] = UNSET
    submit_changes: Union[Unset, bool] = UNSET
    cancel_changes: Union[Unset, bool] = UNSET
    advance: Union[Unset, bool] = UNSET
    publish: Union[Unset, bool] = UNSET
    release: Union[Unset, bool] = UNSET
    round_step: Union[Unset, bool] = UNSET
    extend: Union[Unset, bool] = UNSET
    final_report: Union[Unset, bool] = UNSET
    exhaust_budget: Union[Unset, bool] = UNSET
    override_budget: Union[Unset, str] = UNSET
    scores: Union[Unset, list[int]] = UNSET
    delegate: Union[Unset, "DryRunSlotRequest"] = UNSET
    reopen: Union[Unset, "DryRunSlotRequest"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step

        outcome = self.outcome

        reason = self.reason

        message = self.message

        contributions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.contributions, Unset):
            contributions = []
            for contributions_item_data in self.contributions:
                contributions_item = contributions_item_data.to_dict()
                contributions.append(contributions_item)

        parts: Union[Unset, list[str]] = UNSET
        if not isinstance(self.parts, Unset):
            parts = self.parts

        reject = self.reject

        expire = self.expire

        request_changes = self.request_changes

        submit_changes = self.submit_changes

        cancel_changes = self.cancel_changes

        advance = self.advance

        publish = self.publish

        release = self.release

        round_step = self.round_step

        extend = self.extend

        final_report = self.final_report

        exhaust_budget = self.exhaust_budget

        override_budget = self.override_budget

        scores: Union[Unset, list[int]] = UNSET
        if not isinstance(self.scores, Unset):
            scores = self.scores

        delegate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.delegate, Unset):
            delegate = self.delegate.to_dict()

        reopen: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reopen, Unset):
            reopen = self.reopen.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if step is not UNSET:
            field_dict["step"] = step
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if reason is not UNSET:
            field_dict["reason"] = reason
        if message is not UNSET:
            field_dict["message"] = message
        if contributions is not UNSET:
            field_dict["contributions"] = contributions
        if parts is not UNSET:
            field_dict["parts"] = parts
        if reject is not UNSET:
            field_dict["reject"] = reject
        if expire is not UNSET:
            field_dict["expire"] = expire
        if request_changes is not UNSET:
            field_dict["request_changes"] = request_changes
        if submit_changes is not UNSET:
            field_dict["submit_changes"] = submit_changes
        if cancel_changes is not UNSET:
            field_dict["cancel_changes"] = cancel_changes
        if advance is not UNSET:
            field_dict["advance"] = advance
        if publish is not UNSET:
            field_dict["publish"] = publish
        if release is not UNSET:
            field_dict["release"] = release
        if round_step is not UNSET:
            field_dict["round_step"] = round_step
        if extend is not UNSET:
            field_dict["extend"] = extend
        if final_report is not UNSET:
            field_dict["final_report"] = final_report
        if exhaust_budget is not UNSET:
            field_dict["exhaust_budget"] = exhaust_budget
        if override_budget is not UNSET:
            field_dict["override_budget"] = override_budget
        if scores is not UNSET:
            field_dict["scores"] = scores
        if delegate is not UNSET:
            field_dict["delegate"] = delegate
        if reopen is not UNSET:
            field_dict["reopen"] = reopen

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dry_run_contribution_request import DryRunContributionRequest
        from ..models.dry_run_slot_request import DryRunSlotRequest

        d = dict(src_dict)
        step = d.pop("step", UNSET)

        outcome = d.pop("outcome", UNSET)

        reason = d.pop("reason", UNSET)

        message = d.pop("message", UNSET)

        contributions = []
        _contributions = d.pop("contributions", UNSET)
        for contributions_item_data in _contributions or []:
            contributions_item = DryRunContributionRequest.from_dict(contributions_item_data)

            contributions.append(contributions_item)

        parts = cast(list[str], d.pop("parts", UNSET))

        reject = d.pop("reject", UNSET)

        expire = d.pop("expire", UNSET)

        request_changes = d.pop("request_changes", UNSET)

        submit_changes = d.pop("submit_changes", UNSET)

        cancel_changes = d.pop("cancel_changes", UNSET)

        advance = d.pop("advance", UNSET)

        publish = d.pop("publish", UNSET)

        release = d.pop("release", UNSET)

        round_step = d.pop("round_step", UNSET)

        extend = d.pop("extend", UNSET)

        final_report = d.pop("final_report", UNSET)

        exhaust_budget = d.pop("exhaust_budget", UNSET)

        override_budget = d.pop("override_budget", UNSET)

        scores = cast(list[int], d.pop("scores", UNSET))

        _delegate = d.pop("delegate", UNSET)
        delegate: Union[Unset, DryRunSlotRequest]
        if isinstance(_delegate, Unset):
            delegate = UNSET
        else:
            delegate = DryRunSlotRequest.from_dict(_delegate)

        _reopen = d.pop("reopen", UNSET)
        reopen: Union[Unset, DryRunSlotRequest]
        if isinstance(_reopen, Unset):
            reopen = UNSET
        else:
            reopen = DryRunSlotRequest.from_dict(_reopen)

        dry_run_action_request = cls(
            step=step,
            outcome=outcome,
            reason=reason,
            message=message,
            contributions=contributions,
            parts=parts,
            reject=reject,
            expire=expire,
            request_changes=request_changes,
            submit_changes=submit_changes,
            cancel_changes=cancel_changes,
            advance=advance,
            publish=publish,
            release=release,
            round_step=round_step,
            extend=extend,
            final_report=final_report,
            exhaust_budget=exhaust_budget,
            override_budget=override_budget,
            scores=scores,
            delegate=delegate,
            reopen=reopen,
        )

        dry_run_action_request.additional_properties = d
        return dry_run_action_request

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
