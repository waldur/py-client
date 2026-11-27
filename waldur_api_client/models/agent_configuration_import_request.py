from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_configuration_import_request_values import AgentConfigurationImportRequestValues
    from ..models.apply_component_request import ApplyComponentRequest


T = TypeVar("T", bound="AgentConfigurationImportRequest")


@_attrs_define
class AgentConfigurationImportRequest:
    """
    Attributes:
        configuration (str): The site agent configuration file, as YAML text.
        offering_index (Union[None, Unset, int]): Which entry of the file's offerings list to import. By default the one
            whose waldur_offering_uuid is this offering, else the only one.
        dry_run (Union[Unset, bool]): Only show what would change; save nothing. Default: True.
        values (Union[Unset, AgentConfigurationImportRequestValues]): Values for settings the file leaves to the agent
            host's environment (see unresolved) or does not set, by dotted path such as backend_settings.cscs_dwdi_api_url.
            Never a secret.
        apply_components (Union[Unset, list['ApplyComponentRequest']]): Component differences to apply to the offering's
            components; each must be applicable.
        policy_actions (Union[Unset, list[str]]): What the SLURM periodic usage policy does when it fires, as action
            names from policy.action_choices. Required when apply_policy creates the policy; when it exists, given replaces
            its actions and left out keeps them.
        apply_policy (Union[Unset, bool]): Create or update the offering's SLURM periodic usage policy from the block's
            policy_settings. Default: False.
    """

    configuration: str
    offering_index: Union[None, Unset, int] = UNSET
    dry_run: Union[Unset, bool] = True
    values: Union[Unset, "AgentConfigurationImportRequestValues"] = UNSET
    apply_components: Union[Unset, list["ApplyComponentRequest"]] = UNSET
    policy_actions: Union[Unset, list[str]] = UNSET
    apply_policy: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration

        offering_index: Union[None, Unset, int]
        if isinstance(self.offering_index, Unset):
            offering_index = UNSET
        else:
            offering_index = self.offering_index

        dry_run = self.dry_run

        values: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        apply_components: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.apply_components, Unset):
            apply_components = []
            for apply_components_item_data in self.apply_components:
                apply_components_item = apply_components_item_data.to_dict()
                apply_components.append(apply_components_item)

        policy_actions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.policy_actions, Unset):
            policy_actions = self.policy_actions

        apply_policy = self.apply_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
            }
        )
        if offering_index is not UNSET:
            field_dict["offering_index"] = offering_index
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if values is not UNSET:
            field_dict["values"] = values
        if apply_components is not UNSET:
            field_dict["apply_components"] = apply_components
        if policy_actions is not UNSET:
            field_dict["policy_actions"] = policy_actions
        if apply_policy is not UNSET:
            field_dict["apply_policy"] = apply_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_configuration_import_request_values import AgentConfigurationImportRequestValues
        from ..models.apply_component_request import ApplyComponentRequest

        d = dict(src_dict)
        configuration = d.pop("configuration")

        def _parse_offering_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        offering_index = _parse_offering_index(d.pop("offering_index", UNSET))

        dry_run = d.pop("dry_run", UNSET)

        _values = d.pop("values", UNSET)
        values: Union[Unset, AgentConfigurationImportRequestValues]
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = AgentConfigurationImportRequestValues.from_dict(_values)

        apply_components = []
        _apply_components = d.pop("apply_components", UNSET)
        for apply_components_item_data in _apply_components or []:
            apply_components_item = ApplyComponentRequest.from_dict(apply_components_item_data)

            apply_components.append(apply_components_item)

        policy_actions = cast(list[str], d.pop("policy_actions", UNSET))

        apply_policy = d.pop("apply_policy", UNSET)

        agent_configuration_import_request = cls(
            configuration=configuration,
            offering_index=offering_index,
            dry_run=dry_run,
            values=values,
            apply_components=apply_components,
            policy_actions=policy_actions,
            apply_policy=apply_policy,
        )

        agent_configuration_import_request.additional_properties = d
        return agent_configuration_import_request

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
