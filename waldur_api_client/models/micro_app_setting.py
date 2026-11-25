import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.micro_app_mode_enum import MicroAppModeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MicroAppSetting")


@_attrs_define
class MicroAppSetting:
    """
    Attributes:
        url (str):
        uuid (UUID):
        name (str): The app's directory under apps/ and its path under the portal.
        feature_key (str): The feature_key of the rules that pick this app's audience.
        rules_count (int):
        created (datetime.datetime):
        modified (datetime.datetime):
        mode (Union[Unset, MicroAppModeEnum]):
    """

    url: str
    uuid: UUID
    name: str
    feature_key: str
    rules_count: int
    created: datetime.datetime
    modified: datetime.datetime
    mode: Union[Unset, MicroAppModeEnum] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        uuid = str(self.uuid)

        name = self.name

        feature_key = self.feature_key

        rules_count = self.rules_count

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "feature_key": feature_key,
                "rules_count": rules_count,
                "created": created,
                "modified": modified,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        feature_key = d.pop("feature_key")

        rules_count = d.pop("rules_count")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, MicroAppModeEnum]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = MicroAppModeEnum(_mode)

        micro_app_setting = cls(
            url=url,
            uuid=uuid,
            name=name,
            feature_key=feature_key,
            rules_count=rules_count,
            created=created,
            modified=modified,
            mode=mode,
        )

        micro_app_setting.additional_properties = d
        return micro_app_setting

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
