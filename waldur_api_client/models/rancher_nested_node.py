import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RancherNestedNode")


@_attrs_define
class RancherNestedNode:
    """
    Attributes:
        url (str):
        instance (str):
        created (datetime.datetime):
        modified (datetime.datetime):
        uuid (UUID):
        error_message (str):
        etcd_role (bool):
        worker_role (bool):
        initial_data (Any): Initial data for instance creating.
        runtime_state (str):
        k8s_version (str):
        docker_version (str):
        cpu_allocated (Union[None, float]):
        cpu_total (Union[None, int]):
        ram_allocated (Union[None, int]): Allocated RAM in Mi.
        ram_total (Union[None, int]): Total RAM in Mi.
        pods_allocated (Union[None, int]):
        pods_total (Union[None, int]):
        labels (Any):
        annotations (Any):
        error_traceback (Union[Unset, str]):
        backend_id (Union[Unset, str]):
        controlplane_role (Union[Unset, bool]):
    """

    url: str
    instance: str
    created: datetime.datetime
    modified: datetime.datetime
    uuid: UUID
    error_message: str
    etcd_role: bool
    worker_role: bool
    initial_data: Any
    runtime_state: str
    k8s_version: str
    docker_version: str
    cpu_allocated: Union[None, float]
    cpu_total: Union[None, int]
    ram_allocated: Union[None, int]
    ram_total: Union[None, int]
    pods_allocated: Union[None, int]
    pods_total: Union[None, int]
    labels: Any
    annotations: Any
    error_traceback: Union[Unset, str] = UNSET
    backend_id: Union[Unset, str] = UNSET
    controlplane_role: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        instance = self.instance

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        uuid = str(self.uuid)

        error_message = self.error_message

        etcd_role = self.etcd_role

        worker_role = self.worker_role

        initial_data = self.initial_data

        runtime_state = self.runtime_state

        k8s_version = self.k8s_version

        docker_version = self.docker_version

        cpu_allocated: Union[None, float]
        cpu_allocated = self.cpu_allocated

        cpu_total: Union[None, int]
        cpu_total = self.cpu_total

        ram_allocated: Union[None, int]
        ram_allocated = self.ram_allocated

        ram_total: Union[None, int]
        ram_total = self.ram_total

        pods_allocated: Union[None, int]
        pods_allocated = self.pods_allocated

        pods_total: Union[None, int]
        pods_total = self.pods_total

        labels = self.labels

        annotations = self.annotations

        error_traceback = self.error_traceback

        backend_id = self.backend_id

        controlplane_role = self.controlplane_role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "instance": instance,
                "created": created,
                "modified": modified,
                "uuid": uuid,
                "error_message": error_message,
                "etcd_role": etcd_role,
                "worker_role": worker_role,
                "initial_data": initial_data,
                "runtime_state": runtime_state,
                "k8s_version": k8s_version,
                "docker_version": docker_version,
                "cpu_allocated": cpu_allocated,
                "cpu_total": cpu_total,
                "ram_allocated": ram_allocated,
                "ram_total": ram_total,
                "pods_allocated": pods_allocated,
                "pods_total": pods_total,
                "labels": labels,
                "annotations": annotations,
            }
        )
        if error_traceback is not UNSET:
            field_dict["error_traceback"] = error_traceback
        if backend_id is not UNSET:
            field_dict["backend_id"] = backend_id
        if controlplane_role is not UNSET:
            field_dict["controlplane_role"] = controlplane_role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        instance = d.pop("instance")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        uuid = UUID(d.pop("uuid"))

        error_message = d.pop("error_message")

        etcd_role = d.pop("etcd_role")

        worker_role = d.pop("worker_role")

        initial_data = d.pop("initial_data")

        runtime_state = d.pop("runtime_state")

        k8s_version = d.pop("k8s_version")

        docker_version = d.pop("docker_version")

        def _parse_cpu_allocated(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        cpu_allocated = _parse_cpu_allocated(d.pop("cpu_allocated"))

        def _parse_cpu_total(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        cpu_total = _parse_cpu_total(d.pop("cpu_total"))

        def _parse_ram_allocated(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        ram_allocated = _parse_ram_allocated(d.pop("ram_allocated"))

        def _parse_ram_total(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        ram_total = _parse_ram_total(d.pop("ram_total"))

        def _parse_pods_allocated(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        pods_allocated = _parse_pods_allocated(d.pop("pods_allocated"))

        def _parse_pods_total(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        pods_total = _parse_pods_total(d.pop("pods_total"))

        labels = d.pop("labels")

        annotations = d.pop("annotations")

        error_traceback = d.pop("error_traceback", UNSET)

        backend_id = d.pop("backend_id", UNSET)

        controlplane_role = d.pop("controlplane_role", UNSET)

        rancher_nested_node = cls(
            url=url,
            instance=instance,
            created=created,
            modified=modified,
            uuid=uuid,
            error_message=error_message,
            etcd_role=etcd_role,
            worker_role=worker_role,
            initial_data=initial_data,
            runtime_state=runtime_state,
            k8s_version=k8s_version,
            docker_version=docker_version,
            cpu_allocated=cpu_allocated,
            cpu_total=cpu_total,
            ram_allocated=ram_allocated,
            ram_total=ram_total,
            pods_allocated=pods_allocated,
            pods_total=pods_total,
            labels=labels,
            annotations=annotations,
            error_traceback=error_traceback,
            backend_id=backend_id,
            controlplane_role=controlplane_role,
        )

        rancher_nested_node.additional_properties = d
        return rancher_nested_node

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
