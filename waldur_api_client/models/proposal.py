import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.gender_enum import GenderEnum
from ..models.oecd_fos_2007_code_enum import OecdFos2007CodeEnum
from ..models.post_award_status_enum import PostAwardStatusEnum
from ..models.proposal_states import ProposalStates
from ..models.workflow_phase_enum import WorkflowPhaseEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_round import NestedRound
    from ..models.offering_team_provider import OfferingTeamProvider
    from ..models.proposal_can_submit_response import ProposalCanSubmitResponse
    from ..models.proposal_change_request import ProposalChangeRequest
    from ..models.proposal_compliance_status import ProposalComplianceStatus
    from ..models.proposal_documentation import ProposalDocumentation
    from ..models.proposal_status_label import ProposalStatusLabel


T = TypeVar("T", bound="Proposal")


@_attrs_define
class Proposal:
    """
    Attributes:
        uuid (UUID):
        url (str):
        slug (str):
        name (str):
        project_name (str):
        supporting_documentation (list['ProposalDocumentation']):
        state (ProposalStates):
        approved_by (Union[None, str]):
        created_by (Union[None, str]):
        created_by_name (str):
        created_by_uuid (UUID):
        applicant_username (str): Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters
        applicant_full_name (str):
        applicant_first_name (str):
        applicant_last_name (str):
        applicant_email (str):
        applicant_registration_method (str): Indicates what registration method was used.
        applicant_phone_number (str):
        applicant_organization (str):
        applicant_organization_country (str):
        applicant_organization_type (str): SCHAC URN (e.g., urn:schac:homeOrganizationType:int:university)
        applicant_organization_registry_code (str): Company registration code of the user's organization, if known
        applicant_organization_vat_code (str): VAT code of the user's organization
        applicant_organization_address (Union[None, str]): Postal address of the user's organization
        applicant_job_title (str):
        applicant_affiliations (list[str]):
        applicant_gender (Union[BlankEnum, GenderEnum, None]): User's gender (male, female, or unknown)
        applicant_personal_title (str): Honorific title (Mr, Ms, Dr, Prof, etc.)
        applicant_place_of_birth (str):
        applicant_address (str):
        applicant_country_of_residence (str):
        applicant_nationality (str): Primary citizenship (ISO 3166-1 alpha-2 code)
        applicant_nationalities (list[str]):
        applicant_eduperson_assurance (list[str]):
        applicant_identity_source (str): Indicates what identity provider was used.
        applicant_civil_number (Union[None, str]):
        applicant_birth_date (Union[None, datetime.date]):
        applicant_active_isds (list[str]):
        project (Union[None, str]):
        round_ (NestedRound):
        call_uuid (UUID):
        call_name (str):
        call_managing_organisation_uuid (UUID):
        call_adoption_required (bool): Whether the call's round results are adopted, after which a held decision can no
            longer be reopened.
        oecd_fos_2007_label (str):
        science_sub_domain_name (str):
        science_domain_uuid (UUID):
        science_domain_name (str):
        panel_uuid (Union[None, UUID]): The call panel evaluating the proposal. Null for whoever may not see who
            evaluates it, the applicant team always.
        panel_name (Union[None, str]): The name of the call panel, as panel_uuid is shown.
        allocation_comment (Union[None, str]):
        created (datetime.datetime):
        submitted_at (Union[None, datetime.datetime]): When the proposal left draft. Null for proposals submitted before
            this field existed: their submission was never recorded and the only proxy, the first workflow step instance,
            was backfilled by migration for the oldest of them — so it is left empty rather than filled with a date that
            reads as fact.
        compliance_status (Union['ProposalComplianceStatus', None]):
        can_submit (ProposalCanSubmitResponse):
        awaiting_manual_advance (bool):
        decision_held (Union[None, bool]):
        open_change_requests (list['ProposalChangeRequest']): The changes asked of the applicant and not yet submitted,
            earliest first: several steps of a stage may each ask at once. Each says what to change and which parts it
            unlocks meanwhile; the applicant may edit every part any of them unlocks, and submits them all at once. For the
            applicant team and those overseeing the call; empty otherwise.
        reads_own_offerings_only (bool): Whether the caller reads the proposal only as the provider of some of the
            offerings it requests: its requested resources, award, assessments and extensions then show only their own
            offerings' part.
        offering_team_providers (list['OfferingTeamProvider']): The providers whose offering requested by the proposal
            the caller holds a role on -- its managers, or someone its part of a step can be handed to: each opens the
            proposal as that offering's team. Empty for everyone else.
        workflow_step (Union[None, str]): Key of the call step the proposal stands in.
        status_labels (list['ProposalStatusLabel']): What the call configured the caller's dashboard to call the
            proposal's current stage: one label per step of the stage that has one for the caller (several when the stage
            runs steps side by side). Empty when nothing is configured, so the state stands.
        requested_duration_months (Union[None, int]): The project length the applicant chose from the call's
            allowed_duration_months. Written through update_project_details.
        awarded_duration_months (Union[None, int]): The project length the award grants, in months. Null for whoever may
            not read the award yet, as the awarded resources.
        completed_at (Union[None, datetime.datetime]): When the project was completed: its final report accepted.
        post_award_status (Union[None, PostAwardStatusEnum]): Where an accepted proposal's extension request or final
            report stands. Null before acceptance, without post-award work, and for whoever may not read the award.
        open_run_uuid (Union[None, UUID]): The open extension request or final report, if any.
        open_run_phase (Union[None, WorkflowPhaseEnum]):
        extension_requestable_until (Union[None, datetime.date]): The last day an extension can be requested; null when
            the call takes no extension requests or the project has no end date.
        final_report_openable (bool): Whether the final report can be opened now: the proposal is accepted with a
            project, not completed, has no open extension request or final report, and its call has final report steps. Who
            may open it is decided by the action itself.
        description (Union[Unset, str]):
        project_summary (Union[Unset, str]):
        oecd_fos_2007_code (Union[BlankEnum, None, OecdFos2007CodeEnum, Unset]):
        science_sub_domain (Union[None, UUID, Unset]):
    """

    uuid: UUID
    url: str
    slug: str
    name: str
    project_name: str
    supporting_documentation: list["ProposalDocumentation"]
    state: ProposalStates
    approved_by: Union[None, str]
    created_by: Union[None, str]
    created_by_name: str
    created_by_uuid: UUID
    applicant_username: str
    applicant_full_name: str
    applicant_first_name: str
    applicant_last_name: str
    applicant_email: str
    applicant_registration_method: str
    applicant_phone_number: str
    applicant_organization: str
    applicant_organization_country: str
    applicant_organization_type: str
    applicant_organization_registry_code: str
    applicant_organization_vat_code: str
    applicant_organization_address: Union[None, str]
    applicant_job_title: str
    applicant_affiliations: list[str]
    applicant_gender: Union[BlankEnum, GenderEnum, None]
    applicant_personal_title: str
    applicant_place_of_birth: str
    applicant_address: str
    applicant_country_of_residence: str
    applicant_nationality: str
    applicant_nationalities: list[str]
    applicant_eduperson_assurance: list[str]
    applicant_identity_source: str
    applicant_civil_number: Union[None, str]
    applicant_birth_date: Union[None, datetime.date]
    applicant_active_isds: list[str]
    project: Union[None, str]
    round_: "NestedRound"
    call_uuid: UUID
    call_name: str
    call_managing_organisation_uuid: UUID
    call_adoption_required: bool
    oecd_fos_2007_label: str
    science_sub_domain_name: str
    science_domain_uuid: UUID
    science_domain_name: str
    panel_uuid: Union[None, UUID]
    panel_name: Union[None, str]
    allocation_comment: Union[None, str]
    created: datetime.datetime
    submitted_at: Union[None, datetime.datetime]
    compliance_status: Union["ProposalComplianceStatus", None]
    can_submit: "ProposalCanSubmitResponse"
    awaiting_manual_advance: bool
    decision_held: Union[None, bool]
    open_change_requests: list["ProposalChangeRequest"]
    reads_own_offerings_only: bool
    offering_team_providers: list["OfferingTeamProvider"]
    workflow_step: Union[None, str]
    status_labels: list["ProposalStatusLabel"]
    requested_duration_months: Union[None, int]
    awarded_duration_months: Union[None, int]
    completed_at: Union[None, datetime.datetime]
    post_award_status: Union[None, PostAwardStatusEnum]
    open_run_uuid: Union[None, UUID]
    open_run_phase: Union[None, WorkflowPhaseEnum]
    extension_requestable_until: Union[None, datetime.date]
    final_report_openable: bool
    description: Union[Unset, str] = UNSET
    project_summary: Union[Unset, str] = UNSET
    oecd_fos_2007_code: Union[BlankEnum, None, OecdFos2007CodeEnum, Unset] = UNSET
    science_sub_domain: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.proposal_compliance_status import ProposalComplianceStatus

        uuid = str(self.uuid)

        url = self.url

        slug = self.slug

        name = self.name

        project_name = self.project_name

        supporting_documentation = []
        for supporting_documentation_item_data in self.supporting_documentation:
            supporting_documentation_item = supporting_documentation_item_data.to_dict()
            supporting_documentation.append(supporting_documentation_item)

        state = self.state.value

        approved_by: Union[None, str]
        approved_by = self.approved_by

        created_by: Union[None, str]
        created_by = self.created_by

        created_by_name = self.created_by_name

        created_by_uuid = str(self.created_by_uuid)

        applicant_username = self.applicant_username

        applicant_full_name = self.applicant_full_name

        applicant_first_name = self.applicant_first_name

        applicant_last_name = self.applicant_last_name

        applicant_email = self.applicant_email

        applicant_registration_method = self.applicant_registration_method

        applicant_phone_number = self.applicant_phone_number

        applicant_organization = self.applicant_organization

        applicant_organization_country = self.applicant_organization_country

        applicant_organization_type = self.applicant_organization_type

        applicant_organization_registry_code = self.applicant_organization_registry_code

        applicant_organization_vat_code = self.applicant_organization_vat_code

        applicant_organization_address: Union[None, str]
        applicant_organization_address = self.applicant_organization_address

        applicant_job_title = self.applicant_job_title

        applicant_affiliations = self.applicant_affiliations

        applicant_gender: Union[None, str]
        if isinstance(self.applicant_gender, GenderEnum):
            applicant_gender = self.applicant_gender.value
        elif isinstance(self.applicant_gender, BlankEnum):
            applicant_gender = self.applicant_gender.value
        else:
            applicant_gender = self.applicant_gender

        applicant_personal_title = self.applicant_personal_title

        applicant_place_of_birth = self.applicant_place_of_birth

        applicant_address = self.applicant_address

        applicant_country_of_residence = self.applicant_country_of_residence

        applicant_nationality = self.applicant_nationality

        applicant_nationalities = self.applicant_nationalities

        applicant_eduperson_assurance = self.applicant_eduperson_assurance

        applicant_identity_source = self.applicant_identity_source

        applicant_civil_number: Union[None, str]
        applicant_civil_number = self.applicant_civil_number

        applicant_birth_date: Union[None, str]
        if isinstance(self.applicant_birth_date, datetime.date):
            applicant_birth_date = self.applicant_birth_date.isoformat()
        else:
            applicant_birth_date = self.applicant_birth_date

        applicant_active_isds = self.applicant_active_isds

        project: Union[None, str]
        project = self.project

        round_ = self.round_.to_dict()

        call_uuid = str(self.call_uuid)

        call_name = self.call_name

        call_managing_organisation_uuid = str(self.call_managing_organisation_uuid)

        call_adoption_required = self.call_adoption_required

        oecd_fos_2007_label = self.oecd_fos_2007_label

        science_sub_domain_name = self.science_sub_domain_name

        science_domain_uuid = str(self.science_domain_uuid)

        science_domain_name = self.science_domain_name

        panel_uuid: Union[None, str]
        if isinstance(self.panel_uuid, UUID):
            panel_uuid = str(self.panel_uuid)
        else:
            panel_uuid = self.panel_uuid

        panel_name: Union[None, str]
        panel_name = self.panel_name

        allocation_comment: Union[None, str]
        allocation_comment = self.allocation_comment

        created = self.created.isoformat()

        submitted_at: Union[None, str]
        if isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        compliance_status: Union[None, dict[str, Any]]
        if isinstance(self.compliance_status, ProposalComplianceStatus):
            compliance_status = self.compliance_status.to_dict()
        else:
            compliance_status = self.compliance_status

        can_submit = self.can_submit.to_dict()

        awaiting_manual_advance = self.awaiting_manual_advance

        decision_held: Union[None, bool]
        decision_held = self.decision_held

        open_change_requests = []
        for open_change_requests_item_data in self.open_change_requests:
            open_change_requests_item = open_change_requests_item_data.to_dict()
            open_change_requests.append(open_change_requests_item)

        reads_own_offerings_only = self.reads_own_offerings_only

        offering_team_providers = []
        for offering_team_providers_item_data in self.offering_team_providers:
            offering_team_providers_item = offering_team_providers_item_data.to_dict()
            offering_team_providers.append(offering_team_providers_item)

        workflow_step: Union[None, str]
        workflow_step = self.workflow_step

        status_labels = []
        for status_labels_item_data in self.status_labels:
            status_labels_item = status_labels_item_data.to_dict()
            status_labels.append(status_labels_item)

        requested_duration_months: Union[None, int]
        requested_duration_months = self.requested_duration_months

        awarded_duration_months: Union[None, int]
        awarded_duration_months = self.awarded_duration_months

        completed_at: Union[None, str]
        if isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        post_award_status: Union[None, str]
        if isinstance(self.post_award_status, PostAwardStatusEnum):
            post_award_status = self.post_award_status.value
        else:
            post_award_status = self.post_award_status

        open_run_uuid: Union[None, str]
        if isinstance(self.open_run_uuid, UUID):
            open_run_uuid = str(self.open_run_uuid)
        else:
            open_run_uuid = self.open_run_uuid

        open_run_phase: Union[None, str]
        if isinstance(self.open_run_phase, WorkflowPhaseEnum):
            open_run_phase = self.open_run_phase.value
        else:
            open_run_phase = self.open_run_phase

        extension_requestable_until: Union[None, str]
        if isinstance(self.extension_requestable_until, datetime.date):
            extension_requestable_until = self.extension_requestable_until.isoformat()
        else:
            extension_requestable_until = self.extension_requestable_until

        final_report_openable = self.final_report_openable

        description = self.description

        project_summary = self.project_summary

        oecd_fos_2007_code: Union[None, Unset, str]
        if isinstance(self.oecd_fos_2007_code, Unset):
            oecd_fos_2007_code = UNSET
        elif isinstance(self.oecd_fos_2007_code, OecdFos2007CodeEnum):
            oecd_fos_2007_code = self.oecd_fos_2007_code.value
        elif isinstance(self.oecd_fos_2007_code, BlankEnum):
            oecd_fos_2007_code = self.oecd_fos_2007_code.value
        else:
            oecd_fos_2007_code = self.oecd_fos_2007_code

        science_sub_domain: Union[None, Unset, str]
        if isinstance(self.science_sub_domain, Unset):
            science_sub_domain = UNSET
        elif isinstance(self.science_sub_domain, UUID):
            science_sub_domain = str(self.science_sub_domain)
        else:
            science_sub_domain = self.science_sub_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "url": url,
                "slug": slug,
                "name": name,
                "project_name": project_name,
                "supporting_documentation": supporting_documentation,
                "state": state,
                "approved_by": approved_by,
                "created_by": created_by,
                "created_by_name": created_by_name,
                "created_by_uuid": created_by_uuid,
                "applicant_username": applicant_username,
                "applicant_full_name": applicant_full_name,
                "applicant_first_name": applicant_first_name,
                "applicant_last_name": applicant_last_name,
                "applicant_email": applicant_email,
                "applicant_registration_method": applicant_registration_method,
                "applicant_phone_number": applicant_phone_number,
                "applicant_organization": applicant_organization,
                "applicant_organization_country": applicant_organization_country,
                "applicant_organization_type": applicant_organization_type,
                "applicant_organization_registry_code": applicant_organization_registry_code,
                "applicant_organization_vat_code": applicant_organization_vat_code,
                "applicant_organization_address": applicant_organization_address,
                "applicant_job_title": applicant_job_title,
                "applicant_affiliations": applicant_affiliations,
                "applicant_gender": applicant_gender,
                "applicant_personal_title": applicant_personal_title,
                "applicant_place_of_birth": applicant_place_of_birth,
                "applicant_address": applicant_address,
                "applicant_country_of_residence": applicant_country_of_residence,
                "applicant_nationality": applicant_nationality,
                "applicant_nationalities": applicant_nationalities,
                "applicant_eduperson_assurance": applicant_eduperson_assurance,
                "applicant_identity_source": applicant_identity_source,
                "applicant_civil_number": applicant_civil_number,
                "applicant_birth_date": applicant_birth_date,
                "applicant_active_isds": applicant_active_isds,
                "project": project,
                "round": round_,
                "call_uuid": call_uuid,
                "call_name": call_name,
                "call_managing_organisation_uuid": call_managing_organisation_uuid,
                "call_adoption_required": call_adoption_required,
                "oecd_fos_2007_label": oecd_fos_2007_label,
                "science_sub_domain_name": science_sub_domain_name,
                "science_domain_uuid": science_domain_uuid,
                "science_domain_name": science_domain_name,
                "panel_uuid": panel_uuid,
                "panel_name": panel_name,
                "allocation_comment": allocation_comment,
                "created": created,
                "submitted_at": submitted_at,
                "compliance_status": compliance_status,
                "can_submit": can_submit,
                "awaiting_manual_advance": awaiting_manual_advance,
                "decision_held": decision_held,
                "open_change_requests": open_change_requests,
                "reads_own_offerings_only": reads_own_offerings_only,
                "offering_team_providers": offering_team_providers,
                "workflow_step": workflow_step,
                "status_labels": status_labels,
                "requested_duration_months": requested_duration_months,
                "awarded_duration_months": awarded_duration_months,
                "completed_at": completed_at,
                "post_award_status": post_award_status,
                "open_run_uuid": open_run_uuid,
                "open_run_phase": open_run_phase,
                "extension_requestable_until": extension_requestable_until,
                "final_report_openable": final_report_openable,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if project_summary is not UNSET:
            field_dict["project_summary"] = project_summary
        if oecd_fos_2007_code is not UNSET:
            field_dict["oecd_fos_2007_code"] = oecd_fos_2007_code
        if science_sub_domain is not UNSET:
            field_dict["science_sub_domain"] = science_sub_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_round import NestedRound
        from ..models.offering_team_provider import OfferingTeamProvider
        from ..models.proposal_can_submit_response import ProposalCanSubmitResponse
        from ..models.proposal_change_request import ProposalChangeRequest
        from ..models.proposal_compliance_status import ProposalComplianceStatus
        from ..models.proposal_documentation import ProposalDocumentation
        from ..models.proposal_status_label import ProposalStatusLabel

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        url = d.pop("url")

        slug = d.pop("slug")

        name = d.pop("name")

        project_name = d.pop("project_name")

        supporting_documentation = []
        _supporting_documentation = d.pop("supporting_documentation")
        for supporting_documentation_item_data in _supporting_documentation:
            supporting_documentation_item = ProposalDocumentation.from_dict(supporting_documentation_item_data)

            supporting_documentation.append(supporting_documentation_item)

        state = ProposalStates(d.pop("state"))

        def _parse_approved_by(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        approved_by = _parse_approved_by(d.pop("approved_by"))

        def _parse_created_by(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by = _parse_created_by(d.pop("created_by"))

        created_by_name = d.pop("created_by_name")

        created_by_uuid = UUID(d.pop("created_by_uuid"))

        applicant_username = d.pop("applicant_username")

        applicant_full_name = d.pop("applicant_full_name")

        applicant_first_name = d.pop("applicant_first_name")

        applicant_last_name = d.pop("applicant_last_name")

        applicant_email = d.pop("applicant_email")

        applicant_registration_method = d.pop("applicant_registration_method")

        applicant_phone_number = d.pop("applicant_phone_number")

        applicant_organization = d.pop("applicant_organization")

        applicant_organization_country = d.pop("applicant_organization_country")

        applicant_organization_type = d.pop("applicant_organization_type")

        applicant_organization_registry_code = d.pop("applicant_organization_registry_code")

        applicant_organization_vat_code = d.pop("applicant_organization_vat_code")

        def _parse_applicant_organization_address(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        applicant_organization_address = _parse_applicant_organization_address(d.pop("applicant_organization_address"))

        applicant_job_title = d.pop("applicant_job_title")

        applicant_affiliations = cast(list[str], d.pop("applicant_affiliations"))

        def _parse_applicant_gender(data: object) -> Union[BlankEnum, GenderEnum, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applicant_gender_type_0 = GenderEnum(data)

                return applicant_gender_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applicant_gender_type_1 = BlankEnum(data)

                return applicant_gender_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, GenderEnum, None], data)

        applicant_gender = _parse_applicant_gender(d.pop("applicant_gender"))

        applicant_personal_title = d.pop("applicant_personal_title")

        applicant_place_of_birth = d.pop("applicant_place_of_birth")

        applicant_address = d.pop("applicant_address")

        applicant_country_of_residence = d.pop("applicant_country_of_residence")

        applicant_nationality = d.pop("applicant_nationality")

        applicant_nationalities = cast(list[str], d.pop("applicant_nationalities"))

        applicant_eduperson_assurance = cast(list[str], d.pop("applicant_eduperson_assurance"))

        applicant_identity_source = d.pop("applicant_identity_source")

        def _parse_applicant_civil_number(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        applicant_civil_number = _parse_applicant_civil_number(d.pop("applicant_civil_number"))

        def _parse_applicant_birth_date(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applicant_birth_date_type_0 = isoparse(data).date()

                return applicant_birth_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        applicant_birth_date = _parse_applicant_birth_date(d.pop("applicant_birth_date"))

        applicant_active_isds = cast(list[str], d.pop("applicant_active_isds"))

        def _parse_project(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        project = _parse_project(d.pop("project"))

        round_ = NestedRound.from_dict(d.pop("round"))

        call_uuid = UUID(d.pop("call_uuid"))

        call_name = d.pop("call_name")

        call_managing_organisation_uuid = UUID(d.pop("call_managing_organisation_uuid"))

        call_adoption_required = d.pop("call_adoption_required")

        oecd_fos_2007_label = d.pop("oecd_fos_2007_label")

        science_sub_domain_name = d.pop("science_sub_domain_name")

        science_domain_uuid = UUID(d.pop("science_domain_uuid"))

        science_domain_name = d.pop("science_domain_name")

        def _parse_panel_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                panel_uuid_type_0 = UUID(data)

                return panel_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        panel_uuid = _parse_panel_uuid(d.pop("panel_uuid"))

        def _parse_panel_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        panel_name = _parse_panel_name(d.pop("panel_name"))

        def _parse_allocation_comment(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        allocation_comment = _parse_allocation_comment(d.pop("allocation_comment"))

        created = isoparse(d.pop("created"))

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

        def _parse_compliance_status(data: object) -> Union["ProposalComplianceStatus", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                compliance_status_type_1 = ProposalComplianceStatus.from_dict(data)

                return compliance_status_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ProposalComplianceStatus", None], data)

        compliance_status = _parse_compliance_status(d.pop("compliance_status"))

        can_submit = ProposalCanSubmitResponse.from_dict(d.pop("can_submit"))

        awaiting_manual_advance = d.pop("awaiting_manual_advance")

        def _parse_decision_held(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        decision_held = _parse_decision_held(d.pop("decision_held"))

        open_change_requests = []
        _open_change_requests = d.pop("open_change_requests")
        for open_change_requests_item_data in _open_change_requests:
            open_change_requests_item = ProposalChangeRequest.from_dict(open_change_requests_item_data)

            open_change_requests.append(open_change_requests_item)

        reads_own_offerings_only = d.pop("reads_own_offerings_only")

        offering_team_providers = []
        _offering_team_providers = d.pop("offering_team_providers")
        for offering_team_providers_item_data in _offering_team_providers:
            offering_team_providers_item = OfferingTeamProvider.from_dict(offering_team_providers_item_data)

            offering_team_providers.append(offering_team_providers_item)

        def _parse_workflow_step(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        workflow_step = _parse_workflow_step(d.pop("workflow_step"))

        status_labels = []
        _status_labels = d.pop("status_labels")
        for status_labels_item_data in _status_labels:
            status_labels_item = ProposalStatusLabel.from_dict(status_labels_item_data)

            status_labels.append(status_labels_item)

        def _parse_requested_duration_months(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        requested_duration_months = _parse_requested_duration_months(d.pop("requested_duration_months"))

        def _parse_awarded_duration_months(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        awarded_duration_months = _parse_awarded_duration_months(d.pop("awarded_duration_months"))

        def _parse_completed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        def _parse_post_award_status(data: object) -> Union[None, PostAwardStatusEnum]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                post_award_status_type_0 = PostAwardStatusEnum(data)

                return post_award_status_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, PostAwardStatusEnum], data)

        post_award_status = _parse_post_award_status(d.pop("post_award_status"))

        def _parse_open_run_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                open_run_uuid_type_0 = UUID(data)

                return open_run_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        open_run_uuid = _parse_open_run_uuid(d.pop("open_run_uuid"))

        def _parse_open_run_phase(data: object) -> Union[None, WorkflowPhaseEnum]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                open_run_phase_type_0 = WorkflowPhaseEnum(data)

                return open_run_phase_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, WorkflowPhaseEnum], data)

        open_run_phase = _parse_open_run_phase(d.pop("open_run_phase"))

        def _parse_extension_requestable_until(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                extension_requestable_until_type_0 = isoparse(data).date()

                return extension_requestable_until_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        extension_requestable_until = _parse_extension_requestable_until(d.pop("extension_requestable_until"))

        final_report_openable = d.pop("final_report_openable")

        description = d.pop("description", UNSET)

        project_summary = d.pop("project_summary", UNSET)

        def _parse_oecd_fos_2007_code(data: object) -> Union[BlankEnum, None, OecdFos2007CodeEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                oecd_fos_2007_code_type_0 = OecdFos2007CodeEnum(data)

                return oecd_fos_2007_code_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                oecd_fos_2007_code_type_1 = BlankEnum(data)

                return oecd_fos_2007_code_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, None, OecdFos2007CodeEnum, Unset], data)

        oecd_fos_2007_code = _parse_oecd_fos_2007_code(d.pop("oecd_fos_2007_code", UNSET))

        def _parse_science_sub_domain(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                science_sub_domain_type_0 = UUID(data)

                return science_sub_domain_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        science_sub_domain = _parse_science_sub_domain(d.pop("science_sub_domain", UNSET))

        proposal = cls(
            uuid=uuid,
            url=url,
            slug=slug,
            name=name,
            project_name=project_name,
            supporting_documentation=supporting_documentation,
            state=state,
            approved_by=approved_by,
            created_by=created_by,
            created_by_name=created_by_name,
            created_by_uuid=created_by_uuid,
            applicant_username=applicant_username,
            applicant_full_name=applicant_full_name,
            applicant_first_name=applicant_first_name,
            applicant_last_name=applicant_last_name,
            applicant_email=applicant_email,
            applicant_registration_method=applicant_registration_method,
            applicant_phone_number=applicant_phone_number,
            applicant_organization=applicant_organization,
            applicant_organization_country=applicant_organization_country,
            applicant_organization_type=applicant_organization_type,
            applicant_organization_registry_code=applicant_organization_registry_code,
            applicant_organization_vat_code=applicant_organization_vat_code,
            applicant_organization_address=applicant_organization_address,
            applicant_job_title=applicant_job_title,
            applicant_affiliations=applicant_affiliations,
            applicant_gender=applicant_gender,
            applicant_personal_title=applicant_personal_title,
            applicant_place_of_birth=applicant_place_of_birth,
            applicant_address=applicant_address,
            applicant_country_of_residence=applicant_country_of_residence,
            applicant_nationality=applicant_nationality,
            applicant_nationalities=applicant_nationalities,
            applicant_eduperson_assurance=applicant_eduperson_assurance,
            applicant_identity_source=applicant_identity_source,
            applicant_civil_number=applicant_civil_number,
            applicant_birth_date=applicant_birth_date,
            applicant_active_isds=applicant_active_isds,
            project=project,
            round_=round_,
            call_uuid=call_uuid,
            call_name=call_name,
            call_managing_organisation_uuid=call_managing_organisation_uuid,
            call_adoption_required=call_adoption_required,
            oecd_fos_2007_label=oecd_fos_2007_label,
            science_sub_domain_name=science_sub_domain_name,
            science_domain_uuid=science_domain_uuid,
            science_domain_name=science_domain_name,
            panel_uuid=panel_uuid,
            panel_name=panel_name,
            allocation_comment=allocation_comment,
            created=created,
            submitted_at=submitted_at,
            compliance_status=compliance_status,
            can_submit=can_submit,
            awaiting_manual_advance=awaiting_manual_advance,
            decision_held=decision_held,
            open_change_requests=open_change_requests,
            reads_own_offerings_only=reads_own_offerings_only,
            offering_team_providers=offering_team_providers,
            workflow_step=workflow_step,
            status_labels=status_labels,
            requested_duration_months=requested_duration_months,
            awarded_duration_months=awarded_duration_months,
            completed_at=completed_at,
            post_award_status=post_award_status,
            open_run_uuid=open_run_uuid,
            open_run_phase=open_run_phase,
            extension_requestable_until=extension_requestable_until,
            final_report_openable=final_report_openable,
            description=description,
            project_summary=project_summary,
            oecd_fos_2007_code=oecd_fos_2007_code,
            science_sub_domain=science_sub_domain,
        )

        proposal.additional_properties = d
        return proposal

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
