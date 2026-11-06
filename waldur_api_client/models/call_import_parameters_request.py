from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_import_parameters_request_call_data import CallImportParametersRequestCallData


T = TypeVar("T", bound="CallImportParametersRequest")


@_attrs_define
class CallImportParametersRequest:
    """
    Attributes:
        manager (UUID): Call managing organization that will own the imported call.
        name (Union[Unset, str]): Name for the imported call. Defaults to the exported name.
        call_data (Union[Unset, CallImportParametersRequestCallData]): Exported call document, as a mapping or a YAML
            string. Give this or template.
        template (Union[Unset, UUID]): Published call template to create the call from. Give this or call_data.
        import_documents (Union[Unset, bool]):  Default: True.
        import_rounds (Union[Unset, bool]):  Default: True.
        import_offerings (Union[Unset, bool]):  Default: True.
        import_workflow_steps (Union[Unset, bool]):  Default: True.
        import_field_configs (Union[Unset, bool]):  Default: True.
        import_review_configs (Union[Unset, bool]):  Default: True.
        import_role_mappings (Union[Unset, bool]):  Default: True.
        import_compliance_checklist (Union[Unset, bool]):  Default: True.
    """

    manager: UUID
    name: Union[Unset, str] = UNSET
    call_data: Union[Unset, "CallImportParametersRequestCallData"] = UNSET
    template: Union[Unset, UUID] = UNSET
    import_documents: Union[Unset, bool] = True
    import_rounds: Union[Unset, bool] = True
    import_offerings: Union[Unset, bool] = True
    import_workflow_steps: Union[Unset, bool] = True
    import_field_configs: Union[Unset, bool] = True
    import_review_configs: Union[Unset, bool] = True
    import_role_mappings: Union[Unset, bool] = True
    import_compliance_checklist: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        manager = str(self.manager)

        name = self.name

        call_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.call_data, Unset):
            call_data = self.call_data.to_dict()

        template: Union[Unset, str] = UNSET
        if not isinstance(self.template, Unset):
            template = str(self.template)

        import_documents = self.import_documents

        import_rounds = self.import_rounds

        import_offerings = self.import_offerings

        import_workflow_steps = self.import_workflow_steps

        import_field_configs = self.import_field_configs

        import_review_configs = self.import_review_configs

        import_role_mappings = self.import_role_mappings

        import_compliance_checklist = self.import_compliance_checklist

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "manager": manager,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if call_data is not UNSET:
            field_dict["call_data"] = call_data
        if template is not UNSET:
            field_dict["template"] = template
        if import_documents is not UNSET:
            field_dict["import_documents"] = import_documents
        if import_rounds is not UNSET:
            field_dict["import_rounds"] = import_rounds
        if import_offerings is not UNSET:
            field_dict["import_offerings"] = import_offerings
        if import_workflow_steps is not UNSET:
            field_dict["import_workflow_steps"] = import_workflow_steps
        if import_field_configs is not UNSET:
            field_dict["import_field_configs"] = import_field_configs
        if import_review_configs is not UNSET:
            field_dict["import_review_configs"] = import_review_configs
        if import_role_mappings is not UNSET:
            field_dict["import_role_mappings"] = import_role_mappings
        if import_compliance_checklist is not UNSET:
            field_dict["import_compliance_checklist"] = import_compliance_checklist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.call_import_parameters_request_call_data import CallImportParametersRequestCallData

        d = dict(src_dict)
        manager = UUID(d.pop("manager"))

        name = d.pop("name", UNSET)

        _call_data = d.pop("call_data", UNSET)
        call_data: Union[Unset, CallImportParametersRequestCallData]
        if isinstance(_call_data, Unset):
            call_data = UNSET
        else:
            call_data = CallImportParametersRequestCallData.from_dict(_call_data)

        _template = d.pop("template", UNSET)
        template: Union[Unset, UUID]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = UUID(_template)

        import_documents = d.pop("import_documents", UNSET)

        import_rounds = d.pop("import_rounds", UNSET)

        import_offerings = d.pop("import_offerings", UNSET)

        import_workflow_steps = d.pop("import_workflow_steps", UNSET)

        import_field_configs = d.pop("import_field_configs", UNSET)

        import_review_configs = d.pop("import_review_configs", UNSET)

        import_role_mappings = d.pop("import_role_mappings", UNSET)

        import_compliance_checklist = d.pop("import_compliance_checklist", UNSET)

        call_import_parameters_request = cls(
            manager=manager,
            name=name,
            call_data=call_data,
            template=template,
            import_documents=import_documents,
            import_rounds=import_rounds,
            import_offerings=import_offerings,
            import_workflow_steps=import_workflow_steps,
            import_field_configs=import_field_configs,
            import_review_configs=import_review_configs,
            import_role_mappings=import_role_mappings,
            import_compliance_checklist=import_compliance_checklist,
        )

        call_import_parameters_request.additional_properties = d
        return call_import_parameters_request

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
