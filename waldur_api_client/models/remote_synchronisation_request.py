import json
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_remote_local_category_request import NestedRemoteLocalCategoryRequest


T = TypeVar("T", bound="RemoteSynchronisationRequest")


@_attrs_define
class RemoteSynchronisationRequest:
    """
    Attributes:
        api_url (str):
        token (str):
        remote_organization_uuid (UUID):
        remote_organization_name (str):
        local_service_provider (str):
        remotelocalcategory_set (list['NestedRemoteLocalCategoryRequest']):
        is_active (Union[Unset, bool]):
    """

    api_url: str
    token: str
    remote_organization_uuid: UUID
    remote_organization_name: str
    local_service_provider: str
    remotelocalcategory_set: list["NestedRemoteLocalCategoryRequest"]
    is_active: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_url = self.api_url

        token = self.token

        remote_organization_uuid = str(self.remote_organization_uuid)

        remote_organization_name = self.remote_organization_name

        local_service_provider = self.local_service_provider

        remotelocalcategory_set = []
        for remotelocalcategory_set_item_data in self.remotelocalcategory_set:
            remotelocalcategory_set_item = remotelocalcategory_set_item_data.to_dict()
            remotelocalcategory_set.append(remotelocalcategory_set_item)

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_url": api_url,
                "token": token,
                "remote_organization_uuid": remote_organization_uuid,
                "remote_organization_name": remote_organization_name,
                "local_service_provider": local_service_provider,
                "remotelocalcategory_set": remotelocalcategory_set,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        api_url = (None, str(self.api_url).encode(), "text/plain")

        token = (None, str(self.token).encode(), "text/plain")

        remote_organization_uuid = str(self.remote_organization_uuid)

        remote_organization_name = (None, str(self.remote_organization_name).encode(), "text/plain")

        local_service_provider = (None, str(self.local_service_provider).encode(), "text/plain")

        _temp_remotelocalcategory_set = []
        for remotelocalcategory_set_item_data in self.remotelocalcategory_set:
            remotelocalcategory_set_item = remotelocalcategory_set_item_data.to_dict()
            _temp_remotelocalcategory_set.append(remotelocalcategory_set_item)
        remotelocalcategory_set = (None, json.dumps(_temp_remotelocalcategory_set).encode(), "application/json")

        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "api_url": api_url,
                "token": token,
                "remote_organization_uuid": remote_organization_uuid,
                "remote_organization_name": remote_organization_name,
                "local_service_provider": local_service_provider,
                "remotelocalcategory_set": remotelocalcategory_set,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.nested_remote_local_category_request import NestedRemoteLocalCategoryRequest

        d = src_dict.copy()
        api_url = d.pop("api_url")

        token = d.pop("token")

        remote_organization_uuid = UUID(d.pop("remote_organization_uuid"))

        remote_organization_name = d.pop("remote_organization_name")

        local_service_provider = d.pop("local_service_provider")

        remotelocalcategory_set = []
        _remotelocalcategory_set = d.pop("remotelocalcategory_set")
        for remotelocalcategory_set_item_data in _remotelocalcategory_set:
            remotelocalcategory_set_item = NestedRemoteLocalCategoryRequest.from_dict(remotelocalcategory_set_item_data)

            remotelocalcategory_set.append(remotelocalcategory_set_item)

        is_active = d.pop("is_active", UNSET)

        remote_synchronisation_request = cls(
            api_url=api_url,
            token=token,
            remote_organization_uuid=remote_organization_uuid,
            remote_organization_name=remote_organization_name,
            local_service_provider=local_service_provider,
            remotelocalcategory_set=remotelocalcategory_set,
            is_active=is_active,
        )

        remote_synchronisation_request.additional_properties = d
        return remote_synchronisation_request

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
