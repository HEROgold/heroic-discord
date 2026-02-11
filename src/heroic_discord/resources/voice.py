"""Discord Voice Resource Structures.

This module contains TypedDict definitions for Discord Voice objects.
Reference: https://docs.discord.com/developers/resources/voice
"""

from typing import TypedDict


class VoiceState(TypedDict, total=False):
    """Represents a user's voice connection status.

    https://docs.discord.com/developers/resources/voice#voice-state-object
    """

    guild_id: str  # Guild ID (snowflake)
    channel_id: str | None  # Channel ID user is connected to (snowflake)
    user_id: str  # User ID (snowflake)
    member: dict  # Guild member object
    session_id: str  # Voice connection session ID
    deaf: bool  # Whether user is deafened by server
    mute: bool  # Whether user is muted by server
    self_deaf: bool  # Whether user is locally deafened
    self_mute: bool  # Whether user is locally muted
    self_stream: bool  # Whether user is streaming via "Go Live"
    self_video: bool  # Whether user's camera is enabled
    suppress: bool  # Whether user's permission to speak is denied
    request_to_speak_timestamp: str | None  # ISO8601 timestamp when user requested to speak


class VoiceRegion(TypedDict, total=False):
    """Represents a voice region.

    https://docs.discord.com/developers/resources/voice#voice-region-object
    """

    id: str  # Unique region ID
    name: str  # Region name
    optimal: bool  # True for closest server to current user's client
    deprecated: bool  # Whether this is a deprecated region
    custom: bool  # Whether this is a custom region (for events)


__all__ = [
    "VoiceRegion",
    "VoiceState",
]
