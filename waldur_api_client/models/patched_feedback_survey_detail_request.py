import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.broadcast_message_query_request import BroadcastMessageQueryRequest
    from ..models.survey_question_request import SurveyQuestionRequest


T = TypeVar("T", bound="PatchedFeedbackSurveyDetailRequest")


@_attrs_define
class PatchedFeedbackSurveyDetailRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        intro (Union[Unset, str]): Markdown text shown above the questions.
        starts_at (Union[Unset, datetime.datetime]):
        ends_at (Union[Unset, datetime.datetime]):
        is_active (Union[Unset, bool]):
        audience_query (Union[Unset, BroadcastMessageQueryRequest]):
        max_prompts (Union[Unset, int]): How many times a user is prompted at most.
        snooze_days (Union[Unset, int]): Days the prompt stays hidden after it is shown or postponed.
        questions (Union[Unset, list['SurveyQuestionRequest']]):
    """

    name: Union[Unset, str] = UNSET
    intro: Union[Unset, str] = UNSET
    starts_at: Union[Unset, datetime.datetime] = UNSET
    ends_at: Union[Unset, datetime.datetime] = UNSET
    is_active: Union[Unset, bool] = UNSET
    audience_query: Union[Unset, "BroadcastMessageQueryRequest"] = UNSET
    max_prompts: Union[Unset, int] = UNSET
    snooze_days: Union[Unset, int] = UNSET
    questions: Union[Unset, list["SurveyQuestionRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        intro = self.intro

        starts_at: Union[Unset, str] = UNSET
        if not isinstance(self.starts_at, Unset):
            starts_at = self.starts_at.isoformat()

        ends_at: Union[Unset, str] = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.isoformat()

        is_active = self.is_active

        audience_query: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.audience_query, Unset):
            audience_query = self.audience_query.to_dict()

        max_prompts = self.max_prompts

        snooze_days = self.snooze_days

        questions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.questions, Unset):
            questions = []
            for questions_item_data in self.questions:
                questions_item = questions_item_data.to_dict()
                questions.append(questions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if intro is not UNSET:
            field_dict["intro"] = intro
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if audience_query is not UNSET:
            field_dict["audience_query"] = audience_query
        if max_prompts is not UNSET:
            field_dict["max_prompts"] = max_prompts
        if snooze_days is not UNSET:
            field_dict["snooze_days"] = snooze_days
        if questions is not UNSET:
            field_dict["questions"] = questions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_message_query_request import BroadcastMessageQueryRequest
        from ..models.survey_question_request import SurveyQuestionRequest

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        intro = d.pop("intro", UNSET)

        _starts_at = d.pop("starts_at", UNSET)
        starts_at: Union[Unset, datetime.datetime]
        if isinstance(_starts_at, Unset):
            starts_at = UNSET
        else:
            starts_at = isoparse(_starts_at)

        _ends_at = d.pop("ends_at", UNSET)
        ends_at: Union[Unset, datetime.datetime]
        if isinstance(_ends_at, Unset):
            ends_at = UNSET
        else:
            ends_at = isoparse(_ends_at)

        is_active = d.pop("is_active", UNSET)

        _audience_query = d.pop("audience_query", UNSET)
        audience_query: Union[Unset, BroadcastMessageQueryRequest]
        if isinstance(_audience_query, Unset):
            audience_query = UNSET
        else:
            audience_query = BroadcastMessageQueryRequest.from_dict(_audience_query)

        max_prompts = d.pop("max_prompts", UNSET)

        snooze_days = d.pop("snooze_days", UNSET)

        questions = []
        _questions = d.pop("questions", UNSET)
        for questions_item_data in _questions or []:
            questions_item = SurveyQuestionRequest.from_dict(questions_item_data)

            questions.append(questions_item)

        patched_feedback_survey_detail_request = cls(
            name=name,
            intro=intro,
            starts_at=starts_at,
            ends_at=ends_at,
            is_active=is_active,
            audience_query=audience_query,
            max_prompts=max_prompts,
            snooze_days=snooze_days,
            questions=questions,
        )

        patched_feedback_survey_detail_request.additional_properties = d
        return patched_feedback_survey_detail_request

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
