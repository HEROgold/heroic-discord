"""Discord Events module for handling Gateway and Webhook events.

This module provides structures for both Gateway (WebSocket) and Webhook (HTTP) events
from Discord's API. Gateway events are the primary way to receive real-time updates,
while webhook events provide HTTP-based notifications for specific lifecycle events.

References:
    - https://docs.discord.com/developers/events/overview
    - https://docs.discord.com/developers/events/gateway
    - https://docs.discord.com/developers/events/gateway-events
    - https://docs.discord.com/developers/events/webhook-events

"""

from __future__ import annotations

from . import gateway, webhook
from .base import (
    EventBody,
    GatewayCloseCode,
    GatewayEventPayload,
    GatewayIntent,
    GatewayOpcode,
    WebhookEventPayload,
    WebhookType,
)

__all__ = [
    # Base Types
    "EventBody",
    "GatewayCloseCode",
    "GatewayEventPayload",
    "GatewayIntent",
    "GatewayOpcode",
    "WebhookEventPayload",
    "WebhookType",
    # Modules
    "gateway",
    "webhook",
]
