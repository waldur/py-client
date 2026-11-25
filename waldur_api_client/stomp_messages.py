"""Types of the STOMP messages Waldur publishes to event consumers.

Generated from mastermind's AsyncAPI document (Waldur site agent events 1.0.0, AsyncAPI 3.0.0),
shipped next to this module as ``asyncapi.yaml``. Do not edit by hand: the
client's pipeline regenerates it with scripts/generate_stomp_messages.py.

Each message has a TypedDict named after it. Required keys live in a private
base class and optional keys in a ``total=False`` subclass (``NotRequired``
needs Python 3.11). An object type that carries several messages also has a
merged ``<ObjectType>Event`` TypedDict: a handler subscribed to the type can
receive any of them, so only keys every message carries are required.
"""

# Optional/Union instead of PEP 604 `X | Y` keeps typing.get_type_hints() working on Python 3.9.
# ruff: noqa: UP007, UP045
from typing import Any, Literal, Optional, TypedDict, Union  # noqa: F401


class _OrderMessageRequired(TypedDict):
    """Required keys of OrderMessage."""

    object_type: Literal["order"]
    schema_version: int
    emitted_at: str
    order_uuid: str
    order_state: str


class OrderMessage(_OrderMessageRequired, total=False):
    """Sent on every state transition of an order."""

    event_type: str
    offering_uuid: str
    order_type: str
    resource_uuid: str
    resource_backend_id: str
    resource_name: str
    project_uuid: str
    project_name: str
    attributes: dict[str, Any]
    limits: dict[str, Any]
    plan_uuid: str


class _PendingOrderMessageRequired(TypedDict):
    """Required keys of PendingOrderMessage."""

    object_type: Literal["order"]
    schema_version: int
    emitted_at: str
    order_uuid: str
    order_state: str
    sequence_number: int


class PendingOrderMessage(_PendingOrderMessageRequired, total=False):
    """Periodic resend of pending orders (hourly task)."""

    event_type: str
    offering_uuid: str
    order_type: str
    resource_uuid: str
    resource_backend_id: str
    resource_name: str
    project_uuid: str
    project_name: str
    attributes: dict[str, Any]
    limits: dict[str, Any]
    plan_uuid: str


class _OrderInfoMessageRequired(TypedDict):
    """Required keys of OrderInfoMessage."""

    object_type: Literal["order"]
    schema_version: int
    emitted_at: str
    order_uuid: str
    action: Literal["provider_info_set", "consumer_info_set"]


class OrderInfoMessage(_OrderInfoMessageRequired, total=False):
    """Sent when the provider or the consumer sets order information for the other side."""

    event_type: str
    offering_uuid: str
    order_type: str
    resource_uuid: str
    resource_backend_id: str
    resource_name: str
    project_uuid: str
    project_name: str
    attributes: dict[str, Any]
    limits: dict[str, Any]
    plan_uuid: str


class _ResourceUpdateMessageRequired(TypedDict):
    """Required keys of ResourceUpdateMessage."""

    object_type: Literal["resource"]
    schema_version: int
    emitted_at: str
    resource_uuid: str
    resource_backend_id: str
    downscaled: bool
    restrict_member_access: bool
    paused: bool
    sequence_number: int


class ResourceUpdateMessage(_ResourceUpdateMessageRequired, total=False):
    """Sent when resource downscale, access restriction, or pause state changes."""

    event_type: str
    offering_uuid: str
    resource_name: str
    resource_state: str
    project_uuid: str
    project_name: str
    limits: dict[str, Any]


class _ResourceStateMessageRequired(TypedDict):
    """Required keys of ResourceStateMessage."""

    object_type: Literal["resource"]
    schema_version: int
    emitted_at: str
    resource_uuid: str
    resource_backend_id: str


class ResourceStateMessage(_ResourceStateMessageRequired, total=False):
    """Sent when a resource is created and on every state transition."""

    event_type: str
    offering_uuid: str
    resource_name: str
    resource_state: str
    project_uuid: str
    project_name: str
    limits: dict[str, Any]


class _OfferingUserMessageRequired(TypedDict):
    """Required keys of OfferingUserMessage."""

    object_type: Literal["offering_user"]
    schema_version: int
    emitted_at: str
    offering_user_uuid: str
    user_uuid: str
    username: str
    state: int
    action: Literal["username_set"]
    resource_backend_ids: list[str]


class OfferingUserMessage(_OfferingUserMessageRequired, total=False):
    """Sent when an offering user's username is set or changed."""

    event_type: str
    offering_uuid: str


class _OfferingUserCreatedMessageRequired(TypedDict):
    """Required keys of OfferingUserCreatedMessage."""

    object_type: Literal["offering_user"]
    schema_version: int
    emitted_at: str
    offering_user_uuid: str
    user_uuid: str
    username: str
    state: str
    runtime_state: str
    action: Literal["create"]
    attributes: dict[str, Any]


class OfferingUserCreatedMessage(_OfferingUserCreatedMessageRequired, total=False):
    """Sent when an offering user is created."""

    event_type: str
    offering_uuid: str


class _OfferingUserUpdatedMessageRequired(TypedDict):
    """Required keys of OfferingUserUpdatedMessage."""

    object_type: Literal["offering_user"]
    schema_version: int
    emitted_at: str
    offering_user_uuid: str
    user_uuid: str
    username: str
    state: str
    runtime_state: str
    changed_fields: list[str]
    action: Literal["update"]


class OfferingUserUpdatedMessage(_OfferingUserUpdatedMessageRequired, total=False):
    """Sent when tracked fields of an offering user change."""

    event_type: str
    offering_uuid: str


class _OfferingUserDeletedMessageRequired(TypedDict):
    """Required keys of OfferingUserDeletedMessage."""

    object_type: Literal["offering_user"]
    schema_version: int
    emitted_at: str
    offering_user_uuid: str
    user_uuid: str
    username: str
    action: Literal["delete"]


class OfferingUserDeletedMessage(_OfferingUserDeletedMessageRequired, total=False):
    """Sent when an offering user is deleted."""

    event_type: str
    offering_uuid: str


class _OfferingUserAttributeUpdateMessageRequired(TypedDict):
    """Required keys of OfferingUserAttributeUpdateMessage."""

    object_type: Literal["offering_user"]
    schema_version: int
    emitted_at: str
    offering_user_uuid: str
    user_uuid: str
    username: str
    action: Literal["attribute_update"]
    changed_attributes: list[str]
    attributes: dict[str, Any]


class OfferingUserAttributeUpdateMessage(_OfferingUserAttributeUpdateMessageRequired, total=False):
    """Sent for each offering of a user when profile attributes exposed to that offering change."""

    event_type: str
    offering_uuid: str


class _OfferingUserAccountStatusUpdateMessageRequired(TypedDict):
    """Required keys of OfferingUserAccountStatusUpdateMessage."""

    object_type: Literal["offering_user"]
    schema_version: int
    emitted_at: str
    offering_user_uuid: str
    user_uuid: str
    username: str
    action: Literal["account_status_update"]
    user_is_active: bool


class OfferingUserAccountStatusUpdateMessage(_OfferingUserAccountStatusUpdateMessageRequired, total=False):
    """Sent for each offering of a user when the user's Waldur account is activated or deactivated."""

    event_type: str
    offering_uuid: str


class _UserRoleMessageRequired(TypedDict):
    """Required keys of UserRoleMessage."""

    object_type: Literal["user_role"]
    schema_version: int
    emitted_at: str
    user_uuid: str
    user_username: str
    project_uuid: str
    project_name: str
    role_name: str
    granted: bool


class UserRoleMessage(_UserRoleMessageRequired, total=False):
    """Sent when a user role is granted or revoked in a project."""

    event_type: str
    offering_uuid: str
    user_email: str
    user_full_name: str


class _UserRoleSyncMessageRequired(TypedDict):
    """Required keys of UserRoleSyncMessage."""

    object_type: Literal["user_role"]
    schema_version: int
    emitted_at: str
    project_uuid: str
    project_name: str


class UserRoleSyncMessage(_UserRoleSyncMessageRequired, total=False):
    """Sent to trigger a user-role sync for a project, or for one resource when resource_uuid is present."""

    event_type: str
    offering_uuid: str
    resource_uuid: str


class _AccountMessageRequired(TypedDict):
    """Required keys of AccountMessage."""

    object_type: Literal["service_account", "course_account"]
    schema_version: int
    emitted_at: str
    account_uuid: str
    account_username: str
    scope_type: Literal["project"]
    project_uuid: str
    project_name: str
    action: Literal["create", "delete"]


class AccountMessage(_AccountMessageRequired, total=False):
    """Sent when a service or course account is created or deleted."""

    event_type: str
    offering_uuid: str


class _PeriodicLimitsMessageRequired(TypedDict):
    """Required keys of PeriodicLimitsMessage."""

    object_type: Literal["resource_periodic_limits"]
    schema_version: int
    emitted_at: str
    offering_uuid: str
    resource_uuid: str
    backend_id: str
    policy_uuid: str
    action: Literal["apply_periodic_settings"]
    settings: dict[str, Any]
    timestamp: str


class PeriodicLimitsMessage(_PeriodicLimitsMessageRequired, total=False):
    """Sent when SLURM policy periodic settings need to be applied."""

    event_type: str


class _BackendResourceRequestMessageRequired(TypedDict):
    """Required keys of BackendResourceRequestMessage."""

    object_type: Literal["importable_resources"]
    schema_version: int
    emitted_at: str
    backend_resource_request_uuid: str


class BackendResourceRequestMessage(_BackendResourceRequestMessageRequired, total=False):
    """Asks the agent to list the backend resources that can be imported into the offering."""

    event_type: str
    offering_uuid: str


class _OfferingResourcesSyncMessageRequired(TypedDict):
    """Required keys of OfferingResourcesSyncMessage."""

    object_type: Literal["offering_resources_sync"]
    schema_version: int
    emitted_at: str
    requested_by_user_uuid: str


class OfferingResourcesSyncMessage(_OfferingResourcesSyncMessageRequired, total=False):
    """Asks the agent to reconcile every resource of the offering."""

    event_type: str
    offering_uuid: str


class _ApiKeyCommandMessageRequired(TypedDict):
    """Required keys of ApiKeyCommandMessage."""

    object_type: Literal["resource_api_key_rotation"]
    schema_version: int
    emitted_at: str
    action: Literal["create", "rotate", "pause", "resume", "delete", "update"]
    resource_uuid: str
    resource_backend_id: str
    api_key_uuid: str
    client_id: str


class ApiKeyCommandMessage(_ApiKeyCommandMessageRequired, total=False):
    """A command on one of a resource's API keys: create, rotate, pause, resume, update or delete."""

    event_type: str
    offering_uuid: str
    limits: Optional[dict[str, Any]]
    spending_limits: Optional[dict[str, Any]]
    allowed_models: list[str]


class _ProjectGroupMessageRequired(TypedDict):
    """Required keys of ProjectGroupMessage."""

    object_type: Literal["service_provider_project_group"]
    schema_version: int
    emitted_at: str
    action: Literal["create", "update", "delete", "switch"]
    service_provider_uuid: str
    customer_uuid: str


class ProjectGroupMessage(_ProjectGroupMessageRequired, total=False):
    """A provider project group was created, updated or deleted, or project groups were switched on or off for the provider."""

    event_type: str
    offering_uuid: str
    project_group_uuid: str
    project_uuid: Optional[str]
    name: str
    gid: Optional[int]
    changed_fields: list[str]
    project_groups_enabled: bool


class _OrderEventRequired(TypedDict):
    """Required keys of OrderEvent."""

    object_type: Literal["order"]
    schema_version: int
    emitted_at: str
    order_uuid: str


class OrderEvent(_OrderEventRequired, total=False):
    """Any message delivered for order: OrderMessage, PendingOrderMessage, OrderInfoMessage."""

    event_type: str
    offering_uuid: str
    order_state: str
    order_type: str
    resource_uuid: str
    resource_backend_id: str
    resource_name: str
    project_uuid: str
    project_name: str
    attributes: dict[str, Any]
    limits: dict[str, Any]
    plan_uuid: str
    sequence_number: int
    action: Literal["provider_info_set", "consumer_info_set"]


class _ResourceEventRequired(TypedDict):
    """Required keys of ResourceEvent."""

    object_type: Literal["resource"]
    schema_version: int
    emitted_at: str
    resource_uuid: str
    resource_backend_id: str


class ResourceEvent(_ResourceEventRequired, total=False):
    """Any message delivered for resource: ResourceUpdateMessage, ResourceStateMessage."""

    event_type: str
    offering_uuid: str
    downscaled: bool
    restrict_member_access: bool
    paused: bool
    sequence_number: int
    resource_name: str
    resource_state: str
    project_uuid: str
    project_name: str
    limits: dict[str, Any]


class _OfferingUserEventRequired(TypedDict):
    """Required keys of OfferingUserEvent."""

    object_type: Literal["offering_user"]
    schema_version: int
    emitted_at: str
    offering_user_uuid: str
    user_uuid: str
    username: str
    action: Literal["username_set", "create", "update", "delete", "attribute_update", "account_status_update"]


class OfferingUserEvent(_OfferingUserEventRequired, total=False):
    """Any message delivered for offering_user: OfferingUserMessage, OfferingUserCreatedMessage, OfferingUserUpdatedMessage, OfferingUserDeletedMessage, OfferingUserAttributeUpdateMessage, OfferingUserAccountStatusUpdateMessage."""

    event_type: str
    offering_uuid: str
    state: Union[int, str]
    resource_backend_ids: list[str]
    runtime_state: str
    attributes: dict[str, Any]
    changed_fields: list[str]
    changed_attributes: list[str]
    user_is_active: bool


class _UserRoleEventRequired(TypedDict):
    """Required keys of UserRoleEvent."""

    object_type: Literal["user_role"]
    schema_version: int
    emitted_at: str
    project_uuid: str
    project_name: str


class UserRoleEvent(_UserRoleEventRequired, total=False):
    """Any message delivered for user_role: UserRoleMessage, UserRoleSyncMessage."""

    event_type: str
    offering_uuid: str
    user_uuid: str
    user_username: str
    role_name: str
    granted: bool
    user_email: str
    user_full_name: str
    resource_uuid: str



# Message names by the object type they are delivered for.
MESSAGES_BY_OBJECT_TYPE: dict[str, tuple[str, ...]] = {
    "order": ("OrderMessage", "PendingOrderMessage", "OrderInfoMessage",),
    "resource": ("ResourceUpdateMessage", "ResourceStateMessage",),
    "offering_user": ("OfferingUserMessage", "OfferingUserCreatedMessage", "OfferingUserUpdatedMessage", "OfferingUserDeletedMessage", "OfferingUserAttributeUpdateMessage", "OfferingUserAccountStatusUpdateMessage",),
    "user_role": ("UserRoleMessage", "UserRoleSyncMessage",),
    "service_account": ("AccountMessage",),
    "course_account": ("AccountMessage",),
    "resource_periodic_limits": ("PeriodicLimitsMessage",),
    "importable_resources": ("BackendResourceRequestMessage",),
    "offering_resources_sync": ("OfferingResourcesSyncMessage",),
    "resource_api_key_rotation": ("ApiKeyCommandMessage",),
    "service_provider_project_group": ("ProjectGroupMessage",),
}
