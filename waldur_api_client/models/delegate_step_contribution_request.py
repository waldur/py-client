from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DelegateStepContributionRequest")


@_attrs_define
class DelegateStepContributionRequest:
    """
    Attributes:
        contribution_uuid (UUID):
        user_uuid (Union[None, UUID]): Who to hand the slot to, as the step's delegable_to allows; null takes it back.
    """

    contribution_uuid: UUID
    user_uuid: Union[None, UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contribution_uuid = str(self.contribution_uuid)

        user_uuid: Union[None, str]
        if isinstance(self.user_uuid, UUID):
            user_uuid = str(self.user_uuid)
        else:
            user_uuid = self.user_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contribution_uuid": contribution_uuid,
                "user_uuid": user_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contribution_uuid = UUID(d.pop("contribution_uuid"))

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

        delegate_step_contribution_request = cls(
            contribution_uuid=contribution_uuid,
            user_uuid=user_uuid,
        )

        delegate_step_contribution_request.additional_properties = d
        return delegate_step_contribution_request

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
