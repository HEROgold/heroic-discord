"""Base event structures and types for Discord events.

This module contains common structures and enums used across both Gateway and Webhook events.
"""

from __future__ import annotations

from enum import IntEnum
from typing import Any, TypedDict


class GatewayOpcode(IntEnum):
    """Gateway opcodes for WebSocket communication.

    References:
        https://docs.discord.com/developers/topics/opcodes-and-status-codes#gateway-gateway-opcodes

    """

    DISPATCH = 0  # Receive: An event was dispatched
    HEARTBEAT = 1  # Send/Receive: Fired periodically to keep connection alive
    IDENTIFY = 2  # Send: Start a new session
    PRESENCE_UPDATE = 3  # Send: Update the client's presence
    VOICE_STATE_UPDATE = 4  # Send: Join/leave/move voice channels
    RESUME = 6  # Send: Resume a previous session
    RECONNECT = 7  # Receive: You should reconnect and resume
    REQUEST_GUILD_MEMBERS = 8  # Send: Request guild members
    INVALID_SESSION = 9  # Receive: Session was invalidated, should reconnect and identify/resume
    HELLO = 10  # Receive: Sent on connection start, contains heartbeat interval
    HEARTBEAT_ACK = 11  # Receive: Acknowledgment of heartbeat


class GatewayCloseCode(IntEnum):
    """Gateway close event codes.

    References:
        https://docs.discord.com/developers/topics/opcodes-and-status-codes#gateway-gateway-close-event-codes

    """

    UNKNOWN_ERROR = 4000
    UNKNOWN_OPCODE = 4001
    DECODE_ERROR = 4002
    NOT_AUTHENTICATED = 4003
    AUTHENTICATION_FAILED = 4004
    ALREADY_AUTHENTICATED = 4005
    INVALID_SEQUENCE = 4007
    RATE_LIMITED = 4008
    SESSION_TIMED_OUT = 4009
    INVALID_SHARD = 4010
    SHARDING_REQUIRED = 4011
    INVALID_API_VERSION = 4012
    INVALID_INTENTS = 4013
    DISALLOWED_INTENTS = 4014


class GatewayIntent(IntEnum):
    """Gateway intents bitfield values.

    Intents are bitwise values that correlate to sets of related events.
    Some intents are privileged and require approval for verified bots.

    References:
        https://docs.discord.com/developers/events/gateway#gateway-intents

    """

    GUILDS = 1 << 0
    GUILD_MEMBERS = 1 << 1  # Privileged
    GUILD_MODERATION = 1 << 2
    GUILD_EXPRESSIONS = 1 << 3
    GUILD_INTEGRATIONS = 1 << 4
    GUILD_WEBHOOKS = 1 << 5
    GUILD_INVITES = 1 << 6
    GUILD_VOICE_STATES = 1 << 7
    GUILD_PRESENCES = 1 << 8  # Privileged
    GUILD_MESSAGES = 1 << 9
    GUILD_MESSAGE_REACTIONS = 1 << 10
    GUILD_MESSAGE_TYPING = 1 << 11
    DIRECT_MESSAGES = 1 << 12
    DIRECT_MESSAGE_REACTIONS = 1 << 13
    DIRECT_MESSAGE_TYPING = 1 << 14
    MESSAGE_CONTENT = 1 << 15  # Privileged
    GUILD_SCHEDULED_EVENTS = 1 << 16
    AUTO_MODERATION_CONFIGURATION = 1 << 20
    AUTO_MODERATION_EXECUTION = 1 << 21
    GUILD_MESSAGE_POLLS = 1 << 24
    DIRECT_MESSAGE_POLLS = 1 << 25


class GatewayEventPayload(TypedDict, total=False):
    """Structure of a Gateway event payload.

    All Gateway events follow this common structure, with the data (`d`)
    varying between different event types.

    References:
        https://docs.discord.com/developers/events/gateway-events#payload-structure

    """

    op: int  # Gateway opcode
    d: Any | None  # Event data (varies by type)
    s: int | None  # Sequence number (null when op is not 0)
    t: str | None  # Event name (null when op is not 0)


class WebhookType(IntEnum):
    """Webhook event payload types.

    References:
        https://docs.discord.com/developers/events/webhook-events#webhook-event-payloads

    """

    PING = 0  # PING event to verify webhook URL
    EVENT = 1  # Actual webhook event


class WebhookEventPayload(TypedDict, total=False):
    """Structure of a webhook event payload.

    References:
        https://docs.discord.com/developers/events/webhook-events#webhook-event-payloads

    """

    version: int  # Version scheme (currently always 1)
    application_id: str  # Application ID (snowflake)
    type: int  # Webhook type (0 for PING, 1 for events)
    event: EventBody | None  # Event data payload (only for type 1)


class EventBody(TypedDict, total=False):
    """Inner event body for webhook events.

    Contains high-level data about the event and the specific event data.

    References:
        https://docs.discord.com/developers/events/webhook-events#webhook-event-payloads

    """

    type: str  # Event type name
    timestamp: str  # ISO8601 timestamp
    data: dict[str, Any] | None  # Event-specific data
