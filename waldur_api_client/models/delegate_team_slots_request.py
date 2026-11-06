from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DelegateTeamSlotsRequest")


@_attrs_define
class DelegateTeamSlotsRequest:
    """
    Attributes:
        contribution_uuids (list[UUID]):
        user_uuid (Union[None, UUID]): Who takes the slots over; null takes them back.
    """

    contribution_uuids: list[UUID]
    user_uuid: Union[None, UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contribution_uuids = []
        for contribution_uuids_item_data in self.contribution_uuids:
            contribution_uuids_item = str(contribution_uuids_item_data)
            contribution_uuids.append(contribution_uuids_item)

        user_uuid: Union[None, str]
        if isinstance(self.user_uuid, UUID):
            user_uuid = str(self.user_uuid)
        else:
            user_uuid = self.user_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contribution_uuids": contribution_uuids,
                "user_uuid": user_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contribution_uuids = []
        _contribution_uuids = d.pop("contribution_uuids")
        for contribution_uuids_item_data in _contribution_uuids:
            contribution_uuids_item = UUID(contribution_uuids_item_data)

            contribution_uuids.append(contribution_uuids_item)

        def _parse_user_uuid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_uuid_type_0 = UUID(data)

                return user_uuid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        user_uuid = _parse_user_uuid(d.pop("user_uuid"))

        delegate_team_slots_request = cls(
            contribution_uuids=contribution_uuids,
            user_uuid=user_uuid,
        )

        delegate_team_slots_request.additional_properties = d
        return delegate_team_slots_request

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
