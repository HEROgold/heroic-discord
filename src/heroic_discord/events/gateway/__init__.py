"""Gateway events module for Discord WebSocket connections.

Gateway events are sent over WebSocket connections and are the primary way
to receive and send real-time events with Discord.

References:
    - https://docs.discord.com/developers/events/gateway
    - https://docs.discord.com/developers/events/gateway-events

"""

from __future__ import annotations

from . import receive_events, send_events
from .receive_events import (
    ApplicationCommandPermissionsUpdate,
    AutoModerationActionExecutionFields,
    ChannelPinsUpdateFields,
    GuildBanAddFields,
    GuildBanRemoveFields,
    GuildCreateExtraFields,
    GuildEmojisUpdateFields,
    GuildMemberAddFields,
    GuildMemberRemoveFields,
    GuildMembersChunkFields,
    GuildMemberUpdateFields,
    GuildRoleCreateFields,
    GuildRoleDeleteFields,
    GuildRoleUpdateFields,
    GuildStickersUpdateFields,
    HelloStructure,
    IntegrationCreateFields,
    IntegrationDeleteFields,
    IntegrationUpdateFields,
    InviteCreateFields,
    InviteDeleteFields,
    MessageCreateExtraFields,
    MessageDeleteBulkFields,
    MessageDeleteFields,
    MessagePollVoteAddFields,
    MessagePollVoteRemoveFields,
    MessageReactionAddFields,
    MessageReactionRemoveAllFields,
    MessageReactionRemoveEmojiFields,
    MessageReactionRemoveFields,
    PresenceUpdateFields,
    RateLimitedFields,
    ReadyEventFields,
    ThreadListSyncFields,
    ThreadMembersUpdateFields,
    ThreadMemberUpdateFields,
    TypingStartFields,
    VoiceChannelEffectSendFields,
    VoiceServerUpdateFields,
    WebhooksUpdateFields,
)
from .send_events import (
    ActivityObject,
    IdentifyConnectionProperties,
    IdentifyStructure,
    RequestGuildMembersStructure,
    RequestSoundboardSoundsStructure,
    ResumeStructure,
    UpdatePresenceStructure,
    UpdateVoiceStateStructure,
)

__all__ = [
    # Send Events
    "ActivityObject",
    # Receive Events
    "ApplicationCommandPermissionsUpdate",
    "AutoModerationActionExecutionFields",
    "ChannelPinsUpdateFields",
    "GuildBanAddFields",
    "GuildBanRemoveFields",
    "GuildCreateExtraFields",
    "GuildEmojisUpdateFields",
    "GuildMemberAddFields",
    "GuildMemberRemoveFields",
    "GuildMemberUpdateFields",
    "GuildMembersChunkFields",
    "GuildRoleCreateFields",
    "GuildRoleDeleteFields",
    "GuildRoleUpdateFields",
    "GuildStickersUpdateFields",
    "HelloStructure",
    "IdentifyConnectionProperties",
    "IdentifyStructure",
    "IntegrationCreateFields",
    "IntegrationDeleteFields",
    "IntegrationUpdateFields",
    "InviteCreateFields",
    "InviteDeleteFields",
    "MessageCreateExtraFields",
    "MessageDeleteBulkFields",
    "MessageDeleteFields",
    "MessagePollVoteAddFields",
    "MessagePollVoteRemoveFields",
    "MessageReactionAddFields",
    "MessageReactionRemoveAllFields",
    "MessageReactionRemoveEmojiFields",
    "MessageReactionRemoveFields",
    "PresenceUpdateFields",
    "RateLimitedFields",
    "ReadyEventFields",
    "RequestGuildMembersStructure",
    "RequestSoundboardSoundsStructure",
    "ResumeStructure",
    "ThreadListSyncFields",
    "ThreadMemberUpdateFields",
    "ThreadMembersUpdateFields",
    "TypingStartFields",
    "UpdatePresenceStructure",
    "UpdateVoiceStateStructure",
    "VoiceChannelEffectSendFields",
    "VoiceServerUpdateFields",
    "WebhooksUpdateFields",
    "receive_events",
    # Modules
    "send_events",
]
