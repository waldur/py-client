from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cidr_ip_version_enum import CidrIpVersionEnum
from ..models.infrastructure_mode_enum import InfrastructureModeEnum
from ..models.load_balancer_mode_enum import LoadBalancerModeEnum
from ..models.option_secret_source_enum import OptionSecretSourceEnum
from ..models.topology_mode_enum import TopologyModeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cidr_policy_request import CidrPolicyRequest
    from ..models.ipsec_phase_1_policy_request import IpsecPhase1PolicyRequest
    from ..models.ipsec_phase_2_policy_request import IpsecPhase2PolicyRequest
    from ..models.k8s_egress_rule_request import K8SEgressRuleRequest
    from ..models.option_default_configs_request_fixed_openstack_offerings import (
        OptionDefaultConfigsRequestFixedOpenstackOfferings,
    )


T = TypeVar("T", bound="OptionDefaultConfigsRequest")


@_attrs_define
class OptionDefaultConfigsRequest:
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
        infrastructure_mode (Union[Unset, InfrastructureModeEnum]):
        fixed_openstack_offerings (Union[Unset, OptionDefaultConfigsRequestFixedOpenstackOfferings]): With
            provider_fixed: the UUIDs of the OpenStack tenant offerings a cluster is deployed to, per topology, in site
            order. "1-datacenter" takes one, "3-datacenter" three; every topology the option allows needs its list.
        ip_version (Union[Unset, CidrIpVersionEnum]):
        prefix_length_min (Union[Unset, int]): The smallest prefix length allowed, that is the largest network.
        prefix_length_max (Union[Unset, int]): The largest prefix length allowed, that is the smallest network.
        allowed_ranges (Union[Unset, list[str]]): Networks the value must lie inside one of, such as the private ranges
            10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 and fc00::/7. Any network when empty.
        excluded_ranges (Union[Unset, list[str]]): Networks the value must not overlap.
        max_items (Union[Unset, int]): For a list: the most networks it may hold.
        multiple (Union[Unset, bool]): Whether the value is a list of networks. Off when omitted.
        secret_source (Union[Unset, OptionSecretSourceEnum]):
        customer_can_reveal (Union[Unset, bool]): Whether users holding RESOURCE.REVEAL_API_KEY on the resource's
            project or organization may read the secret back. When omitted: no for a customer-set secret, yes for a
            provider-set one.
        min_length (Union[Unset, int]): 1 when omitted.
        max_length (Union[Unset, int]): 4096 when omitted; at most 65536.
        multiline (Union[Unset, bool]): Whether the secret may span lines, such as a PEM key or a kubeconfig. Off when
            omitted.
        ikev1_allowed (Union[Unset, bool]): Whether IKEv1 is accepted. Off when omitted.
        allow_private_peer (Union[Unset, bool]): Whether the customer's gateway may have a private, loopback, link-
            local, multicast, reserved or CGNAT address. Off when omitted.
        provider_gateway_ip (Union[Unset, str]): The provider's end of new tunnels: its gateway's IP address.
        provider_local_subnets (Union[Unset, list[str]]): The provider's end of new tunnels: the networks behind it.
        remote_subnets (Union[Unset, CidrPolicyRequest]):
        no_overlap_with (Union[Unset, list[str]]): Names of cidr options whose networks the remote subnets must not
            overlap. A resource option may name order options too.
        phase1 (Union[Unset, IpsecPhase1PolicyRequest]):
        phase2 (Union[Unset, IpsecPhase2PolicyRequest]):
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
    infrastructure_mode: Union[Unset, InfrastructureModeEnum] = UNSET
    fixed_openstack_offerings: Union[Unset, "OptionDefaultConfigsRequestFixedOpenstackOfferings"] = UNSET
    ip_version: Union[Unset, CidrIpVersionEnum] = UNSET
    prefix_length_min: Union[Unset, int] = UNSET
    prefix_length_max: Union[Unset, int] = UNSET
    allowed_ranges: Union[Unset, list[str]] = UNSET
    excluded_ranges: Union[Unset, list[str]] = UNSET
    max_items: Union[Unset, int] = UNSET
    multiple: Union[Unset, bool] = UNSET
    secret_source: Union[Unset, OptionSecretSourceEnum] = UNSET
    customer_can_reveal: Union[Unset, bool] = UNSET
    min_length: Union[Unset, int] = UNSET
    max_length: Union[Unset, int] = UNSET
    multiline: Union[Unset, bool] = UNSET
    ikev1_allowed: Union[Unset, bool] = UNSET
    allow_private_peer: Union[Unset, bool] = UNSET
    provider_gateway_ip: Union[Unset, str] = UNSET
    provider_local_subnets: Union[Unset, list[str]] = UNSET
    remote_subnets: Union[Unset, "CidrPolicyRequest"] = UNSET
    no_overlap_with: Union[Unset, list[str]] = UNSET
    phase1: Union[Unset, "IpsecPhase1PolicyRequest"] = UNSET
    phase2: Union[Unset, "IpsecPhase2PolicyRequest"] = UNSET
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

        infrastructure_mode: Union[Unset, str] = UNSET
        if not isinstance(self.infrastructure_mode, Unset):
            infrastructure_mode = self.infrastructure_mode.value

        fixed_openstack_offerings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fixed_openstack_offerings, Unset):
            fixed_openstack_offerings = self.fixed_openstack_offerings.to_dict()

        ip_version: Union[Unset, str] = UNSET
        if not isinstance(self.ip_version, Unset):
            ip_version = self.ip_version.value

        prefix_length_min = self.prefix_length_min

        prefix_length_max = self.prefix_length_max

        allowed_ranges: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_ranges, Unset):
            allowed_ranges = self.allowed_ranges

        excluded_ranges: Union[Unset, list[str]] = UNSET
        if not isinstance(self.excluded_ranges, Unset):
            excluded_ranges = self.excluded_ranges

        max_items = self.max_items

        multiple = self.multiple

        secret_source: Union[Unset, str] = UNSET
        if not isinstance(self.secret_source, Unset):
            secret_source = self.secret_source.value

        customer_can_reveal = self.customer_can_reveal

        min_length = self.min_length

        max_length = self.max_length

        multiline = self.multiline

        ikev1_allowed = self.ikev1_allowed

        allow_private_peer = self.allow_private_peer

        provider_gateway_ip = self.provider_gateway_ip

        provider_local_subnets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.provider_local_subnets, Unset):
            provider_local_subnets = self.provider_local_subnets

        remote_subnets: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.remote_subnets, Unset):
            remote_subnets = self.remote_subnets.to_dict()

        no_overlap_with: Union[Unset, list[str]] = UNSET
        if not isinstance(self.no_overlap_with, Unset):
            no_overlap_with = self.no_overlap_with

        phase1: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.phase1, Unset):
            phase1 = self.phase1.to_dict()

        phase2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.phase2, Unset):
            phase2 = self.phase2.to_dict()

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
        if infrastructure_mode is not UNSET:
            field_dict["infrastructure_mode"] = infrastructure_mode
        if fixed_openstack_offerings is not UNSET:
            field_dict["fixed_openstack_offerings"] = fixed_openstack_offerings
        if ip_version is not UNSET:
            field_dict["ip_version"] = ip_version
        if prefix_length_min is not UNSET:
            field_dict["prefix_length_min"] = prefix_length_min
        if prefix_length_max is not UNSET:
            field_dict["prefix_length_max"] = prefix_length_max
        if allowed_ranges is not UNSET:
            field_dict["allowed_ranges"] = allowed_ranges
        if excluded_ranges is not UNSET:
            field_dict["excluded_ranges"] = excluded_ranges
        if max_items is not UNSET:
            field_dict["max_items"] = max_items
        if multiple is not UNSET:
            field_dict["multiple"] = multiple
        if secret_source is not UNSET:
            field_dict["secret_source"] = secret_source
        if customer_can_reveal is not UNSET:
            field_dict["customer_can_reveal"] = customer_can_reveal
        if min_length is not UNSET:
            field_dict["min_length"] = min_length
        if max_length is not UNSET:
            field_dict["max_length"] = max_length
        if multiline is not UNSET:
            field_dict["multiline"] = multiline
        if ikev1_allowed is not UNSET:
            field_dict["ikev1_allowed"] = ikev1_allowed
        if allow_private_peer is not UNSET:
            field_dict["allow_private_peer"] = allow_private_peer
        if provider_gateway_ip is not UNSET:
            field_dict["provider_gateway_ip"] = provider_gateway_ip
        if provider_local_subnets is not UNSET:
            field_dict["provider_local_subnets"] = provider_local_subnets
        if remote_subnets is not UNSET:
            field_dict["remote_subnets"] = remote_subnets
        if no_overlap_with is not UNSET:
            field_dict["no_overlap_with"] = no_overlap_with
        if phase1 is not UNSET:
            field_dict["phase1"] = phase1
        if phase2 is not UNSET:
            field_dict["phase2"] = phase2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cidr_policy_request import CidrPolicyRequest
        from ..models.ipsec_phase_1_policy_request import IpsecPhase1PolicyRequest
        from ..models.ipsec_phase_2_policy_request import IpsecPhase2PolicyRequest
        from ..models.k8s_egress_rule_request import K8SEgressRuleRequest
        from ..models.option_default_configs_request_fixed_openstack_offerings import (
            OptionDefaultConfigsRequestFixedOpenstackOfferings,
        )

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

        _infrastructure_mode = d.pop("infrastructure_mode", UNSET)
        infrastructure_mode: Union[Unset, InfrastructureModeEnum]
        if isinstance(_infrastructure_mode, Unset):
            infrastructure_mode = UNSET
        else:
            infrastructure_mode = InfrastructureModeEnum(_infrastructure_mode)

        _fixed_openstack_offerings = d.pop("fixed_openstack_offerings", UNSET)
        fixed_openstack_offerings: Union[Unset, OptionDefaultConfigsRequestFixedOpenstackOfferings]
        if isinstance(_fixed_openstack_offerings, Unset):
            fixed_openstack_offerings = UNSET
        else:
            fixed_openstack_offerings = OptionDefaultConfigsRequestFixedOpenstackOfferings.from_dict(
                _fixed_openstack_offerings
            )

        _ip_version = d.pop("ip_version", UNSET)
        ip_version: Union[Unset, CidrIpVersionEnum]
        if isinstance(_ip_version, Unset):
            ip_version = UNSET
        else:
            ip_version = CidrIpVersionEnum(_ip_version)

        prefix_length_min = d.pop("prefix_length_min", UNSET)

        prefix_length_max = d.pop("prefix_length_max", UNSET)

        allowed_ranges = cast(list[str], d.pop("allowed_ranges", UNSET))

        excluded_ranges = cast(list[str], d.pop("excluded_ranges", UNSET))

        max_items = d.pop("max_items", UNSET)

        multiple = d.pop("multiple", UNSET)

        _secret_source = d.pop("secret_source", UNSET)
        secret_source: Union[Unset, OptionSecretSourceEnum]
        if isinstance(_secret_source, Unset):
            secret_source = UNSET
        else:
            secret_source = OptionSecretSourceEnum(_secret_source)

        customer_can_reveal = d.pop("customer_can_reveal", UNSET)

        min_length = d.pop("min_length", UNSET)

        max_length = d.pop("max_length", UNSET)

        multiline = d.pop("multiline", UNSET)

        ikev1_allowed = d.pop("ikev1_allowed", UNSET)

        allow_private_peer = d.pop("allow_private_peer", UNSET)

        provider_gateway_ip = d.pop("provider_gateway_ip", UNSET)

        provider_local_subnets = cast(list[str], d.pop("provider_local_subnets", UNSET))

        _remote_subnets = d.pop("remote_subnets", UNSET)
        remote_subnets: Union[Unset, CidrPolicyRequest]
        if isinstance(_remote_subnets, Unset):
            remote_subnets = UNSET
        else:
            remote_subnets = CidrPolicyRequest.from_dict(_remote_subnets)

        no_overlap_with = cast(list[str], d.pop("no_overlap_with", UNSET))

        _phase1 = d.pop("phase1", UNSET)
        phase1: Union[Unset, IpsecPhase1PolicyRequest]
        if isinstance(_phase1, Unset):
            phase1 = UNSET
        else:
            phase1 = IpsecPhase1PolicyRequest.from_dict(_phase1)

        _phase2 = d.pop("phase2", UNSET)
        phase2: Union[Unset, IpsecPhase2PolicyRequest]
        if isinstance(_phase2, Unset):
            phase2 = UNSET
        else:
            phase2 = IpsecPhase2PolicyRequest.from_dict(_phase2)

        option_default_configs_request = cls(
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
            infrastructure_mode=infrastructure_mode,
            fixed_openstack_offerings=fixed_openstack_offerings,
            ip_version=ip_version,
            prefix_length_min=prefix_length_min,
            prefix_length_max=prefix_length_max,
            allowed_ranges=allowed_ranges,
            excluded_ranges=excluded_ranges,
            max_items=max_items,
            multiple=multiple,
            secret_source=secret_source,
            customer_can_reveal=customer_can_reveal,
            min_length=min_length,
            max_length=max_length,
            multiline=multiline,
            ikev1_allowed=ikev1_allowed,
            allow_private_peer=allow_private_peer,
            provider_gateway_ip=provider_gateway_ip,
            provider_local_subnets=provider_local_subnets,
            remote_subnets=remote_subnets,
            no_overlap_with=no_overlap_with,
            phase1=phase1,
            phase2=phase2,
        )

        option_default_configs_request.additional_properties = d
        return option_default_configs_request

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
