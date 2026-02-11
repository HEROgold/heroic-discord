"""TypedDict structures for Discord application commands and options."""

from typing import TYPE_CHECKING, NotRequired, Required, TypedDict

if TYPE_CHECKING:
    from heroic_discord.installable_apps.enums import (
        ApplicationCommandOptionType,
        ApplicationCommandType,
        CommandHandlerType,
        IntegrationType,
        InteractionContextType,
    )


class ApplicationCommandOptionChoice(TypedDict):
    """Structure for a command option choice.

    References:
        https://docs.discord.com/developers/interactions/application-commands#application-command-object-application-command-option-choice-structure

    """

    name: Required[str]
    """1-100 character choice name."""

    name_localizations: NotRequired[dict[str, str] | None]
    """Localization dictionary for the name field."""

    value: Required[str | int | float]
    """Value for the choice, up to 100 characters if string."""


class ApplicationCommandOption(TypedDict):
    """Structure for an application command option.

    References:
        https://docs.discord.com/developers/interactions/application-commands#application-command-object-application-command-option-structure

    """

    type: Required[ApplicationCommandOptionType]
    """Type of option."""

    name: Required[str]
    """1-32 character name."""

    name_localizations: NotRequired[dict[str, str] | None]
    """Localization dictionary for the name field."""

    description: Required[str]
    """1-100 character description."""

    description_localizations: NotRequired[dict[str, str] | None]
    """Localization dictionary for the description field."""

    required: NotRequired[bool]
    """Whether the parameter is required or optional, default false."""

    choices: NotRequired[list[ApplicationCommandOptionChoice]]
    """Choices for STRING, INTEGER, NUMBER options (max 25)."""

    options: NotRequired[list[ApplicationCommandOption]]
    """Nested options for SUB_COMMAND and SUB_COMMAND_GROUP types."""

    channel_types: NotRequired[list[int]]
    """Channel types to restrict selection to (for CHANNEL options)."""

    min_value: NotRequired[int | float]
    """Minimum value permitted (for INTEGER or NUMBER options)."""

    max_value: NotRequired[int | float]
    """Maximum value permitted (for INTEGER or NUMBER options)."""

    min_length: NotRequired[int]
    """Minimum allowed length (0-6000) for STRING options."""

    max_length: NotRequired[int]
    """Maximum allowed length (1-6000) for STRING options."""

    autocomplete: NotRequired[bool]
    """Enable autocomplete interactions for STRING, INTEGER, NUMBER options."""


class ApplicationCommand(TypedDict):
    """Structure for an application command.

    References:
        https://docs.discord.com/developers/interactions/application-commands#application-command-object-application-command-structure

    """

    id: NotRequired[str]
    """Unique ID of command (present when fetched from API)."""

    type: NotRequired[ApplicationCommandType]
    """Type of command, defaults to CHAT_INPUT."""

    application_id: NotRequired[str]
    """ID of the parent application (present when fetched from API)."""

    guild_id: NotRequired[str]
    """Guild ID of the command, if not global."""

    name: Required[str]
    """Name of command, 1-32 characters."""

    name_localizations: NotRequired[dict[str, str] | None]
    """Localization dictionary for name field."""

    description: Required[str]
    """Description for CHAT_INPUT commands (1-100 chars). Empty string for USER and MESSAGE."""

    description_localizations: NotRequired[dict[str, str] | None]
    """Localization dictionary for description field."""

    options: NotRequired[list[ApplicationCommandOption]]
    """Parameters for the command (max 25, only for CHAT_INPUT)."""

    default_member_permissions: NotRequired[str | None]
    """Set of permissions represented as a bit set."""

    dm_permission: NotRequired[bool]
    """Deprecated (use contexts instead). Indicates if available in DMs."""

    default_permission: NotRequired[bool | None]
    """Deprecated. Indicates if enabled by default when app is added."""

    nsfw: NotRequired[bool]
    """Indicates whether the command is age-restricted."""

    integration_types: NotRequired[list[IntegrationType]]
    """Installation contexts where the command is available (for global commands)."""

    contexts: NotRequired[list[InteractionContextType] | None]
    """Interaction context(s) where the command can be used (for global commands)."""

    version: NotRequired[str]
    """Autoincrementing version identifier (present when fetched from API)."""

    handler: NotRequired[CommandHandlerType]
    """Handler for PRIMARY_ENTRY_POINT commands (for apps with EMBEDDED flag)."""


class CreateApplicationCommand(TypedDict):
    """Simplified structure for creating an application command.

    This is a convenience type for command creation that only includes
    the fields typically needed when creating a new command.
    """

    name: Required[str]
    """Name of command, 1-32 characters."""

    description: Required[str]
    """Description (1-100 chars for CHAT_INPUT, empty for USER/MESSAGE)."""

    type: NotRequired[ApplicationCommandType]
    """Type of command, defaults to CHAT_INPUT."""

    options: NotRequired[list[ApplicationCommandOption]]
    """Parameters for the command (max 25, only for CHAT_INPUT)."""

    integration_types: NotRequired[list[IntegrationType]]
    """Installation contexts where the command is available."""

    contexts: NotRequired[list[InteractionContextType]]
    """Interaction context(s) where the command can be used."""

    default_member_permissions: NotRequired[str | None]
    """Set of permissions represented as a bit set."""

    nsfw: NotRequired[bool]
    """Indicates whether the command is age-restricted."""

    name_localizations: NotRequired[dict[str, str] | None]
    """Localization dictionary for name field."""

    description_localizations: NotRequired[dict[str, str] | None]
    """Localization dictionary for description field."""
