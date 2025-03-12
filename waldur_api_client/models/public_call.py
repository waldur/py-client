import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.call_states import CallStates
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_document import CallDocument
    from ..models.nested_requested_offering import NestedRequestedOffering
    from ..models.nested_round import NestedRound


T = TypeVar("T", bound="PublicCall")


@_attrs_define
class PublicCall:
    """
    Attributes:
        url (str):
        uuid (UUID):
        created (datetime.datetime):
        start_date (datetime.datetime):
        end_date (datetime.datetime):
        slug (str):
        name (str):
        state (CallStates):
        manager (str):
        customer_name (str):
        customer_uuid (UUID):
        offerings (list['NestedRequestedOffering']):
        rounds (list['NestedRound']):
        documents (list['CallDocument']):
        description (Union[Unset, str]):
        backend_id (Union[Unset, str]):
        external_url (Union[None, Unset, str]):
    """

    url: str
    uuid: UUID
    created: datetime.datetime
    start_date: datetime.datetime
    end_date: datetime.datetime
    slug: str
    name: str
    state: CallStates
    manager: str
    customer_name: str
    customer_uuid: UUID
    offerings: list["NestedRequestedOffering"]
    rounds: list["NestedRound"]
    documents: list["CallDocument"]
    description: Union[Unset, str] = UNSET
    backend_id: Union[Unset, str] = UNSET
    external_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        created = self.created.isoformat()

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        slug = self.slug

        name = self.name

        state = self.state.value

        manager = self.manager

        customer_name = self.customer_name

        customer_uuid = str(self.customer_uuid)

        offerings = []
        for offerings_item_data in self.offerings:
            offerings_item = offerings_item_data.to_dict()
            offerings.append(offerings_item)

        rounds = []
        for rounds_item_data in self.rounds:
            rounds_item = rounds_item_data.to_dict()
            rounds.append(rounds_item)

        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()
            documents.append(documents_item)

        description = self.description

        backend_id = self.backend_id

        external_url: Union[None, Unset, str]
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "created": created,
                "start_date": start_date,
                "end_date": end_date,
                "slug": slug,
                "name": name,
                "state": state,
                "manager": manager,
                "customer_name": customer_name,
                "customer_uuid": customer_uuid,
                "offerings": offerings,
                "rounds": rounds,
                "documents": documents,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if external_url is not UNSET:
            field_dict["external_url"] = external_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.call_document import CallDocument
        from ..models.nested_requested_offering import NestedRequestedOffering
        from ..models.nested_round import NestedRound

        d = src_dict.copy()
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        start_date = isoparse(d.pop("start_date"))

        end_date = isoparse(d.pop("end_date"))

        slug = d.pop("slug")

        name = d.pop("name")

        state = CallStates(d.pop("state"))

        manager = d.pop("manager")

        customer_name = d.pop("customer_name")

        customer_uuid = UUID(d.pop("customer_uuid"))

        offerings = []
        _offerings = d.pop("offerings")
        for offerings_item_data in _offerings:
            offerings_item = NestedRequestedOffering.from_dict(offerings_item_data)

            offerings.append(offerings_item)

        rounds = []
        _rounds = d.pop("rounds")
        for rounds_item_data in _rounds:
            rounds_item = NestedRound.from_dict(rounds_item_data)

            rounds.append(rounds_item)

        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = CallDocument.from_dict(documents_item_data)

            documents.append(documents_item)

        description = d.pop("description", UNSET)

        backend_id = d.pop("backend_id", UNSET)

        def _parse_external_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        public_call = cls(
            url=url,
            uuid=uuid,
            created=created,
            start_date=start_date,
            end_date=end_date,
            slug=slug,
            name=name,
            state=state,
            manager=manager,
            customer_name=customer_name,
            customer_uuid=customer_uuid,
            offerings=offerings,
            rounds=rounds,
            documents=documents,
            description=description,
            backend_id=backend_id,
            external_url=external_url,
        )

        public_call.additional_properties = d
        return public_call

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
