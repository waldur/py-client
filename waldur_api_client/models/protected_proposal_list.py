import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.proposal_states import ProposalStates

if TYPE_CHECKING:
    from ..models.proposal_review import ProposalReview


T = TypeVar("T", bound="ProtectedProposalList")


@_attrs_define
class ProtectedProposalList:
    """
    Attributes:
        uuid (UUID):
        name (str):
        state (ProposalStates):
        reviews (list['ProposalReview']):
        approved_by_name (str):
        created_by_name (str):
        created (datetime.datetime):
    """

    uuid: UUID
    name: str
    state: ProposalStates
    reviews: list["ProposalReview"]
    approved_by_name: str
    created_by_name: str
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        state = self.state.value

        reviews = []
        for reviews_item_data in self.reviews:
            reviews_item = reviews_item_data.to_dict()
            reviews.append(reviews_item)

        approved_by_name = self.approved_by_name

        created_by_name = self.created_by_name

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "state": state,
                "reviews": reviews,
                "approved_by_name": approved_by_name,
                "created_by_name": created_by_name,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_review import ProposalReview

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        state = ProposalStates(d.pop("state"))

        reviews = []
        _reviews = d.pop("reviews")
        for reviews_item_data in _reviews:
            reviews_item = ProposalReview.from_dict(reviews_item_data)

            reviews.append(reviews_item)

        approved_by_name = d.pop("approved_by_name")

        created_by_name = d.pop("created_by_name")

        created = isoparse(d.pop("created"))

        protected_proposal_list = cls(
            uuid=uuid,
            name=name,
            state=state,
            reviews=reviews,
            approved_by_name=approved_by_name,
            created_by_name=created_by_name,
            created=created,
        )

        protected_proposal_list.additional_properties = d
        return protected_proposal_list

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
