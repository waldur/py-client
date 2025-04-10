import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.policy_type_enum import PolicyTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkRBACPolicy")


@_attrs_define
class NetworkRBACPolicy:
    """
    Attributes:
        uuid (Union[Unset, UUID]):
        network (Union[Unset, str]):
        target_tenant (Union[Unset, str]):
        backend_id (Union[Unset, str]):
        policy_type (Union[Unset, PolicyTypeEnum]):  Default: PolicyTypeEnum.ACCESS_AS_SHARED.
        created (Union[Unset, datetime.datetime]):
    """

    uuid: Union[Unset, UUID] = UNSET
    network: Union[Unset, str] = UNSET
    target_tenant: Union[Unset, str] = UNSET
    backend_id: Union[Unset, str] = UNSET
    policy_type: Union[Unset, PolicyTypeEnum] = PolicyTypeEnum.ACCESS_AS_SHARED
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: Union[Unset, str] = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        network = self.network

        target_tenant = self.target_tenant

        backend_id = self.backend_id

        policy_type: Union[Unset, str] = UNSET
        if not isinstance(self.policy_type, Unset):
            policy_type = self.policy_type.value

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if network is not UNSET:
            field_dict["network"] = network
        if target_tenant is not UNSET:
            field_dict["target_tenant"] = target_tenant
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if policy_type is not UNSET:
            field_dict["policy_type"] = policy_type
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: Union[Unset, UUID]
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        network = d.pop("network", UNSET)

        target_tenant = d.pop("target_tenant", UNSET)

        backend_id = d.pop("backend_id", UNSET)

        _policy_type = d.pop("policy_type", UNSET)
        policy_type: Union[Unset, PolicyTypeEnum]
        if isinstance(_policy_type, Unset):
            policy_type = UNSET
        else:
            policy_type = PolicyTypeEnum(_policy_type)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        network_rbac_policy = cls(
            uuid=uuid,
            network=network,
            target_tenant=target_tenant,
            backend_id=backend_id,
            policy_type=policy_type,
            created=created,
        )

        network_rbac_policy.additional_properties = d
        return network_rbac_policy

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
