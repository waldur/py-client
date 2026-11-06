import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.budget_enforcement_enum import BudgetEnforcementEnum
from ..models.call_states import CallStates
from ..models.evaluation_start_enum import EvaluationStartEnum
from ..models.order_author_enum import OrderAuthorEnum
from ..models.publish_results_enum import PublishResultsEnum
from ..models.resource_template_selection_mode_enum import ResourceTemplateSelectionModeEnum
from ..models.undecided_at_round_completion_enum import UndecidedAtRoundCompletionEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_applicant_visibility_config import CallApplicantVisibilityConfig
    from ..models.call_document import CallDocument
    from ..models.call_offering_component_bounds import CallOfferingComponentBounds
    from ..models.call_proposal_field_config import CallProposalFieldConfig
    from ..models.call_resource_template import CallResourceTemplate
    from ..models.call_reviewer_eligibility import CallReviewerEligibility
    from ..models.nested_requested_offering import NestedRequestedOffering
    from ..models.nested_round import NestedRound
    from ..models.proposal_field_metadata import ProposalFieldMetadata


T = TypeVar("T", bound="ProtectedCall")


@_attrs_define
class ProtectedCall:
    """
    Attributes:
        url (Union[Unset, str]):
        uuid (Union[Unset, UUID]):
        created (Union[Unset, datetime.datetime]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[None, Unset, datetime.datetime]):
        slug (Union[Unset, str]): URL-friendly identifier. Only editable by staff users.
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        state (Union[Unset, CallStates]):
        manager (Union[Unset, str]):
        manager_uuid (Union[Unset, UUID]):
        customer_name (Union[Unset, str]):
        customer_uuid (Union[Unset, UUID]):
        offerings (Union[Unset, list['NestedRequestedOffering']]):
        rounds (Union[Unset, list['NestedRound']]):
        documents (Union[Unset, list['CallDocument']]):
        resource_templates (Union[Unset, list['CallResourceTemplate']]):
        component_rules (Union[Unset, list['CallOfferingComponentBounds']]): What a proposal may request of each
            component of the call's accepted offerings, in the component's unit and per its limit period.
        fixed_duration_in_days (Union[None, Unset, int]):
        allowed_duration_months (Union[Unset, list[int]]): Durations, in months, the applicant chooses the project's
            length from. Empty offers no choice. Cannot be combined with fixed_duration_in_days. Proposals already submitted
            keep the length they asked for.
        max_prepaid_duration_months (Union[None, Unset, int]): The longest prepaid subscription, in whole months, that
            fits inside fixed_duration_in_days measured from today; null when the call fixes no duration.
        backend_id (Union[Unset, str]):
        external_url (Union[None, Unset, str]):
        reviewer_identity_visible_to_submitters (Union[Unset, bool]): Whether proposal applicants can see reviewer
            identities
        reviews_visible_to_submitters (Union[Unset, bool]): Whether proposal applicants can see review comments and
            scores. Applicants still see what an applicant step lists as its input steps, such as the reviews they respond
            to.
        has_eligibility_restrictions (Union[Unset, bool]): Check if call has any eligibility restrictions configured.
        proposal_field_config (Union[Unset, CallProposalFieldConfig]):
        evaluation_start (Union[Unset, EvaluationStartEnum]):
        publish_results (Union[Unset, PublishResultsEnum]):
        resource_template_selection_mode (Union[Unset, ResourceTemplateSelectionModeEnum]):
        created_by (Union[None, Unset, str]):
        reference_code (Union[Unset, str]):
        compliance_checklist (Union[None, UUID, Unset]): Compliance checklist that proposals must complete before
            submission
        compliance_checklist_name (Union[Unset, str]):
        panel_chair (Union[None, UUID, Unset]):
        panel_chair_uuid (Union[Unset, UUID]):
        panel_chair_name (Union[Unset, str]):
        panel_vice_chair (Union[None, UUID, Unset]):
        panel_vice_chair_uuid (Union[Unset, UUID]):
        panel_vice_chair_name (Union[Unset, str]):
        proposal_slug_template (Union[None, Unset, str]): Template for proposal slugs. Supports: {call_slug},
            {round_slug}, {org_slug}, {year}, {month}, {counter}, {counter_padded}. Default: {round_slug}-{counter_padded}
        user_email_patterns (Union[Unset, list[str]]): List of email regex patterns. User must match one.
        user_affiliations (Union[Unset, list[str]]): List of allowed affiliations. User must have one.
        user_identity_sources (Union[Unset, list[str]]): List of allowed identity sources (identity providers).
        user_nationalities (Union[Unset, list[str]]): List of allowed nationality codes (ISO 3166-1 alpha-2). User must
            have one.
        user_organization_types (Union[Unset, list[str]]): List of allowed organization type URNs (SCHAC). User must
            match one.
        user_assurance_levels (Union[Unset, list[str]]): List of required assurance URIs (REFEDS). User must have ALL of
            these.
        applicant_visibility_config (Union['CallApplicantVisibilityConfig', None, Unset]):
        reviewer_eligibility (Union['CallReviewerEligibility', None, Unset]): Who may review for the call: checked when
            a reviewer is invited, accepts, is suggested or is given the call's reviewer role. Kept apart from the
            restrictions on applicants.
        proposal_field_metadata (Union[Unset, list['ProposalFieldMetadata']]): Per-field state, permitted transitions
            and downstream consumers for the Project details step.
        has_proposals (Union[Unset, bool]): Whether any proposal has been submitted to this call. Used by the frontend
            to gate slug-template and checklist fields.
        order_author (Union[Unset, OrderAuthorEnum]):
        order_author_user (Union[None, UUID, Unset]): The person orders are attributed to when the author is a named
            contact. Must hold a role on this call or on the organization managing it.
        order_author_user_uuid (Union[None, UUID, Unset]):
        order_author_user_name (Union[None, Unset, str]):
        carry_over_drafts (Union[Unset, bool]): Whether a draft still open when its round's cut-off passes moves on to
            the call's next round instead of being canceled. Without a later round the draft is canceled either way.
        coi_declaration_text (Union[Unset, str]): The conflict-of-interest declaration evaluators confirm, for every
            step asking them to that has no text of its own. Empty for the platform's standard declaration.
        undecided_at_round_completion (Union[Unset, UndecidedAtRoundCompletionEnum]):
        adoption_required (Union[Unset, bool]): Whether a round's results must be adopted (by a board, say) before they
            are published. The adoption is then recorded while the round is deciding, and publication waits for it.
        budget_enforcement (Union[Unset, BudgetEnforcementEnum]):
        applicant_cc_roles (Union[Unset, list[str]]): Names of the proposal roles whose holders are copied (Cc) on every
            mail to the applicant about a proposal: PROPOSAL.MANAGER for the principal investigator, PROPOSAL.ADMIN for the
            proposal administrators. Only the proposal's current team is copied. Empty copies nobody.
        target_decision_days (Union[None, Unset, int]): Days from a round's cut-off to its decision the workflow is
            planned for, when the round has no allocation date. The workflow check compares the steps' durations with it.
        template_uuid (Union[None, UUID, Unset]):
        template_name (Union[None, Unset, str]):
        template_version (Union[None, Unset, int]): Version of the template the call was created from.
        template_latest_version (Union[None, Unset, int]): The template's current version.
    """

    url: Union[Unset, str] = UNSET
    uuid: Union[Unset, UUID] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[None, Unset, datetime.datetime] = UNSET
    slug: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    state: Union[Unset, CallStates] = UNSET
    manager: Union[Unset, str] = UNSET
    manager_uuid: Union[Unset, UUID] = UNSET
    customer_name: Union[Unset, str] = UNSET
    customer_uuid: Union[Unset, UUID] = UNSET
    offerings: Union[Unset, list["NestedRequestedOffering"]] = UNSET
    rounds: Union[Unset, list["NestedRound"]] = UNSET
    documents: Union[Unset, list["CallDocument"]] = UNSET
    resource_templates: Union[Unset, list["CallResourceTemplate"]] = UNSET
    component_rules: Union[Unset, list["CallOfferingComponentBounds"]] = UNSET
    fixed_duration_in_days: Union[None, Unset, int] = UNSET
    allowed_duration_months: Union[Unset, list[int]] = UNSET
    max_prepaid_duration_months: Union[None, Unset, int] = UNSET
    backend_id: Union[Unset, str] = UNSET
    external_url: Union[None, Unset, str] = UNSET
    reviewer_identity_visible_to_submitters: Union[Unset, bool] = UNSET
    reviews_visible_to_submitters: Union[Unset, bool] = UNSET
    has_eligibility_restrictions: Union[Unset, bool] = UNSET
    proposal_field_config: Union[Unset, "CallProposalFieldConfig"] = UNSET
    evaluation_start: Union[Unset, EvaluationStartEnum] = UNSET
    publish_results: Union[Unset, PublishResultsEnum] = UNSET
    resource_template_selection_mode: Union[Unset, ResourceTemplateSelectionModeEnum] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    reference_code: Union[Unset, str] = UNSET
    compliance_checklist: Union[None, UUID, Unset] = UNSET
    compliance_checklist_name: Union[Unset, str] = UNSET
    panel_chair: Union[None, UUID, Unset] = UNSET
    panel_chair_uuid: Union[Unset, UUID] = UNSET
    panel_chair_name: Union[Unset, str] = UNSET
    panel_vice_chair: Union[None, UUID, Unset] = UNSET
    panel_vice_chair_uuid: Union[Unset, UUID] = UNSET
    panel_vice_chair_name: Union[Unset, str] = UNSET
    proposal_slug_template: Union[None, Unset, str] = UNSET
    user_email_patterns: Union[Unset, list[str]] = UNSET
    user_affiliations: Union[Unset, list[str]] = UNSET
    user_identity_sources: Union[Unset, list[str]] = UNSET
    user_nationalities: Union[Unset, list[str]] = UNSET
    user_organization_types: Union[Unset, list[str]] = UNSET
    user_assurance_levels: Union[Unset, list[str]] = UNSET
    applicant_visibility_config: Union["CallApplicantVisibilityConfig", None, Unset] = UNSET
    reviewer_eligibility: Union["CallReviewerEligibility", None, Unset] = UNSET
    proposal_field_metadata: Union[Unset, list["ProposalFieldMetadata"]] = UNSET
    has_proposals: Union[Unset, bool] = UNSET
    order_author: Union[Unset, OrderAuthorEnum] = UNSET
    order_author_user: Union[None, UUID, Unset] = UNSET
    order_author_user_uuid: Union[None, UUID, Unset] = UNSET
    order_author_user_name: Union[None, Unset, str] = UNSET
    carry_over_drafts: Union[Unset, bool] = UNSET
    coi_declaration_text: Union[Unset, str] = UNSET
    undecided_at_round_completion: Union[Unset, UndecidedAtRoundCompletionEnum] = UNSET
    adoption_required: Union[Unset, bool] = UNSET
    budget_enforcement: Union[Unset, BudgetEnforcementEnum] = UNSET
    applicant_cc_roles: Union[Unset, list[str]] = UNSET
    target_decision_days: Union[None, Unset, int] = UNSET
    template_uuid: Union[None, UUID, Unset] = UNSET
    template_name: Union[None, Unset, str] = UNSET
    template_version: Union[None, Unset, int] = UNSET
    template_latest_version: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.call_applicant_visibility_config import CallApplicantVisibilityConfig
        from ..models.call_reviewer_eligibility import CallReviewerEligibility

        url = self.url

        uuid: Union[Unset, str] = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        slug = self.slug

        name = self.name

        description = self.description

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        manager = self.manager

        manager_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.manager_uuid, Unset):
            manager_uuid = str(self.manager_uuid)

        customer_name = self.customer_name

        customer_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.customer_uuid, Unset):
            customer_uuid = str(self.customer_uuid)

        offerings: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.offerings, Unset):
            offerings = []
            for offerings_item_data in self.offerings:
                offerings_item = offerings_item_data.to_dict()
                offerings.append(offerings_item)

        rounds: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rounds, Unset):
            rounds = []
            for rounds_item_data in self.rounds:
                rounds_item = rounds_item_data.to_dict()
                rounds.append(rounds_item)

        documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        resource_templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.resource_templates, Unset):
            resource_templates = []
            for resource_templates_item_data in self.resource_templates:
                resource_templates_item = resource_templates_item_data.to_dict()
                resource_templates.append(resource_templates_item)

        component_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.component_rules, Unset):
            component_rules = []
            for component_rules_item_data in self.component_rules:
                component_rules_item = component_rules_item_data.to_dict()
                component_rules.append(component_rules_item)

        fixed_duration_in_days: Union[None, Unset, int]
        if isinstance(self.fixed_duration_in_days, Unset):
            fixed_duration_in_days = UNSET
        else:
            fixed_duration_in_days = self.fixed_duration_in_days

        allowed_duration_months: Union[Unset, list[int]] = UNSET
        if not isinstance(self.allowed_duration_months, Unset):
            allowed_duration_months = self.allowed_duration_months

        max_prepaid_duration_months: Union[None, Unset, int]
        if isinstance(self.max_prepaid_duration_months, Unset):
            max_prepaid_duration_months = UNSET
        else:
            max_prepaid_duration_months = self.max_prepaid_duration_months

        backend_id = self.backend_id

        external_url: Union[None, Unset, str]
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        reviewer_identity_visible_to_submitters = self.reviewer_identity_visible_to_submitters

        reviews_visible_to_submitters = self.reviews_visible_to_submitters

        has_eligibility_restrictions = self.has_eligibility_restrictions

        proposal_field_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.proposal_field_config, Unset):
            proposal_field_config = self.proposal_field_config.to_dict()

        evaluation_start: Union[Unset, str] = UNSET
        if not isinstance(self.evaluation_start, Unset):
            evaluation_start = self.evaluation_start.value

        publish_results: Union[Unset, str] = UNSET
        if not isinstance(self.publish_results, Unset):
            publish_results = self.publish_results.value

        resource_template_selection_mode: Union[Unset, str] = UNSET
        if not isinstance(self.resource_template_selection_mode, Unset):
            resource_template_selection_mode = self.resource_template_selection_mode.value

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        reference_code = self.reference_code

        compliance_checklist: Union[None, Unset, str]
        if isinstance(self.compliance_checklist, Unset):
            compliance_checklist = UNSET
        elif isinstance(self.compliance_checklist, UUID):
            compliance_checklist = str(self.compliance_checklist)
        else:
            compliance_checklist = self.compliance_checklist

        compliance_checklist_name = self.compliance_checklist_name

        panel_chair: Union[None, Unset, str]
        if isinstance(self.panel_chair, Unset):
            panel_chair = UNSET
        elif isinstance(self.panel_chair, UUID):
            panel_chair = str(self.panel_chair)
        else:
            panel_chair = self.panel_chair

        panel_chair_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.panel_chair_uuid, Unset):
            panel_chair_uuid = str(self.panel_chair_uuid)

        panel_chair_name = self.panel_chair_name

        panel_vice_chair: Union[None, Unset, str]
        if isinstance(self.panel_vice_chair, Unset):
            panel_vice_chair = UNSET
        elif isinstance(self.panel_vice_chair, UUID):
            panel_vice_chair = str(self.panel_vice_chair)
        else:
            panel_vice_chair = self.panel_vice_chair

        panel_vice_chair_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.panel_vice_chair_uuid, Unset):
            panel_vice_chair_uuid = str(self.panel_vice_chair_uuid)

        panel_vice_chair_name = self.panel_vice_chair_name

        proposal_slug_template: Union[None, Unset, str]
        if isinstance(self.proposal_slug_template, Unset):
            proposal_slug_template = UNSET
        else:
            proposal_slug_template = self.proposal_slug_template

        user_email_patterns: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_email_patterns, Unset):
            user_email_patterns = self.user_email_patterns

        user_affiliations: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_affiliations, Unset):
            user_affiliations = self.user_affiliations

        user_identity_sources: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_identity_sources, Unset):
            user_identity_sources = self.user_identity_sources

        user_nationalities: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_nationalities, Unset):
            user_nationalities = self.user_nationalities

        user_organization_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_organization_types, Unset):
            user_organization_types = self.user_organization_types

        user_assurance_levels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_assurance_levels, Unset):
            user_assurance_levels = self.user_assurance_levels

        applicant_visibility_config: Union[None, Unset, dict[str, Any]]
        if isinstance(self.applicant_visibility_config, Unset):
            applicant_visibility_config = UNSET
        elif isinstance(self.applicant_visibility_config, CallApplicantVisibilityConfig):
            applicant_visibility_config = self.applicant_visibility_config.to_dict()
        else:
            applicant_visibility_config = self.applicant_visibility_config

        reviewer_eligibility: Union[None, Unset, dict[str, Any]]
        if isinstance(self.reviewer_eligibility, Unset):
            reviewer_eligibility = UNSET
        elif isinstance(self.reviewer_eligibility, CallReviewerEligibility):
            reviewer_eligibility = self.reviewer_eligibility.to_dict()
        else:
            reviewer_eligibility = self.reviewer_eligibility

        proposal_field_metadata: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.proposal_field_metadata, Unset):
            proposal_field_metadata = []
            for proposal_field_metadata_item_data in self.proposal_field_metadata:
                proposal_field_metadata_item = proposal_field_metadata_item_data.to_dict()
                proposal_field_metadata.append(proposal_field_metadata_item)

        has_proposals = self.has_proposals

        order_author: Union[Unset, str] = UNSET
        if not isinstance(self.order_author, Unset):
            order_author = self.order_author.value

        order_author_user: Union[None, Unset, str]
        if isinstance(self.order_author_user, Unset):
            order_author_user = UNSET
        elif isinstance(self.order_author_user, UUID):
            order_author_user = str(self.order_author_user)
        else:
            order_author_user = self.order_author_user

        order_author_user_uuid: Union[None, Unset, str]
        if isinstance(self.order_author_user_uuid, Unset):
            order_author_user_uuid = UNSET
        elif isinstance(self.order_author_user_uuid, UUID):
            order_author_user_uuid = str(self.order_author_user_uuid)
        else:
            order_author_user_uuid = self.order_author_user_uuid

        order_author_user_name: Union[None, Unset, str]
        if isinstance(self.order_author_user_name, Unset):
            order_author_user_name = UNSET
        else:
            order_author_user_name = self.order_author_user_name

        carry_over_drafts = self.carry_over_drafts

        coi_declaration_text = self.coi_declaration_text

        undecided_at_round_completion: Union[Unset, str] = UNSET
        if not isinstance(self.undecided_at_round_completion, Unset):
            undecided_at_round_completion = self.undecided_at_round_completion.value

        adoption_required = self.adoption_required

        budget_enforcement: Union[Unset, str] = UNSET
        if not isinstance(self.budget_enforcement, Unset):
            budget_enforcement = self.budget_enforcement.value

        applicant_cc_roles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.applicant_cc_roles, Unset):
            applicant_cc_roles = self.applicant_cc_roles

        target_decision_days: Union[None, Unset, int]
        if isinstance(self.target_decision_days, Unset):
            target_decision_days = UNSET
        else:
            target_decision_days = self.target_decision_days

        template_uuid: Union[None, Unset, str]
        if isinstance(self.template_uuid, Unset):
            template_uuid = UNSET
        elif isinstance(self.template_uuid, UUID):
            template_uuid = str(self.template_uuid)
        else:
            template_uuid = self.template_uuid

        template_name: Union[None, Unset, str]
        if isinstance(self.template_name, Unset):
            template_name = UNSET
        else:
            template_name = self.template_name

        template_version: Union[None, Unset, int]
        if isinstance(self.template_version, Unset):
            template_version = UNSET
        else:
            template_version = self.template_version

        template_latest_version: Union[None, Unset, int]
        if isinstance(self.template_latest_version, Unset):
            template_latest_version = UNSET
        else:
            template_latest_version = self.template_latest_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if created is not UNSET:
            field_dict["created"] = created
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if state is not UNSET:
            field_dict["state"] = state
        if manager is not UNSET:
            field_dict["manager"] = manager
        if manager_uuid is not UNSET:
            field_dict["manager_uuid"] = manager_uuid
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name
        if customer_uuid is not UNSET:
            field_dict["customer_uuid"] = customer_uuid
        if offerings is not UNSET:
            field_dict["offerings"] = offerings
        if rounds is not UNSET:
            field_dict["rounds"] = rounds
        if documents is not UNSET:
            field_dict["documents"] = documents
        if resource_templates is not UNSET:
            field_dict["resource_templates"] = resource_templates
        if component_rules is not UNSET:
            field_dict["component_rules"] = component_rules
        if fixed_duration_in_days is not UNSET:
            field_dict["fixed_duration_in_days"] = fixed_duration_in_days
        if allowed_duration_months is not UNSET:
            field_dict["allowed_duration_months"] = allowed_duration_months
        if max_prepaid_duration_months is not UNSET:
            field_dict["max_prepaid_duration_months"] = max_prepaid_duration_months
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if reviewer_identity_visible_to_submitters is not UNSET:
            field_dict["reviewer_identity_visible_to_submitters"] = reviewer_identity_visible_to_submitters
        if reviews_visible_to_submitters is not UNSET:
            field_dict["reviews_visible_to_submitters"] = reviews_visible_to_submitters
        if has_eligibility_restrictions is not UNSET:
            field_dict["has_eligibility_restrictions"] = has_eligibility_restrictions
        if proposal_field_config is not UNSET:
            field_dict["proposal_field_config"] = proposal_field_config
        if evaluation_start is not UNSET:
            field_dict["evaluation_start"] = evaluation_start
        if publish_results is not UNSET:
            field_dict["publish_results"] = publish_results
        if resource_template_selection_mode is not UNSET:
            field_dict["resource_template_selection_mode"] = resource_template_selection_mode
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if reference_code is not UNSET:
            field_dict["reference_code"] = reference_code
        if compliance_checklist is not UNSET:
            field_dict["compliance_checklist"] = compliance_checklist
        if compliance_checklist_name is not UNSET:
            field_dict["compliance_checklist_name"] = compliance_checklist_name
        if panel_chair is not UNSET:
            field_dict["panel_chair"] = panel_chair
        if panel_chair_uuid is not UNSET:
            field_dict["panel_chair_uuid"] = panel_chair_uuid
        if panel_chair_name is not UNSET:
            field_dict["panel_chair_name"] = panel_chair_name
        if panel_vice_chair is not UNSET:
            field_dict["panel_vice_chair"] = panel_vice_chair
        if panel_vice_chair_uuid is not UNSET:
            field_dict["panel_vice_chair_uuid"] = panel_vice_chair_uuid
        if panel_vice_chair_name is not UNSET:
            field_dict["panel_vice_chair_name"] = panel_vice_chair_name
        if proposal_slug_template is not UNSET:
            field_dict["proposal_slug_template"] = proposal_slug_template
        if user_email_patterns is not UNSET:
            field_dict["user_email_patterns"] = user_email_patterns
        if user_affiliations is not UNSET:
            field_dict["user_affiliations"] = user_affiliations
        if user_identity_sources is not UNSET:
            field_dict["user_identity_sources"] = user_identity_sources
        if user_nationalities is not UNSET:
            field_dict["user_nationalities"] = user_nationalities
        if user_organization_types is not UNSET:
            field_dict["user_organization_types"] = user_organization_types
        if user_assurance_levels is not UNSET:
            field_dict["user_assurance_levels"] = user_assurance_levels
        if applicant_visibility_config is not UNSET:
            field_dict["applicant_visibility_config"] = applicant_visibility_config
        if reviewer_eligibility is not UNSET:
            field_dict["reviewer_eligibility"] = reviewer_eligibility
        if proposal_field_metadata is not UNSET:
            field_dict["proposal_field_metadata"] = proposal_field_metadata
        if has_proposals is not UNSET:
            field_dict["has_proposals"] = has_proposals
        if order_author is not UNSET:
            field_dict["order_author"] = order_author
        if order_author_user is not UNSET:
            field_dict["order_author_user"] = order_author_user
        if order_author_user_uuid is not UNSET:
            field_dict["order_author_user_uuid"] = order_author_user_uuid
        if order_author_user_name is not UNSET:
            field_dict["order_author_user_name"] = order_author_user_name
        if carry_over_drafts is not UNSET:
            field_dict["carry_over_drafts"] = carry_over_drafts
        if coi_declaration_text is not UNSET:
            field_dict["coi_declaration_text"] = coi_declaration_text
        if undecided_at_round_completion is not UNSET:
            field_dict["undecided_at_round_completion"] = undecided_at_round_completion
        if adoption_required is not UNSET:
            field_dict["adoption_required"] = adoption_required
        if budget_enforcement is not UNSET:
            field_dict["budget_enforcement"] = budget_enforcement
        if applicant_cc_roles is not UNSET:
            field_dict["applicant_cc_roles"] = applicant_cc_roles
        if target_decision_days is not UNSET:
            field_dict["target_decision_days"] = target_decision_days
        if template_uuid is not UNSET:
            field_dict["template_uuid"] = template_uuid
        if template_name is not UNSET:
            field_dict["template_name"] = template_name
        if template_version is not UNSET:
            field_dict["template_version"] = template_version
        if template_latest_version is not UNSET:
            field_dict["template_latest_version"] = template_latest_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.call_applicant_visibility_config import CallApplicantVisibilityConfig
        from ..models.call_document import CallDocument
        from ..models.call_offering_component_bounds import CallOfferingComponentBounds
        from ..models.call_proposal_field_config import CallProposalFieldConfig
        from ..models.call_resource_template import CallResourceTemplate
        from ..models.call_reviewer_eligibility import CallReviewerEligibility
        from ..models.nested_requested_offering import NestedRequestedOffering
        from ..models.nested_round import NestedRound
        from ..models.proposal_field_metadata import ProposalFieldMetadata

        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: Union[Unset, UUID]
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, CallStates]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CallStates(_state)

        manager = d.pop("manager", UNSET)

        _manager_uuid = d.pop("manager_uuid", UNSET)
        manager_uuid: Union[Unset, UUID]
        if isinstance(_manager_uuid, Unset):
            manager_uuid = UNSET
        else:
            manager_uuid = UUID(_manager_uuid)

        customer_name = d.pop("customer_name", UNSET)

        _customer_uuid = d.pop("customer_uuid", UNSET)
        customer_uuid: Union[Unset, UUID]
        if isinstance(_customer_uuid, Unset):
            customer_uuid = UNSET
        else:
            customer_uuid = UUID(_customer_uuid)

        offerings = []
        _offerings = d.pop("offerings", UNSET)
        for offerings_item_data in _offerings or []:
            offerings_item = NestedRequestedOffering.from_dict(offerings_item_data)

            offerings.append(offerings_item)

        rounds = []
        _rounds = d.pop("rounds", UNSET)
        for rounds_item_data in _rounds or []:
            rounds_item = NestedRound.from_dict(rounds_item_data)

            rounds.append(rounds_item)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = CallDocument.from_dict(documents_item_data)

            documents.append(documents_item)

        resource_templates = []
        _resource_templates = d.pop("resource_templates", UNSET)
        for resource_templates_item_data in _resource_templates or []:
            resource_templates_item = CallResourceTemplate.from_dict(resource_templates_item_data)

            resource_templates.append(resource_templates_item)

        component_rules = []
        _component_rules = d.pop("component_rules", UNSET)
        for component_rules_item_data in _component_rules or []:
            component_rules_item = CallOfferingComponentBounds.from_dict(component_rules_item_data)

            component_rules.append(component_rules_item)

        def _parse_fixed_duration_in_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fixed_duration_in_days = _parse_fixed_duration_in_days(d.pop("fixed_duration_in_days", UNSET))

        allowed_duration_months = cast(list[int], d.pop("allowed_duration_months", UNSET))

        def _parse_max_prepaid_duration_months(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_prepaid_duration_months = _parse_max_prepaid_duration_months(d.pop("max_prepaid_duration_months", UNSET))

        backend_id = d.pop("backend_id", UNSET)

        def _parse_external_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        reviewer_identity_visible_to_submitters = d.pop("reviewer_identity_visible_to_submitters", UNSET)

        reviews_visible_to_submitters = d.pop("reviews_visible_to_submitters", UNSET)

        has_eligibility_restrictions = d.pop("has_eligibility_restrictions", UNSET)

        _proposal_field_config = d.pop("proposal_field_config", UNSET)
        proposal_field_config: Union[Unset, CallProposalFieldConfig]
        if isinstance(_proposal_field_config, Unset):
            proposal_field_config = UNSET
        else:
            proposal_field_config = CallProposalFieldConfig.from_dict(_proposal_field_config)

        _evaluation_start = d.pop("evaluation_start", UNSET)
        evaluation_start: Union[Unset, EvaluationStartEnum]
        if isinstance(_evaluation_start, Unset):
            evaluation_start = UNSET
        else:
            evaluation_start = EvaluationStartEnum(_evaluation_start)

        _publish_results = d.pop("publish_results", UNSET)
        publish_results: Union[Unset, PublishResultsEnum]
        if isinstance(_publish_results, Unset):
            publish_results = UNSET
        else:
            publish_results = PublishResultsEnum(_publish_results)

        _resource_template_selection_mode = d.pop("resource_template_selection_mode", UNSET)
        resource_template_selection_mode: Union[Unset, ResourceTemplateSelectionModeEnum]
        if isinstance(_resource_template_selection_mode, Unset):
            resource_template_selection_mode = UNSET
        else:
            resource_template_selection_mode = ResourceTemplateSelectionModeEnum(_resource_template_selection_mode)

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        reference_code = d.pop("reference_code", UNSET)

        def _parse_compliance_checklist(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                compliance_checklist_type_0 = UUID(data)

                return compliance_checklist_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        compliance_checklist = _parse_compliance_checklist(d.pop("compliance_checklist", UNSET))

        compliance_checklist_name = d.pop("compliance_checklist_name", UNSET)

        def _parse_panel_chair(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                panel_chair_type_0 = UUID(data)

                return panel_chair_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        panel_chair = _parse_panel_chair(d.pop("panel_chair", UNSET))

        _panel_chair_uuid = d.pop("panel_chair_uuid", UNSET)
        panel_chair_uuid: Union[Unset, UUID]
        if isinstance(_panel_chair_uuid, Unset):
            panel_chair_uuid = UNSET
        else:
            panel_chair_uuid = UUID(_panel_chair_uuid)

        panel_chair_name = d.pop("panel_chair_name", UNSET)

        def _parse_panel_vice_chair(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                panel_vice_chair_type_0 = UUID(data)

                return panel_vice_chair_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        panel_vice_chair = _parse_panel_vice_chair(d.pop("panel_vice_chair", UNSET))

        _panel_vice_chair_uuid = d.pop("panel_vice_chair_uuid", UNSET)
        panel_vice_chair_uuid: Union[Unset, UUID]
        if isinstance(_panel_vice_chair_uuid, Unset):
            panel_vice_chair_uuid = UNSET
        else:
            panel_vice_chair_uuid = UUID(_panel_vice_chair_uuid)

        panel_vice_chair_name = d.pop("panel_vice_chair_name", UNSET)

        def _parse_proposal_slug_template(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        proposal_slug_template = _parse_proposal_slug_template(d.pop("proposal_slug_template", UNSET))

        user_email_patterns = cast(list[str], d.pop("user_email_patterns", UNSET))

        user_affiliations = cast(list[str], d.pop("user_affiliations", UNSET))

        user_identity_sources = cast(list[str], d.pop("user_identity_sources", UNSET))

        user_nationalities = cast(list[str], d.pop("user_nationalities", UNSET))

        user_organization_types = cast(list[str], d.pop("user_organization_types", UNSET))

        user_assurance_levels = cast(list[str], d.pop("user_assurance_levels", UNSET))

        def _parse_applicant_visibility_config(data: object) -> Union["CallApplicantVisibilityConfig", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                applicant_visibility_config_type_1 = CallApplicantVisibilityConfig.from_dict(data)

                return applicant_visibility_config_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CallApplicantVisibilityConfig", None, Unset], data)

        applicant_visibility_config = _parse_applicant_visibility_config(d.pop("applicant_visibility_config", UNSET))

        def _parse_reviewer_eligibility(data: object) -> Union["CallReviewerEligibility", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reviewer_eligibility_type_1 = CallReviewerEligibility.from_dict(data)

                return reviewer_eligibility_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CallReviewerEligibility", None, Unset], data)

        reviewer_eligibility = _parse_reviewer_eligibility(d.pop("reviewer_eligibility", UNSET))

        proposal_field_metadata = []
        _proposal_field_metadata = d.pop("proposal_field_metadata", UNSET)
        for proposal_field_metadata_item_data in _proposal_field_metadata or []:
            proposal_field_metadata_item = ProposalFieldMetadata.from_dict(proposal_field_metadata_item_data)

            proposal_field_metadata.append(proposal_field_metadata_item)

        has_proposals = d.pop("has_proposals", UNSET)

        _order_author = d.pop("order_author", UNSET)
        order_author: Union[Unset, OrderAuthorEnum]
        if isinstance(_order_author, Unset):
            order_author = UNSET
        else:
            order_author = OrderAuthorEnum(_order_author)

        def _parse_order_author_user(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_author_user_type_0 = UUID(data)

                return order_author_user_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        order_author_user = _parse_order_author_user(d.pop("order_author_user", UNSET))

        def _parse_order_author_user_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_author_user_uuid_type_0 = UUID(data)

                return order_author_user_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        order_author_user_uuid = _parse_order_author_user_uuid(d.pop("order_author_user_uuid", UNSET))

        def _parse_order_author_user_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        order_author_user_name = _parse_order_author_user_name(d.pop("order_author_user_name", UNSET))

        carry_over_drafts = d.pop("carry_over_drafts", UNSET)

        coi_declaration_text = d.pop("coi_declaration_text", UNSET)

        _undecided_at_round_completion = d.pop("undecided_at_round_completion", UNSET)
        undecided_at_round_completion: Union[Unset, UndecidedAtRoundCompletionEnum]
        if isinstance(_undecided_at_round_completion, Unset):
            undecided_at_round_completion = UNSET
        else:
            undecided_at_round_completion = UndecidedAtRoundCompletionEnum(_undecided_at_round_completion)

        adoption_required = d.pop("adoption_required", UNSET)

        _budget_enforcement = d.pop("budget_enforcement", UNSET)
        budget_enforcement: Union[Unset, BudgetEnforcementEnum]
        if isinstance(_budget_enforcement, Unset):
            budget_enforcement = UNSET
        else:
            budget_enforcement = BudgetEnforcementEnum(_budget_enforcement)

        applicant_cc_roles = cast(list[str], d.pop("applicant_cc_roles", UNSET))

        def _parse_target_decision_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        target_decision_days = _parse_target_decision_days(d.pop("target_decision_days", UNSET))

        def _parse_template_uuid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                template_uuid_type_0 = UUID(data)

                return template_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        template_uuid = _parse_template_uuid(d.pop("template_uuid", UNSET))

        def _parse_template_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        template_name = _parse_template_name(d.pop("template_name", UNSET))

        def _parse_template_version(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        template_version = _parse_template_version(d.pop("template_version", UNSET))

        def _parse_template_latest_version(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        template_latest_version = _parse_template_latest_version(d.pop("template_latest_version", UNSET))

        protected_call = cls(
            url=url,
            uuid=uuid,
            created=created,
            start_date=start_date,
            end_date=end_date,
            slug=slug,
            name=name,
            description=description,
            state=state,
            manager=manager,
            manager_uuid=manager_uuid,
            customer_name=customer_name,
            customer_uuid=customer_uuid,
            offerings=offerings,
            rounds=rounds,
            documents=documents,
            resource_templates=resource_templates,
            component_rules=component_rules,
            fixed_duration_in_days=fixed_duration_in_days,
            allowed_duration_months=allowed_duration_months,
            max_prepaid_duration_months=max_prepaid_duration_months,
            backend_id=backend_id,
            external_url=external_url,
            reviewer_identity_visible_to_submitters=reviewer_identity_visible_to_submitters,
            reviews_visible_to_submitters=reviews_visible_to_submitters,
            has_eligibility_restrictions=has_eligibility_restrictions,
            proposal_field_config=proposal_field_config,
            evaluation_start=evaluation_start,
            publish_results=publish_results,
            resource_template_selection_mode=resource_template_selection_mode,
            created_by=created_by,
            reference_code=reference_code,
            compliance_checklist=compliance_checklist,
            compliance_checklist_name=compliance_checklist_name,
            panel_chair=panel_chair,
            panel_chair_uuid=panel_chair_uuid,
            panel_chair_name=panel_chair_name,
            panel_vice_chair=panel_vice_chair,
            panel_vice_chair_uuid=panel_vice_chair_uuid,
            panel_vice_chair_name=panel_vice_chair_name,
            proposal_slug_template=proposal_slug_template,
            user_email_patterns=user_email_patterns,
            user_affiliations=user_affiliations,
            user_identity_sources=user_identity_sources,
            user_nationalities=user_nationalities,
            user_organization_types=user_organization_types,
            user_assurance_levels=user_assurance_levels,
            applicant_visibility_config=applicant_visibility_config,
            reviewer_eligibility=reviewer_eligibility,
            proposal_field_metadata=proposal_field_metadata,
            has_proposals=has_proposals,
            order_author=order_author,
            order_author_user=order_author_user,
            order_author_user_uuid=order_author_user_uuid,
            order_author_user_name=order_author_user_name,
            carry_over_drafts=carry_over_drafts,
            coi_declaration_text=coi_declaration_text,
            undecided_at_round_completion=undecided_at_round_completion,
            adoption_required=adoption_required,
            budget_enforcement=budget_enforcement,
            applicant_cc_roles=applicant_cc_roles,
            target_decision_days=target_decision_days,
            template_uuid=template_uuid,
            template_name=template_name,
            template_version=template_version,
            template_latest_version=template_latest_version,
        )

        protected_call.additional_properties = d
        return protected_call

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
