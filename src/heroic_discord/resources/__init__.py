"""Discord Resources Module.

This module provides TypedDict definitions for all Discord API resource objects.
Reference: https://docs.discord.com/developers/resources
"""

from heroic_discord.resources.application import (
    Application,
    ApplicationFlag,
    ApplicationIntegrationType,
    InstallParams,
)
from heroic_discord.resources.audit_log import (
    AuditLog,
    AuditLogChange,
    AuditLogEntry,
    AuditLogEvent,
    OptionalAuditEntryInfo,
)
from heroic_discord.resources.auto_moderation import (
    ActionMetadata,
    ActionType,
    AutoModerationAction,
    AutoModerationRule,
    EventType,
    KeywordPresetType,
    TriggerMetadata,
    TriggerType,
)
from heroic_discord.resources.channel import (
    Channel,
    ChannelFlags,
    ChannelType,
    DefaultReaction,
    ForumLayoutType,
    ForumTag,
    Overwrite,
    SortOrderType,
    ThreadMember,
    ThreadMetadata,
    VideoQualityMode,
)
from heroic_discord.resources.emoji import Emoji
from heroic_discord.resources.entitlement import Entitlement, EntitlementType
from heroic_discord.resources.guild import (
    Ban,
    DefaultMessageNotificationLevel,
    ExplicitContentFilterLevel,
    Guild,
    GuildMember,
    GuildMemberFlags,
    GuildNSFWLevel,
    GuildOnboarding,
    GuildPreview,
    GuildWidget,
    GuildWidgetSettings,
    IncidentsData,
    Integration,
    IntegrationAccount,
    IntegrationApplication,
    IntegrationExpireBehavior,
    MFALevel,
    OnboardingMode,
    OnboardingPrompt,
    PremiumTier,
    PromptOption,
    PromptType,
    SystemChannelFlags,
    UnavailableGuild,
    VerificationLevel,
    WelcomeScreen,
    WelcomeScreenChannel,
)
from heroic_discord.resources.guild_scheduled_event import (
    EntityMetadata,
    EntityType,
    EventStatus,
    GuildScheduledEvent,
    GuildScheduledEventUser,
    PrivacyLevel,
    RecurrenceRule,
    RecurrenceRuleFrequency,
    RecurrenceRuleMonth,
    RecurrenceRuleNWeekday,
    RecurrenceRuleWeekday,
)
from heroic_discord.resources.guild_template import GuildTemplate
from heroic_discord.resources.invite import (
    Invite,
    InviteFlags,
    InviteMetadata,
    InviteTargetType,
    InviteType,
)
from heroic_discord.resources.lobby import Lobby, LobbyMember, LobbyMemberFlags
from heroic_discord.resources.message import (
    AllowedMentions,
    Attachment,
    AttachmentFlags,
    ChannelMention,
    Embed,
    Message,
    MessageActivity,
    MessageActivityType,
    MessageCall,
    MessageFlags,
    MessagePin,
    MessageReference,
    MessageReferenceType,
    MessageSnapshot,
    MessageType,
    Reaction,
    ReactionCountDetails,
    ReactionType,
    RoleSubscriptionData,
)
from heroic_discord.resources.poll import (
    LayoutType,
    Poll,
    PollAnswer,
    PollAnswerCount,
    PollCreateRequest,
    PollMedia,
    PollResults,
)
from heroic_discord.resources.sku import SKU, SKUFlags, SKUType
from heroic_discord.resources.soundboard import SoundboardSound
from heroic_discord.resources.stage_instance import (
    PrivacyLevel as StagePrivacyLevel,
)
from heroic_discord.resources.stage_instance import StageInstance
from heroic_discord.resources.sticker import (
    Sticker,
    StickerFormatType,
    StickerItem,
    StickerPack,
    StickerType,
)
from heroic_discord.resources.subscription import (
    Subscription,
    SubscriptionStatus,
)
from heroic_discord.resources.user import (
    ApplicationRoleConnection,
    AvatarDecorationData,
    Collectibles,
    Connection,
    Nameplate,
    PremiumType,
    User,
    UserFlags,
    UserPrimaryGuild,
)
from heroic_discord.resources.voice import VoiceRegion, VoiceState
from heroic_discord.resources.webhook import Webhook, WebhookType

__all__ = [
    # SKU
    "SKU",
    # Auto Moderation
    "ActionMetadata",
    "ActionType",
    # Message
    "AllowedMentions",
    # Application
    "Application",
    "ApplicationFlag",
    "ApplicationIntegrationType",
    # User
    "ApplicationRoleConnection",
    "Attachment",
    "AttachmentFlags",
    # Audit Log
    "AuditLog",
    "AuditLogChange",
    "AuditLogEntry",
    "AuditLogEvent",
    "AutoModerationAction",
    "AutoModerationRule",
    "AvatarDecorationData",
    # Guild
    "Ban",
    # Channel
    "Channel",
    "ChannelFlags",
    "ChannelMention",
    "ChannelType",
    "Collectibles",
    "Connection",
    "DefaultMessageNotificationLevel",
    "DefaultReaction",
    "Embed",
    # Emoji
    "Emoji",
    # Entitlement
    "Entitlement",
    "EntitlementType",
    # Guild Scheduled Event
    "EntityMetadata",
    "EntityType",
    "EventStatus",
    "EventType",
    "ExplicitContentFilterLevel",
    "ForumLayoutType",
    "ForumTag",
    "Guild",
    "GuildMember",
    "GuildMemberFlags",
    "GuildNSFWLevel",
    "GuildOnboarding",
    "GuildPreview",
    "GuildScheduledEvent",
    "GuildScheduledEventUser",
    # Guild Template
    "GuildTemplate",
    "GuildWidget",
    "GuildWidgetSettings",
    "IncidentsData",
    "InstallParams",
    "Integration",
    "IntegrationAccount",
    "IntegrationApplication",
    "IntegrationExpireBehavior",
    # Invite
    "Invite",
    "InviteFlags",
    "InviteMetadata",
    "InviteTargetType",
    "InviteType",
    "KeywordPresetType",
    # Poll
    "LayoutType",
    # Lobby
    "Lobby",
    "LobbyMember",
    "LobbyMemberFlags",
    "MFALevel",
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
    "Nameplate",
    "OnboardingMode",
    "OnboardingPrompt",
    "OptionalAuditEntryInfo",
    "Overwrite",
    "Poll",
    "PollAnswer",
    "PollAnswerCount",
    "PollCreateRequest",
    "PollMedia",
    "PollResults",
    "PremiumTier",
    "PremiumType",
    "PrivacyLevel",
    "PromptOption",
    "PromptType",
    "Reaction",
    "ReactionCountDetails",
    "ReactionType",
    "RecurrenceRule",
    "RecurrenceRuleFrequency",
    "RecurrenceRuleMonth",
    "RecurrenceRuleNWeekday",
    "RecurrenceRuleWeekday",
    "RoleSubscriptionData",
    "SKUFlags",
    "SKUType",
    "SortOrderType",
    # Soundboard
    "SoundboardSound",
    # Stage Instance
    "StageInstance",
    "StagePrivacyLevel",
    # Sticker
    "Sticker",
    "StickerFormatType",
    "StickerItem",
    "StickerPack",
    "StickerType",
    # Subscription
    "Subscription",
    "SubscriptionStatus",
    "SystemChannelFlags",
    "ThreadMember",
    "ThreadMetadata",
    "TriggerMetadata",
    "TriggerType",
    "UnavailableGuild",
    "User",
    "UserFlags",
    "UserPrimaryGuild",
    "VerificationLevel",
    "VideoQualityMode",
    # Voice
    "VoiceRegion",
    "VoiceState",
    # Webhook
    "Webhook",
    "WebhookType",
    "WelcomeScreen",
    "WelcomeScreenChannel",
]
