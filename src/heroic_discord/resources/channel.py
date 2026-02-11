"""Discord Channel Resource Structures.

This module contains TypedDict definitions for Discord Channel objects.
Reference: https://docs.discord.com/developers/resources/channel
"""

from enum import IntEnum
from typing import TypedDict


class ChannelType(IntEnum):
    """Types of Discord channels.

    https://docs.discord.com/developers/resources/channel#channel-object-channel-types
    """

    GUILD_TEXT = 0
    DM = 1
    GUILD_VOICE = 2
    GROUP_DM = 3
    GUILD_CATEGORY = 4
    GUILD_ANNOUNCEMENT = 5
    ANNOUNCEMENT_THREAD = 10
    PUBLIC_THREAD = 11
    PRIVATE_THREAD = 12
    GUILD_STAGE_VOICE = 13
    GUILD_DIRECTORY = 14
    GUILD_FORUM = 15
    GUILD_MEDIA = 16


class VideoQualityMode(IntEnum):
    """Video quality modes for voice channels.

    https://docs.discord.com/developers/resources/channel#channel-object-video-quality-modes
    """

    AUTO = 1
    FULL = 2


class ChannelFlags(IntEnum):
    """Channel flags as powers of 2.

    https://docs.discord.com/developers/resources/channel#channel-object-channel-flags
    """

    PINNED = 1 << 1
    REQUIRE_TAG = 1 << 4
    HIDE_MEDIA_DOWNLOAD_OPTIONS = 1 << 15


class SortOrderType(IntEnum):
    """Sort order types for forum channels.

    https://docs.discord.com/developers/resources/channel#channel-object-sort-order-types
    """

    LATEST_ACTIVITY = 0
    CREATION_DATE = 1


class ForumLayoutType(IntEnum):
    """Forum layout types.

    https://docs.discord.com/developers/resources/channel#channel-object-forum-layout-types
    """

    NOT_SET = 0
    LIST_VIEW = 1
    GALLERY_VIEW = 2


class Overwrite(TypedDict, total=False):
    """Permission overwrite for a channel.

    https://docs.discord.com/developers/resources/channel#overwrite-object
    """

    id: str  # Role or user ID (snowflake)
    type: int  # 0 for role, 1 for member
    allow: str  # Permission bit set
    deny: str  # Permission bit set


class ThreadMetadata(TypedDict, total=False):
    """Metadata for a thread channel.

    https://docs.discord.com/developers/resources/channel#thread-metadata-object
    """

    archived: bool  # Whether the thread is archived
    auto_archive_duration: int  # Duration in minutes to auto-archive (60, 1440, 4320, 10080)
    archive_timestamp: str  # ISO8601 timestamp when archived
    locked: bool  # Whether the thread is locked
    invitable: bool  # Whether non-moderators can add users (private threads only)
    create_timestamp: str | None  # ISO8601 timestamp when created


class ThreadMember(TypedDict, total=False):
    """Represents a user's connection to a thread.

    https://docs.discord.com/developers/resources/channel#thread-member-object
    """

    id: str  # Thread ID (snowflake)
    user_id: str  # User ID (snowflake)
    join_timestamp: str  # ISO8601 timestamp when joined
    flags: int  # User-thread settings flags
    member: dict  # Guild member object


class DefaultReaction(TypedDict, total=False):
    """Default reaction emoji for forum/media channels.

    https://docs.discord.com/developers/resources/channel#default-reaction-object
    """

    emoji_id: str | None  # Emoji ID (snowflake) or None
    emoji_name: str | None  # Emoji name or None


class ForumTag(TypedDict, total=False):
    """Tag for forum/media channels.

    https://docs.discord.com/developers/resources/channel#forum-tag-object
    """

    id: str  # Tag ID (snowflake)
    name: str  # Tag name (max 20 characters)
    moderated: bool  # Whether only moderators can add this tag
    emoji_id: str | None  # Emoji ID (snowflake)
    emoji_name: str | None  # Unicode emoji name


class Channel(TypedDict, total=False):
    """Represents a Discord channel.

    https://docs.discord.com/developers/resources/channel#channel-object-channel-structure
    """

    id: str  # Channel ID (snowflake)
    type: int  # Channel type (ChannelType)
    guild_id: str  # Guild ID (snowflake)
    position: int  # Sorting position
    permission_overwrites: list[Overwrite]  # Permission overwrites
    name: str | None  # Channel name (1-100 characters)
    topic: str | None  # Channel topic (0-1024 characters for text, 0-120 for voice/stage)
    nsfw: bool  # Whether the channel is NSFW
    last_message_id: str | None  # ID of last message (snowflake)
    bitrate: int  # Voice channel bitrate (in bits)
    user_limit: int  # Voice channel user limit (0-99)
    rate_limit_per_user: int  # Slowmode seconds per user (0-21600)
    recipients: list[dict]  # Recipients (DM channels)
    icon: str | None  # Icon hash
    owner_id: str  # Creator ID for DM/group DM (snowflake)
    application_id: str  # Application ID if bot-created (snowflake)
    managed: bool  # Whether the channel is managed by an app
    parent_id: str | None  # Parent category ID (snowflake)
    last_pin_timestamp: str | None  # ISO8601 timestamp of last pinned message
    rtc_region: str | None  # Voice region ID
    video_quality_mode: int  # Video quality mode
    message_count: int  # Approximate message count (threads)
    member_count: int  # Approximate member count (threads, stops at 50)
    thread_metadata: ThreadMetadata  # Thread-specific metadata
    member: ThreadMember  # Thread member object for the current user
    default_auto_archive_duration: int  # Default auto-archive duration in minutes
    permissions: str  # Computed permissions for invoking user
    flags: int  # Channel flags bitfield
    total_message_sent: int  # Total messages sent in thread
    available_tags: list[ForumTag]  # Available tags for forum/media channels
    applied_tags: list[str]  # Tag IDs applied to a thread (snowflakes)
    default_reaction_emoji: DefaultReaction | None  # Default reaction emoji
    default_thread_rate_limit_per_user: int  # Initial rate_limit_per_user for threads
    default_sort_order: int | None  # Default sort order type
    default_forum_layout: int  # Default forum layout type


__all__ = [
    "Channel",
    "ChannelFlags",
    "ChannelType",
    "DefaultReaction",
    "ForumLayoutType",
    "ForumTag",
    "Overwrite",
    "SortOrderType",
    "ThreadMember",
    "ThreadMetadata",
    "VideoQualityMode",
]
