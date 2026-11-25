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
    """Sent on every state transition of an order.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        order_uuid: UUID of the order
        order_state: Display name of the order state
        order_type (optional): Order type
        resource_uuid (optional): UUID of the resource
        resource_backend_id (optional): Backend identifier of the resource
        resource_name (optional): Name of the resource
        project_uuid (optional): UUID of the project
        project_name (optional): Name of the project
        attributes (optional): Order attributes with secrets removed
        limits (optional): Resource limits
        plan_uuid (optional): UUID of the resource's plan, when it has one
    """

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
    """Periodic resend of pending orders (hourly task).

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        order_uuid: UUID of the order
        order_state: Display name of the order state
        sequence_number: Incremental message sequence number
        order_type (optional): Order type
        resource_uuid (optional): UUID of the resource
        resource_backend_id (optional): Backend identifier of the resource
        resource_name (optional): Name of the resource
        project_uuid (optional): UUID of the project
        project_name (optional): Name of the project
        attributes (optional): Order attributes with secrets removed
        limits (optional): Resource limits
        plan_uuid (optional): UUID of the resource's plan, when it has one
    """

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
    """Sent when the provider or the consumer sets order information for the other side.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        order_uuid: UUID of the order
        action: Action: 'provider_info_set' or 'consumer_info_set'
        order_type (optional): Order type
        resource_uuid (optional): UUID of the resource
        resource_backend_id (optional): Backend identifier of the resource
        resource_name (optional): Name of the resource
        project_uuid (optional): UUID of the project
        project_name (optional): Name of the project
        attributes (optional): Order attributes with secrets removed
        limits (optional): Resource limits
        plan_uuid (optional): UUID of the resource's plan, when it has one
    """

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
    """Sent when resource downscale, access restriction, or pause state changes.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        resource_uuid: UUID of the resource
        resource_backend_id: Backend identifier of the resource
        downscaled: Whether the resource is downscaled
        restrict_member_access: Whether member access is restricted
        paused: Whether the resource is paused
        sequence_number: Incremental message sequence number
        resource_name (optional): Name of the resource
        resource_state (optional): Display name of the resource state
        project_uuid (optional): UUID of the project
        project_name (optional): Name of the project
        limits (optional): Resource limits
    """

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
    """Sent when a resource is created and on every state transition.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        resource_uuid: UUID of the resource
        resource_backend_id: Backend identifier of the resource
        resource_name (optional): Name of the resource
        resource_state (optional): Display name of the resource state
        project_uuid (optional): UUID of the project
        project_name (optional): Name of the project
        limits (optional): Resource limits
    """

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
    """Sent when an offering user's username is set or changed.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        offering_user_uuid: UUID of the offering user
        user_uuid: UUID of the Waldur user
        username: Username of the offering user
        state: State of the offering user, as its raw value
        action: Action type: username_set
        resource_backend_ids: Backend IDs of associated resources
    """

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
    """Sent when an offering user is created.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        offering_user_uuid: UUID of the offering user
        user_uuid: UUID of the Waldur user
        username: Username of the offering user
        state: Display name of the offering user state
        runtime_state: Runtime state reported by the backend
        action: Action type: create
        attributes: User profile attributes exposed to the offering
    """

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
    """Sent when tracked fields of an offering user change.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        offering_user_uuid: UUID of the offering user
        user_uuid: UUID of the Waldur user
        username: Username of the offering user
        state: Display name of the offering user state
        runtime_state: Runtime state reported by the backend
        changed_fields: Fields that changed
        action: Action type: update
    """

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
    """Sent when an offering user is deleted.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        offering_user_uuid: UUID of the offering user
        user_uuid: UUID of the Waldur user
        username: Username of the offering user
        action: Action type: delete
    """

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
    """Sent for each offering of a user when profile attributes exposed to that offering change.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        offering_user_uuid: UUID of the offering user
        user_uuid: UUID of the Waldur user
        username: Username of the offering user
        action: Action type: attribute_update
        changed_attributes: Exposed profile fields that changed
        attributes: User profile attributes exposed to the offering
    """

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
    """Sent for each offering of a user when the user's Waldur account is activated or deactivated.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        offering_user_uuid: UUID of the offering user
        user_uuid: UUID of the Waldur user
        username: Username of the offering user
        action: Action type: account_status_update
        user_is_active: Whether the Waldur user account is active
    """

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
    """Sent when a user role is granted or revoked in a project.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        user_uuid: UUID of the user
        user_username: Username of the user
        project_uuid: UUID of the project
        project_name: Name of the project
        role_name: Name of the role
        granted: True if granted, False if revoked
        user_email (optional): Email of the user
        user_full_name (optional): Full name of the user
    """

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
    """Sent to trigger a user-role sync for a project, or for one resource when resource_uuid is present.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        project_uuid: UUID of the project
        project_name: Name of the project
        resource_uuid (optional): UUID of the resource to re-sync; absent for a project-wide sync
    """

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
    """Sent when a service or course account is created or deleted.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        account_uuid: UUID of the account
        account_username: Username of the account
        scope_type: Scope type (always 'project')
        project_uuid: UUID of the project
        project_name: Name of the project
        action: Action: 'create' or 'delete'
    """

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
    """Sent when SLURM policy periodic settings need to be applied.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid: UUID of the offering
        resource_uuid: UUID of the resource
        backend_id: Backend resource identifier (SLURM account name)
        policy_uuid: UUID of the policy
        action: Action: 'apply_periodic_settings'
        settings: SLURM settings dict (fairshare, limits, thresholds)
        timestamp: ISO 8601 timestamp for the current period
    """

    event_type: str


class _BackendResourceRequestMessageRequired(TypedDict):
    """Required keys of BackendResourceRequestMessage."""

    object_type: Literal["importable_resources"]
    schema_version: int
    emitted_at: str
    backend_resource_request_uuid: str


class BackendResourceRequestMessage(_BackendResourceRequestMessageRequired, total=False):
    """Asks the agent to list the backend resources that can be imported into the offering.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        backend_resource_request_uuid: UUID of the backend resource request to fulfill
    """

    event_type: str
    offering_uuid: str


class _OfferingResourcesSyncMessageRequired(TypedDict):
    """Required keys of OfferingResourcesSyncMessage."""

    object_type: Literal["offering_resources_sync"]
    schema_version: int
    emitted_at: str
    requested_by_user_uuid: str


class OfferingResourcesSyncMessage(_OfferingResourcesSyncMessageRequired, total=False):
    """Asks the agent to reconcile every resource of the offering.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        requested_by_user_uuid: UUID of the user who requested the synchronization
    """

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
    """A command on one of a resource's API keys: create, rotate, pause, resume, update or delete. Carried on the resource_api_key_rotation observable type, which is named for the first command and kept so subscriptions do not change.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        action: One of ResourceApiKeyActions
        resource_uuid: UUID of the resource
        resource_backend_id: Backend identifier of the resource
        api_key_uuid: UUID of the API key
        client_id: Backend client id of the key; blank on a key being created
        limits (optional): Monthly limits per component, null when the key has none; only on commands that carry the key's settings
        spending_limits (optional): Spending limits for every period, null when the key has none; only on commands that carry the key's settings
        allowed_models (optional): Models the key may call (['*'] for all, [] for none): the key's own list narrowed by its resource's model selection. Only on commands that carry the key's settings; absent from Waldur versions older than ['*'], where absence allows every model
    """

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
    """A provider project group was created, updated or deleted, or project groups were switched on or off for the provider.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        action: Action: 'create' (the group got its first GID), 'update' (its name or GID changed), 'delete', or 'switch' (project groups switched on or off for the provider)
        service_provider_uuid: UUID of the service provider
        customer_uuid: UUID of the provider's organization
        project_group_uuid (optional): UUID of the group; absent on 'switch'
        project_uuid (optional): UUID of the group's project if it still exists; absent on 'switch'
        name (optional): Group name; absent on 'switch'
        gid (optional): Group GID; absent on 'switch'
        changed_fields (optional): Fields that changed; only on 'update'
        project_groups_enabled (optional): The new setting; only on 'switch'
    """

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
    """Any message delivered for order: OrderMessage, PendingOrderMessage, OrderInfoMessage.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        order_uuid: UUID of the order
        order_state (optional): Display name of the order state
        order_type (optional): Order type
        resource_uuid (optional): UUID of the resource
        resource_backend_id (optional): Backend identifier of the resource
        resource_name (optional): Name of the resource
        project_uuid (optional): UUID of the project
        project_name (optional): Name of the project
        attributes (optional): Order attributes with secrets removed
        limits (optional): Resource limits
        plan_uuid (optional): UUID of the resource's plan, when it has one
        sequence_number (optional): Incremental message sequence number
        action (optional): Action: 'provider_info_set' or 'consumer_info_set'
    """

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
    """Any message delivered for resource: ResourceUpdateMessage, ResourceStateMessage.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        resource_uuid: UUID of the resource
        resource_backend_id: Backend identifier of the resource
        downscaled (optional): Whether the resource is downscaled
        restrict_member_access (optional): Whether member access is restricted
        paused (optional): Whether the resource is paused
        sequence_number (optional): Incremental message sequence number
        resource_name (optional): Name of the resource
        resource_state (optional): Display name of the resource state
        project_uuid (optional): UUID of the project
        project_name (optional): Name of the project
        limits (optional): Resource limits
    """

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
    """Any message delivered for offering_user: OfferingUserMessage, OfferingUserCreatedMessage, OfferingUserUpdatedMessage, OfferingUserDeletedMessage, OfferingUserAttributeUpdateMessage, OfferingUserAccountStatusUpdateMessage.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        offering_user_uuid: UUID of the offering user
        user_uuid: UUID of the Waldur user
        username: Username of the offering user
        state (optional): State of the offering user, as its raw value; Display name of the offering user state
        action: Action type: username_set; Action type: create; Action type: update; Action type: delete; Action type: attribute_update; Action type: account_status_update
        resource_backend_ids (optional): Backend IDs of associated resources
        runtime_state (optional): Runtime state reported by the backend
        attributes (optional): User profile attributes exposed to the offering
        changed_fields (optional): Fields that changed
        changed_attributes (optional): Exposed profile fields that changed
        user_is_active (optional): Whether the Waldur user account is active
    """

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
    """Any message delivered for user_role: UserRoleMessage, UserRoleSyncMessage.

    Attributes:
        object_type: ObservableObjectType this message is delivered for
        schema_version: Version of the envelope format
        emitted_at: ISO 8601 time the event was emitted, for discarding stale updates
        event_type (optional): Event type, when the event comes from the event log
        offering_uuid (optional): UUID of the offering; added to every offering-scoped event
        user_uuid (optional): UUID of the user
        user_username (optional): Username of the user
        project_uuid: UUID of the project
        project_name: Name of the project
        role_name (optional): Name of the role
        granted (optional): True if granted, False if revoked
        user_email (optional): Email of the user
        user_full_name (optional): Full name of the user
        resource_uuid (optional): UUID of the resource to re-sync; absent for a project-wide sync
    """

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
