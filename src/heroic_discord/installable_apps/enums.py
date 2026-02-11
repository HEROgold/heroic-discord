"""Enums for Discord user-installable apps and application commands."""

from enum import IntEnum


class IntegrationType(IntEnum):
    """Installation context types for Discord applications.

    Defines where an application can be installed - to a guild (server)
    or to a user account, or both.

    References:
        https://docs.discord.com/developers/resources/application#installation-context

    """

    GUILD_INSTALL = 0
    """Application can be installed to a guild/server."""

    USER_INSTALL = 1
    """Application can be installed to a user account."""


class InteractionContextType(IntEnum):
    """Interaction context types where commands can be used.

    Defines the surfaces in Discord where a command can be invoked.

    References:
        https://docs.discord.com/developers/interactions/application-commands#interaction-contexts

    """

    GUILD = 0
    """Command can be used in guild channels."""

    BOT_DM = 1
    """Command can be used in DMs with the bot."""

    PRIVATE_CHANNEL = 2
    """Command can be used in DMs and group DMs (excluding bot DM).

    Note:
        This context is only valid for USER_INSTALL commands.
    """


class ApplicationCommandType(IntEnum):
    """Types of application commands available in Discord.

    References:
        https://docs.discord.com/developers/interactions/application-commands#application-command-object-application-command-types

    """

    CHAT_INPUT = 1
    """Slash command - text-based command that appears when a user types /."""

    USER = 2
    """User command - context menu command shown when right-clicking a user."""

    MESSAGE = 3
    """Message command - context menu command shown when right-clicking a message."""

    PRIMARY_ENTRY_POINT = 4
    """Entry point command - primary way to invoke an app's Activity."""


class ApplicationCommandOptionType(IntEnum):
    """Types of options for application commands.

    References:
        https://docs.discord.com/developers/interactions/application-commands#application-command-object-application-command-option-type

    """

    SUB_COMMAND = 1
    """A subcommand."""

    SUB_COMMAND_GROUP = 2
    """A group of subcommands."""

    STRING = 3
    """A string option."""

    INTEGER = 4
    """An integer option (between -2^53+1 and 2^53-1)."""

    BOOLEAN = 5
    """A boolean option."""

    USER = 6
    """A user option."""

    CHANNEL = 7
    """A channel option (includes all channel types + categories)."""

    ROLE = 8
    """A role option."""

    MENTIONABLE = 9
    """A mentionable option (includes users and roles)."""

    NUMBER = 10
    """A number option (double between -2^53 and 2^53)."""

    ATTACHMENT = 11
    """An attachment option."""


class CommandHandlerType(IntEnum):
    """Handler types for Entry Point commands.

    References:
        https://docs.discord.com/developers/interactions/application-commands#application-command-object-entry-point-command-handler-types

    """

    APP_HANDLER = 1
    """The app handles the interaction using an interaction token."""

    DISCORD_LAUNCH_ACTIVITY = 2
    """Discord handles the interaction by launching an Activity automatically."""
