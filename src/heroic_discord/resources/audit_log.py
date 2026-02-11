"""Discord Audit Log Resource Structures.

This module contains TypedDict definitions for Discord Audit Log objects.
Reference: https://docs.discord.com/developers/resources/audit-log
"""

from enum import IntEnum
from typing import TypedDict


class AuditLogEvent(IntEnum):
    """Audit log event types.

    https://docs.discord.com/developers/resources/audit-log#audit-log-entry-object-audit-log-events
    """

    GUILD_UPDATE = 1
    CHANNEL_CREATE = 10
    CHANNEL_UPDATE = 11
    CHANNEL_DELETE = 12
    CHANNEL_OVERWRITE_CREATE = 13
    CHANNEL_OVERWRITE_UPDATE = 14
    CHANNEL_OVERWRITE_DELETE = 15
    MEMBER_KICK = 20
    MEMBER_PRUNE = 21
    MEMBER_BAN_ADD = 22
    MEMBER_BAN_REMOVE = 23
    MEMBER_UPDATE = 24
    MEMBER_ROLE_UPDATE = 25
    MEMBER_MOVE = 26
    MEMBER_DISCONNECT = 27
    BOT_ADD = 28
    ROLE_CREATE = 30
    ROLE_UPDATE = 31
    ROLE_DELETE = 32
    INVITE_CREATE = 40
    INVITE_UPDATE = 41
    INVITE_DELETE = 42
    WEBHOOK_CREATE = 50
    WEBHOOK_UPDATE = 51
    WEBHOOK_DELETE = 52
    EMOJI_CREATE = 60
    EMOJI_UPDATE = 61
    EMOJI_DELETE = 62
    MESSAGE_DELETE = 72
    MESSAGE_BULK_DELETE = 73
    MESSAGE_PIN = 74
    MESSAGE_UNPIN = 75
    INTEGRATION_CREATE = 80
    INTEGRATION_UPDATE = 81
    INTEGRATION_DELETE = 82
    STAGE_INSTANCE_CREATE = 83
    STAGE_INSTANCE_UPDATE = 84
    STAGE_INSTANCE_DELETE = 85
    STICKER_CREATE = 90
    STICKER_UPDATE = 91
    STICKER_DELETE = 92
    GUILD_SCHEDULED_EVENT_CREATE = 100
    GUILD_SCHEDULED_EVENT_UPDATE = 101
    GUILD_SCHEDULED_EVENT_DELETE = 102
    THREAD_CREATE = 110
    THREAD_UPDATE = 111
    THREAD_DELETE = 112
    APPLICATION_COMMAND_PERMISSION_UPDATE = 121
    SOUNDBOARD_SOUND_CREATE = 130
    SOUNDBOARD_SOUND_UPDATE = 131
    SOUNDBOARD_SOUND_DELETE = 132
    AUTO_MODERATION_RULE_CREATE = 140
    AUTO_MODERATION_RULE_UPDATE = 141
    AUTO_MODERATION_RULE_DELETE = 142
    AUTO_MODERATION_BLOCK_MESSAGE = 143
    AUTO_MODERATION_FLAG_TO_CHANNEL = 144
    AUTO_MODERATION_USER_COMMUNICATION_DISABLED = 145
    CREATOR_MONETIZATION_REQUEST_CREATED = 150
    CREATOR_MONETIZATION_TERMS_ACCEPTED = 151
    ONBOARDING_PROMPT_CREATE = 163
    ONBOARDING_PROMPT_UPDATE = 164
    ONBOARDING_PROMPT_DELETE = 165
    ONBOARDING_CREATE = 166
    ONBOARDING_UPDATE = 167
    HOME_SETTINGS_CREATE = 190
    HOME_SETTINGS_UPDATE = 191


class AuditLogChange(TypedDict, total=False):
    """Represents a change in an audit log entry.

    https://docs.discord.com/developers/resources/audit-log#audit-log-change-object
    """

    new_value: object  # New value of the key
    old_value: object  # Old value of the key
    key: str  # Name of the audit log change key


class OptionalAuditEntryInfo(TypedDict, total=False):
    """Optional information for certain audit log action types.

    https://docs.discord.com/developers/resources/audit-log#audit-log-entry-object-optional-audit-entry-info
    """

    application_id: str  # ID of the app whose permissions were targeted (snowflake)
    auto_moderation_rule_name: str  # Name of the Auto Moderation rule that was triggered
    auto_moderation_rule_trigger_type: str  # Trigger type of the Auto Moderation rule
    channel_id: str  # Channel in which entities were targeted (snowflake)
    count: str  # Number of entities that were targeted
    delete_member_days: str  # Number of days after which inactive members were kicked
    id: str  # ID of the over-written entity (snowflake)
    members_removed: str  # Number of members removed by the prune
    message_id: str  # ID of the message that was targeted (snowflake)
    role_name: str  # Name of the role
    type: str  # Type of overwrite (0 for role, 1 for member)
    integration_type: str  # Type of integration which performed the action


class AuditLogEntry(TypedDict, total=False):
    """Represents an entry in an audit log.

    https://docs.discord.com/developers/resources/audit-log#audit-log-entry-object
    """

    target_id: str | None  # ID of the affected entity (snowflake as string or None)
    changes: list[AuditLogChange]  # Changes made to the target_id
    user_id: str | None  # User or app that made the changes (snowflake as string or None)
    id: str  # ID of the entry (snowflake)
    action_type: int  # Type of action that occurred (AuditLogEvent)
    options: OptionalAuditEntryInfo  # Additional info for certain event types
    reason: str  # Reason for the change


class AuditLog(TypedDict, total=False):
    """Represents a guild's audit log.

    https://docs.discord.com/developers/resources/audit-log#audit-log-object
    """

    application_commands: list[dict]  # List of application commands referenced
    audit_log_entries: list[AuditLogEntry]  # Array of audit log entry objects
    auto_moderation_rules: list[dict]  # List of auto moderation rules referenced
    guild_scheduled_events: list[dict]  # List of guild scheduled events referenced
    integrations: list[dict]  # Array of partial integration objects
    threads: list[dict]  # Array of thread channel objects
    users: list[dict]  # Array of user objects
    webhooks: list[dict]  # Array of webhook objects


__all__ = [
    "AuditLog",
    "AuditLogChange",
    "AuditLogEntry",
    "AuditLogEvent",
    "OptionalAuditEntryInfo",
]
