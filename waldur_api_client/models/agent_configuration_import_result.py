from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.agent_configuration import AgentConfiguration
    from ..models.agent_configuration_change import AgentConfigurationChange
    from ..models.agent_configuration_import_result_errors import AgentConfigurationImportResultErrors
    from ..models.component_difference import ComponentDifference
    from ..models.ignored_key import IgnoredKey
    from ..models.imported_offering_block import ImportedOfferingBlock
    from ..models.imported_policy import ImportedPolicy
    from ..models.unresolved_setting import UnresolvedSetting


T = TypeVar("T", bound="AgentConfigurationImportResult")


@_attrs_define
class AgentConfigurationImportResult:
    """
    Attributes:
        offerings (list['ImportedOfferingBlock']):
        selected_index (int):
        agent_configuration (AgentConfiguration):
        current (AgentConfiguration):
        changes (list['AgentConfigurationChange']):
        dropped_secrets (list[str]):
        unresolved (list['UnresolvedSetting']):
        ignored (list['IgnoredKey']):
        component_differences (list['ComponentDifference']):
        policy (Union['ImportedPolicy', None]): The block's policy_settings against the offering's SLURM periodic usage
            policy; null when the block has none.
        errors (AgentConfigurationImportResultErrors): Why the proposed configuration cannot be saved, in the shape of
            update_integration's agent_configuration errors, with apply_components and policy for the changes opted into;
            empty when it can.
        applied (bool):
    """

    offerings: list["ImportedOfferingBlock"]
    selected_index: int
    agent_configuration: "AgentConfiguration"
    current: "AgentConfiguration"
    changes: list["AgentConfigurationChange"]
    dropped_secrets: list[str]
    unresolved: list["UnresolvedSetting"]
    ignored: list["IgnoredKey"]
    component_differences: list["ComponentDifference"]
    policy: Union["ImportedPolicy", None]
    errors: "AgentConfigurationImportResultErrors"
    applied: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.imported_policy import ImportedPolicy

        offerings = []
        for offerings_item_data in self.offerings:
            offerings_item = offerings_item_data.to_dict()
            offerings.append(offerings_item)

        selected_index = self.selected_index

        agent_configuration = self.agent_configuration.to_dict()

        current = self.current.to_dict()

        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)

        dropped_secrets = self.dropped_secrets

        unresolved = []
        for unresolved_item_data in self.unresolved:
            unresolved_item = unresolved_item_data.to_dict()
            unresolved.append(unresolved_item)

        ignored = []
        for ignored_item_data in self.ignored:
            ignored_item = ignored_item_data.to_dict()
            ignored.append(ignored_item)

        component_differences = []
        for component_differences_item_data in self.component_differences:
            component_differences_item = component_differences_item_data.to_dict()
            component_differences.append(component_differences_item)

        policy: Union[None, dict[str, Any]]
        if isinstance(self.policy, ImportedPolicy):
            policy = self.policy.to_dict()
        else:
            policy = self.policy

        errors = self.errors.to_dict()

        applied = self.applied

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offerings": offerings,
                "selected_index": selected_index,
                "agent_configuration": agent_configuration,
                "current": current,
                "changes": changes,
                "dropped_secrets": dropped_secrets,
                "unresolved": unresolved,
                "ignored": ignored,
                "component_differences": component_differences,
                "policy": policy,
                "errors": errors,
                "applied": applied,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_configuration import AgentConfiguration
        from ..models.agent_configuration_change import AgentConfigurationChange
        from ..models.agent_configuration_import_result_errors import AgentConfigurationImportResultErrors
        from ..models.component_difference import ComponentDifference
        from ..models.ignored_key import IgnoredKey
        from ..models.imported_offering_block import ImportedOfferingBlock
        from ..models.imported_policy import ImportedPolicy
        from ..models.unresolved_setting import UnresolvedSetting

        d = dict(src_dict)
        offerings = []
        _offerings = d.pop("offerings")
        for offerings_item_data in _offerings:
            offerings_item = ImportedOfferingBlock.from_dict(offerings_item_data)

            offerings.append(offerings_item)

        selected_index = d.pop("selected_index")

        agent_configuration = AgentConfiguration.from_dict(d.pop("agent_configuration"))

        current = AgentConfiguration.from_dict(d.pop("current"))

        changes = []
        _changes = d.pop("changes")
        for changes_item_data in _changes:
            changes_item = AgentConfigurationChange.from_dict(changes_item_data)

            changes.append(changes_item)

        dropped_secrets = cast(list[str], d.pop("dropped_secrets"))

        unresolved = []
        _unresolved = d.pop("unresolved")
        for unresolved_item_data in _unresolved:
            unresolved_item = UnresolvedSetting.from_dict(unresolved_item_data)

            unresolved.append(unresolved_item)

        ignored = []
        _ignored = d.pop("ignored")
        for ignored_item_data in _ignored:
            ignored_item = IgnoredKey.from_dict(ignored_item_data)

            ignored.append(ignored_item)

        component_differences = []
        _component_differences = d.pop("component_differences")
        for component_differences_item_data in _component_differences:
            component_differences_item = ComponentDifference.from_dict(component_differences_item_data)

            component_differences.append(component_differences_item)

        def _parse_policy(data: object) -> Union["ImportedPolicy", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                policy_type_1 = ImportedPolicy.from_dict(data)

                return policy_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ImportedPolicy", None], data)

        policy = _parse_policy(d.pop("policy"))

        errors = AgentConfigurationImportResultErrors.from_dict(d.pop("errors"))

        applied = d.pop("applied")

        agent_configuration_import_result = cls(
            offerings=offerings,
            selected_index=selected_index,
            agent_configuration=agent_configuration,
            current=current,
            changes=changes,
            dropped_secrets=dropped_secrets,
            unresolved=unresolved,
            ignored=ignored,
            component_differences=component_differences,
            policy=policy,
            errors=errors,
            applied=applied,
        )

        agent_configuration_import_result.additional_properties = d
        return agent_configuration_import_result

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
