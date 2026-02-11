"""Webhook event structures and types.

These events are sent to your app over HTTP when specific actions occur,
such as when your app is authorized or entitlements are created.

References:
    https://docs.discord.com/developers/events/webhook-events

"""

from __future__ import annotations

from typing import Any, TypedDict

# Application Lifecycle Events

class ApplicationAuthorizedStructure(TypedDict, total=False):
    """Application Authorized event structure.

    Sent when the app is added to a server or user account.
    Event: APPLICATION_AUTHORIZED

    References:
        https://docs.discord.com/developers/events/webhook-events#application-authorized

    """

    integration_type: int  # Installation context: 0 (guild) or 1 (user)
    user: dict[str, Any]  # User who authorized the app
    scopes: list[str]  # List of scopes user authorized
    guild: dict[str, Any]  # Server where app was authorized (when type is 0)


class ApplicationDeauthorizedStructure(TypedDict):
    """Application Deauthorized event structure.

    Sent when the app is deauthorized by a user.
    Event: APPLICATION_DEAUTHORIZED

    References:
        https://docs.discord.com/developers/events/webhook-events#application-deauthorized

    """

    user: dict[str, Any]  # User who deauthorized the app


# Entitlement Events

class EntitlementCreateStructure(TypedDict):
    """Entitlement Create event structure.

    Sent when an entitlement is created when a user purchases or is granted
    one of your app's SKUs.
    Event: ENTITLEMENT_CREATE

    The inner payload is an entitlement object.

    References:
        https://docs.discord.com/developers/events/webhook-events#entitlement-create
        https://docs.discord.com/developers/resources/entitlement#entitlement-object

    """

    application_id: str  # Application ID (snowflake)
    consumed: bool  # Whether entitlement has been consumed
    deleted: bool  # Whether entitlement has been deleted
    gift_code_flags: int  # Gift code flags
    id: str  # Entitlement ID (snowflake)
    promotion_id: str | None  # Promotion ID if applicable (snowflake)
    sku_id: str  # SKU ID (snowflake)
    type: int  # Entitlement type
    user_id: str  # User ID (snowflake)


class EntitlementUpdateStructure(TypedDict):
    """Entitlement Update event structure.

    Sent when an entitlement is updated.
    Event: ENTITLEMENT_UPDATE

    The inner payload is an entitlement object.

    References:
        https://docs.discord.com/developers/events/webhook-events#entitlement-update
        https://docs.discord.com/developers/resources/entitlement#entitlement-object

    """

    application_id: str  # Application ID (snowflake)
    consumed: bool  # Whether entitlement has been consumed
    deleted: bool  # Whether entitlement has been deleted
    gift_code_flags: int  # Gift code flags
    id: str  # Entitlement ID (snowflake)
    promotion_id: str | None  # Promotion ID if applicable (snowflake)
    sku_id: str  # SKU ID (snowflake)
    type: int  # Entitlement type
    user_id: str  # User ID (snowflake)


class EntitlementDeleteStructure(TypedDict):
    """Entitlement Delete event structure.

    Sent when an entitlement is deleted (rare occurrence).
    Event: ENTITLEMENT_DELETE

    The inner payload is an entitlement object.

    References:
        https://docs.discord.com/developers/events/webhook-events#entitlement-delete
        https://docs.discord.com/developers/resources/entitlement#entitlement-object

    """

    application_id: str  # Application ID (snowflake)
    consumed: bool  # Whether entitlement has been consumed
    deleted: bool  # Whether entitlement has been deleted (always true)
    gift_code_flags: int  # Gift code flags
    id: str  # Entitlement ID (snowflake)
    promotion_id: str | None  # Promotion ID if applicable (snowflake)
    sku_id: str  # SKU ID (snowflake)
    type: int  # Entitlement type
    user_id: str  # User ID (snowflake)


# Social SDK Message Events

class LobbyMessageCreateStructure(TypedDict, total=False):
    """Lobby Message Create event structure.

    Sent when a message is created in a lobby.
    Event: LOBBY_MESSAGE_CREATE

    The inner payload is a lobby message object.

    References:
        https://docs.discord.com/developers/events/webhook-events#lobby-message-create

    """

    id: str  # Message ID (snowflake)
    type: int  # Message type
    content: str  # Message contents
    lobby_id: str  # Lobby ID (snowflake)
    channel_id: str  # Channel ID (snowflake)
    author: dict[str, Any]  # User object
    flags: int  # Message flags bitfield
    application_id: str  # Application ID (snowflake)


class LobbyMessageUpdateStructure(TypedDict, total=False):
    """Lobby Message Update event structure.

    Sent when a message is updated in a lobby.
    Event: LOBBY_MESSAGE_UPDATE

    The inner payload is a lobby message object with update fields.

    References:
        https://docs.discord.com/developers/events/webhook-events#lobby-message-update

    """

    id: str  # Message ID (snowflake)
    type: int  # Message type
    content: str  # Message contents
    lobby_id: str  # Lobby ID (snowflake)
    channel_id: str  # Channel ID (snowflake)
    author: dict[str, Any]  # User object
    edited_timestamp: str  # ISO8601 timestamp of last edit
    flags: int  # Message flags bitfield
    timestamp: str  # ISO8601 timestamp of message creation


class LobbyMessageDeleteStructure(TypedDict):
    """Lobby Message Delete event structure.

    Sent when a message is deleted from a lobby.
    Event: LOBBY_MESSAGE_DELETE

    References:
        https://docs.discord.com/developers/events/webhook-events#lobby-message-delete

    """

    id: str  # Deleted message ID (snowflake)
    lobby_id: str  # Lobby ID (snowflake)


class GameDirectMessageCreateStructure(TypedDict, total=False):
    """Game Direct Message Create event structure.

    Sent when a direct message is created during an active Social SDK session.
    Event: GAME_DIRECT_MESSAGE_CREATE

    The inner payload is a message object or passthrough message object.

    References:
        https://docs.discord.com/developers/events/webhook-events#game-direct-message-create

    """

    id: str  # Message ID (snowflake)
    type: int  # Message type
    content: str  # Message contents
    channel_id: str  # Channel ID (snowflake)
    author: dict[str, Any]  # User object
    timestamp: str  # ISO8601 timestamp
    application_id: str  # Application ID (snowflake)
    attachments: list[dict[str, Any]]  # Message attachments


class GameDirectMessageUpdateStructure(TypedDict, total=False):
    """Game Direct Message Update event structure.

    Sent when a direct message is updated during an active Social SDK session.
    Event: GAME_DIRECT_MESSAGE_UPDATE

    The inner payload is a message object or passthrough message object.

    References:
        https://docs.discord.com/developers/events/webhook-events#game-direct-message-update

    """

    id: str  # Message ID (snowflake)
    content: str  # Message contents
    channel_id: str  # Channel ID (snowflake)
    author: dict[str, Any]  # User object
    recipient_id: str  # Recipient ID (snowflake)


class GameDirectMessageDeleteStructure(TypedDict, total=False):
    """Game Direct Message Delete event structure.

    Sent when a direct message is deleted during an active Social SDK session.
    Event: GAME_DIRECT_MESSAGE_DELETE

    The inner payload is a message object or passthrough message object.

    References:
        https://docs.discord.com/developers/events/webhook-events#game-direct-message-delete

    """

    id: str  # Message ID (snowflake)
    type: int  # Message type
    content: str  # Message contents
    channel_id: str  # Channel ID (snowflake)
    author: dict[str, Any]  # User object
    timestamp: str  # ISO8601 timestamp
    flags: int  # Message flags bitfield
    attachments: list[dict[str, Any]]  # Message attachments
    components: list[dict[str, Any]]  # Message components


# Social SDK Message Objects

class LobbyMessageObject(TypedDict, total=False):
    """Lobby Message object.

    Represents a message sent in a lobby or Linked Channel.

    References:
        https://docs.discord.com/developers/events/webhook-events#lobby-message-object

    """

    id: str  # Message ID (snowflake)
    type: int  # Message type
    content: str  # Message contents
    lobby_id: str  # Lobby ID (snowflake)
    channel_id: str  # Channel ID (snowflake)
    author: dict[str, Any]  # User object
    metadata: dict[str, Any]  # Additional metadata (key-value pairs)
    flags: int  # Message flags bitfield
    application_id: str  # Application ID (only during active SDK sessions)


class MessageObject(TypedDict, total=False):
    """Standard Message object with additional fields.

    Standard Discord message object with lobby and channel information.

    References:
        https://docs.discord.com/developers/events/webhook-events#message-object

    """

    lobby_id: str  # Lobby ID (only in Linked Channel messages, snowflake)
    channel: dict[str, Any]  # Channel object with recipient information
    # Plus all standard message object fields


class PassthroughMessageObject(TypedDict):
    """Passthrough Message object.

    Represents messages between provisional users that exist only in-game.
    Used when both users in a DM are provisional accounts.

    References:
        https://docs.discord.com/developers/events/webhook-events#passthrough-message-object

    """

    id: str  # Message ID (snowflake)
    type: int  # Message type
    content: str  # Message contents
    channel_id: str  # Channel ID (snowflake)
    recipient_id: str  # Recipient ID (snowflake)
    author: dict[str, Any]  # User object
    flags: int  # Message flags bitfield
    application_id: str  # Application ID (snowflake)
    channel: dict[str, Any]  # Channel object with recipient information
