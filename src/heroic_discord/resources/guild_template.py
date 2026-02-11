"""Discord Guild Template Resource Structures.

This module contains TypedDict definitions for Discord Guild Template objects.
Reference: https://docs.discord.com/developers/resources/guild-template
"""

from typing import TypedDict


class GuildTemplate(TypedDict, total=False):
    """Represents a guild template for creating guilds.

    https://docs.discord.com/developers/resources/guild-template#guild-template-object
    """

    code: str  # Template code (unique ID)
    name: str  # Template name
    description: str | None  # Description
    usage_count: int  # Number of times template has been used
    creator_id: str  # User ID who created template (snowflake)
    creator: dict  # User object of creator
    created_at: str  # ISO8601 timestamp when created
    updated_at: str  # ISO8601 timestamp of last sync to source guild
    source_guild_id: str  # Source guild ID (snowflake)
    serialized_source_guild: dict  # Partial guild object (guild snapshot)
    is_dirty: bool | None  # Whether template has unsynced changes


__all__ = ["GuildTemplate"]
