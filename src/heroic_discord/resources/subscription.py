"""Discord Subscription Resource Structures.

This module contains TypedDict definitions for Discord Subscription objects.
Reference: https://docs.discord.com/developers/resources/subscription
"""

from enum import IntEnum
from typing import TypedDict


class SubscriptionStatus(IntEnum):
    """Subscription status values.

    https://docs.discord.com/developers/resources/subscription#subscription-object-subscription-statuses
    """

    ACTIVE = 0
    ENDING = 1
    INACTIVE = 2


class Subscription(TypedDict, total=False):
    """Represents a recurring subscription.

    https://docs.discord.com/developers/resources/subscription#subscription-object
    """

    id: str  # Subscription ID (snowflake)
    user_id: str  # Subscribed user ID (snowflake)
    sku_ids: list[str]  # SKUs subscribed to (snowflakes)
    entitlement_ids: list[str]  # Entitlements granted (snowflakes)
    renewal_sku_ids: list[str] | None  # SKUs at renewal (snowflakes)
    current_period_start: str  # ISO8601 timestamp of period start
    current_period_end: str  # ISO8601 timestamp of period end
    status: int  # Subscription status (SubscriptionStatus)
    canceled_at: str | None  # ISO8601 timestamp when canceled
    country: str  # ISO3166-1 alpha-2 country code


__all__ = [
    "Subscription",
    "SubscriptionStatus",
]
