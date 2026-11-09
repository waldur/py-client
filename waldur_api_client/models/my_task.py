import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.call_step_kind_enum import CallStepKindEnum
from ..models.needed_enum import NeededEnum
from ..models.target_enum import TargetEnum
from ..models.view_enum import ViewEnum
from ..models.workflow_phase_enum import WorkflowPhaseEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MyTask")


@_attrs_define
class MyTask:
    """
    Attributes:
        key (str): Identifies the task among the user's tasks; stable while it is open.
        needed (NeededEnum):
        needed_label (str):
        detail (str): What the task is about within the step: the offering a per-offering slot assesses, or the
            evaluator role to confirm.
        due_at (Union[None, datetime.datetime]):
        is_overdue (bool):
        target (TargetEnum):
        target_section (Union[None, str]): Id of the section of the proposal page to scroll to.
        target_uuid (Union[None, str]): The object the target page opens: the review, the assignment batch, the pool
            invitation, the evaluator role, the round report, the round, or the provider organization whose requests for
            offerings list the request.
        coi_declaration_text (str): The conflict-of-interest declaration the task has the user confirm -- taking a
            contribution over, or holding an evaluator role. Empty for the platform's standard one, or for a task asking for
            none.
        view (Union[None, ViewEnum]): Whose view of the proposal page opens a task on a proposal, by the role that gave
            the user the task; null for other targets.
        proposal_uuid (Union[None, UUID, Unset]):
        proposal_name (Union[None, Unset, str]):
        proposal_slug (Union[None, Unset, str]):
        call_uuid (Union[None, UUID, Unset]):
        call_name (Union[None, Unset, str]):
        round_uuid (Union[None, UUID, Unset]):
        offering_uuid (Union[None, UUID, Unset]): The offering the task is about: the one a per-offering slot assesses,
            or the one an offering request asks to include.
        offering_name (Union[None, Unset, str]):
        provider_uuid (Union[None, UUID, Unset]): The organization providing the task's offering.
        provider_name (Union[None, Unset, str]):
        round_name (Union[None, Unset, str]):
        step_uuid (Union[None, UUID, Unset]): The proposal's step instance.
        call_step_uuid (Union[None, UUID, Unset]):
        step_name (Union[None, Unset, str]):
        step_kind (Union[CallStepKindEnum, None, Unset]):
        phase (Union[None, Unset, WorkflowPhaseEnum]): The phase of the task's step: the evaluation before the award, or
            an extension or closing after it; null for a task on no step.
        view_customer_uuid (Union[None, UUID, Unset]): The organization the view is under: the one managing the call for
            the call team's view, the provider for the offering team's.
    """

    key: str
    needed: NeededEnum
    needed_label: str
    detail: str
    due_at: Union[None, datetime.datetime]
    is_overdue: bool
    target: TargetEnum
    target_section: Union[None, str]
    target_uuid: Union[None, str]
    coi_declaration_text: str
    view: Union[None, ViewEnum]
    proposal_uuid: Union[None, UUID, Unset] = UNSET
    proposal_name: Union[None, Unset, str] = UNSET
    proposal_slug: Union[None, Unset, str] = UNSET
    call_uuid: Union[None, UUID, Unset] = UNSET
    call_name: Union[None, Unset, str] = UNSET
    round_uuid: Union[None, UUID, Unset] = UNSET
    offering_uuid: Union[None, UUID, Unset] = UNSET
    offering_name: Union[None, Unset, str] = UNSET
    provider_uuid: Union[None, UUID, Unset] = UNSET
    provider_name: Union[None, Unset, str] = UNSET
    round_name: Union[None, Unset, str] = UNSET
    step_uuid: Union[None, UUID, Unset] = UNSET
    call_step_uuid: Union[None, UUID, Unset] = UNSET
    step_name: Union[None, Unset, str] = UNSET
    step_kind: Union[CallStepKindEnum, None, Unset] = UNSET
    phase: Union[None, Unset, WorkflowPhaseEnum] = UNSET
    view_customer_uuid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        needed = self.needed.value

        needed_label = self.needed_label

        detail = self.detail

        due_at: Union[None, str]
        if isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        is_overdue = self.is_overdue

        target = self.target.value

        target_section: Union[None, str]
        target_section = self.target_section

        target_uuid: Union[None, str]
        target_uuid = self.target_uuid

        coi_declaration_text = self.coi_declaration_text

        view: Union[None, str]
        if isinstance(self.view, ViewEnum):
            view = self.view.value
        else:
            view = self.view

        proposal_uuid: Union[None, Unset, str]
        if isinstance(self.proposal_uuid, Unset):
            proposal_uuid = UNSET
        elif isinstance(self.proposal_uuid, UUID):
            proposal_uuid = str(self.proposal_uuid)
        else:
            proposal_uuid = self.proposal_uuid

        proposal_name: Union[None, Unset, str]
        if isinstance(self.proposal_name, Unset):
            proposal_name = UNSET
        else:
            proposal_name = self.proposal_name

        proposal_slug: Union[None, Unset, str]
        if isinstance(self.proposal_slug, Unset):
            proposal_slug = UNSET
        else:
            proposal_slug = self.proposal_slug

        call_uuid: Union[None, Unset, str]
        if isinstance(self.call_uuid, Unset):
            call_uuid = UNSET
        elif isinstance(self.call_uuid, UUID):
            call_uuid = str(self.call_uuid)
        else:
            call_uuid = self.call_uuid

        call_name: Union[None, Unset, str]
        if isinstance(self.call_name, Unset):
            call_name = UNSET
        else:
            call_name = self.call_name

        round_uuid: Union[None, Unset, str]
        if isinstance(self.round_uuid, Unset):
            round_uuid = UNSET
        elif isinstance(self.round_uuid, UUID):
            round_uuid = str(self.round_uuid)
        else:
            round_uuid = self.round_uuid

        offering_uuid: Union[None, Unset, str]
        if isinstance(self.offering_uuid, Unset):
            offering_uuid = UNSET
        elif isinstance(self.offering_uuid, UUID):
            offering_uuid = str(self.offering_uuid)
        else:
            offering_uuid = self.offering_uuid

        offering_name: Union[None, Unset, str]
        if isinstance(self.offering_name, Unset):
            offering_name = UNSET
        else:
            offering_name = self.offering_name

        provider_uuid: Union[None, Unset, str]
        if isinstance(self.provider_uuid, Unset):
            provider_uuid = UNSET
        elif isinstance(self.provider_uuid, UUID):
            provider_uuid = str(self.provider_uuid)
        else:
            provider_uuid = self.provider_uuid

        provider_name: Union[None, Unset, str]
        if isinstance(self.provider_name, Unset):
            provider_name = UNSET
        else:
            provider_name = self.provider_name

        round_name: Union[None, Unset, str]
        if isinstance(self.round_name, Unset):
            round_name = UNSET
        else:
            round_name = self.round_name

        step_uuid: Union[None, Unset, str]
        if isinstance(self.step_uuid, Unset):
            step_uuid = UNSET
        elif isinstance(self.step_uuid, UUID):
            step_uuid = str(self.step_uuid)
        else:
            step_uuid = self.step_uuid

        call_step_uuid: Union[None, Unset, str]
        if isinstance(self.call_step_uuid, Unset):
            call_step_uuid = UNSET
        elif isinstance(self.call_step_uuid, UUID):
            call_step_uuid = str(self.call_step_uuid)
        else:
            call_step_uuid = self.call_step_uuid

        step_name: Union[None, Unset, str]
        if isinstance(self.step_name, Unset):
            step_name = UNSET
        else:
            step_name = self.step_name

        step_kind: Union[None, Unset, str]
        if isinstance(self.step_kind, Unset):
            step_kind = UNSET
        elif isinstance(self.step_kind, CallStepKindEnum):
            step_kind = self.step_kind.value
        else:
            step_kind = self.step_kind

        phase: Union[None, Unset, str]
        if isinstance(self.phase, Unset):
            phase = UNSET
        elif isinstance(self.phase, WorkflowPhaseEnum):
            phase = self.phase.value
        else:
            phase = self.phase

        view_customer_uuid: Union[None, Unset, str]
        if isinstance(self.view_customer_uuid, Unset):
            view_customer_uuid = UNSET
        elif isinstance(self.view_customer_uuid, UUID):
            view_customer_uuid = str(self.view_customer_uuid)
        else:
            view_customer_uuid = self.view_customer_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "needed": needed,
                "needed_label": needed_label,
                "detail": detail,
                "due_at": due_at,
                "is_overdue": is_overdue,
                "target": target,
                "target_section": target_section,
                "target_uuid": target_uuid,
                "coi_declaration_text": coi_declaration_text,
                "view": view,
            }
        )
        if proposal_uuid is not UNSET:
            field_dict["proposal_uuid"] = proposal_uuid
        if proposal_name is not UNSET:
            field_dict["proposal_name"] = proposal_name
        if proposal_slug is not UNSET:
            field_dict["proposal_slug"] = proposal_slug
        if call_uuid is not UNSET:
            field_dict["call_uuid"] = call_uuid
        if call_name is not UNSET:
            field_dict["call_name"] = call_name
        if round_uuid is not UNSET:
            field_dict["round_uuid"] = round_uuid
        if offering_uuid is not UNSET:
            field_dict["offering_uuid"] = offering_uuid
        if offering_name is not UNSET:
            field_dict["offering_name"] = offering_name
        if provider_uuid is not UNSET:
            field_dict["provider_uuid"] = provider_uuid
        if provider_name is not UNSET:
            field_dict["provider_name"] = provider_name
        if round_name is not UNSET:
            field_dict["round_name"] = round_name
        if step_uuid is not UNSET:
            field_dict["step_uuid"] = step_uuid
        if call_step_uuid is not UNSET:
            field_dict["call_step_uuid"] = call_step_uuid
        if step_name is not UNSET:
            field_dict["step_name"] = step_name
        if step_kind is not UNSET:
            field_dict["step_kind"] = step_kind
        if phase is not UNSET:
            field_dict["phase"] = phase
        if view_customer_uuid is not UNSET:
            field_dict["view_customer_uuid"] = view_customer_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        needed = NeededEnum(d.pop("needed"))

        needed_label = d.pop("needed_label")

        detail = d.pop("detail")

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

        is_overdue = d.pop("is_overdue")

        target = TargetEnum(d.pop("target"))

        def _parse_target_section(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        target_section = _parse_target_section(d.pop("target_section"))

        def _parse_target_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        target_uuid = _parse_target_uuid(d.pop("target_uuid"))

        coi_declaration_text = d.pop("coi_declaration_text")

        def _parse_view(data: object) -> Union[None, ViewEnum]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                view_type_0 = ViewEnum(data)

                return view_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, ViewEnum], data)

        view = _parse_view(d.pop("view"))

        def _parse_proposal_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proposal_uuid_type_0 = UUID(data)

                return proposal_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        proposal_uuid = _parse_proposal_uuid(d.pop("proposal_uuid", UNSET))

        def _parse_proposal_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        proposal_name = _parse_proposal_name(d.pop("proposal_name", UNSET))

        def _parse_proposal_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        proposal_slug = _parse_proposal_slug(d.pop("proposal_slug", UNSET))

        def _parse_call_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                call_uuid_type_0 = UUID(data)

                return call_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        call_uuid = _parse_call_uuid(d.pop("call_uuid", UNSET))

        def _parse_call_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        call_name = _parse_call_name(d.pop("call_name", UNSET))

        def _parse_round_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                round_uuid_type_0 = UUID(data)

                return round_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        round_uuid = _parse_round_uuid(d.pop("round_uuid", UNSET))

        def _parse_offering_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                offering_uuid_type_0 = UUID(data)

                return offering_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        offering_uuid = _parse_offering_uuid(d.pop("offering_uuid", UNSET))

        def _parse_offering_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        offering_name = _parse_offering_name(d.pop("offering_name", UNSET))

        def _parse_provider_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_uuid_type_0 = UUID(data)

                return provider_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        provider_uuid = _parse_provider_uuid(d.pop("provider_uuid", UNSET))

        def _parse_provider_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider_name = _parse_provider_name(d.pop("provider_name", UNSET))

        def _parse_round_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_name = _parse_round_name(d.pop("round_name", UNSET))

        def _parse_step_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                step_uuid_type_0 = UUID(data)

                return step_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        step_uuid = _parse_step_uuid(d.pop("step_uuid", UNSET))

        def _parse_call_step_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                call_step_uuid_type_0 = UUID(data)

                return call_step_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        call_step_uuid = _parse_call_step_uuid(d.pop("call_step_uuid", UNSET))

        def _parse_step_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        step_name = _parse_step_name(d.pop("step_name", UNSET))

        def _parse_step_kind(data: object) -> Union[CallStepKindEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                step_kind_type_0 = CallStepKindEnum(data)

                return step_kind_type_0
            except:  # noqa: E722
                pass
            return cast(Union[CallStepKindEnum, None, Unset], data)

        step_kind = _parse_step_kind(d.pop("step_kind", UNSET))

        def _parse_phase(data: object) -> Union[None, Unset, WorkflowPhaseEnum]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                phase_type_0 = WorkflowPhaseEnum(data)

                return phase_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, WorkflowPhaseEnum], data)

        phase = _parse_phase(d.pop("phase", UNSET))

        def _parse_view_customer_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                view_customer_uuid_type_0 = UUID(data)

                return view_customer_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        view_customer_uuid = _parse_view_customer_uuid(d.pop("view_customer_uuid", UNSET))

        my_task = cls(
            key=key,
            needed=needed,
            needed_label=needed_label,
            detail=detail,
            due_at=due_at,
            is_overdue=is_overdue,
            target=target,
            target_section=target_section,
            target_uuid=target_uuid,
            coi_declaration_text=coi_declaration_text,
            view=view,
            proposal_uuid=proposal_uuid,
            proposal_name=proposal_name,
            proposal_slug=proposal_slug,
            call_uuid=call_uuid,
            call_name=call_name,
            round_uuid=round_uuid,
            offering_uuid=offering_uuid,
            offering_name=offering_name,
            provider_uuid=provider_uuid,
            provider_name=provider_name,
            round_name=round_name,
            step_uuid=step_uuid,
            call_step_uuid=call_step_uuid,
            step_name=step_name,
            step_kind=step_kind,
            phase=phase,
            view_customer_uuid=view_customer_uuid,
        )

        my_task.additional_properties = d
        return my_task

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
