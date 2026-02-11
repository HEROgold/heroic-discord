"""Discord Auto Moderation Resource Structures.

This module contains TypedDict definitions for Discord Auto Moderation objects.
Reference: https://docs.discord.com/developers/resources/auto-moderation
"""

from enum import IntEnum
from typing import TypedDict


class TriggerType(IntEnum):
    """Auto moderation trigger types.

    https://docs.discord.com/developers/resources/auto-moderation#auto-moderation-rule-object-trigger-types
    """

    KEYWORD = 1
    SPAM = 3
    KEYWORD_PRESET = 4
    MENTION_SPAM = 5
    MEMBER_PROFILE = 6


class KeywordPresetType(IntEnum):
    """Keyword preset types for auto moderation.

    https://docs.discord.com/developers/resources/auto-moderation#auto-moderation-rule-object-keyword-preset-types
    """

    PROFANITY = 1
    SEXUAL_CONTENT = 2
    SLURS = 3


class EventType(IntEnum):
    """Event types that trigger auto moderation.

    https://docs.discord.com/developers/resources/auto-moderation#auto-moderation-rule-object-event-types
    """

    MESSAGE_SEND = 1
    MEMBER_UPDATE = 2


class ActionType(IntEnum):
    """Types of actions auto moderation can take.

    https://docs.discord.com/developers/resources/auto-moderation#auto-moderation-action-object-action-types
    """

    BLOCK_MESSAGE = 1
    SEND_ALERT_MESSAGE = 2
    TIMEOUT = 3
    BLOCK_MEMBER_INTERACTION = 4


class TriggerMetadata(TypedDict, total=False):
    """Metadata associated with a trigger.

    https://docs.discord.com/developers/resources/auto-moderation#auto-moderation-rule-object-trigger-metadata
    """

    keyword_filter: list[str]  # Substrings to search for (max 1000)
    regex_patterns: list[str]  # Regular expressions to match (max 10)
    presets: list[int]  # Preset keyword types (KeywordPresetType values)
    allow_list: list[str]  # Substrings exempt from triggering (max 100)
    mention_total_limit: int  # Total mentions allowed (1-50)
    mention_raid_protection_enabled: bool  # Whether mention raid protection is enabled


class ActionMetadata(TypedDict, total=False):
    """Metadata for auto moderation actions.

    https://docs.discord.com/developers/resources/auto-moderation#auto-moderation-action-object-action-metadata
    """

    channel_id: str  # Channel to send alert message to (snowflake)
    duration_seconds: int  # Timeout duration in seconds (max 2419200 = 28 days)
    custom_message: str  # Custom message shown to the user (max 150 characters)


class AutoModerationAction(TypedDict, total=False):
    """Represents an action taken by auto moderation.

    https://docs.discord.com/developers/resources/auto-moderation#auto-moderation-action-object
    """

    type: int  # Type of action (ActionType)
    metadata: ActionMetadata  # Additional metadata needed for the action


class AutoModerationRule(TypedDict, total=False):
    """Represents an auto moderation rule.

    https://docs.discord.com/developers/resources/auto-moderation#auto-moderation-rule-object
    """

    id: str  # Rule ID (snowflake)
    guild_id: str  # Guild ID this rule belongs to (snowflake)
    name: str  # Rule name
    creator_id: str  # User who created the rule (snowflake)
    event_type: int  # Event type (EventType)
    trigger_type: int  # Trigger type (TriggerType)
    trigger_metadata: TriggerMetadata  # Metadata for the trigger
    actions: list[AutoModerationAction]  # Actions to execute when rule is triggered
    enabled: bool  # Whether the rule is enabled
    exempt_roles: list[str]  # Roles exempt from the rule (snowflakes, max 20)
    exempt_channels: list[str]  # Channels exempt from the rule (snowflakes, max 50)


__all__ = [
    "ActionMetadata",
    "ActionType",
    "AutoModerationAction",
    "AutoModerationRule",
    "EventType",
    "KeywordPresetType",
    "TriggerMetadata",
    "TriggerType",
]
