from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_path import WorkflowPath


T = TypeVar("T", bound="WorkflowPaths")


@_attrs_define
class WorkflowPaths:
    """
    Attributes:
        round_ (Union[None, str]):
        scenarios_known (bool): Whether the call has saved scenarios to compare against.
        paths (list['WorkflowPath']):
    """

    round_: Union[None, str]
    scenarios_known: bool
    paths: list["WorkflowPath"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        round_: Union[None, str]
        round_ = self.round_

        scenarios_known = self.scenarios_known

        paths = []
        for paths_item_data in self.paths:
            paths_item = paths_item_data.to_dict()
            paths.append(paths_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "round": round_,
                "scenarios_known": scenarios_known,
                "paths": paths,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_path import WorkflowPath

        d = dict(src_dict)

        def _parse_round_(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        round_ = _parse_round_(d.pop("round"))

        scenarios_known = d.pop("scenarios_known")

        paths = []
        _paths = d.pop("paths")
        for paths_item_data in _paths:
            paths_item = WorkflowPath.from_dict(paths_item_data)

            paths.append(paths_item)

        workflow_paths = cls(
            round_=round_,
            scenarios_known=scenarios_known,
            paths=paths,
        )

        workflow_paths.additional_properties = d
        return workflow_paths

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
