from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.question_answer_project_answers_item import QuestionAnswerProjectAnswersItem


T = TypeVar("T", bound="QuestionAnswer")


@_attrs_define
class QuestionAnswer:
    """
    Attributes:
        question_uuid (UUID):
        question_description (str):
        question_type (str):
        required (bool):
        order (int):
        total_projects (int): Get total projects count.
        answered_projects_count (int): Get count of projects that answered this question.
        project_answers (list['QuestionAnswerProjectAnswersItem']): Get all project answers for this question.
    """

    question_uuid: UUID
    question_description: str
    question_type: str
    required: bool
    order: int
    total_projects: int
    answered_projects_count: int
    project_answers: list["QuestionAnswerProjectAnswersItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        question_uuid = str(self.question_uuid)

        question_description = self.question_description

        question_type = self.question_type

        required = self.required

        order = self.order

        total_projects = self.total_projects

        answered_projects_count = self.answered_projects_count

        project_answers = []
        for project_answers_item_data in self.project_answers:
            project_answers_item = project_answers_item_data.to_dict()
            project_answers.append(project_answers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "question_uuid": question_uuid,
                "question_description": question_description,
                "question_type": question_type,
                "required": required,
                "order": order,
                "total_projects": total_projects,
                "answered_projects_count": answered_projects_count,
                "project_answers": project_answers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.question_answer_project_answers_item import QuestionAnswerProjectAnswersItem

        d = dict(src_dict)
        question_uuid = UUID(d.pop("question_uuid"))

        question_description = d.pop("question_description")

        question_type = d.pop("question_type")

        required = d.pop("required")

        order = d.pop("order")

        total_projects = d.pop("total_projects")

        answered_projects_count = d.pop("answered_projects_count")

        project_answers = []
        _project_answers = d.pop("project_answers")
        for project_answers_item_data in _project_answers:
            project_answers_item = QuestionAnswerProjectAnswersItem.from_dict(project_answers_item_data)

            project_answers.append(project_answers_item)

        question_answer = cls(
            question_uuid=question_uuid,
            question_description=question_description,
            question_type=question_type,
            required=required,
            order=order,
            total_projects=total_projects,
            answered_projects_count=answered_projects_count,
            project_answers=project_answers,
        )

        question_answer.additional_properties = d
        return question_answer

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
