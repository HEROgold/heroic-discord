"""Discord Application Resource Structures.

This module contains TypedDict definitions for Discord Application objects.
Reference: https://docs.discord.com/developers/resources/application
"""

from enum import IntEnum
from typing import TypedDict


class ApplicationIntegrationType(IntEnum):
    """Types of application integrations.

    https://docs.discord.com/developers/resources/application#application-object-application-integration-types
    """

    GUILD_INSTALL = 0
    USER_INSTALL = 1


class ApplicationFlag(IntEnum):
    """Application flags as powers of 2.

    https://docs.discord.com/developers/resources/application#application-object-application-flags
    """

    APPLICATION_AUTO_MODERATION_RULE_CREATE_BADGE = 1 << 6
    GATEWAY_PRESENCE = 1 << 12
    GATEWAY_PRESENCE_LIMITED = 1 << 13
    GATEWAY_GUILD_MEMBERS = 1 << 14
    GATEWAY_GUILD_MEMBERS_LIMITED = 1 << 15
    VERIFICATION_PENDING_GUILD_LIMIT = 1 << 16
    EMBEDDED = 1 << 17
    GATEWAY_MESSAGE_CONTENT = 1 << 18
    GATEWAY_MESSAGE_CONTENT_LIMITED = 1 << 19
    APPLICATION_COMMAND_BADGE = 1 << 23


class InstallParams(TypedDict, total=False):
    """OAuth2 install parameters for an application.

    https://docs.discord.com/developers/resources/application#install-params-object
    """

    scopes: list[str]  # OAuth2 scopes to add the application with
    permissions: str  # Permissions to grant the application


class ApplicationIntegrationTypeConfiguration(TypedDict, total=False):
    """Configuration for an application integration type.

    https://docs.discord.com/developers/resources/application#application-object-application-integration-type-configuration-object
    """

    oauth2_install_params: InstallParams  # Install params for this integration type


class EventWebhooksConfiguration(TypedDict, total=False):
    """Configuration for event webhooks.

    https://docs.discord.com/developers/resources/application#application-object
    """

    url: str  # The URL to send event webhooks to
    status: int  # Status of the webhook (e.g., 1 = active)


class ActivityInstance(TypedDict, total=False):
    """Represents an activity instance.

    https://docs.discord.com/developers/resources/application#activity-instance-object
    """

    id: str  # Instance ID


class ActivityLocation(TypedDict, total=False):
    """Represents location information for an activity.

    https://docs.discord.com/developers/resources/application#activity-location-object
    """

    id: str  # Location ID
    kind: str  # Type of location (e.g., "gc" for guild channel)
    channel_id: str  # Channel ID
    guild_id: str  # Guild ID


class Application(TypedDict, total=False):
    """Represents a Discord Application.

    https://docs.discord.com/developers/resources/application#application-object-application-structure
    """

    id: str  # Application ID (snowflake)
    name: str  # Name of the application
    icon: str | None  # Icon hash
    description: str  # Description of the application
    rpc_origins: list[str]  # RPC origin URLs
    bot_public: bool  # Whether the bot is public
    bot_require_code_grant: bool  # Whether the bot requires OAuth2 code grant
    bot: dict  # Partial user object for the bot
    terms_of_service_url: str  # Terms of service URL
    privacy_policy_url: str  # Privacy policy URL
    owner: dict  # Partial user object of the owner
    verify_key: str  # Hex encoded verification key
    team: dict | None  # Team object if the application belongs to a team
    guild_id: str  # Guild ID if the application is a game sold on Discord
    guild: dict  # Partial guild object
    primary_sku_id: str  # Primary SKU ID if the application is a game sold on Discord
    slug: str  # URL slug
    cover_image: str  # Cover image hash
    flags: int  # Application flags bitfield
    approximate_guild_count: int  # Approximate count of guilds the app is in
    approximate_user_install_count: int  # Approximate count of user installs
    redirect_uris: list[str]  # OAuth2 redirect URIs
    interactions_endpoint_url: str  # Interactions endpoint URL
    role_connections_verification_url: str  # Role connections verification URL
    event_webhooks_url: str  # Event webhooks URL
    event_webhooks_status: int  # Event webhooks status
    event_webhooks_types: list[str]  # Event webhook types subscribed to
    tags: list[str]  # Tags describing the application
    install_params: InstallParams  # Settings for custom OAuth2 authorization
    integration_types_config: dict[str, ApplicationIntegrationTypeConfiguration]  # Integration configs  # noqa: E501
    custom_install_url: str  # Custom OAuth2 authorization URL
    event_webhooks: EventWebhooksConfiguration  # Event webhooks configuration


__all__ = [
    "ActivityInstance",
    "ActivityLocation",
    "Application",
    "ApplicationFlag",
    "ApplicationIntegrationType",
    "ApplicationIntegrationTypeConfiguration",
    "EventWebhooksConfiguration",
    "InstallParams",
]
