"""Discord SKU Resource Structures.

This module contains TypedDict definitions for Discord SKU objects.
Reference: https://docs.discord.com/developers/resources/sku
"""

from enum import IntEnum
from typing import TypedDict


class SKUType(IntEnum):
    """Types of SKUs.

    https://docs.discord.com/developers/resources/sku#sku-object-sku-types
    """

    DURABLE = 2
    CONSUMABLE = 3
    SUBSCRIPTION = 5
    SUBSCRIPTION_GROUP = 6


class SKUFlags(IntEnum):
    """SKU flags as powers of 2.

    https://docs.discord.com/developers/resources/sku#sku-object-sku-flags
    """

    AVAILABLE = 1 << 2
    GUILD_SUBSCRIPTION = 1 << 7
    USER_SUBSCRIPTION = 1 << 8


class SKU(TypedDict, total=False):
    """Represents a Stock Keeping Unit.

    https://docs.discord.com/developers/resources/sku#sku-object-sku-structure
    """

    id: str  # SKU ID (snowflake)
    type: int  # SKU type (SKUType)
    application_id: str  # Application ID (snowflake)
    name: str  # Customer-facing name
    slug: str  # System-generated URL slug based on name
    flags: int  # SKU flags bitfield


__all__ = [
    "SKU",
    "SKUFlags",
    "SKUType",
]
