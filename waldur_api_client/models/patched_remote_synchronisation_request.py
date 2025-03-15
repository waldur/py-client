import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_remote_local_category_request import NestedRemoteLocalCategoryRequest


T = TypeVar("T", bound="PatchedRemoteSynchronisationRequest")


@_attrs_define
class PatchedRemoteSynchronisationRequest:
    """
    Attributes:
        api_url (Union[Unset, str]):
        token (Union[Unset, str]):
        remote_organization_name (Union[Unset, str]):
        local_service_provider (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        remotelocalcategory_set (Union[Unset, list['NestedRemoteLocalCategoryRequest']]):
    """

    api_url: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    remote_organization_name: Union[Unset, str] = UNSET
    local_service_provider: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    remotelocalcategory_set: Union[Unset, list["NestedRemoteLocalCategoryRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_url = self.api_url

        token = self.token

        remote_organization_name = self.remote_organization_name

        local_service_provider = self.local_service_provider

        is_active = self.is_active

        remotelocalcategory_set: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.remotelocalcategory_set, Unset):
            remotelocalcategory_set = []
            for remotelocalcategory_set_item_data in self.remotelocalcategory_set:
                remotelocalcategory_set_item = remotelocalcategory_set_item_data.to_dict()
                remotelocalcategory_set.append(remotelocalcategory_set_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_url is not UNSET:
            field_dict["api_url"] = api_url
        if token is not UNSET:
            field_dict["token"] = token
        if remote_organization_name is not UNSET:
            field_dict["remote_organization_name"] = remote_organization_name
        if local_service_provider is not UNSET:
            field_dict["local_service_provider"] = local_service_provider
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if remotelocalcategory_set is not UNSET:
            field_dict["remotelocalcategory_set"] = remotelocalcategory_set

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        api_url = self.api_url if isinstance(self.api_url, Unset) else (None, str(self.api_url).encode(), "text/plain")

        token = self.token if isinstance(self.token, Unset) else (None, str(self.token).encode(), "text/plain")

        remote_organization_name = (
            self.remote_organization_name
            if isinstance(self.remote_organization_name, Unset)
            else (None, str(self.remote_organization_name).encode(), "text/plain")
        )

        local_service_provider = (
            self.local_service_provider
            if isinstance(self.local_service_provider, Unset)
            else (None, str(self.local_service_provider).encode(), "text/plain")
        )

        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )

        remotelocalcategory_set: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.remotelocalcategory_set, Unset):
            _temp_remotelocalcategory_set = []
            for remotelocalcategory_set_item_data in self.remotelocalcategory_set:
                remotelocalcategory_set_item = remotelocalcategory_set_item_data.to_dict()
                _temp_remotelocalcategory_set.append(remotelocalcategory_set_item)
            remotelocalcategory_set = (None, json.dumps(_temp_remotelocalcategory_set).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if api_url is not UNSET:
            field_dict["api_url"] = api_url
        if token is not UNSET:
            field_dict["token"] = token
        if remote_organization_name is not UNSET:
            field_dict["remote_organization_name"] = remote_organization_name
        if local_service_provider is not UNSET:
            field_dict["local_service_provider"] = local_service_provider
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if remotelocalcategory_set is not UNSET:
            field_dict["remotelocalcategory_set"] = remotelocalcategory_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_remote_local_category_request import NestedRemoteLocalCategoryRequest

        d = dict(src_dict)
        api_url = d.pop("api_url", UNSET)

        token = d.pop("token", UNSET)

        remote_organization_name = d.pop("remote_organization_name", UNSET)

        local_service_provider = d.pop("local_service_provider", UNSET)

        is_active = d.pop("is_active", UNSET)

        remotelocalcategory_set = []
        _remotelocalcategory_set = d.pop("remotelocalcategory_set", UNSET)
        for remotelocalcategory_set_item_data in _remotelocalcategory_set or []:
            remotelocalcategory_set_item = NestedRemoteLocalCategoryRequest.from_dict(remotelocalcategory_set_item_data)

            remotelocalcategory_set.append(remotelocalcategory_set_item)

        patched_remote_synchronisation_request = cls(
            api_url=api_url,
            token=token,
            remote_organization_name=remote_organization_name,
            local_service_provider=local_service_provider,
            is_active=is_active,
            remotelocalcategory_set=remotelocalcategory_set,
        )

        patched_remote_synchronisation_request.additional_properties = d
        return patched_remote_synchronisation_request

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
