from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BackendMetadata")


@_attrs_define
class BackendMetadata:
    """
    Attributes:
        state (str):
        runtime_state (str):
        action (str):
        instance_name (Union[None, str]):
    """

    state: str
    runtime_state: str
    action: str
    instance_name: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        runtime_state = self.runtime_state

        action = self.action

        instance_name: Union[None, str]
        instance_name = self.instance_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "runtime_state": runtime_state,
                "action": action,
                "instance_name": instance_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        state = d.pop("state")

        runtime_state = d.pop("runtime_state")

        action = d.pop("action")

        def _parse_instance_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        instance_name = _parse_instance_name(d.pop("instance_name"))

        backend_metadata = cls(
            state=state,
            runtime_state=runtime_state,
            action=action,
            instance_name=instance_name,
        )

        backend_metadata.additional_properties = d
        return backend_metadata

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
