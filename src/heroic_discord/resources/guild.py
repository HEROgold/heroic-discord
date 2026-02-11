"""Discord Guild Resource Structures.

This module contains TypedDict definitions for Discord Guild objects.
Reference: https://docs.discord.com/developers/resources/guild

Note: This is one of the most complex Discord resources with many nested structures.
"""

from enum import IntEnum
from typing import TypedDict


class DefaultMessageNotificationLevel(IntEnum):
    """Default notification level for guilds.

    https://docs.discord.com/developers/resources/guild#guild-object-default-message-notification-level
    """

    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1


class ExplicitContentFilterLevel(IntEnum):
    """Explicit content filter level.

    https://docs.discord.com/developers/resources/guild#guild-object-explicit-content-filter-level
    """

    DISABLED = 0
    MEMBERS_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2


class MFALevel(IntEnum):
    """MFA level for guild.

    https://docs.discord.com/developers/resources/guild#guild-object-mfa-level
    """

    NONE = 0
    ELEVATED = 1


class VerificationLevel(IntEnum):
    """Verification level for guild.

    https://docs.discord.com/developers/resources/guild#guild-object-verification-level
    """

    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4


class GuildNSFWLevel(IntEnum):
    """Guild NSFW level.

    https://docs.discord.com/developers/resources/guild#guild-object-guild-nsfw-level
    """

    DEFAULT = 0
    EXPLICIT = 1
    SAFE = 2
    AGE_RESTRICTED = 3


class PremiumTier(IntEnum):
    """Guild premium (boost) tier.

    https://docs.discord.com/developers/resources/guild#guild-object-premium-tier
    """

    NONE = 0
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 3


class SystemChannelFlags(IntEnum):
    """System channel flags as powers of 2.

    https://docs.discord.com/developers/resources/guild#guild-object-system-channel-flags
    """

    SUPPRESS_JOIN_NOTIFICATIONS = 1 << 0
    SUPPRESS_PREMIUM_SUBSCRIPTIONS = 1 << 1
    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS = 1 << 2
    SUPPRESS_JOIN_NOTIFICATION_REPLIES = 1 << 3
    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATIONS = 1 << 4
    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATION_REPLIES = 1 << 5


class GuildMemberFlags(IntEnum):
    """Guild member flags as powers of 2.

    https://docs.discord.com/developers/resources/guild#guild-member-object-guild-member-flags
    """

    DID_REJOIN = 1 << 0
    COMPLETED_ONBOARDING = 1 << 1
    BYPASSES_VERIFICATION = 1 << 2
    STARTED_ONBOARDING = 1 << 3
    IS_GUEST = 1 << 4
    STARTED_HOME_ACTIONS = 1 << 5
    COMPLETED_HOME_ACTIONS = 1 << 6
    AUTOMOD_QUARANTINED_USERNAME = 1 << 7
    DM_SETTINGS_UPSELL_ACKNOWLEDGED = 1 << 9


class IntegrationExpireBehavior(IntEnum):
    """Integration expiration behavior.

    https://docs.discord.com/developers/resources/guild#integration-object-integration-expire-behaviors
    """

    REMOVE_ROLE = 0
    KICK = 1


class OnboardingMode(IntEnum):
    """Onboarding mode for guilds.

    https://docs.discord.com/developers/resources/guild#guild-onboarding-object-onboarding-mode
    """

    ONBOARDING_DEFAULT = 0
    ONBOARDING_ADVANCED = 1


class PromptType(IntEnum):
    """Onboarding prompt type.

    https://docs.discord.com/developers/resources/guild#guild-onboarding-object-prompt-types
    """

    MULTIPLE_CHOICE = 0
    DROPDOWN = 1


class UnavailableGuild(TypedDict, total=False):
    """Partial guild object for unavailable guilds.

    https://docs.discord.com/developers/resources/guild#unavailable-guild-object
    """

    id: str  # Guild ID (snowflake)
    unavailable: bool  # True if guild is unavailable


class GuildPreview(TypedDict, total=False):
    """Preview of a public guild.

    https://docs.discord.com/developers/resources/guild#guild-preview-object
    """

    id: str  # Guild ID (snowflake)
    name: str  # Guild name
    icon: str | None  # Icon hash
    splash: str | None  # Splash hash
    discovery_splash: str | None  # Discovery splash hash
    emojis: list[dict]  # Emoji objects
    features: list[str]  # Guild features
    approximate_member_count: int  # Approximate member count
    approximate_presence_count: int  # Approximate online member count
    description: str | None  # Guild description
    stickers: list[dict]  # Sticker objects


class GuildWidgetSettings(TypedDict, total=False):
    """Guild widget settings.

    https://docs.discord.com/developers/resources/guild#guild-widget-settings-object
    """

    enabled: bool  # Whether widget is enabled
    channel_id: str | None  # Widget channel ID (snowflake)


class GuildWidget(TypedDict, total=False):
    """Guild widget.

    https://docs.discord.com/developers/resources/guild#guild-widget-object
    """

    id: str  # Guild ID (snowflake)
    name: str  # Guild name
    instant_invite: str | None  # Instant invite URL
    channels: list[dict]  # Voice and stage channels
    members: list[dict]  # Special widget user objects
    presence_count: int  # Online member count


class GuildMember(TypedDict, total=False):
    """Guild member object.

    https://docs.discord.com/developers/resources/guild#guild-member-object
    """

    user: dict  # User object
    nick: str | None  # Nickname
    avatar: str | None  # Guild-specific avatar hash
    roles: list[str]  # Role IDs (snowflakes)
    joined_at: str  # ISO8601 timestamp when joined
    premium_since: str | None  # ISO8601 timestamp when boosted
    deaf: bool  # Whether deafened in voice
    mute: bool  # Whether muted in voice
    flags: int  # Guild member flags bitfield
    pending: bool  # Whether user has passed membership screening
    permissions: str  # Total permissions in channel
    communication_disabled_until: str | None  # ISO8601 timeout until
    avatar_decoration_data: dict | None  # Avatar decoration data object
    banner: str | None  # Guild-specific banner hash


class IntegrationAccount(TypedDict, total=False):
    """Integration account object.

    https://docs.discord.com/developers/resources/guild#integration-account-object
    """

    id: str  # Account ID
    name: str  # Account name


class IntegrationApplication(TypedDict, total=False):
    """Integration application object.

    https://docs.discord.com/developers/resources/guild#integration-application-object
    """

    id: str  # Application ID (snowflake)
    name: str  # Application name
    icon: str | None  # Icon hash
    description: str  # Application description
    bot: dict  # Bot user object


class Integration(TypedDict, total=False):
    """Guild integration object.

    https://docs.discord.com/developers/resources/guild#integration-object
    """

    id: str  # Integration ID (snowflake)
    name: str  # Integration name
    type: str  # Integration type (twitch, youtube, discord, guild_subscription)
    enabled: bool  # Whether integration is enabled
    syncing: bool  # Whether integration is syncing
    role_id: str  # Role ID that integration uses (snowflake)
    enable_emoticons: bool  # Whether emoticons are synced
    expire_behavior: int  # Expiration behavior (IntegrationExpireBehavior)
    expire_grace_period: int  # Grace period in days before expiring
    user: dict  # User object for this integration
    account: IntegrationAccount  # Integration account object
    synced_at: str  # ISO8601 timestamp when last synced
    subscriber_count: int  # Subscriber count
    revoked: bool  # Whether integration has been revoked
    application: IntegrationApplication  # Integration application
    scopes: list[str]  # OAuth2 scopes


class Ban(TypedDict, total=False):
    """Guild ban object.

    https://docs.discord.com/developers/resources/guild#ban-object
    """

    reason: str | None  # Reason for ban
    user: dict  # Banned user object


class WelcomeScreenChannel(TypedDict, total=False):
    """Welcome screen channel.

    https://docs.discord.com/developers/resources/guild#welcome-screen-object-welcome-screen-channel-structure
    """

    channel_id: str  # Channel ID (snowflake)
    description: str  # Channel description
    emoji_id: str | None  # Emoji ID (snowflake)
    emoji_name: str | None  # Emoji name


class WelcomeScreen(TypedDict, total=False):
    """Guild welcome screen.

    https://docs.discord.com/developers/resources/guild#welcome-screen-object
    """

    description: str | None  # Server description
    welcome_channels: list[WelcomeScreenChannel]  # Welcome screen channels


class PromptOption(TypedDict, total=False):
    """Onboarding prompt option.

    https://docs.discord.com/developers/resources/guild#guild-onboarding-object-prompt-option-structure
    """

    id: str  # Option ID (snowflake)
    channel_ids: list[str]  # Channel IDs (snowflakes)
    role_ids: list[str]  # Role IDs (snowflakes)
    emoji: dict  # Emoji object
    emoji_id: str  # Emoji ID (snowflake)
    emoji_name: str  # Emoji name
    emoji_animated: bool  # Whether emoji is animated
    title: str  # Option title
    description: str | None  # Option description


class OnboardingPrompt(TypedDict, total=False):
    """Onboarding prompt.

    https://docs.discord.com/developers/resources/guild#guild-onboarding-object-onboarding-prompt-structure
    """

    id: str  # Prompt ID (snowflake)
    type: int  # Prompt type (PromptType)
    options: list[PromptOption]  # Prompt options
    title: str  # Prompt title
    single_select: bool  # Whether single selection
    required: bool  # Whether required
    in_onboarding: bool  # Whether shown in onboarding
    in_home: bool  # Whether shown in customize guild


class GuildOnboarding(TypedDict, total=False):
    """Guild onboarding configuration.

    https://docs.discord.com/developers/resources/guild#guild-onboarding-object
    """

    guild_id: str  # Guild ID (snowflake)
    prompts: list[OnboardingPrompt]  # Onboarding prompts
    default_channel_ids: list[str]  # Default channel IDs (snowflakes)
    enabled: bool  # Whether onboarding is enabled
    mode: int  # Onboarding mode (OnboardingMode)


class IncidentsData(TypedDict, total=False):
    """Guild incidents data.

    https://docs.discord.com/developers/resources/guild#guild-object-guild-incidents-data-structure
    """

    invites_disabled_until: str | None  # ISO8601 timestamp when invites re-enabled
    dms_disabled_until: str | None  # ISO8601 timestamp when DMs to non-friends re-enabled


class Guild(TypedDict, total=False):
    """Represents a guild (server) in Discord.

    https://docs.discord.com/developers/resources/guild#guild-object

    Note: This is one of the most complex Discord objects with many fields.
    """

    id: str  # Guild ID (snowflake)
    name: str  # Guild name (2-100 chars)
    icon: str | None  # Icon hash
    icon_hash: str | None  # Icon hash (returned in template)
    splash: str | None  # Splash hash
    discovery_splash: str | None  # Discovery splash hash
    owner: bool  # Whether user is owner
    owner_id: str  # Owner user ID (snowflake)
    permissions: str  # Total permissions for user
    region: str | None  # Deprecated voice region ID
    afk_channel_id: str | None  # AFK channel ID (snowflake)
    afk_timeout: int  # AFK timeout in seconds
    widget_enabled: bool  # Whether widget is enabled
    widget_channel_id: str | None  # Widget channel ID (snowflake)
    verification_level: int  # Verification level (VerificationLevel)
    default_message_notifications: int  # Default notification level
    explicit_content_filter: int  # Explicit content filter level
    roles: list[dict]  # Role objects
    emojis: list[dict]  # Emoji objects
    features: list[str]  # Guild features
    mfa_level: int  # Required MFA level (MFALevel)
    application_id: str | None  # Application ID if bot-created (snowflake)
    system_channel_id: str | None  # System channel ID (snowflake)
    system_channel_flags: int  # System channel flags bitfield
    rules_channel_id: str | None  # Rules channel ID (snowflake)
    max_presences: int | None  # Max presences (null is always 25000)
    max_members: int  # Maximum members
    vanity_url_code: str | None  # Vanity URL code
    description: str | None  # Guild description
    banner: str | None  # Banner hash
    premium_tier: int  # Premium tier (PremiumTier)
    premium_subscription_count: int  # Number of boosts
    preferred_locale: str  # Preferred locale
    public_updates_channel_id: str | None  # Public updates channel ID (snowflake)
    max_video_channel_users: int  # Max users in video channel
    max_stage_video_channel_users: int  # Max users in stage video channel
    approximate_member_count: int  # Approximate member count
    approximate_presence_count: int  # Approximate presence count
    welcome_screen: WelcomeScreen  # Welcome screen object
    nsfw_level: int  # Guild NSFW level (GuildNSFWLevel)
    stickers: list[dict]  # Sticker objects
    premium_progress_bar_enabled: bool  # Whether boost progress bar is enabled
    safety_alerts_channel_id: str | None  # Safety alerts channel ID (snowflake)
    latest_onboarding_question_id: str | None  # Latest onboarding question ID (snowflake)
    hub_type: str | None  # Hub type for Student Hubs
    clan: dict | None  # Clan object
    inventory_settings: dict | None  # Inventory settings
    home_header: str | None  # Home header hash
    incidents_data: IncidentsData | None  # Guild incidents data


__all__ = [
    "Ban",
    "DefaultMessageNotificationLevel",
    "ExplicitContentFilterLevel",
    "Guild",
    "GuildMember",
    "GuildMemberFlags",
    "GuildNSFWLevel",
    "GuildOnboarding",
    "GuildPreview",
    "GuildWidget",
    "GuildWidgetSettings",
    "IncidentsData",
    "Integration",
    "IntegrationAccount",
    "IntegrationApplication",
    "IntegrationExpireBehavior",
    "MFALevel",
    "OnboardingMode",
    "OnboardingPrompt",
    "PremiumTier",
    "PromptOption",
    "PromptType",
    "SystemChannelFlags",
    "UnavailableGuild",
    "VerificationLevel",
    "WelcomeScreen",
    "WelcomeScreenChannel",
]
