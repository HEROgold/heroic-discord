"""Discord user-installable apps and application commands support.

This module provides comprehensive support for creating Discord applications
that can be installed to user accounts, guilds, or both, with full control
over installation and interaction contexts.

Key Features:
    - Installation context types (GUILD_INSTALL, USER_INSTALL)
    - Interaction context types (GUILD, BOT_DM, PRIVATE_CHANNEL)
    - Application command types (CHAT_INPUT, USER, MESSAGE, PRIMARY_ENTRY_POINT)
    - Command builder with fluent interface
    - Command registration helpers
    - Interaction metadata structures
    - Utility functions for common operations

References:
    - Tutorial: https://docs.discord.com/developers/tutorials/developing-a-user-installable-app
    - Commands: https://docs.discord.com/developers/interactions/application-commands
    - Contexts: https://docs.discord.com/developers/interactions/application-commands#contexts

Examples:
    >>> from heroic_discord.installable_apps import (
    ...     CommandBuilder,
    ...     IntegrationType,
    ...     InteractionContextType,
    ... )
    >>> # Create a user-installable command
    >>> builder = CommandBuilder("profile", "View your profile")
    >>> builder.add_user_install_context()
    >>> builder.add_interaction_context(InteractionContextType.BOT_DM)
    >>> command = builder.build()

"""

from heroic_discord.installable_apps.builder import CommandBuilder, CommandRegistrar
from heroic_discord.installable_apps.commands import (
    ApplicationCommand,
    ApplicationCommandOption,
    ApplicationCommandOptionChoice,
    CreateApplicationCommand,
)
from heroic_discord.installable_apps.enums import (
    ApplicationCommandOptionType,
    ApplicationCommandType,
    CommandHandlerType,
    IntegrationType,
    InteractionContextType,
)
from heroic_discord.installable_apps.interactions import (
    AuthorizingIntegrationOwners,
    Interaction,
    InteractionData,
    InteractionMetadata,
    PartialChannel,
    PartialUser,
)
from heroic_discord.installable_apps.utils import (
    create_ephemeral_response,
    create_response,
    format_permissions_bitset,
    get_authorizing_guild_id,
    get_authorizing_user_id,
    get_integration_type_name,
    get_interaction_context_name,
    is_bot_dm_interaction,
    is_guild_installed,
    is_guild_interaction,
    is_private_channel_interaction,
    is_user_installed,
    parse_permissions_bitset,
    should_respond_ephemeral,
)

__all__ = [
    # Command structures
    "ApplicationCommand",
    "ApplicationCommandOption",
    "ApplicationCommandOptionChoice",
    "ApplicationCommandOptionType",
    "ApplicationCommandType",
    "AuthorizingIntegrationOwners",
    # Builder classes
    "CommandBuilder",
    "CommandHandlerType",
    "CommandRegistrar",
    "CreateApplicationCommand",
    # Enums
    "IntegrationType",
    # Interaction structures
    "Interaction",
    "InteractionContextType",
    "InteractionData",
    "InteractionMetadata",
    "PartialChannel",
    "PartialUser",
    "create_ephemeral_response",
    "create_response",
    "format_permissions_bitset",
    "get_authorizing_guild_id",
    "get_authorizing_user_id",
    "get_integration_type_name",
    "get_interaction_context_name",
    "is_bot_dm_interaction",
    "is_guild_installed",
    # Utility functions
    "is_guild_interaction",
    "is_private_channel_interaction",
    "is_user_installed",
    "parse_permissions_bitset",
    "should_respond_ephemeral",
]
