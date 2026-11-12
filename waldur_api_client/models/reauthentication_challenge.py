from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reauthentication_action_enum import ReauthenticationActionEnum
from ..models.reauthentication_method_enum import ReauthenticationMethodEnum

T = TypeVar("T", bound="ReauthenticationChallenge")


@_attrs_define
class ReauthenticationChallenge:
    """
    Attributes:
        detail (str):
        code (str): Always reauthentication_required.
        action (ReauthenticationActionEnum):
        methods (list[ReauthenticationMethodEnum]): The methods this user can obtain a grant with.
    """

    detail: str
    code: str
    action: ReauthenticationActionEnum
    methods: list[ReauthenticationMethodEnum]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        code = self.code

        action = self.action.value

        methods = []
        for methods_item_data in self.methods:
            methods_item = methods_item_data.value
            methods.append(methods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
                "code": code,
                "action": action,
                "methods": methods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        detail = d.pop("detail")

        code = d.pop("code")

        action = ReauthenticationActionEnum(d.pop("action"))

        methods = []
        _methods = d.pop("methods")
        for methods_item_data in _methods:
            methods_item = ReauthenticationMethodEnum(methods_item_data)

            methods.append(methods_item)

        reauthentication_challenge = cls(
            detail=detail,
            code=code,
            action=action,
            methods=methods,
        )

        reauthentication_challenge.additional_properties = d
        return reauthentication_challenge

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
