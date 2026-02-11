"""Gateway send events - events sent from the app to Discord.

These events are encapsulated in an event payload and sent by an app
to Discord through a Gateway connection.

References:
    https://docs.discord.com/developers/events/gateway-events#send-events

"""

from __future__ import annotations

from typing import Any, TypedDict


class IdentifyConnectionProperties(TypedDict):
    """Connection properties for Identify event.

    References:
        https://docs.discord.com/developers/events/gateway-events#identify-identify-connection-properties

    """

    os: str  # Operating system
    browser: str  # Library name
    device: str  # Library name


class IdentifyStructure(TypedDict, total=False):
    """Identify event structure - triggers initial handshake with gateway.

    Used to trigger the initial handshake with the gateway.

    References:
        https://docs.discord.com/developers/events/gateway-events#identify-identify-structure

    """

    token: str  # Authentication token
    properties: IdentifyConnectionProperties  # Connection properties
    compress: bool  # Whether connection supports compression (default: False)
    large_threshold: int  # Value between 50-250 for offline member threshold (default: 50)
    shard: tuple[int, int] | None  # [shard_id, num_shards] for Guild Sharding
    presence: dict[str, Any] | None  # Initial presence information
    intents: int  # Gateway Intents you wish to receive


class ResumeStructure(TypedDict):
    """Resume event structure - replays missed events after disconnect.

    Used to replay missed events when a disconnected client resumes.

    References:
        https://docs.discord.com/developers/events/gateway-events#resume

    """

    token: str  # Session token
    session_id: str  # Session ID
    seq: int  # Last sequence number received


class RequestGuildMembersStructure(TypedDict, total=False):
    """Request Guild Members event structure.

    Used to request all members for a guild or a list of guilds.
    Requires GUILD_MEMBERS intent for certain operations.

    References:
        https://docs.discord.com/developers/events/gateway-events#request-guild-members

    """

    guild_id: str  # Guild ID to get members for (snowflake)
    query: str  # Username prefix, or empty string for all members
    limit: int  # Max members to send (0 with empty query = all members)
    presences: bool  # Include presences of matched members (default: False)
    user_ids: str | list[str]  # Specific user ID(s) to fetch
    nonce: str  # Nonce to identify Guild Members Chunk response (max 32 bytes)


class RequestSoundboardSoundsStructure(TypedDict):
    """Request Soundboard Sounds event structure.

    Used to request soundboard sounds for a list of guilds.

    References:
        https://docs.discord.com/developers/events/gateway-events#request-soundboard-sounds

    """

    guild_ids: list[str]  # Guild IDs to get soundboard sounds for (snowflakes)


class UpdateVoiceStateStructure(TypedDict):
    """Update Voice State event structure.

    Sent when client wants to join, move, or disconnect from a voice channel.

    References:
        https://docs.discord.com/developers/events/gateway-events#update-voice-state

    """

    guild_id: str  # Guild ID (snowflake)
    channel_id: str | None  # Voice channel ID (null if disconnecting)
    self_mute: bool  # Whether client is muted
    self_deaf: bool  # Whether client is deafened


class ActivityObject(TypedDict, total=False):
    """Activity object for presence updates.

    References:
        https://docs.discord.com/developers/events/gateway-events#activity-object

    """

    name: str  # Activity's name
    type: int  # Activity type (0-5)
    url: str | None  # Stream URL (for type 1)


class UpdatePresenceStructure(TypedDict):
    """Update Presence event structure.

    Sent to indicate a presence or status update.
    Note: Clients may only update their game status 5 times per 20 seconds.

    References:
        https://docs.discord.com/developers/events/gateway-events#update-presence

    """

    since: int | None  # Unix time (ms) when client went idle, or null
    activities: list[ActivityObject]  # User's activities
    status: str  # User's new status (online, dnd, idle, invisible, offline)
    afk: bool  # Whether client is AFK
