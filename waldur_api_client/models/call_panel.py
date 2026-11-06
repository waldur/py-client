import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_panel_domain import CallPanelDomain
    from ..models.call_panel_person import CallPanelPerson


T = TypeVar("T", bound="CallPanel")


@_attrs_define
class CallPanel:
    """
    Attributes:
        uuid (UUID):
        created (datetime.datetime):
        modified (datetime.datetime):
        call_uuid (UUID):
        name (str):
        chair_name (Union[None, str]):
        member_details (list['CallPanelPerson']):
        science_domain_details (list['CallPanelDomain']):
        science_sub_domain_details (list['CallPanelDomain']):
        proposals_count (int): How many proposals of the call are routed to the panel.
        key (Union[Unset, str]): Identifier of the panel within its call. Derived from the name when left out. Cannot
            change once the panel exists.
        description (Union[Unset, str]):
        order (Union[Unset, int]): Position of the panel in the call's list.
        chair (Union[None, UUID, Unset]): The panel's chair, one of its members.
        members (Union[Unset, list[UUID]]): Panel members of the call who sit on the panel.
        science_domains (Union[Unset, list[UUID]]): Proposals of these science domains go to the panel.
        science_sub_domains (Union[Unset, list[UUID]]): Proposals of these science sub-domains go to the panel,
            whichever panel their domain maps to.
    """

    uuid: UUID
    created: datetime.datetime
    modified: datetime.datetime
    call_uuid: UUID
    name: str
    chair_name: Union[None, str]
    member_details: list["CallPanelPerson"]
    science_domain_details: list["CallPanelDomain"]
    science_sub_domain_details: list["CallPanelDomain"]
    proposals_count: int
    key: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    order: Union[Unset, int] = UNSET
    chair: Union[None, UUID, Unset] = UNSET
    members: Union[Unset, list[UUID]] = UNSET
    science_domains: Union[Unset, list[UUID]] = UNSET
    science_sub_domains: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        call_uuid = str(self.call_uuid)

        name = self.name

        chair_name: Union[None, str]
        chair_name = self.chair_name

        member_details = []
        for member_details_item_data in self.member_details:
            member_details_item = member_details_item_data.to_dict()
            member_details.append(member_details_item)

        science_domain_details = []
        for science_domain_details_item_data in self.science_domain_details:
            science_domain_details_item = science_domain_details_item_data.to_dict()
            science_domain_details.append(science_domain_details_item)

        science_sub_domain_details = []
        for science_sub_domain_details_item_data in self.science_sub_domain_details:
            science_sub_domain_details_item = science_sub_domain_details_item_data.to_dict()
            science_sub_domain_details.append(science_sub_domain_details_item)

        proposals_count = self.proposals_count

        key = self.key

        description = self.description

        order = self.order

        chair: Union[None, Unset, str]
        if isinstance(self.chair, Unset):
            chair = UNSET
        elif isinstance(self.chair, UUID):
            chair = str(self.chair)
        else:
            chair = self.chair

        members: Union[Unset, list[str]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = str(members_item_data)
                members.append(members_item)

        science_domains: Union[Unset, list[str]] = UNSET
        if not isinstance(self.science_domains, Unset):
            science_domains = []
            for science_domains_item_data in self.science_domains:
                science_domains_item = str(science_domains_item_data)
                science_domains.append(science_domains_item)

        science_sub_domains: Union[Unset, list[str]] = UNSET
        if not isinstance(self.science_sub_domains, Unset):
            science_sub_domains = []
            for science_sub_domains_item_data in self.science_sub_domains:
                science_sub_domains_item = str(science_sub_domains_item_data)
                science_sub_domains.append(science_sub_domains_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "created": created,
                "modified": modified,
                "call_uuid": call_uuid,
                "name": name,
                "chair_name": chair_name,
                "member_details": member_details,
                "science_domain_details": science_domain_details,
                "science_sub_domain_details": science_sub_domain_details,
                "proposals_count": proposals_count,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if description is not UNSET:
            field_dict["description"] = description
        if order is not UNSET:
            field_dict["order"] = order
        if chair is not UNSET:
            field_dict["chair"] = chair
        if members is not UNSET:
            field_dict["members"] = members
        if science_domains is not UNSET:
            field_dict["science_domains"] = science_domains
        if science_sub_domains is not UNSET:
            field_dict["science_sub_domains"] = science_sub_domains

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.call_panel_domain import CallPanelDomain
        from ..models.call_panel_person import CallPanelPerson

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        call_uuid = UUID(d.pop("call_uuid"))

        name = d.pop("name")

        def _parse_chair_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        chair_name = _parse_chair_name(d.pop("chair_name"))

        member_details = []
        _member_details = d.pop("member_details")
        for member_details_item_data in _member_details:
            member_details_item = CallPanelPerson.from_dict(member_details_item_data)

            member_details.append(member_details_item)

        science_domain_details = []
        _science_domain_details = d.pop("science_domain_details")
        for science_domain_details_item_data in _science_domain_details:
            science_domain_details_item = CallPanelDomain.from_dict(science_domain_details_item_data)

            science_domain_details.append(science_domain_details_item)

        science_sub_domain_details = []
        _science_sub_domain_details = d.pop("science_sub_domain_details")
        for science_sub_domain_details_item_data in _science_sub_domain_details:
            science_sub_domain_details_item = CallPanelDomain.from_dict(science_sub_domain_details_item_data)

            science_sub_domain_details.append(science_sub_domain_details_item)

        proposals_count = d.pop("proposals_count")

        key = d.pop("key", UNSET)

        description = d.pop("description", UNSET)

        order = d.pop("order", UNSET)

        def _parse_chair(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                chair_type_0 = UUID(data)

                return chair_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        chair = _parse_chair(d.pop("chair", UNSET))

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = UUID(members_item_data)

            members.append(members_item)

        science_domains = []
        _science_domains = d.pop("science_domains", UNSET)
        for science_domains_item_data in _science_domains or []:
            science_domains_item = UUID(science_domains_item_data)

            science_domains.append(science_domains_item)

        science_sub_domains = []
        _science_sub_domains = d.pop("science_sub_domains", UNSET)
        for science_sub_domains_item_data in _science_sub_domains or []:
            science_sub_domains_item = UUID(science_sub_domains_item_data)

            science_sub_domains.append(science_sub_domains_item)

        call_panel = cls(
            uuid=uuid,
            created=created,
            modified=modified,
            call_uuid=call_uuid,
            name=name,
            chair_name=chair_name,
            member_details=member_details,
            science_domain_details=science_domain_details,
            science_sub_domain_details=science_sub_domain_details,
            proposals_count=proposals_count,
            key=key,
            description=description,
            order=order,
            chair=chair,
            members=members,
            science_domains=science_domains,
            science_sub_domains=science_sub_domains,
        )

        call_panel.additional_properties = d
        return call_panel

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
