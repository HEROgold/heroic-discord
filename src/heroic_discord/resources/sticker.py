"""Discord Sticker Resource Structures.

This module contains TypedDict definitions for Discord Sticker objects.
Reference: https://docs.discord.com/developers/resources/sticker
"""

from enum import IntEnum
from typing import TypedDict


class StickerType(IntEnum):
    """Types of stickers.

    https://docs.discord.com/developers/resources/sticker#sticker-object-sticker-types
    """

    STANDARD = 1
    GUILD = 2


class StickerFormatType(IntEnum):
    """Sticker format types.

    https://docs.discord.com/developers/resources/sticker#sticker-object-sticker-format-types
    """

    PNG = 1
    APNG = 2
    LOTTIE = 3
    GIF = 4


class Sticker(TypedDict, total=False):
    """Represents a sticker.

    https://docs.discord.com/developers/resources/sticker#sticker-object-sticker-structure
    """

    id: str  # Sticker ID (snowflake)
    pack_id: str  # Pack ID for standard stickers (snowflake)
    name: str  # Sticker name
    description: str | None  # Sticker description
    tags: str  # Autocomplete/suggestion tags (max 200 characters)
    type: int  # Sticker type (StickerType)
    format_type: int  # Sticker format type (StickerFormatType)
    available: bool  # Whether sticker can be used (may be false due to loss of Server Boosts)
    guild_id: str  # Guild ID that owns this sticker (snowflake)
    user: dict  # User object that uploaded the guild sticker
    sort_value: int  # Standard sticker's sort order within its pack


class StickerItem(TypedDict, total=False):
    """Minimal sticker data required to render a sticker.

    https://docs.discord.com/developers/resources/sticker#sticker-item-object
    """

    id: str  # Sticker ID (snowflake)
    name: str  # Sticker name
    format_type: int  # Sticker format type (StickerFormatType)


class StickerPack(TypedDict, total=False):
    """Represents a pack of standard stickers.

    https://docs.discord.com/developers/resources/sticker#sticker-pack-object
    """

    id: str  # Sticker pack ID (snowflake)
    stickers: list[Sticker]  # Stickers in the pack
    name: str  # Pack name
    sku_id: str  # Pack's SKU ID (snowflake)
    cover_sticker_id: str  # ID of sticker shown as pack's icon (snowflake)
    description: str  # Description of the sticker pack
    banner_asset_id: str  # Pack's banner image ID (snowflake)


__all__ = [
    "Sticker",
    "StickerFormatType",
    "StickerItem",
    "StickerPack",
    "StickerType",
]
