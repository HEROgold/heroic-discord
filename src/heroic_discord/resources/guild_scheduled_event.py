"""Discord Guild Scheduled Event Resource Structures.

This module contains TypedDict definitions for Discord Guild Scheduled Event objects.
Reference: https://docs.discord.com/developers/resources/guild-scheduled-event
"""

from enum import IntEnum
from typing import TypedDict


class PrivacyLevel(IntEnum):
    """Privacy levels for scheduled events.

    https://docs.discord.com/developers/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-privacy-level
    """

    GUILD_ONLY = 2


class EntityType(IntEnum):
    """Entity types for scheduled events.

    https://docs.discord.com/developers/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-entity-types
    """

    STAGE_INSTANCE = 1
    VOICE = 2
    EXTERNAL = 3


class EventStatus(IntEnum):
    """Status values for scheduled events.

    https://docs.discord.com/developers/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-status
    """

    SCHEDULED = 1
    ACTIVE = 2
    COMPLETED = 3
    CANCELED = 4


class RecurrenceRuleFrequency(IntEnum):
    """Recurrence frequencies.

    https://docs.discord.com/developers/resources/guild-scheduled-event#guild-scheduled-event-recurrence-rule-object-guild-scheduled-event-recurrence-rule-frequency
    """

    YEARLY = 0
    MONTHLY = 1
    WEEKLY = 2
    DAILY = 3


class RecurrenceRuleWeekday(IntEnum):
    """Days of the week for recurrence rules.

    https://docs.discord.com/developers/resources/guild-scheduled-event#guild-scheduled-event-recurrence-rule-object-guild-scheduled-event-recurrence-rule-weekday
    """

    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class RecurrenceRuleMonth(IntEnum):
    """Months for recurrence rules.

    https://docs.discord.com/developers/resources/guild-scheduled-event#guild-scheduled-event-recurrence-rule-object-guild-scheduled-event-recurrence-rule-month
    """

    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class EntityMetadata(TypedDict, total=False):
    """Additional metadata for scheduled events.

    https://docs.discord.com/developers/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-entity-metadata
    """

    location: str  # Location of event (1-100 characters, required for EXTERNAL)


class RecurrenceRuleNWeekday(TypedDict, total=False):
    """Specific day within a specific week for recurrence.

    https://docs.discord.com/developers/resources/guild-scheduled-event#guild-scheduled-event-recurrence-rule-object-guild-scheduled-event-recurrence-rule-nweekday-structure
    """

    n: int  # Week to reoccur on (1-5)
    day: int  # Day within week (RecurrenceRuleWeekday)


class RecurrenceRule(TypedDict, total=False):
    """Recurrence rule for scheduled events.

    https://docs.discord.com/developers/resources/guild-scheduled-event#guild-scheduled-event-recurrence-rule-object
    """

    start: str  # ISO8601 timestamp of recurrence interval start
    end: str | None  # ISO8601 timestamp of recurrence interval end
    frequency: int  # How often event occurs (RecurrenceRuleFrequency)
    interval: int  # Spacing between events defined by frequency
    by_weekday: list[int] | None  # Specific days within week to recur on
    by_n_weekday: list[RecurrenceRuleNWeekday] | None  # Specific days within specific weeks
    by_month: list[int] | None  # Specific months to recur on
    by_month_day: list[int] | None  # Specific dates within month to recur on
    by_year_day: list[int] | None  # Days within year to recur on (1-364)
    count: int | None  # Total times event can recur before stopping


class GuildScheduledEvent(TypedDict, total=False):
    """Represents a scheduled event in a guild.

    https://docs.discord.com/developers/resources/guild-scheduled-event#guild-scheduled-event-object
    """

    id: str  # Event ID (snowflake)
    guild_id: str  # Guild ID (snowflake)
    channel_id: str | None  # Channel ID (snowflake) or None for EXTERNAL
    creator_id: str | None  # User ID that created event (snowflake)
    name: str  # Event name (1-100 characters)
    description: str | None  # Event description (1-1000 characters)
    scheduled_start_time: str  # ISO8601 timestamp when event starts
    scheduled_end_time: str | None  # ISO8601 timestamp when event ends (required for EXTERNAL)
    privacy_level: int  # Privacy level (PrivacyLevel)
    status: int  # Event status (EventStatus)
    entity_type: int  # Entity type (EntityType)
    entity_id: str | None  # Entity ID (snowflake)
    entity_metadata: EntityMetadata | None  # Additional metadata
    creator: dict  # User object of creator
    user_count: int  # Number of users subscribed to event
    image: str | None  # Cover image hash
    recurrence_rule: RecurrenceRule | None  # Recurrence definition


class GuildScheduledEventUser(TypedDict, total=False):
    """User subscribed to a scheduled event.

    https://docs.discord.com/developers/resources/guild-scheduled-event#guild-scheduled-event-user-object
    """

    guild_scheduled_event_id: str  # Event ID (snowflake)
    user: dict  # User object
    member: dict  # Guild member object


__all__ = [
    "EntityMetadata",
    "EntityType",
    "EventStatus",
    "GuildScheduledEvent",
    "GuildScheduledEventUser",
    "PrivacyLevel",
    "RecurrenceRule",
    "RecurrenceRuleFrequency",
    "RecurrenceRuleMonth",
    "RecurrenceRuleNWeekday",
    "RecurrenceRuleWeekday",
]
