from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsentDecisionRequest")


@_attrs_define
class ConsentDecisionRequest:
    """
    Attributes:
        client_id (str):
        response_type (str):
        code_challenge (str):
        code_challenge_method (str):
        allow (bool):
        redirect_uri (Union[Unset, str]):
        scope (Union[Unset, str]):
        state (Union[Unset, str]):
        resource (Union[Unset, list[str]]):
    """

    client_id: str
    response_type: str
    code_challenge: str
    code_challenge_method: str
    allow: bool
    redirect_uri: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    resource: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        response_type = self.response_type

        code_challenge = self.code_challenge

        code_challenge_method = self.code_challenge_method

        allow = self.allow

        redirect_uri = self.redirect_uri

        scope = self.scope

        state = self.state

        resource: Union[Unset, list[str]] = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "response_type": response_type,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "allow": allow,
            }
        )
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if scope is not UNSET:
            field_dict["scope"] = scope
        if state is not UNSET:
            field_dict["state"] = state
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id")

        response_type = d.pop("response_type")

        code_challenge = d.pop("code_challenge")

        code_challenge_method = d.pop("code_challenge_method")

        allow = d.pop("allow")

        redirect_uri = d.pop("redirect_uri", UNSET)

        scope = d.pop("scope", UNSET)

        state = d.pop("state", UNSET)

        resource = cast(list[str], d.pop("resource", UNSET))

        consent_decision_request = cls(
            client_id=client_id,
            response_type=response_type,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            allow=allow,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            resource=resource,
        )

        consent_decision_request.additional_properties = d
        return consent_decision_request

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
