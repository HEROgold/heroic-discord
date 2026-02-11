"""Gateway receive events - events sent from Discord to the app.

These events represent actions happening in Discord servers where the app
is installed. Receive events are Gateway events sent by Discord to an app.

References:
    https://docs.discord.com/developers/events/gateway-events#receive-events

"""

from __future__ import annotations

from typing import Any, TypedDict

# Connection/Lifecycle Events

class HelloStructure(TypedDict):
    """Hello event data - sent on connection to websocket.

    Defines the heartbeat interval that an app should heartbeat with.

    References:
        https://docs.discord.com/developers/events/gateway-events#hello

    """

    heartbeat_interval: int  # Interval (in milliseconds) to heartbeat with


class ReadyEventFields(TypedDict, total=False):
    """Ready event fields - dispatched when client completes initial handshake.

    Contains all state required for a client to begin interacting with the platform.

    References:
        https://docs.discord.com/developers/events/gateway-events#ready

    """

    v: int  # API version
    user: dict[str, Any]  # User object with email
    guilds: list[dict[str, Any]]  # Unavailable Guild objects
    session_id: str  # Used for resuming connections
    resume_gateway_url: str  # Gateway URL for resuming connections
    shard: tuple[int, int] | None  # [shard_id, num_shards] if sent when identifying
    application: dict[str, Any]  # Partial application object (id and flags)


# Application Command Events

class ApplicationCommandPermissionsUpdate(TypedDict):
    """Application command permissions update event.

    Sent when application command permissions are updated.
    Payload is an application command permissions object.

    Event: APPLICATION_COMMAND_PERMISSIONS_UPDATE
    """

    # Uses application command permissions object structure


# Auto Moderation Events

class AutoModerationActionExecutionFields(TypedDict, total=False):
    """Auto Moderation Action Execution event fields.

    Sent when a rule is triggered and an action is executed.
    Requires MANAGE_GUILD permission.

    Event: AUTO_MODERATION_ACTION_EXECUTION

    References:
        https://docs.discord.com/developers/events/gateway-events#auto-moderation-action-execution

    """

    guild_id: str  # Guild ID where action was executed (snowflake)
    action: dict[str, Any]  # Action which was executed
    rule_id: str  # Rule ID which action belongs to (snowflake)
    rule_trigger_type: int  # Trigger type of rule
    user_id: str  # User ID who generated triggering content (snowflake)
    channel_id: str  # Channel ID where content was posted (snowflake)
    message_id: str  # Message ID of user content (snowflake)
    alert_system_message_id: str  # System message ID from this action (snowflake)
    content: str  # User-generated text content (requires MESSAGE_CONTENT intent)
    matched_keyword: str | None  # Word/phrase that triggered the rule
    matched_content: str | None  # Substring that triggered (requires MESSAGE_CONTENT)


# Channel Events

class ThreadListSyncFields(TypedDict, total=False):
    """Thread List Sync event fields.

    Sent when gaining access to a channel.
    Event: THREAD_LIST_SYNC

    References:
        https://docs.discord.com/developers/events/gateway-events#thread-list-sync

    """

    guild_id: str  # Guild ID (snowflake)
    channel_ids: list[str]  # Parent channel IDs being synced (snowflakes)
    threads: list[dict[str, Any]]  # All active threads (channel objects)
    members: list[dict[str, Any]]  # Thread member objects for current user


class ThreadMemberUpdateFields(TypedDict):
    """Thread Member Update event fields.

    Sent when thread member for current user is updated.
    Event: THREAD_MEMBER_UPDATE

    References:
        https://docs.discord.com/developers/events/gateway-events#thread-member-update

    """

    guild_id: str  # Guild ID (snowflake)
    # Rest of fields from thread member object


class ThreadMembersUpdateFields(TypedDict, total=False):
    """Thread Members Update event fields.

    Sent when anyone is added/removed from a thread.
    Event: THREAD_MEMBERS_UPDATE

    References:
        https://docs.discord.com/developers/events/gateway-events#thread-members-update

    """

    id: str  # Thread ID (snowflake)
    guild_id: str  # Guild ID (snowflake)
    member_count: int  # Approximate member count (capped at 50)
    added_members: list[dict[str, Any]]  # Added thread members
    removed_member_ids: list[str]  # Removed user IDs (snowflakes)


class ChannelPinsUpdateFields(TypedDict, total=False):
    """Channel Pins Update event fields.

    Sent when message is pinned/unpinned in a text channel.
    Event: CHANNEL_PINS_UPDATE

    References:
        https://docs.discord.com/developers/events/gateway-events#channel-pins-update

    """

    guild_id: str  # Guild ID (snowflake)
    channel_id: str  # Channel ID (snowflake)
    last_pin_timestamp: str | None  # ISO8601 timestamp of most recent pin


# Guild Events

class GuildCreateExtraFields(TypedDict, total=False):
    """Guild Create extra fields beyond standard guild object.

    Event: GUILD_CREATE

    References:
        https://docs.discord.com/developers/events/gateway-events#guild-create

    """

    joined_at: str  # ISO8601 timestamp when guild was joined
    large: bool  # True if considered a large guild
    unavailable: bool  # True if unavailable due to outage
    member_count: int  # Total members in guild
    voice_states: list[dict[str, Any]]  # Partial voice state objects
    members: list[dict[str, Any]]  # Guild member objects
    channels: list[dict[str, Any]]  # Channel objects
    threads: list[dict[str, Any]]  # Active thread channel objects
    presences: list[dict[str, Any]]  # Partial presence objects
    stage_instances: list[dict[str, Any]]  # Stage instance objects
    guild_scheduled_events: list[dict[str, Any]]  # Guild scheduled event objects
    soundboard_sounds: list[dict[str, Any]]  # Soundboard sound objects


class GuildBanAddFields(TypedDict):
    """Guild Ban Add event fields.

    Sent when a user is banned from a guild.
    Event: GUILD_BAN_ADD

    References:
        https://docs.discord.com/developers/events/gateway-events#guild-ban-add

    """

    guild_id: str  # Guild ID (snowflake)
    user: dict[str, Any]  # Banned user object


class GuildBanRemoveFields(TypedDict):
    """Guild Ban Remove event fields.

    Sent when a user is unbanned from a guild.
    Event: GUILD_BAN_REMOVE

    References:
        https://docs.discord.com/developers/events/gateway-events#guild-ban-remove

    """

    guild_id: str  # Guild ID (snowflake)
    user: dict[str, Any]  # Unbanned user object


class GuildEmojisUpdateFields(TypedDict):
    """Guild Emojis Update event fields.

    Sent when guild's emojis are updated.
    Event: GUILD_EMOJIS_UPDATE

    References:
        https://docs.discord.com/developers/events/gateway-events#guild-emojis-update

    """

    guild_id: str  # Guild ID (snowflake)
    emojis: list[dict[str, Any]]  # Array of emoji objects


class GuildStickersUpdateFields(TypedDict):
    """Guild Stickers Update event fields.

    Sent when guild's stickers are updated.
    Event: GUILD_STICKERS_UPDATE

    References:
        https://docs.discord.com/developers/events/gateway-events#guild-stickers-update

    """

    guild_id: str  # Guild ID (snowflake)
    stickers: list[dict[str, Any]]  # Array of sticker objects


class GuildMemberAddFields(TypedDict):
    """Guild Member Add extra fields.

    Sent when new user joins a guild. Requires GUILD_MEMBERS intent.
    Event: GUILD_MEMBER_ADD

    References:
        https://docs.discord.com/developers/events/gateway-events#guild-member-add

    """

    guild_id: str  # Guild ID (snowflake)
    # Plus all guild member object fields


class GuildMemberRemoveFields(TypedDict):
    """Guild Member Remove event fields.

    Sent when user is removed from guild. Requires GUILD_MEMBERS intent.
    Event: GUILD_MEMBER_REMOVE

    References:
        https://docs.discord.com/developers/events/gateway-events#guild-member-remove

    """

    guild_id: str  # Guild ID (snowflake)
    user: dict[str, Any]  # Removed user object


class GuildMemberUpdateFields(TypedDict, total=False):
    """Guild Member Update event fields.

    Sent when guild member is updated. Requires GUILD_MEMBERS intent.
    Event: GUILD_MEMBER_UPDATE

    References:
        https://docs.discord.com/developers/events/gateway-events#guild-member-update

    """

    guild_id: str  # Guild ID (snowflake)
    roles: list[str]  # User role IDs (snowflakes)
    user: dict[str, Any]  # User object
    nick: str | None  # Nickname in guild
    avatar: str | None  # Guild avatar hash
    banner: str | None  # Guild banner hash
    joined_at: str | None  # ISO8601 timestamp when user joined
    premium_since: str | None  # ISO8601 timestamp when started boosting
    deaf: bool  # Whether deafened in voice channels
    mute: bool  # Whether muted in voice channels
    pending: bool  # Whether passed Membership Screening
    communication_disabled_until: str | None  # ISO8601 timeout expiration
    avatar_decoration_data: dict[str, Any] | None  # Avatar decoration data


class GuildMembersChunkFields(TypedDict, total=False):
    """Guild Members Chunk event fields.

    Sent in response to Request Guild Members.
    Event: GUILD_MEMBERS_CHUNK

    References:
        https://docs.discord.com/developers/events/gateway-events#guild-members-chunk

    """

    guild_id: str  # Guild ID (snowflake)
    members: list[dict[str, Any]]  # Set of guild member objects
    chunk_index: int  # Chunk index in expected chunks
    chunk_count: int  # Total expected chunks
    not_found: list[Any]  # Invalid IDs from REQUEST_GUILD_MEMBERS
    presences: list[dict[str, Any]]  # Presence objects if requested
    nonce: str  # Nonce from Guild Members Request


class GuildRoleCreateFields(TypedDict):
    """Guild Role Create event fields.

    Sent when a guild role is created.
    Event: GUILD_ROLE_CREATE

    References:
        https://docs.discord.com/developers/events/gateway-events#guild-role-create

    """

    guild_id: str  # Guild ID (snowflake)
    role: dict[str, Any]  # Created role object


class GuildRoleUpdateFields(TypedDict):
    """Guild Role Update event fields.

    Sent when a guild role is updated.
    Event: GUILD_ROLE_UPDATE

    References:
        https://docs.discord.com/developers/events/gateway-events#guild-role-update

    """

    guild_id: str  # Guild ID (snowflake)
    role: dict[str, Any]  # Updated role object


class GuildRoleDeleteFields(TypedDict):
    """Guild Role Delete event fields.

    Sent when a guild role is deleted.
    Event: GUILD_ROLE_DELETE

    References:
        https://docs.discord.com/developers/events/gateway-events#guild-role-delete

    """

    guild_id: str  # Guild ID (snowflake)
    role_id: str  # Role ID (snowflake)


# Message Events

class MessageCreateExtraFields(TypedDict, total=False):
    """Message Create extra fields.

    Sent when a message is created.
    Event: MESSAGE_CREATE

    References:
        https://docs.discord.com/developers/events/gateway-events#message-create

    """

    guild_id: str  # Guild ID (snowflake, unless ephemeral)
    member: dict[str, Any]  # Partial guild member object
    mentions: list[dict[str, Any]]  # User objects with optional partial member


class MessageDeleteFields(TypedDict, total=False):
    """Message Delete event fields.

    Sent when a message is deleted.
    Event: MESSAGE_DELETE

    References:
        https://docs.discord.com/developers/events/gateway-events#message-delete

    """

    id: str  # Message ID (snowflake)
    channel_id: str  # Channel ID (snowflake)
    guild_id: str  # Guild ID (snowflake)


class MessageDeleteBulkFields(TypedDict, total=False):
    """Message Delete Bulk event fields.

    Sent when multiple messages are deleted at once.
    Event: MESSAGE_DELETE_BULK

    References:
        https://docs.discord.com/developers/events/gateway-events#message-delete-bulk

    """

    ids: list[str]  # Message IDs (snowflakes)
    channel_id: str  # Channel ID (snowflake)
    guild_id: str  # Guild ID (snowflake)


class MessageReactionAddFields(TypedDict, total=False):
    """Message Reaction Add event fields.

    Sent when a user adds a reaction to a message.
    Event: MESSAGE_REACTION_ADD

    References:
        https://docs.discord.com/developers/events/gateway-events#message-reaction-add

    """

    user_id: str  # User ID (snowflake)
    channel_id: str  # Channel ID (snowflake)
    message_id: str  # Message ID (snowflake)
    guild_id: str  # Guild ID (snowflake)
    member: dict[str, Any]  # Member who reacted (if in guild)
    emoji: dict[str, Any]  # Partial emoji object
    message_author_id: str  # Message author ID (snowflake)
    burst: bool  # True if super-reaction
    burst_colors: list[str]  # Super-reaction colors in #rrggbb format
    type: int  # Reaction type


class MessageReactionRemoveFields(TypedDict, total=False):
    """Message Reaction Remove event fields.

    Sent when a user removes a reaction from a message.
    Event: MESSAGE_REACTION_REMOVE

    References:
        https://docs.discord.com/developers/events/gateway-events#message-reaction-remove

    """

    user_id: str  # User ID (snowflake)
    channel_id: str  # Channel ID (snowflake)
    message_id: str  # Message ID (snowflake)
    guild_id: str  # Guild ID (snowflake)
    emoji: dict[str, Any]  # Partial emoji object
    burst: bool  # True if super-reaction
    type: int  # Reaction type


class MessageReactionRemoveAllFields(TypedDict, total=False):
    """Message Reaction Remove All event fields.

    Sent when all reactions are removed from a message.
    Event: MESSAGE_REACTION_REMOVE_ALL

    References:
        https://docs.discord.com/developers/events/gateway-events#message-reaction-remove-all

    """

    channel_id: str  # Channel ID (snowflake)
    message_id: str  # Message ID (snowflake)
    guild_id: str  # Guild ID (snowflake)


class MessageReactionRemoveEmojiFields(TypedDict, total=False):
    """Message Reaction Remove Emoji event fields.

    Sent when all instances of a given emoji are removed.
    Event: MESSAGE_REACTION_REMOVE_EMOJI

    References:
        https://docs.discord.com/developers/events/gateway-events#message-reaction-remove-emoji

    """

    channel_id: str  # Channel ID (snowflake)
    guild_id: str  # Guild ID (snowflake)
    message_id: str  # Message ID (snowflake)
    emoji: dict[str, Any]  # Partial emoji object


# Presence Events

class PresenceUpdateFields(TypedDict):
    """Presence Update event fields.

    Sent when user's presence or info is updated. Requires GUILD_PRESENCES intent.
    Event: PRESENCE_UPDATE

    References:
        https://docs.discord.com/developers/events/gateway-events#presence-update

    """

    user: dict[str, Any]  # User object (may be partial)
    guild_id: str  # Guild ID (snowflake)
    status: str  # Status: idle, dnd, online, or offline
    activities: list[dict[str, Any]]  # Activity objects
    client_status: dict[str, str]  # Platform-dependent status


class TypingStartFields(TypedDict, total=False):
    """Typing Start event fields.

    Sent when a user starts typing in a channel.
    Event: TYPING_START

    References:
        https://docs.discord.com/developers/events/gateway-events#typing-start

    """

    channel_id: str  # Channel ID (snowflake)
    guild_id: str  # Guild ID (snowflake)
    user_id: str  # User ID (snowflake)
    timestamp: int  # Unix time (seconds) when user started typing
    member: dict[str, Any]  # Member who started typing (if in guild)


# Voice Events

class VoiceChannelEffectSendFields(TypedDict, total=False):
    """Voice Channel Effect Send event fields.

    Sent when someone sends an effect in a voice channel.
    Event: VOICE_CHANNEL_EFFECT_SEND

    References:
        https://docs.discord.com/developers/events/gateway-events#voice-channel-effect-send

    """

    channel_id: str  # Channel ID (snowflake)
    guild_id: str  # Guild ID (snowflake)
    user_id: str  # User ID who sent effect (snowflake)
    emoji: dict[str, Any] | None  # Emoji sent (for emoji/soundboard effects)
    animation_type: int | None  # Emoji animation type
    animation_id: int | None  # Emoji animation ID
    sound_id: str | int | None  # Soundboard sound ID
    sound_volume: float  # Soundboard sound volume (0-1)


class VoiceServerUpdateFields(TypedDict):
    """Voice Server Update event fields.

    Sent when guild's voice server is updated.
    Event: VOICE_SERVER_UPDATE

    References:
        https://docs.discord.com/developers/events/gateway-events#voice-server-update

    """

    token: str  # Voice connection token
    guild_id: str  # Guild ID (snowflake)
    endpoint: str | None  # Voice server host (null if reallocating)


# Webhook Events

class WebhooksUpdateFields(TypedDict):
    """Webhooks Update event fields.

    Sent when guild channel's webhook is created/updated/deleted.
    Event: WEBHOOKS_UPDATE

    References:
        https://docs.discord.com/developers/events/gateway-events#webhooks-update

    """

    guild_id: str  # Guild ID (snowflake)
    channel_id: str  # Channel ID (snowflake)


# Integration Events

class IntegrationCreateFields(TypedDict):
    """Integration Create event fields.

    Sent when an integration is created.
    Event: INTEGRATION_CREATE

    References:
        https://docs.discord.com/developers/events/gateway-events#integration-create

    """

    guild_id: str  # Guild ID (snowflake)
    # Plus integration object fields (without user)


class IntegrationUpdateFields(TypedDict):
    """Integration Update event fields.

    Sent when an integration is updated.
    Event: INTEGRATION_UPDATE

    References:
        https://docs.discord.com/developers/events/gateway-events#integration-update

    """

    guild_id: str  # Guild ID (snowflake)
    # Plus integration object fields (without user)


class IntegrationDeleteFields(TypedDict, total=False):
    """Integration Delete event fields.

    Sent when an integration is deleted.
    Event: INTEGRATION_DELETE

    References:
        https://docs.discord.com/developers/events/gateway-events#integration-delete

    """

    id: str  # Integration ID (snowflake)
    guild_id: str  # Guild ID (snowflake)
    application_id: str  # Bot/OAuth2 application ID (snowflake)


# Invite Events

class InviteCreateFields(TypedDict, total=False):
    """Invite Create event fields.

    Sent when new invite to channel is created. Requires MANAGE_CHANNELS.
    Event: INVITE_CREATE

    References:
        https://docs.discord.com/developers/events/gateway-events#invite-create

    """

    channel_id: str  # Channel ID (snowflake)
    code: str  # Unique invite code
    created_at: str  # ISO8601 timestamp when created
    guild_id: str  # Guild ID (snowflake)
    inviter: dict[str, Any]  # User who created invite
    max_age: int  # How long invite is valid (seconds)
    max_uses: int  # Maximum uses
    target_type: int  # Target type for voice channel invite
    target_user: dict[str, Any]  # Target user for stream invite
    target_application: dict[str, Any]  # Target application for embedded app
    temporary: bool  # Whether invite is temporary
    uses: int  # How many times used (always 0)
    expires_at: str | None  # ISO8601 expiration date
    role_ids: list[str]  # Role IDs granted on acceptance (snowflakes)


class InviteDeleteFields(TypedDict, total=False):
    """Invite Delete event fields.

    Sent when an invite is deleted. Requires MANAGE_CHANNELS.
    Event: INVITE_DELETE

    References:
        https://docs.discord.com/developers/events/gateway-events#invite-delete

    """

    channel_id: str  # Channel ID (snowflake)
    guild_id: str  # Guild ID (snowflake)
    code: str  # Unique invite code


# Poll Events

class MessagePollVoteAddFields(TypedDict, total=False):
    """Message Poll Vote Add event fields.

    Sent when a user votes on a poll.
    Event: MESSAGE_POLL_VOTE_ADD

    References:
        https://docs.discord.com/developers/events/gateway-events#message-poll-vote-add

    """

    user_id: str  # User ID (snowflake)
    channel_id: str  # Channel ID (snowflake)
    message_id: str  # Message ID (snowflake)
    guild_id: str  # Guild ID (snowflake)
    answer_id: int  # Answer ID


class MessagePollVoteRemoveFields(TypedDict, total=False):
    """Message Poll Vote Remove event fields.

    Sent when a user removes vote on a poll.
    Event: MESSAGE_POLL_VOTE_REMOVE

    References:
        https://docs.discord.com/developers/events/gateway-events#message-poll-vote-remove

    """

    user_id: str  # User ID (snowflake)
    channel_id: str  # Channel ID (snowflake)
    message_id: str  # Message ID (snowflake)
    guild_id: str  # Guild ID (snowflake)
    answer_id: int  # Answer ID


# Rate Limit Events

class RateLimitedFields(TypedDict, total=False):
    """Rate Limited event fields.

    Sent when app encounters a gateway rate limit.
    Event: RATE_LIMITED

    References:
        https://docs.discord.com/developers/events/gateway-events#rate-limited

    """

    opcode: int  # Gateway opcode that was rate limited
    retry_after: float  # Seconds to wait before submitting another request
    meta: dict[str, Any]  # Metadata for the rate limited event
