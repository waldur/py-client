from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StepScoreGate")


@_attrs_define
class StepScoreGate:
    """
    Attributes:
        score (Union[None, float]): The score the threshold is checked against; null while there is none.
        threshold (float): The step's minimum score.
        source_step_name (Union[None, str]): The input step the score comes from; null when it is the average of the
            proposal's (or this step's) reviews.
        passes (bool): Whether the step may be completed with an outcome other than declined.
    """

    score: Union[None, float]
    threshold: float
    source_step_name: Union[None, str]
    passes: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score: Union[None, float]
        score = self.score

        threshold = self.threshold

        source_step_name: Union[None, str]
        source_step_name = self.source_step_name

        passes = self.passes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "score": score,
                "threshold": threshold,
                "source_step_name": source_step_name,
                "passes": passes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_score(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        score = _parse_score(d.pop("score"))

        threshold = d.pop("threshold")

        def _parse_source_step_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        source_step_name = _parse_source_step_name(d.pop("source_step_name"))

        passes = d.pop("passes")

        step_score_gate = cls(
            score=score,
            threshold=threshold,
            source_step_name=source_step_name,
            passes=passes,
        )

        step_score_gate.additional_properties = d
        return step_score_gate

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
