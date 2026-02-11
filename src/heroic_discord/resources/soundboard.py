"""Discord Soundboard Resource Structures.

This module contains TypedDict definitions for Discord Soundboard objects.
Reference: https://docs.discord.com/developers/resources/soundboard
"""

from typing import TypedDict


class SoundboardSound(TypedDict, total=False):
    """Represents a soundboard sound.

    https://docs.discord.com/developers/resources/soundboard#soundboard-sound-object
    """

    name: str  # Sound name
    sound_id: str  # Sound ID (snowflake)
    volume: float  # Volume (0 to 1)
    emoji_id: str | None  # Custom emoji ID (snowflake)
    emoji_name: str | None  # Unicode emoji or None
    guild_id: str  # Guild ID this sound is in (snowflake)
    available: bool  # Whether sound can be used
    user: dict  # User object who created this sound


__all__ = ["SoundboardSound"]
