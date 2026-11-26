import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.option_secret_source_enum import OptionSecretSourceEnum

T = TypeVar("T", bound="ResourceOptionSecretStatus")


@_attrs_define
class ResourceOptionSecretStatus:
    """
    Attributes:
        is_set (bool):
        source (Union[None, OptionSecretSourceEnum]): Who set it: the customer or the provider. Null when not set.
        modified (Union[None, datetime.datetime]): When it was last set. Null when not set.
    """

    is_set: bool
    source: Union[None, OptionSecretSourceEnum]
    modified: Union[None, datetime.datetime]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_set = self.is_set

        source: Union[None, str]
        if isinstance(self.source, OptionSecretSourceEnum):
            source = self.source.value
        else:
            source = self.source

        modified: Union[None, str]
        if isinstance(self.modified, datetime.datetime):
            modified = self.modified.isoformat()
        else:
            modified = self.modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_set": is_set,
                "source": source,
                "modified": modified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_set = d.pop("is_set")

        def _parse_source(data: object) -> Union[None, OptionSecretSourceEnum]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_0 = OptionSecretSourceEnum(data)

                return source_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, OptionSecretSourceEnum], data)

        source = _parse_source(d.pop("source"))

        def _parse_modified(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_type_0 = isoparse(data)

                return modified_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        modified = _parse_modified(d.pop("modified"))

        resource_option_secret_status = cls(
            is_set=is_set,
            source=source,
            modified=modified,
        )

        resource_option_secret_status.additional_properties = d
        return resource_option_secret_status

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
