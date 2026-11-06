import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reviewer_standing_enum import ReviewerStandingEnum

if TYPE_CHECKING:
    from ..models.reviewer_publication_approval import ReviewerPublicationApproval
    from ..models.reviewer_registry_pool import ReviewerRegistryPool


T = TypeVar("T", bound="ReviewerRegistry")


@_attrs_define
class ReviewerRegistry:
    """
    Attributes:
        uuid (UUID):
        user_uuid (UUID):
        user_full_name (str):
        user_email (str):
        user_username (str): Required. 128 characters or fewer. Lowercase letters, numbers and @/./+/-/_ characters
        user_is_active (bool): Designates whether this user should be treated as active. Unselect this instead of
            deleting accounts.
        standing (ReviewerStandingEnum):
        standing_reason (str):
        standing_changed_by_name (str):
        standing_changed_at (Union[None, datetime.datetime]):
        is_published (bool): Whether profile is discoverable by call managers
        published_at (Union[None, datetime.datetime]): When the profile was published
        publication_request (Union['ReviewerPublicationApproval', None]):
        available_for_reviews (bool): Whether reviewer is currently accepting review requests
        pools (list['ReviewerRegistryPool']): The calls whose reviewer pool the reviewer accepted.
        open_assignments (int): Assignments still occupying the reviewer: pending offers and accepted ones whose review
            is not finished.
        reviews_in_progress (int): Reviews in progress given without an assignment.
        created (datetime.datetime):
    """

    uuid: UUID
    user_uuid: UUID
    user_full_name: str
    user_email: str
    user_username: str
    user_is_active: bool
    standing: ReviewerStandingEnum
    standing_reason: str
    standing_changed_by_name: str
    standing_changed_at: Union[None, datetime.datetime]
    is_published: bool
    published_at: Union[None, datetime.datetime]
    publication_request: Union["ReviewerPublicationApproval", None]
    available_for_reviews: bool
    pools: list["ReviewerRegistryPool"]
    open_assignments: int
    reviews_in_progress: int
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.reviewer_publication_approval import ReviewerPublicationApproval

        uuid = str(self.uuid)

        user_uuid = str(self.user_uuid)

        user_full_name = self.user_full_name

        user_email = self.user_email

        user_username = self.user_username

        user_is_active = self.user_is_active

        standing = self.standing.value

        standing_reason = self.standing_reason

        standing_changed_by_name = self.standing_changed_by_name

        standing_changed_at: Union[None, str]
        if isinstance(self.standing_changed_at, datetime.datetime):
            standing_changed_at = self.standing_changed_at.isoformat()
        else:
            standing_changed_at = self.standing_changed_at

        is_published = self.is_published

        published_at: Union[None, str]
        if isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        publication_request: Union[None, dict[str, Any]]
        if isinstance(self.publication_request, ReviewerPublicationApproval):
            publication_request = self.publication_request.to_dict()
        else:
            publication_request = self.publication_request

        available_for_reviews = self.available_for_reviews

        pools = []
        for pools_item_data in self.pools:
            pools_item = pools_item_data.to_dict()
            pools.append(pools_item)

        open_assignments = self.open_assignments

        reviews_in_progress = self.reviews_in_progress

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "user_uuid": user_uuid,
                "user_full_name": user_full_name,
                "user_email": user_email,
                "user_username": user_username,
                "user_is_active": user_is_active,
                "standing": standing,
                "standing_reason": standing_reason,
                "standing_changed_by_name": standing_changed_by_name,
                "standing_changed_at": standing_changed_at,
                "is_published": is_published,
                "published_at": published_at,
                "publication_request": publication_request,
                "available_for_reviews": available_for_reviews,
                "pools": pools,
                "open_assignments": open_assignments,
                "reviews_in_progress": reviews_in_progress,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reviewer_publication_approval import ReviewerPublicationApproval
        from ..models.reviewer_registry_pool import ReviewerRegistryPool

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        user_uuid = UUID(d.pop("user_uuid"))

        user_full_name = d.pop("user_full_name")

        user_email = d.pop("user_email")

        user_username = d.pop("user_username")

        user_is_active = d.pop("user_is_active")

        standing = ReviewerStandingEnum(d.pop("standing"))

        standing_reason = d.pop("standing_reason")

        standing_changed_by_name = d.pop("standing_changed_by_name")

        def _parse_standing_changed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                standing_changed_at_type_0 = isoparse(data)

                return standing_changed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        standing_changed_at = _parse_standing_changed_at(d.pop("standing_changed_at"))

        is_published = d.pop("is_published")

        def _parse_published_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = isoparse(data)

                return published_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        published_at = _parse_published_at(d.pop("published_at"))

        def _parse_publication_request(data: object) -> Union["ReviewerPublicationApproval", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                publication_request_type_1 = ReviewerPublicationApproval.from_dict(data)

                return publication_request_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ReviewerPublicationApproval", None], data)

        publication_request = _parse_publication_request(d.pop("publication_request"))

        available_for_reviews = d.pop("available_for_reviews")

        pools = []
        _pools = d.pop("pools")
        for pools_item_data in _pools:
            pools_item = ReviewerRegistryPool.from_dict(pools_item_data)

            pools.append(pools_item)

        open_assignments = d.pop("open_assignments")

        reviews_in_progress = d.pop("reviews_in_progress")

        created = isoparse(d.pop("created"))

        reviewer_registry = cls(
            uuid=uuid,
            user_uuid=user_uuid,
            user_full_name=user_full_name,
            user_email=user_email,
            user_username=user_username,
            user_is_active=user_is_active,
            standing=standing,
            standing_reason=standing_reason,
            standing_changed_by_name=standing_changed_by_name,
            standing_changed_at=standing_changed_at,
            is_published=is_published,
            published_at=published_at,
            publication_request=publication_request,
            available_for_reviews=available_for_reviews,
            pools=pools,
            open_assignments=open_assignments,
            reviews_in_progress=reviews_in_progress,
            created=created,
        )

        reviewer_registry.additional_properties = d
        return reviewer_registry

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
