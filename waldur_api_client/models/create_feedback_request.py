from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateFeedbackRequest")


@_attrs_define
class CreateFeedbackRequest:
    """
    Attributes:
        evaluation (int):
        token (str):
        comment (Union[Unset, str]):
    """

    evaluation: int
    token: str
    comment: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        evaluation = self.evaluation

        token = self.token

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "evaluation": evaluation,
                "token": token,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        evaluation = d.pop("evaluation")

        token = d.pop("token")

        comment = d.pop("comment", UNSET)

        create_feedback_request = cls(
            evaluation=evaluation,
            token=token,
            comment=comment,
        )

        create_feedback_request.additional_properties = d
        return create_feedback_request

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
