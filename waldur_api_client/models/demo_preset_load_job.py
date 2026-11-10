import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.demo_preset_load_job_state_enum import DemoPresetLoadJobStateEnum

T = TypeVar("T", bound="DemoPresetLoadJob")


@_attrs_define
class DemoPresetLoadJob:
    """
    Attributes:
        uuid (UUID):
        preset (str):
        state (DemoPresetLoadJobStateEnum):
        created (datetime.datetime):
        started_at (Union[None, datetime.datetime]):
        finished_at (Union[None, datetime.datetime]):
        error_message (str):
    """

    uuid: UUID
    preset: str
    state: DemoPresetLoadJobStateEnum
    created: datetime.datetime
    started_at: Union[None, datetime.datetime]
    finished_at: Union[None, datetime.datetime]
    error_message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        preset = self.preset

        state = self.state.value

        created = self.created.isoformat()

        started_at: Union[None, str]
        if isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        finished_at: Union[None, str]
        if isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "preset": preset,
                "state": state,
                "created": created,
                "started_at": started_at,
                "finished_at": finished_at,
                "error_message": error_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        preset = d.pop("preset")

        state = DemoPresetLoadJobStateEnum(d.pop("state"))

        created = isoparse(d.pop("created"))

        def _parse_started_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        started_at = _parse_started_at(d.pop("started_at"))

        def _parse_finished_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = isoparse(data)

                return finished_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        finished_at = _parse_finished_at(d.pop("finished_at"))

        error_message = d.pop("error_message")

        demo_preset_load_job = cls(
            uuid=uuid,
            preset=preset,
            state=state,
            created=created,
            started_at=started_at,
            finished_at=finished_at,
            error_message=error_message,
        )

        demo_preset_load_job.additional_properties = d
        return demo_preset_load_job

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
