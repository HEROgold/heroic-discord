"""Discord Emoji Resource Structures.

This module contains TypedDict definitions for Discord Emoji objects.
Reference: https://docs.discord.com/developers/resources/emoji
"""

from typing import TypedDict


class Emoji(TypedDict, total=False):
    """Represents a Discord emoji.

    https://docs.discord.com/developers/resources/emoji#emoji-object-emoji-structure
    """

    id: str | None  # Emoji ID (snowflake) or None for standard emoji
    name: str | None  # Emoji name (can be None for deleted custom emoji)
    roles: list[str]  # Role IDs allowed to use this emoji (snowflakes)
    user: dict  # User object that created this emoji
    require_colons: bool  # Whether this emoji must be wrapped in colons
    managed: bool  # Whether this emoji is managed
    animated: bool  # Whether this emoji is animated
    available: bool  # Whether this emoji can be used (may be false due to loss of Server Boosts)


__all__ = ["Emoji"]
