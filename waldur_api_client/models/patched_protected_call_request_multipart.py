import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.budget_enforcement_enum import BudgetEnforcementEnum
from ..models.evaluation_start_enum import EvaluationStartEnum
from ..models.order_author_enum import OrderAuthorEnum
from ..models.publish_results_enum import PublishResultsEnum
from ..models.resource_template_selection_mode_enum import ResourceTemplateSelectionModeEnum
from ..models.undecided_at_round_completion_enum import UndecidedAtRoundCompletionEnum
from ..types import UNSET, File, Unset

if TYPE_CHECKING:
    from ..models.call_applicant_visibility_config_request import CallApplicantVisibilityConfigRequest
    from ..models.call_proposal_field_config_request import CallProposalFieldConfigRequest
    from ..models.call_reviewer_eligibility_request import CallReviewerEligibilityRequest


T = TypeVar("T", bound="PatchedProtectedCallRequestMultipart")


@_attrs_define
class PatchedProtectedCallRequestMultipart:
    """
    Attributes:
        slug (Union[Unset, str]): URL-friendly identifier. Only editable by staff users.
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        image (Union[File, None, Unset]): Logo shown on the call's card in place of its initials. A PNG, JPEG or GIF of
            at most 2 MB; null or an empty value removes it.
        fixed_duration_in_days (Union[None, Unset, int]):
        allowed_duration_months (Union[Unset, list[int]]): Durations, in months, the applicant chooses the project's
            length from. Empty offers no choice. Cannot be combined with fixed_duration_in_days. Proposals already submitted
            keep the length they asked for.
        backend_id (Union[Unset, str]):
        external_url (Union[None, Unset, str]):
        reviewer_identity_visible_to_submitters (Union[Unset, bool]): Whether proposal applicants can see reviewer
            identities
        reviews_visible_to_submitters (Union[Unset, bool]): Whether proposal applicants can see review comments and
            scores. Applicants still see what an applicant step lists as its input steps, such as the reviews they respond
            to.
        proposal_field_config (Union[Unset, CallProposalFieldConfigRequest]):
        evaluation_start (Union[Unset, EvaluationStartEnum]):
        publish_results (Union[Unset, PublishResultsEnum]):
        resource_template_selection_mode (Union[Unset, ResourceTemplateSelectionModeEnum]):
        project_name_template (Union[None, Unset, str]): Name given to the project an accepted proposal creates.
            Placeholders: {proposal_name}, {proposal_slug}, {call_prefix}, {call_slug}, {call_name}, {round_start},
            {round_slug}, {org_slug}, {year}. Empty means {call_prefix} - {round_start} - {proposal_name}.
        created_by (Union[None, Unset, str]):
        reference_code (Union[Unset, str]):
        compliance_checklist (Union[None, UUID, Unset]): Compliance checklist that proposals must complete before
            submission
        panel_chair (Union[None, UUID, Unset]):
        panel_vice_chair (Union[None, UUID, Unset]):
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
        applicant_visibility_config (Union['CallApplicantVisibilityConfigRequest', None, Unset]):
        reviewer_eligibility (Union['CallReviewerEligibilityRequest', None, Unset]): Who may review for the call:
            checked when a reviewer is invited, accepts, is suggested or is given the call's reviewer role. Kept apart from
            the restrictions on applicants.
        order_author (Union[Unset, OrderAuthorEnum]):
        order_author_user (Union[None, UUID, Unset]): The person orders are attributed to when the author is a named
            contact. Must hold a role on this call or on the organization managing it.
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
    """

    slug: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    image: Union[File, None, Unset] = UNSET
    fixed_duration_in_days: Union[None, Unset, int] = UNSET
    allowed_duration_months: Union[Unset, list[int]] = UNSET
    backend_id: Union[Unset, str] = UNSET
    external_url: Union[None, Unset, str] = UNSET
    reviewer_identity_visible_to_submitters: Union[Unset, bool] = UNSET
    reviews_visible_to_submitters: Union[Unset, bool] = UNSET
    proposal_field_config: Union[Unset, "CallProposalFieldConfigRequest"] = UNSET
    evaluation_start: Union[Unset, EvaluationStartEnum] = UNSET
    publish_results: Union[Unset, PublishResultsEnum] = UNSET
    resource_template_selection_mode: Union[Unset, ResourceTemplateSelectionModeEnum] = UNSET
    project_name_template: Union[None, Unset, str] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    reference_code: Union[Unset, str] = UNSET
    compliance_checklist: Union[None, UUID, Unset] = UNSET
    panel_chair: Union[None, UUID, Unset] = UNSET
    panel_vice_chair: Union[None, UUID, Unset] = UNSET
    proposal_slug_template: Union[None, Unset, str] = UNSET
    user_email_patterns: Union[Unset, list[str]] = UNSET
    user_affiliations: Union[Unset, list[str]] = UNSET
    user_identity_sources: Union[Unset, list[str]] = UNSET
    user_nationalities: Union[Unset, list[str]] = UNSET
    user_organization_types: Union[Unset, list[str]] = UNSET
    user_assurance_levels: Union[Unset, list[str]] = UNSET
    applicant_visibility_config: Union["CallApplicantVisibilityConfigRequest", None, Unset] = UNSET
    reviewer_eligibility: Union["CallReviewerEligibilityRequest", None, Unset] = UNSET
    order_author: Union[Unset, OrderAuthorEnum] = UNSET
    order_author_user: Union[None, UUID, Unset] = UNSET
    carry_over_drafts: Union[Unset, bool] = UNSET
    coi_declaration_text: Union[Unset, str] = UNSET
    undecided_at_round_completion: Union[Unset, UndecidedAtRoundCompletionEnum] = UNSET
    adoption_required: Union[Unset, bool] = UNSET
    budget_enforcement: Union[Unset, BudgetEnforcementEnum] = UNSET
    applicant_cc_roles: Union[Unset, list[str]] = UNSET
    target_decision_days: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.call_applicant_visibility_config_request import CallApplicantVisibilityConfigRequest
        from ..models.call_reviewer_eligibility_request import CallReviewerEligibilityRequest

        slug = self.slug

        name = self.name

        description = self.description

        image: Union[None, Unset, types.FileTypes]
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, File):
            image = self.image.to_tuple()

        else:
            image = self.image

        fixed_duration_in_days: Union[None, Unset, int]
        if isinstance(self.fixed_duration_in_days, Unset):
            fixed_duration_in_days = UNSET
        else:
            fixed_duration_in_days = self.fixed_duration_in_days

        allowed_duration_months: Union[Unset, list[int]] = UNSET
        if not isinstance(self.allowed_duration_months, Unset):
            allowed_duration_months = self.allowed_duration_months

        backend_id = self.backend_id

        external_url: Union[None, Unset, str]
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        reviewer_identity_visible_to_submitters = self.reviewer_identity_visible_to_submitters

        reviews_visible_to_submitters = self.reviews_visible_to_submitters

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

        project_name_template: Union[None, Unset, str]
        if isinstance(self.project_name_template, Unset):
            project_name_template = UNSET
        else:
            project_name_template = self.project_name_template

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

        panel_chair: Union[None, Unset, str]
        if isinstance(self.panel_chair, Unset):
            panel_chair = UNSET
        elif isinstance(self.panel_chair, UUID):
            panel_chair = str(self.panel_chair)
        else:
            panel_chair = self.panel_chair

        panel_vice_chair: Union[None, Unset, str]
        if isinstance(self.panel_vice_chair, Unset):
            panel_vice_chair = UNSET
        elif isinstance(self.panel_vice_chair, UUID):
            panel_vice_chair = str(self.panel_vice_chair)
        else:
            panel_vice_chair = self.panel_vice_chair

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
        elif isinstance(self.applicant_visibility_config, CallApplicantVisibilityConfigRequest):
            applicant_visibility_config = self.applicant_visibility_config.to_dict()
        else:
            applicant_visibility_config = self.applicant_visibility_config

        reviewer_eligibility: Union[None, Unset, dict[str, Any]]
        if isinstance(self.reviewer_eligibility, Unset):
            reviewer_eligibility = UNSET
        elif isinstance(self.reviewer_eligibility, CallReviewerEligibilityRequest):
            reviewer_eligibility = self.reviewer_eligibility.to_dict()
        else:
            reviewer_eligibility = self.reviewer_eligibility

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if image is not UNSET:
            field_dict["image"] = image
        if fixed_duration_in_days is not UNSET:
            field_dict["fixed_duration_in_days"] = fixed_duration_in_days
        if allowed_duration_months is not UNSET:
            field_dict["allowed_duration_months"] = allowed_duration_months
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if reviewer_identity_visible_to_submitters is not UNSET:
            field_dict["reviewer_identity_visible_to_submitters"] = reviewer_identity_visible_to_submitters
        if reviews_visible_to_submitters is not UNSET:
            field_dict["reviews_visible_to_submitters"] = reviews_visible_to_submitters
        if proposal_field_config is not UNSET:
            field_dict["proposal_field_config"] = proposal_field_config
        if evaluation_start is not UNSET:
            field_dict["evaluation_start"] = evaluation_start
        if publish_results is not UNSET:
            field_dict["publish_results"] = publish_results
        if resource_template_selection_mode is not UNSET:
            field_dict["resource_template_selection_mode"] = resource_template_selection_mode
        if project_name_template is not UNSET:
            field_dict["project_name_template"] = project_name_template
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if reference_code is not UNSET:
            field_dict["reference_code"] = reference_code
        if compliance_checklist is not UNSET:
            field_dict["compliance_checklist"] = compliance_checklist
        if panel_chair is not UNSET:
            field_dict["panel_chair"] = panel_chair
        if panel_vice_chair is not UNSET:
            field_dict["panel_vice_chair"] = panel_vice_chair
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
        if order_author is not UNSET:
            field_dict["order_author"] = order_author
        if order_author_user is not UNSET:
            field_dict["order_author_user"] = order_author_user
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

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.slug, Unset):
            files.append(("slug", (None, str(self.slug).encode(), "text/plain")))

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.image, Unset):
            if isinstance(self.image, File):
                files.append(("image", self.image.to_tuple()))
            else:
                files.append(("image", (None, str(self.image).encode(), "text/plain")))

        if not isinstance(self.fixed_duration_in_days, Unset):
            if isinstance(self.fixed_duration_in_days, int):
                files.append(
                    ("fixed_duration_in_days", (None, str(self.fixed_duration_in_days).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("fixed_duration_in_days", (None, str(self.fixed_duration_in_days).encode(), "text/plain"))
                )

        if not isinstance(self.allowed_duration_months, Unset):
            for allowed_duration_months_item_element in self.allowed_duration_months:
                files.append(
                    (
                        "allowed_duration_months",
                        (None, str(allowed_duration_months_item_element).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.backend_id, Unset):
            files.append(("backend_id", (None, str(self.backend_id).encode(), "text/plain")))

        if not isinstance(self.external_url, Unset):
            if isinstance(self.external_url, str):
                files.append(("external_url", (None, str(self.external_url).encode(), "text/plain")))
            else:
                files.append(("external_url", (None, str(self.external_url).encode(), "text/plain")))

        if not isinstance(self.reviewer_identity_visible_to_submitters, Unset):
            files.append(
                (
                    "reviewer_identity_visible_to_submitters",
                    (None, str(self.reviewer_identity_visible_to_submitters).encode(), "text/plain"),
                )
            )

        if not isinstance(self.reviews_visible_to_submitters, Unset):
            files.append(
                (
                    "reviews_visible_to_submitters",
                    (None, str(self.reviews_visible_to_submitters).encode(), "text/plain"),
                )
            )

        if not isinstance(self.proposal_field_config, Unset):
            files.append(
                (
                    "proposal_field_config",
                    (None, json.dumps(self.proposal_field_config.to_dict()).encode(), "application/json"),
                )
            )

        if not isinstance(self.evaluation_start, Unset):
            files.append(("evaluation_start", (None, str(self.evaluation_start.value).encode(), "text/plain")))

        if not isinstance(self.publish_results, Unset):
            files.append(("publish_results", (None, str(self.publish_results.value).encode(), "text/plain")))

        if not isinstance(self.resource_template_selection_mode, Unset):
            files.append(
                (
                    "resource_template_selection_mode",
                    (None, str(self.resource_template_selection_mode.value).encode(), "text/plain"),
                )
            )

        if not isinstance(self.project_name_template, Unset):
            if isinstance(self.project_name_template, str):
                files.append(("project_name_template", (None, str(self.project_name_template).encode(), "text/plain")))
            else:
                files.append(("project_name_template", (None, str(self.project_name_template).encode(), "text/plain")))

        if not isinstance(self.created_by, Unset):
            if isinstance(self.created_by, str):
                files.append(("created_by", (None, str(self.created_by).encode(), "text/plain")))
            else:
                files.append(("created_by", (None, str(self.created_by).encode(), "text/plain")))

        if not isinstance(self.reference_code, Unset):
            files.append(("reference_code", (None, str(self.reference_code).encode(), "text/plain")))

        if not isinstance(self.compliance_checklist, Unset):
            if isinstance(self.compliance_checklist, UUID):
                files.append(("compliance_checklist", (None, str(self.compliance_checklist), "text/plain")))
            else:
                files.append(("compliance_checklist", (None, str(self.compliance_checklist).encode(), "text/plain")))

        if not isinstance(self.panel_chair, Unset):
            if isinstance(self.panel_chair, UUID):
                files.append(("panel_chair", (None, str(self.panel_chair), "text/plain")))
            else:
                files.append(("panel_chair", (None, str(self.panel_chair).encode(), "text/plain")))

        if not isinstance(self.panel_vice_chair, Unset):
            if isinstance(self.panel_vice_chair, UUID):
                files.append(("panel_vice_chair", (None, str(self.panel_vice_chair), "text/plain")))
            else:
                files.append(("panel_vice_chair", (None, str(self.panel_vice_chair).encode(), "text/plain")))

        if not isinstance(self.proposal_slug_template, Unset):
            if isinstance(self.proposal_slug_template, str):
                files.append(
                    ("proposal_slug_template", (None, str(self.proposal_slug_template).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("proposal_slug_template", (None, str(self.proposal_slug_template).encode(), "text/plain"))
                )

        if not isinstance(self.user_email_patterns, Unset):
            for user_email_patterns_item_element in self.user_email_patterns:
                files.append(
                    ("user_email_patterns", (None, str(user_email_patterns_item_element).encode(), "text/plain"))
                )

        if not isinstance(self.user_affiliations, Unset):
            for user_affiliations_item_element in self.user_affiliations:
                files.append(("user_affiliations", (None, str(user_affiliations_item_element).encode(), "text/plain")))

        if not isinstance(self.user_identity_sources, Unset):
            for user_identity_sources_item_element in self.user_identity_sources:
                files.append(
                    ("user_identity_sources", (None, str(user_identity_sources_item_element).encode(), "text/plain"))
                )

        if not isinstance(self.user_nationalities, Unset):
            for user_nationalities_item_element in self.user_nationalities:
                files.append(
                    ("user_nationalities", (None, str(user_nationalities_item_element).encode(), "text/plain"))
                )

        if not isinstance(self.user_organization_types, Unset):
            for user_organization_types_item_element in self.user_organization_types:
                files.append(
                    (
                        "user_organization_types",
                        (None, str(user_organization_types_item_element).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.user_assurance_levels, Unset):
            for user_assurance_levels_item_element in self.user_assurance_levels:
                files.append(
                    ("user_assurance_levels", (None, str(user_assurance_levels_item_element).encode(), "text/plain"))
                )

        if not isinstance(self.applicant_visibility_config, Unset):
            if self.applicant_visibility_config is None:
                files.append(
                    (
                        "applicant_visibility_config",
                        (None, str(self.applicant_visibility_config).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "applicant_visibility_config",
                        (None, json.dumps(self.applicant_visibility_config.to_dict()).encode(), "application/json"),
                    )
                )

        if not isinstance(self.reviewer_eligibility, Unset):
            if self.reviewer_eligibility is None:
                files.append(("reviewer_eligibility", (None, str(self.reviewer_eligibility).encode(), "text/plain")))
            else:
                files.append(
                    (
                        "reviewer_eligibility",
                        (None, json.dumps(self.reviewer_eligibility.to_dict()).encode(), "application/json"),
                    )
                )

        if not isinstance(self.order_author, Unset):
            files.append(("order_author", (None, str(self.order_author.value).encode(), "text/plain")))

        if not isinstance(self.order_author_user, Unset):
            if isinstance(self.order_author_user, UUID):
                files.append(("order_author_user", (None, str(self.order_author_user), "text/plain")))
            else:
                files.append(("order_author_user", (None, str(self.order_author_user).encode(), "text/plain")))

        if not isinstance(self.carry_over_drafts, Unset):
            files.append(("carry_over_drafts", (None, str(self.carry_over_drafts).encode(), "text/plain")))

        if not isinstance(self.coi_declaration_text, Unset):
            files.append(("coi_declaration_text", (None, str(self.coi_declaration_text).encode(), "text/plain")))

        if not isinstance(self.undecided_at_round_completion, Unset):
            files.append(
                (
                    "undecided_at_round_completion",
                    (None, str(self.undecided_at_round_completion.value).encode(), "text/plain"),
                )
            )

        if not isinstance(self.adoption_required, Unset):
            files.append(("adoption_required", (None, str(self.adoption_required).encode(), "text/plain")))

        if not isinstance(self.budget_enforcement, Unset):
            files.append(("budget_enforcement", (None, str(self.budget_enforcement.value).encode(), "text/plain")))

        if not isinstance(self.applicant_cc_roles, Unset):
            for applicant_cc_roles_item_element in self.applicant_cc_roles:
                files.append(
                    ("applicant_cc_roles", (None, str(applicant_cc_roles_item_element).encode(), "text/plain"))
                )

        if not isinstance(self.target_decision_days, Unset):
            if isinstance(self.target_decision_days, int):
                files.append(("target_decision_days", (None, str(self.target_decision_days).encode(), "text/plain")))
            else:
                files.append(("target_decision_days", (None, str(self.target_decision_days).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.call_applicant_visibility_config_request import CallApplicantVisibilityConfigRequest
        from ..models.call_proposal_field_config_request import CallProposalFieldConfigRequest
        from ..models.call_reviewer_eligibility_request import CallReviewerEligibilityRequest

        d = dict(src_dict)
        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_image(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                image_type_0 = File(payload=BytesIO(data))

                return image_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_fixed_duration_in_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fixed_duration_in_days = _parse_fixed_duration_in_days(d.pop("fixed_duration_in_days", UNSET))

        allowed_duration_months = cast(list[int], d.pop("allowed_duration_months", UNSET))

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

        _proposal_field_config = d.pop("proposal_field_config", UNSET)
        proposal_field_config: Union[Unset, CallProposalFieldConfigRequest]
        if isinstance(_proposal_field_config, Unset):
            proposal_field_config = UNSET
        else:
            proposal_field_config = CallProposalFieldConfigRequest.from_dict(_proposal_field_config)

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

        def _parse_project_name_template(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        project_name_template = _parse_project_name_template(d.pop("project_name_template", UNSET))

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

        def _parse_applicant_visibility_config(
            data: object,
        ) -> Union["CallApplicantVisibilityConfigRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                applicant_visibility_config_type_1 = CallApplicantVisibilityConfigRequest.from_dict(data)

                return applicant_visibility_config_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CallApplicantVisibilityConfigRequest", None, Unset], data)

        applicant_visibility_config = _parse_applicant_visibility_config(d.pop("applicant_visibility_config", UNSET))

        def _parse_reviewer_eligibility(data: object) -> Union["CallReviewerEligibilityRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reviewer_eligibility_type_1 = CallReviewerEligibilityRequest.from_dict(data)

                return reviewer_eligibility_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CallReviewerEligibilityRequest", None, Unset], data)

        reviewer_eligibility = _parse_reviewer_eligibility(d.pop("reviewer_eligibility", UNSET))

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

        patched_protected_call_request_multipart = cls(
            slug=slug,
            name=name,
            description=description,
            image=image,
            fixed_duration_in_days=fixed_duration_in_days,
            allowed_duration_months=allowed_duration_months,
            backend_id=backend_id,
            external_url=external_url,
            reviewer_identity_visible_to_submitters=reviewer_identity_visible_to_submitters,
            reviews_visible_to_submitters=reviews_visible_to_submitters,
            proposal_field_config=proposal_field_config,
            evaluation_start=evaluation_start,
            publish_results=publish_results,
            resource_template_selection_mode=resource_template_selection_mode,
            project_name_template=project_name_template,
            created_by=created_by,
            reference_code=reference_code,
            compliance_checklist=compliance_checklist,
            panel_chair=panel_chair,
            panel_vice_chair=panel_vice_chair,
            proposal_slug_template=proposal_slug_template,
            user_email_patterns=user_email_patterns,
            user_affiliations=user_affiliations,
            user_identity_sources=user_identity_sources,
            user_nationalities=user_nationalities,
            user_organization_types=user_organization_types,
            user_assurance_levels=user_assurance_levels,
            applicant_visibility_config=applicant_visibility_config,
            reviewer_eligibility=reviewer_eligibility,
            order_author=order_author,
            order_author_user=order_author_user,
            carry_over_drafts=carry_over_drafts,
            coi_declaration_text=coi_declaration_text,
            undecided_at_round_completion=undecided_at_round_completion,
            adoption_required=adoption_required,
            budget_enforcement=budget_enforcement,
            applicant_cc_roles=applicant_cc_roles,
            target_decision_days=target_decision_days,
        )

        patched_protected_call_request_multipart.additional_properties = d
        return patched_protected_call_request_multipart

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
