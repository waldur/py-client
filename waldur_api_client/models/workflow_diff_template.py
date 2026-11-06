from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowDiffTemplate")


@_attrs_define
class WorkflowDiffTemplate:
    """
    Attributes:
        uuid (UUID):
        name (str):
        version (Union[None, int]): The version the call was created from.
        latest_version (int):
    """

    uuid: UUID
    name: str
    version: Union[None, int]
    latest_version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        version: Union[None, int]
        version = self.version

        latest_version = self.latest_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "version": version,
                "latest_version": latest_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        def _parse_version(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        version = _parse_version(d.pop("version"))

        latest_version = d.pop("latest_version")

        workflow_diff_template = cls(
            uuid=uuid,
            name=name,
            version=version,
            latest_version=latest_version,
        )

        workflow_diff_template.additional_properties = d
        return workflow_diff_template

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
