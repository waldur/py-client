import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_template_document import CallTemplateDocument
    from ..models.call_template_origin import CallTemplateOrigin
    from ..models.call_template_preset_info import CallTemplatePresetInfo
    from ..models.call_template_scenarios_item import CallTemplateScenariosItem
    from ..models.call_template_step import CallTemplateStep


T = TypeVar("T", bound="CallTemplate")


@_attrs_define
class CallTemplate:
    """
    Attributes:
        uuid (UUID):
        name (str):
        document (CallTemplateDocument): Call document in the export format, as a mapping or a YAML string: call
            settings and workflow, without rounds, requested offerings or documents.
        schema_version (int):
        preset (Union['CallTemplatePresetInfo', None]): The preset block of the template's own document: where the
            process it models comes from; null when it does not say.
        origin (Union['CallTemplateOrigin', None]): Organization, process and reference page of the process this
            template models; null when it does not say.
        steps (list['CallTemplateStep']):
        created_by (Union[None, UUID]):
        created (datetime.datetime):
        modified (datetime.datetime):
        warnings (list[str]): What a call created from the saved document would leave out, such as forms or roles this
            portal does not have.
        description (Union[Unset, str]):
        is_published (Union[Unset, bool]):
        scenarios (Union[Unset, list['CallTemplateScenariosItem']]): Named paths through the workflow: {key, name,
            description, request: {offerings, actions}, assertions}. Definitions only: they run as dry runs on each call
            created from the template.
    """

    uuid: UUID
    name: str
    document: "CallTemplateDocument"
    schema_version: int
    preset: Union["CallTemplatePresetInfo", None]
    origin: Union["CallTemplateOrigin", None]
    steps: list["CallTemplateStep"]
    created_by: Union[None, UUID]
    created: datetime.datetime
    modified: datetime.datetime
    warnings: list[str]
    description: Union[Unset, str] = UNSET
    is_published: Union[Unset, bool] = UNSET
    scenarios: Union[Unset, list["CallTemplateScenariosItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.call_template_origin import CallTemplateOrigin
        from ..models.call_template_preset_info import CallTemplatePresetInfo

        uuid = str(self.uuid)

        name = self.name

        document = self.document.to_dict()

        schema_version = self.schema_version

        preset: Union[None, dict[str, Any]]
        if isinstance(self.preset, CallTemplatePresetInfo):
            preset = self.preset.to_dict()
        else:
            preset = self.preset

        origin: Union[None, dict[str, Any]]
        if isinstance(self.origin, CallTemplateOrigin):
            origin = self.origin.to_dict()
        else:
            origin = self.origin

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        created_by: Union[None, str]
        if isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        warnings = self.warnings

        description = self.description

        is_published = self.is_published

        scenarios: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.scenarios, Unset):
            scenarios = []
            for scenarios_item_data in self.scenarios:
                scenarios_item = scenarios_item_data.to_dict()
                scenarios.append(scenarios_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "document": document,
                "schema_version": schema_version,
                "preset": preset,
                "origin": origin,
                "steps": steps,
                "created_by": created_by,
                "created": created,
                "modified": modified,
                "warnings": warnings,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if scenarios is not UNSET:
            field_dict["scenarios"] = scenarios

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.call_template_document import CallTemplateDocument
        from ..models.call_template_origin import CallTemplateOrigin
        from ..models.call_template_preset_info import CallTemplatePresetInfo
        from ..models.call_template_scenarios_item import CallTemplateScenariosItem
        from ..models.call_template_step import CallTemplateStep

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        document = CallTemplateDocument.from_dict(d.pop("document"))

        schema_version = d.pop("schema_version")

        def _parse_preset(data: object) -> Union["CallTemplatePresetInfo", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                preset_type_1 = CallTemplatePresetInfo.from_dict(data)

                return preset_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CallTemplatePresetInfo", None], data)

        preset = _parse_preset(d.pop("preset"))

        def _parse_origin(data: object) -> Union["CallTemplateOrigin", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                origin_type_1 = CallTemplateOrigin.from_dict(data)

                return origin_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CallTemplateOrigin", None], data)

        origin = _parse_origin(d.pop("origin"))

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = CallTemplateStep.from_dict(steps_item_data)

            steps.append(steps_item)

        def _parse_created_by(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        created_by = _parse_created_by(d.pop("created_by"))

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        warnings = cast(list[str], d.pop("warnings"))

        description = d.pop("description", UNSET)

        is_published = d.pop("is_published", UNSET)

        scenarios = []
        _scenarios = d.pop("scenarios", UNSET)
        for scenarios_item_data in _scenarios or []:
            scenarios_item = CallTemplateScenariosItem.from_dict(scenarios_item_data)

            scenarios.append(scenarios_item)

        call_template = cls(
            uuid=uuid,
            name=name,
            document=document,
            schema_version=schema_version,
            preset=preset,
            origin=origin,
            steps=steps,
            created_by=created_by,
            created=created,
            modified=modified,
            warnings=warnings,
            description=description,
            is_published=is_published,
            scenarios=scenarios,
        )

        call_template.additional_properties = d
        return call_template

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
