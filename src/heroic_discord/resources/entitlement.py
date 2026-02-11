"""Discord Entitlement Resource Structures.

This module contains TypedDict definitions for Discord Entitlement objects.
Reference: https://docs.discord.com/developers/resources/entitlement
"""

from enum import IntEnum
from typing import TypedDict


class EntitlementType(IntEnum):
    """Types of entitlements.

    https://docs.discord.com/developers/resources/entitlement#entitlement-object-entitlement-types
    """

    PURCHASE = 1
    PREMIUM_SUBSCRIPTION = 2
    DEVELOPER_GIFT = 3
    TEST_MODE_PURCHASE = 4
    FREE_PURCHASE = 5
    USER_GIFT = 6
    PREMIUM_PURCHASE = 7
    APPLICATION_SUBSCRIPTION = 8


class Entitlement(TypedDict, total=False):
    """Represents an entitlement.

    https://docs.discord.com/developers/resources/entitlement#entitlement-object-entitlement-structure
    """

    id: str  # Entitlement ID (snowflake)
    sku_id: str  # SKU ID (snowflake)
    application_id: str  # Application ID (snowflake)
    user_id: str  # User ID granted access (snowflake)
    type: int  # Entitlement type (EntitlementType)
    deleted: bool  # Whether entitlement was deleted
    starts_at: str  # ISO8601 timestamp when valid starts
    ends_at: str  # ISO8601 timestamp when valid ends
    guild_id: str  # Guild ID granted access (snowflake)
    consumed: bool  # Whether consumable entitlement has been consumed


__all__ = [
    "Entitlement",
    "EntitlementType",
]
