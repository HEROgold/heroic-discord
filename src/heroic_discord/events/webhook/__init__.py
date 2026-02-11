"""Webhook events module for Discord HTTP-based events.

Webhook events are sent to your app's Webhook Event URL over HTTP to notify
you when certain events occur. Unlike Gateway events, webhook events are not
real-time and not guaranteed to be in order.

References:
    - https://docs.discord.com/developers/events/webhook-events

"""

from __future__ import annotations

from . import events
from .events import (
    ApplicationAuthorizedStructure,
    ApplicationDeauthorizedStructure,
    EntitlementCreateStructure,
    EntitlementDeleteStructure,
    EntitlementUpdateStructure,
    GameDirectMessageCreateStructure,
    GameDirectMessageDeleteStructure,
    GameDirectMessageUpdateStructure,
    LobbyMessageCreateStructure,
    LobbyMessageDeleteStructure,
    LobbyMessageObject,
    LobbyMessageUpdateStructure,
    MessageObject,
    PassthroughMessageObject,
)

__all__ = [
    # Event Structures
    "ApplicationAuthorizedStructure",
    "ApplicationDeauthorizedStructure",
    "EntitlementCreateStructure",
    "EntitlementDeleteStructure",
    "EntitlementUpdateStructure",
    "GameDirectMessageCreateStructure",
    "GameDirectMessageDeleteStructure",
    "GameDirectMessageUpdateStructure",
    "LobbyMessageCreateStructure",
    "LobbyMessageDeleteStructure",
    # Message Objects
    "LobbyMessageObject",
    "LobbyMessageUpdateStructure",
    "MessageObject",
    "PassthroughMessageObject",
    # Module
    "events",
]
