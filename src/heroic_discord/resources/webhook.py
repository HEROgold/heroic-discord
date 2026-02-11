"""Discord Webhook Resource Structures.

This module contains TypedDict definitions for Discord Webhook objects.
Reference: https://docs.discord.com/developers/resources/webhook
"""

from enum import IntEnum
from typing import TypedDict


class WebhookType(IntEnum):
    """Types of webhooks.

    https://docs.discord.com/developers/resources/webhook#webhook-object-webhook-types
    """

    INCOMING = 1
    CHANNEL_FOLLOWER = 2
    APPLICATION = 3


class Webhook(TypedDict, total=False):
    """Represents a webhook.

    https://docs.discord.com/developers/resources/webhook#webhook-object
    """

    id: str  # Webhook ID (snowflake)
    type: int  # Webhook type (WebhookType)
    guild_id: str | None  # Guild ID (snowflake)
    channel_id: str | None  # Channel ID (snowflake)
    user: dict  # User object that created the webhook
    name: str | None  # Default webhook name
    avatar: str | None  # Default webhook avatar hash
    token: str  # Secure webhook token (for Incoming Webhooks)
    application_id: str | None  # Bot/OAuth2 application ID (snowflake)
    source_guild: dict  # Partial guild object for Channel Follower Webhooks
    source_channel: dict  # Partial channel object for Channel Follower Webhooks
    url: str  # URL for executing the webhook


__all__ = [
    "Webhook",
    "WebhookType",
]
