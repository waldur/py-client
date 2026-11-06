from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pool_status_enum import PoolStatusEnum

T = TypeVar("T", bound="ReviewerSuggestionCandidate")


@_attrs_define
class ReviewerSuggestionCandidate:
    """
    Attributes:
        uuid (UUID):
        full_name (str):
        affiliation (Union[None, str]): The current affiliation on the person's reviewer profile.
        has_published_profile (bool): The person published their reviewer profile.
        pool_status (Union[None, PoolStatusEnum]): Where the person stands in the call's reviewer pool; null when they
            are not in it.
        has_conflict (bool): A conflict of interest stands between the person and the proposal.
    """

    uuid: UUID
    full_name: str
    affiliation: Union[None, str]
    has_published_profile: bool
    pool_status: Union[None, PoolStatusEnum]
    has_conflict: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        full_name = self.full_name

        affiliation: Union[None, str]
        affiliation = self.affiliation

        has_published_profile = self.has_published_profile

        pool_status: Union[None, str]
        if isinstance(self.pool_status, PoolStatusEnum):
            pool_status = self.pool_status.value
        else:
            pool_status = self.pool_status

        has_conflict = self.has_conflict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "full_name": full_name,
                "affiliation": affiliation,
                "has_published_profile": has_published_profile,
                "pool_status": pool_status,
                "has_conflict": has_conflict,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        full_name = d.pop("full_name")

        def _parse_affiliation(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        affiliation = _parse_affiliation(d.pop("affiliation"))

        has_published_profile = d.pop("has_published_profile")

        def _parse_pool_status(data: object) -> Union[None, PoolStatusEnum]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pool_status_type_0 = PoolStatusEnum(data)

                return pool_status_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, PoolStatusEnum], data)

        pool_status = _parse_pool_status(d.pop("pool_status"))

        has_conflict = d.pop("has_conflict")

        reviewer_suggestion_candidate = cls(
            uuid=uuid,
            full_name=full_name,
            affiliation=affiliation,
            has_published_profile=has_published_profile,
            pool_status=pool_status,
            has_conflict=has_conflict,
        )

        reviewer_suggestion_candidate.additional_properties = d
        return reviewer_suggestion_candidate

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
