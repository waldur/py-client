from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.load_balancer_mode_enum import LoadBalancerModeEnum
from ..models.topology_mode_enum import TopologyModeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.k8s_egress_rule_request import K8SEgressRuleRequest


T = TypeVar("T", bound="K8SDefaultConfigurationRequest")


@_attrs_define
class K8SDefaultConfigurationRequest:
    """
    Attributes:
        default_controller_vcpus (Union[Unset, int]):
        default_controller_ram_gb (Union[Unset, int]):
        default_controller_system_disk_gb (Union[Unset, int]):
        default_controller_etcd_disk_gb (Union[Unset, int]):
        default_lb_vcpus (Union[Unset, int]):
        default_lb_ram_gb (Union[Unset, int]):
        default_lb_system_disk_gb (Union[Unset, int]):
        default_lb_logs_disk_gb (Union[Unset, int]):
        load_balancer_mode (Union[Unset, LoadBalancerModeEnum]):
        topology_mode (Union[Unset, TopologyModeEnum]):
        minimal_worker_vcpus (Union[Unset, int]):
        minimal_worker_ram_gb (Union[Unset, int]):
        default_worker_data_disk_gb (Union[Unset, int]):
        default_storage_data_disk_gb (Union[Unset, int]):
        default_storage_san_disk_gb (Union[Unset, int]):
        available_kubernetes_versions (Union[Unset, str]): Comma-separated list of Kubernetes versions (e.g.,
            1.32.0,1.33.0,1.34.0)
        egress_rules_enabled (Union[Unset, bool]): Whether customers may restrict the cluster's outbound traffic to a
            list of destinations (egress_rules). Off when omitted.
        egress_domain_rules_allowed (Union[Unset, bool]): Whether customers' egress rules may name domains; otherwise
            only networks (CIDR). Off when omitted.
        egress_baseline_rules (Union[Unset, list['K8SEgressRuleRequest']]): Destinations every cluster of the offering
            may reach, such as DNS, NTP and image registries. Shown to customers read-only; once a cluster has any egress
            rule, outbound traffic is allowed to these and to the customer's destinations only.
    """

    default_controller_vcpus: Union[Unset, int] = UNSET
    default_controller_ram_gb: Union[Unset, int] = UNSET
    default_controller_system_disk_gb: Union[Unset, int] = UNSET
    default_controller_etcd_disk_gb: Union[Unset, int] = UNSET
    default_lb_vcpus: Union[Unset, int] = UNSET
    default_lb_ram_gb: Union[Unset, int] = UNSET
    default_lb_system_disk_gb: Union[Unset, int] = UNSET
    default_lb_logs_disk_gb: Union[Unset, int] = UNSET
    load_balancer_mode: Union[Unset, LoadBalancerModeEnum] = UNSET
    topology_mode: Union[Unset, TopologyModeEnum] = UNSET
    minimal_worker_vcpus: Union[Unset, int] = UNSET
    minimal_worker_ram_gb: Union[Unset, int] = UNSET
    default_worker_data_disk_gb: Union[Unset, int] = UNSET
    default_storage_data_disk_gb: Union[Unset, int] = UNSET
    default_storage_san_disk_gb: Union[Unset, int] = UNSET
    available_kubernetes_versions: Union[Unset, str] = UNSET
    egress_rules_enabled: Union[Unset, bool] = UNSET
    egress_domain_rules_allowed: Union[Unset, bool] = UNSET
    egress_baseline_rules: Union[Unset, list["K8SEgressRuleRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_controller_vcpus = self.default_controller_vcpus

        default_controller_ram_gb = self.default_controller_ram_gb

        default_controller_system_disk_gb = self.default_controller_system_disk_gb

        default_controller_etcd_disk_gb = self.default_controller_etcd_disk_gb

        default_lb_vcpus = self.default_lb_vcpus

        default_lb_ram_gb = self.default_lb_ram_gb

        default_lb_system_disk_gb = self.default_lb_system_disk_gb

        default_lb_logs_disk_gb = self.default_lb_logs_disk_gb

        load_balancer_mode: Union[Unset, str] = UNSET
        if not isinstance(self.load_balancer_mode, Unset):
            load_balancer_mode = self.load_balancer_mode.value

        topology_mode: Union[Unset, str] = UNSET
        if not isinstance(self.topology_mode, Unset):
            topology_mode = self.topology_mode.value

        minimal_worker_vcpus = self.minimal_worker_vcpus

        minimal_worker_ram_gb = self.minimal_worker_ram_gb

        default_worker_data_disk_gb = self.default_worker_data_disk_gb

        default_storage_data_disk_gb = self.default_storage_data_disk_gb

        default_storage_san_disk_gb = self.default_storage_san_disk_gb

        available_kubernetes_versions = self.available_kubernetes_versions

        egress_rules_enabled = self.egress_rules_enabled

        egress_domain_rules_allowed = self.egress_domain_rules_allowed

        egress_baseline_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.egress_baseline_rules, Unset):
            egress_baseline_rules = []
            for egress_baseline_rules_item_data in self.egress_baseline_rules:
                egress_baseline_rules_item = egress_baseline_rules_item_data.to_dict()
                egress_baseline_rules.append(egress_baseline_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_controller_vcpus is not UNSET:
            field_dict["default_controller_vcpus"] = default_controller_vcpus
        if default_controller_ram_gb is not UNSET:
            field_dict["default_controller_ram_gb"] = default_controller_ram_gb
        if default_controller_system_disk_gb is not UNSET:
            field_dict["default_controller_system_disk_gb"] = default_controller_system_disk_gb
        if default_controller_etcd_disk_gb is not UNSET:
            field_dict["default_controller_etcd_disk_gb"] = default_controller_etcd_disk_gb
        if default_lb_vcpus is not UNSET:
            field_dict["default_lb_vcpus"] = default_lb_vcpus
        if default_lb_ram_gb is not UNSET:
            field_dict["default_lb_ram_gb"] = default_lb_ram_gb
        if default_lb_system_disk_gb is not UNSET:
            field_dict["default_lb_system_disk_gb"] = default_lb_system_disk_gb
        if default_lb_logs_disk_gb is not UNSET:
            field_dict["default_lb_logs_disk_gb"] = default_lb_logs_disk_gb
        if load_balancer_mode is not UNSET:
            field_dict["load_balancer_mode"] = load_balancer_mode
        if topology_mode is not UNSET:
            field_dict["topology_mode"] = topology_mode
        if minimal_worker_vcpus is not UNSET:
            field_dict["minimal_worker_vcpus"] = minimal_worker_vcpus
        if minimal_worker_ram_gb is not UNSET:
            field_dict["minimal_worker_ram_gb"] = minimal_worker_ram_gb
        if default_worker_data_disk_gb is not UNSET:
            field_dict["default_worker_data_disk_gb"] = default_worker_data_disk_gb
        if default_storage_data_disk_gb is not UNSET:
            field_dict["default_storage_data_disk_gb"] = default_storage_data_disk_gb
        if default_storage_san_disk_gb is not UNSET:
            field_dict["default_storage_san_disk_gb"] = default_storage_san_disk_gb
        if available_kubernetes_versions is not UNSET:
            field_dict["available_kubernetes_versions"] = available_kubernetes_versions
        if egress_rules_enabled is not UNSET:
            field_dict["egress_rules_enabled"] = egress_rules_enabled
        if egress_domain_rules_allowed is not UNSET:
            field_dict["egress_domain_rules_allowed"] = egress_domain_rules_allowed
        if egress_baseline_rules is not UNSET:
            field_dict["egress_baseline_rules"] = egress_baseline_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.k8s_egress_rule_request import K8SEgressRuleRequest

        d = dict(src_dict)
        default_controller_vcpus = d.pop("default_controller_vcpus", UNSET)

        default_controller_ram_gb = d.pop("default_controller_ram_gb", UNSET)

        default_controller_system_disk_gb = d.pop("default_controller_system_disk_gb", UNSET)

        default_controller_etcd_disk_gb = d.pop("default_controller_etcd_disk_gb", UNSET)

        default_lb_vcpus = d.pop("default_lb_vcpus", UNSET)

        default_lb_ram_gb = d.pop("default_lb_ram_gb", UNSET)

        default_lb_system_disk_gb = d.pop("default_lb_system_disk_gb", UNSET)

        default_lb_logs_disk_gb = d.pop("default_lb_logs_disk_gb", UNSET)

        _load_balancer_mode = d.pop("load_balancer_mode", UNSET)
        load_balancer_mode: Union[Unset, LoadBalancerModeEnum]
        if isinstance(_load_balancer_mode, Unset):
            load_balancer_mode = UNSET
        else:
            load_balancer_mode = LoadBalancerModeEnum(_load_balancer_mode)

        _topology_mode = d.pop("topology_mode", UNSET)
        topology_mode: Union[Unset, TopologyModeEnum]
        if isinstance(_topology_mode, Unset):
            topology_mode = UNSET
        else:
            topology_mode = TopologyModeEnum(_topology_mode)

        minimal_worker_vcpus = d.pop("minimal_worker_vcpus", UNSET)

        minimal_worker_ram_gb = d.pop("minimal_worker_ram_gb", UNSET)

        default_worker_data_disk_gb = d.pop("default_worker_data_disk_gb", UNSET)

        default_storage_data_disk_gb = d.pop("default_storage_data_disk_gb", UNSET)

        default_storage_san_disk_gb = d.pop("default_storage_san_disk_gb", UNSET)

        available_kubernetes_versions = d.pop("available_kubernetes_versions", UNSET)

        egress_rules_enabled = d.pop("egress_rules_enabled", UNSET)

        egress_domain_rules_allowed = d.pop("egress_domain_rules_allowed", UNSET)

        egress_baseline_rules = []
        _egress_baseline_rules = d.pop("egress_baseline_rules", UNSET)
        for egress_baseline_rules_item_data in _egress_baseline_rules or []:
            egress_baseline_rules_item = K8SEgressRuleRequest.from_dict(egress_baseline_rules_item_data)

            egress_baseline_rules.append(egress_baseline_rules_item)

        k8s_default_configuration_request = cls(
            default_controller_vcpus=default_controller_vcpus,
            default_controller_ram_gb=default_controller_ram_gb,
            default_controller_system_disk_gb=default_controller_system_disk_gb,
            default_controller_etcd_disk_gb=default_controller_etcd_disk_gb,
            default_lb_vcpus=default_lb_vcpus,
            default_lb_ram_gb=default_lb_ram_gb,
            default_lb_system_disk_gb=default_lb_system_disk_gb,
            default_lb_logs_disk_gb=default_lb_logs_disk_gb,
            load_balancer_mode=load_balancer_mode,
            topology_mode=topology_mode,
            minimal_worker_vcpus=minimal_worker_vcpus,
            minimal_worker_ram_gb=minimal_worker_ram_gb,
            default_worker_data_disk_gb=default_worker_data_disk_gb,
            default_storage_data_disk_gb=default_storage_data_disk_gb,
            default_storage_san_disk_gb=default_storage_san_disk_gb,
            available_kubernetes_versions=available_kubernetes_versions,
            egress_rules_enabled=egress_rules_enabled,
            egress_domain_rules_allowed=egress_domain_rules_allowed,
            egress_baseline_rules=egress_baseline_rules,
        )

        k8s_default_configuration_request.additional_properties = d
        return k8s_default_configuration_request

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
