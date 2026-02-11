"""Discord Stage Instance Resource Structures.

This module contains TypedDict definitions for Discord Stage Instance objects.
Reference: https://docs.discord.com/developers/resources/stage-instance
"""

from enum import IntEnum
from typing import TypedDict


class PrivacyLevel(IntEnum):
    """Privacy levels for stage instances.

    https://docs.discord.com/developers/resources/stage-instance#stage-instance-object-privacy-level
    """

    PUBLIC = 1  # Deprecated
    GUILD_ONLY = 2


class StageInstance(TypedDict, total=False):
    """Represents a live stage.

    https://docs.discord.com/developers/resources/stage-instance#stage-instance-object-stage-instance-structure
    """

    id: str  # Stage instance ID (snowflake)
    guild_id: str  # Guild ID (snowflake)
    channel_id: str  # Stage channel ID (snowflake)
    topic: str  # Topic of the stage instance (1-120 characters)
    privacy_level: int  # Privacy level (PrivacyLevel)
    discoverable_disabled: bool  # Whether Stage Discovery is disabled (deprecated)
    guild_scheduled_event_id: str | None  # Scheduled event ID for this stage (snowflake)


__all__ = [
    "PrivacyLevel",
    "StageInstance",
]
