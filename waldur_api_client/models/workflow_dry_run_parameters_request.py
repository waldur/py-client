from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dry_run_action_request import DryRunActionRequest
    from ..models.dry_run_view_as_request import DryRunViewAsRequest


T = TypeVar("T", bound="WorkflowDryRunParametersRequest")


@_attrs_define
class WorkflowDryRunParametersRequest:
    """
    Attributes:
        requested_offerings (Union[Unset, list[UUID]]): Requested offerings of the call, accepted ones, in the order
            actions name them; the call's first accepted ones by default.
        actions (Union[Unset, list['DryRunActionRequest']]):
        view_as (Union['DryRunViewAsRequest', None, Unset]):
    """

    requested_offerings: Union[Unset, list[UUID]] = UNSET
    actions: Union[Unset, list["DryRunActionRequest"]] = UNSET
    view_as: Union["DryRunViewAsRequest", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dry_run_view_as_request import DryRunViewAsRequest

        requested_offerings: Union[Unset, list[str]] = UNSET
        if not isinstance(self.requested_offerings, Unset):
            requested_offerings = []
            for requested_offerings_item_data in self.requested_offerings:
                requested_offerings_item = str(requested_offerings_item_data)
                requested_offerings.append(requested_offerings_item)

        actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        view_as: Union[None, Unset, dict[str, Any]]
        if isinstance(self.view_as, Unset):
            view_as = UNSET
        elif isinstance(self.view_as, DryRunViewAsRequest):
            view_as = self.view_as.to_dict()
        else:
            view_as = self.view_as

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requested_offerings is not UNSET:
            field_dict["requested_offerings"] = requested_offerings
        if actions is not UNSET:
            field_dict["actions"] = actions
        if view_as is not UNSET:
            field_dict["view_as"] = view_as

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dry_run_action_request import DryRunActionRequest
        from ..models.dry_run_view_as_request import DryRunViewAsRequest

        d = dict(src_dict)
        requested_offerings = []
        _requested_offerings = d.pop("requested_offerings", UNSET)
        for requested_offerings_item_data in _requested_offerings or []:
            requested_offerings_item = UUID(requested_offerings_item_data)

            requested_offerings.append(requested_offerings_item)

        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = DryRunActionRequest.from_dict(actions_item_data)

            actions.append(actions_item)

        def _parse_view_as(data: object) -> Union["DryRunViewAsRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                view_as_type_1 = DryRunViewAsRequest.from_dict(data)

                return view_as_type_1
            except:  # noqa: E722
                pass
            return cast(Union["DryRunViewAsRequest", None, Unset], data)

        view_as = _parse_view_as(d.pop("view_as", UNSET))

        workflow_dry_run_parameters_request = cls(
            requested_offerings=requested_offerings,
            actions=actions,
            view_as=view_as,
        )

        workflow_dry_run_parameters_request.additional_properties = d
        return workflow_dry_run_parameters_request

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
