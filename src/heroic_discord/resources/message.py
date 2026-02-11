"""Discord Message Resource Structures.

This module contains TypedDict definitions for Discord Message objects.
Reference: https://docs.discord.com/developers/resources/message

Note: This is one of the most complex Discord resources with many nested structures.
"""

from enum import IntEnum
from typing import TypedDict


class MessageType(IntEnum):
    """Message types.

    https://docs.discord.com/developers/resources/message#message-object-message-types
    """

    DEFAULT = 0
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    CHANNEL_NAME_CHANGE = 4
    CHANNEL_ICON_CHANGE = 5
    CHANNEL_PINNED_MESSAGE = 6
    USER_JOIN = 7
    GUILD_BOOST = 8
    GUILD_BOOST_TIER_1 = 9
    GUILD_BOOST_TIER_2 = 10
    GUILD_BOOST_TIER_3 = 11
    CHANNEL_FOLLOW_ADD = 12
    GUILD_DISCOVERY_DISQUALIFIED = 14
    GUILD_DISCOVERY_REQUALIFIED = 15
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING = 16
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING = 17
    THREAD_CREATED = 18
    REPLY = 19
    CHAT_INPUT_COMMAND = 20
    THREAD_STARTER_MESSAGE = 21
    GUILD_INVITE_REMINDER = 22
    CONTEXT_MENU_COMMAND = 23
    AUTO_MODERATION_ACTION = 24
    ROLE_SUBSCRIPTION_PURCHASE = 25
    INTERACTION_PREMIUM_UPSELL = 26
    STAGE_START = 27
    STAGE_END = 28
    STAGE_SPEAKER = 29
    STAGE_TOPIC = 31
    GUILD_APPLICATION_PREMIUM_SUBSCRIPTION = 32
    GUILD_INCIDENT_ALERT_MODE_ENABLED = 36
    GUILD_INCIDENT_ALERT_MODE_DISABLED = 37
    GUILD_INCIDENT_REPORT_RAID = 38
    GUILD_INCIDENT_REPORT_FALSE_ALARM = 39
    PURCHASE_NOTIFICATION = 44
    POLL_RESULT = 46


class MessageActivityType(IntEnum):
    """Message activity types.

    https://docs.discord.com/developers/resources/message#message-object-message-activity-types
    """

    JOIN = 1
    SPECTATE = 2
    LISTEN = 3
    JOIN_REQUEST = 5


class MessageFlags(IntEnum):
    """Message flags as powers of 2.

    https://docs.discord.com/developers/resources/message#message-object-message-flags
    """

    CROSSPOSTED = 1 << 0
    IS_CROSSPOST = 1 << 1
    SUPPRESS_EMBEDS = 1 << 2
    SOURCE_MESSAGE_DELETED = 1 << 3
    URGENT = 1 << 4
    HAS_THREAD = 1 << 5
    EPHEMERAL = 1 << 6
    LOADING = 1 << 7
    FAILED_TO_MENTION_SOME_ROLES_IN_THREAD = 1 << 8
    SUPPRESS_NOTIFICATIONS = 1 << 12
    IS_VOICE_MESSAGE = 1 << 13
    HAS_SNAPSHOT = 1 << 14
    IS_COMPONENTS_V2 = 1 << 15


class MessageReferenceType(IntEnum):
    """Message reference types.

    https://docs.discord.com/developers/resources/message#message-reference-object-message-reference-types
    """

    DEFAULT = 0
    FORWARD = 1


class ReactionType(IntEnum):
    """Reaction types.

    https://docs.discord.com/developers/resources/message#get-reactions-reaction-types
    """

    NORMAL = 0
    BURST = 1


class AttachmentFlags(IntEnum):
    """Attachment flags.

    https://docs.discord.com/developers/resources/message#attachment-object-attachment-flags
    """

    IS_REMIX = 1 << 2


class MessageActivity(TypedDict, total=False):
    """Message activity for Rich Presence.

    https://docs.discord.com/developers/resources/message#message-object-message-activity-structure
    """

    type: int  # Activity type (MessageActivityType)
    party_id: str  # Party ID from Rich Presence event


class MessageReference(TypedDict, total=False):
    """Reference to another message.

    https://docs.discord.com/developers/resources/message#message-reference-object
    """

    type: int  # Reference type (MessageReferenceType)
    message_id: str  # ID of originating message (snowflake)
    channel_id: str  # ID of originating channel (snowflake)
    guild_id: str  # ID of originating guild (snowflake)
    fail_if_not_exists: bool  # Whether to error if referenced message doesn't exist


class MessageSnapshot(TypedDict, total=False):
    """Snapshot of a forwarded message.

    https://docs.discord.com/developers/resources/message#message-snapshot-object
    """

    message: dict  # Partial message object (forwarded message subset)


class ReactionCountDetails(TypedDict, total=False):
    """Breakdown of reaction counts.

    https://docs.discord.com/developers/resources/message#reaction-count-details-object
    """

    burst: int  # Count of super reactions
    normal: int  # Count of normal reactions


class Reaction(TypedDict, total=False):
    """Reaction on a message.

    https://docs.discord.com/developers/resources/message#reaction-object
    """

    count: int  # Total reaction count
    count_details: ReactionCountDetails  # Reaction count breakdown
    me: bool  # Whether current user reacted
    me_burst: bool  # Whether current user super-reacted
    emoji: dict  # Partial emoji object
    burst_colors: list[str]  # HEX colors for super reaction


class Embed(TypedDict, total=False):
    """Rich embed content.

    https://docs.discord.com/developers/resources/message#embed-object
    """

    title: str  # Embed title (max 256 chars)
    type: str  # Embed type (always "rich" for webhooks)
    description: str  # Embed description (max 4096 chars)
    url: str  # URL of embed
    timestamp: str  # ISO8601 timestamp
    color: int  # Color code
    footer: dict  # Embed footer object
    image: dict  # Embed image object
    thumbnail: dict  # Embed thumbnail object
    video: dict  # Embed video object
    provider: dict  # Embed provider object
    author: dict  # Embed author object
    fields: list[dict]  # Embed field objects (max 25)


class Attachment(TypedDict, total=False):
    """Attached file on a message.

    https://docs.discord.com/developers/resources/message#attachment-object
    """

    id: str  # Attachment ID (snowflake)
    filename: str  # Filename
    title: str  # Title of the file
    description: str  # Description (max 1024 chars)
    content_type: str  # Media type
    size: int  # Size in bytes
    url: str  # Source URL
    proxy_url: str  # Proxied URL
    height: int | None  # Height if image
    width: int | None  # Width if image
    ephemeral: bool  # Whether attachment is ephemeral
    duration_secs: float  # Audio file duration (voice messages)
    waveform: str  # Base64 waveform (voice messages)
    flags: int  # Attachment flags bitfield


class ChannelMention(TypedDict, total=False):
    """Channel mentioned in message.

    https://docs.discord.com/developers/resources/message#channel-mention-object
    """

    id: str  # Channel ID (snowflake)
    guild_id: str  # Guild ID (snowflake)
    type: int  # Channel type
    name: str  # Channel name


class AllowedMentions(TypedDict, total=False):
    """Controls mention parsing.

    https://docs.discord.com/developers/resources/message#allowed-mentions-object
    """

    parse: list[str]  # Allowed mention types to parse
    roles: list[str]  # Role IDs to mention (snowflakes, max 100)
    users: list[str]  # User IDs to mention (snowflakes, max 100)
    replied_user: bool  # Whether to mention author of message being replied to


class RoleSubscriptionData(TypedDict, total=False):
    """Role subscription data for purchase messages.

    https://docs.discord.com/developers/resources/message#role-subscription-data-object
    """

    role_subscription_listing_id: str  # SKU/listing ID (snowflake)
    tier_name: str  # Tier name
    total_months_subscribed: int  # Cumulative months subscribed
    is_renewal: bool  # Whether this is a renewal notification


class MessageCall(TypedDict, total=False):
    """Call information in private channels.

    https://docs.discord.com/developers/resources/message#message-call-object
    """

    participants: list[str]  # User IDs that participated (snowflakes)
    ended_timestamp: str | None  # ISO8601 timestamp when call ended


class MessagePin(TypedDict, total=False):
    """Pinned message information.

    https://docs.discord.com/developers/resources/message#message-pin-object
    """

    pinned_at: str  # ISO8601 timestamp when pinned
    message: dict  # Pinned message object


class Message(TypedDict, total=False):
    """Represents a message in Discord.

    https://docs.discord.com/developers/resources/message#message-object

    Note: This is one of the most complex Discord objects with many fields.
    """

    id: str  # Message ID (snowflake)
    channel_id: str  # Channel ID (snowflake)
    author: dict  # User object (not always valid user)
    content: str  # Message contents (up to 2000 chars)
    timestamp: str  # ISO8601 timestamp when sent
    edited_timestamp: str | None  # ISO8601 timestamp when edited
    tts: bool  # Whether TTS message
    mention_everyone: bool  # Whether mentions everyone
    mentions: list[dict]  # Users mentioned
    mention_roles: list[str]  # Roles mentioned (snowflakes)
    mention_channels: list[ChannelMention]  # Channels mentioned
    attachments: list[Attachment]  # Attached files
    embeds: list[Embed]  # Embedded content
    reactions: list[Reaction]  # Reactions to message
    nonce: int | str  # Used for message send validation
    pinned: bool  # Whether message is pinned
    webhook_id: str  # Webhook ID if generated by webhook (snowflake)
    type: int  # Message type (MessageType)
    activity: MessageActivity  # Rich Presence activity
    application: dict  # Partial application object
    application_id: str  # Application ID (snowflake)
    flags: int  # Message flags bitfield
    message_reference: MessageReference  # Referenced message data
    message_snapshots: list[MessageSnapshot]  # Forwarded message snapshots
    referenced_message: dict | None  # Referenced message object
    interaction_metadata: dict  # Interaction metadata object
    interaction: dict  # Deprecated message interaction object
    thread: dict  # Thread started from this message
    components: list[dict]  # Message components
    sticker_items: list[dict]  # Message sticker item objects
    stickers: list[dict]  # Deprecated stickers
    position: int  # Approximate position in thread
    role_subscription_data: RoleSubscriptionData  # Role subscription data
    resolved: dict  # Resolved data for users/members/channels/roles
    poll: dict  # Poll object
    call: MessageCall  # Call information


__all__ = [
    "AllowedMentions",
    "Attachment",
    "AttachmentFlags",
    "ChannelMention",
    "Embed",
    "Message",
    "MessageActivity",
    "MessageActivityType",
    "MessageCall",
    "MessageFlags",
    "MessagePin",
    "MessageReference",
    "MessageReferenceType",
    "MessageSnapshot",
    "MessageType",
    "Reaction",
    "ReactionCountDetails",
    "ReactionType",
    "RoleSubscriptionData",
]
