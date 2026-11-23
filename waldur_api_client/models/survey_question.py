from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dependency_logic_operator_enum import DependencyLogicOperatorEnum
from ..models.likert_scale_length_enum import LikertScaleLengthEnum
from ..models.rich_text_toolbar_level_enum import RichTextToolbarLevelEnum
from ..models.survey_question_type_enum import SurveyQuestionTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.survey_question_condition import SurveyQuestionCondition
    from ..models.survey_question_option import SurveyQuestionOption


T = TypeVar("T", bound="SurveyQuestion")


@_attrs_define
class SurveyQuestion:
    """
    Attributes:
        key (str):
        description (str):
        question_type (SurveyQuestionTypeEnum):
        required (Union[Unset, bool]):  Default: False.
        user_guidance (Union[Unset, str]):  Default: ''.
        min_value (Union[None, Unset, str]):
        max_value (Union[None, Unset, str]):
        likert_scale_length (Union[LikertScaleLengthEnum, None, Unset]):
        likert_low_label (Union[Unset, str]):
        likert_high_label (Union[Unset, str]):
        likert_allow_na (Union[Unset, bool]):
        rich_text_char_limit (Union[None, Unset, int]):
        rich_text_toolbar_level (Union[Unset, RichTextToolbarLevelEnum]):
        dependency_logic_operator (Union[Unset, DependencyLogicOperatorEnum]):
        options (Union[Unset, list['SurveyQuestionOption']]):
        conditions (Union[Unset, list['SurveyQuestionCondition']]):
    """

    key: str
    description: str
    question_type: SurveyQuestionTypeEnum
    required: Union[Unset, bool] = False
    user_guidance: Union[Unset, str] = ""
    min_value: Union[None, Unset, str] = UNSET
    max_value: Union[None, Unset, str] = UNSET
    likert_scale_length: Union[LikertScaleLengthEnum, None, Unset] = UNSET
    likert_low_label: Union[Unset, str] = UNSET
    likert_high_label: Union[Unset, str] = UNSET
    likert_allow_na: Union[Unset, bool] = UNSET
    rich_text_char_limit: Union[None, Unset, int] = UNSET
    rich_text_toolbar_level: Union[Unset, RichTextToolbarLevelEnum] = UNSET
    dependency_logic_operator: Union[Unset, DependencyLogicOperatorEnum] = UNSET
    options: Union[Unset, list["SurveyQuestionOption"]] = UNSET
    conditions: Union[Unset, list["SurveyQuestionCondition"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        description = self.description

        question_type = self.question_type.value

        required = self.required

        user_guidance = self.user_guidance

        min_value: Union[None, Unset, str]
        if isinstance(self.min_value, Unset):
            min_value = UNSET
        else:
            min_value = self.min_value

        max_value: Union[None, Unset, str]
        if isinstance(self.max_value, Unset):
            max_value = UNSET
        else:
            max_value = self.max_value

        likert_scale_length: Union[None, Unset, int]
        if isinstance(self.likert_scale_length, Unset):
            likert_scale_length = UNSET
        elif isinstance(self.likert_scale_length, LikertScaleLengthEnum):
            likert_scale_length = self.likert_scale_length.value
        else:
            likert_scale_length = self.likert_scale_length

        likert_low_label = self.likert_low_label

        likert_high_label = self.likert_high_label

        likert_allow_na = self.likert_allow_na

        rich_text_char_limit: Union[None, Unset, int]
        if isinstance(self.rich_text_char_limit, Unset):
            rich_text_char_limit = UNSET
        else:
            rich_text_char_limit = self.rich_text_char_limit

        rich_text_toolbar_level: Union[Unset, str] = UNSET
        if not isinstance(self.rich_text_toolbar_level, Unset):
            rich_text_toolbar_level = self.rich_text_toolbar_level.value

        dependency_logic_operator: Union[Unset, str] = UNSET
        if not isinstance(self.dependency_logic_operator, Unset):
            dependency_logic_operator = self.dependency_logic_operator.value

        options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        conditions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "description": description,
                "question_type": question_type,
            }
        )
        if required is not UNSET:
            field_dict["required"] = required
        if user_guidance is not UNSET:
            field_dict["user_guidance"] = user_guidance
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if max_value is not UNSET:
            field_dict["max_value"] = max_value
        if likert_scale_length is not UNSET:
            field_dict["likert_scale_length"] = likert_scale_length
        if likert_low_label is not UNSET:
            field_dict["likert_low_label"] = likert_low_label
        if likert_high_label is not UNSET:
            field_dict["likert_high_label"] = likert_high_label
        if likert_allow_na is not UNSET:
            field_dict["likert_allow_na"] = likert_allow_na
        if rich_text_char_limit is not UNSET:
            field_dict["rich_text_char_limit"] = rich_text_char_limit
        if rich_text_toolbar_level is not UNSET:
            field_dict["rich_text_toolbar_level"] = rich_text_toolbar_level
        if dependency_logic_operator is not UNSET:
            field_dict["dependency_logic_operator"] = dependency_logic_operator
        if options is not UNSET:
            field_dict["options"] = options
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.survey_question_condition import SurveyQuestionCondition
        from ..models.survey_question_option import SurveyQuestionOption

        d = dict(src_dict)
        key = d.pop("key")

        description = d.pop("description")

        question_type = SurveyQuestionTypeEnum(d.pop("question_type"))

        required = d.pop("required", UNSET)

        user_guidance = d.pop("user_guidance", UNSET)

        def _parse_min_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        min_value = _parse_min_value(d.pop("min_value", UNSET))

        def _parse_max_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        max_value = _parse_max_value(d.pop("max_value", UNSET))

        def _parse_likert_scale_length(data: object) -> Union[LikertScaleLengthEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                likert_scale_length_type_0 = LikertScaleLengthEnum(data)

                return likert_scale_length_type_0
            except:  # noqa: E722
                pass
            return cast(Union[LikertScaleLengthEnum, None, Unset], data)

        likert_scale_length = _parse_likert_scale_length(d.pop("likert_scale_length", UNSET))

        likert_low_label = d.pop("likert_low_label", UNSET)

        likert_high_label = d.pop("likert_high_label", UNSET)

        likert_allow_na = d.pop("likert_allow_na", UNSET)

        def _parse_rich_text_char_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rich_text_char_limit = _parse_rich_text_char_limit(d.pop("rich_text_char_limit", UNSET))

        _rich_text_toolbar_level = d.pop("rich_text_toolbar_level", UNSET)
        rich_text_toolbar_level: Union[Unset, RichTextToolbarLevelEnum]
        if isinstance(_rich_text_toolbar_level, Unset):
            rich_text_toolbar_level = UNSET
        else:
            rich_text_toolbar_level = RichTextToolbarLevelEnum(_rich_text_toolbar_level)

        _dependency_logic_operator = d.pop("dependency_logic_operator", UNSET)
        dependency_logic_operator: Union[Unset, DependencyLogicOperatorEnum]
        if isinstance(_dependency_logic_operator, Unset):
            dependency_logic_operator = UNSET
        else:
            dependency_logic_operator = DependencyLogicOperatorEnum(_dependency_logic_operator)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = SurveyQuestionOption.from_dict(options_item_data)

            options.append(options_item)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = SurveyQuestionCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        survey_question = cls(
            key=key,
            description=description,
            question_type=question_type,
            required=required,
            user_guidance=user_guidance,
            min_value=min_value,
            max_value=max_value,
            likert_scale_length=likert_scale_length,
            likert_low_label=likert_low_label,
            likert_high_label=likert_high_label,
            likert_allow_na=likert_allow_na,
            rich_text_char_limit=rich_text_char_limit,
            rich_text_toolbar_level=rich_text_toolbar_level,
            dependency_logic_operator=dependency_logic_operator,
            options=options,
            conditions=conditions,
        )

        survey_question.additional_properties = d
        return survey_question

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
