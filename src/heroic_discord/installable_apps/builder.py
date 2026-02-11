"""Helper class for building Discord application commands."""

from __future__ import annotations

from typing import TYPE_CHECKING, NotRequired, TypedDict, Unpack

from heroic_discord.client import AsyncDiscordClient, DiscordClient
from heroic_discord.installable_apps.enums import (
    ApplicationCommandOptionType,
    ApplicationCommandType,
    IntegrationType,
    InteractionContextType,
)

if TYPE_CHECKING:
    import httpx

    from heroic_discord.installable_apps.commands import (
        ApplicationCommand,
        ApplicationCommandOption,
        ApplicationCommandOptionChoice,
        CreateApplicationCommand,
    )


class OptionKwargs(TypedDict, total=False):
    """Additional optional parameters for application command options.

    These correspond to the optional fields in ApplicationCommandOption.
    """

    name_localizations: NotRequired[dict[str, str] | None]
    """Localization dictionary for the name field."""

    description_localizations: NotRequired[dict[str, str] | None]
    """Localization dictionary for the description field."""

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


class CommandBuilder:
    """Builder for Discord application commands.

    Provides a fluent interface for creating application commands with
    support for user-installable apps and various interaction contexts.

    Examples:
        >>> builder = CommandBuilder("profile", "View your game profile")
        >>> builder.add_user_install_context()
        >>> builder.add_interaction_context(InteractionContextType.GUILD)
        >>> builder.add_interaction_context(InteractionContextType.BOT_DM)
        >>> command = builder.build()

    """

    def __init__(
        self,
        name: str,
        description: str,
        command_type: ApplicationCommandType = ApplicationCommandType.CHAT_INPUT,
    ) -> None:
        """Initialize a command builder.

        Args:
            name: Command name (1-32 characters)
            description: Command description (1-100 chars for CHAT_INPUT, empty for others)
            command_type: Type of command (defaults to CHAT_INPUT/slash command)

        """
        self.name = name
        self.description = description
        self.command_type = command_type
        self.options: list[ApplicationCommandOption] = []
        self.integration_types: list[IntegrationType] = []
        self.contexts: list[InteractionContextType] = []
        self.default_member_permissions: str | None = None
        self.nsfw: bool = False
        self.name_localizations: dict[str, str] | None = None
        self.description_localizations: dict[str, str] | None = None

    def add_guild_install_context(self) -> CommandBuilder:
        """Add GUILD_INSTALL as a supported installation context.

        Returns:
            Self for method chaining.

        """
        if IntegrationType.GUILD_INSTALL not in self.integration_types:
            self.integration_types.append(IntegrationType.GUILD_INSTALL)
        return self

    def add_user_install_context(self) -> CommandBuilder:
        """Add USER_INSTALL as a supported installation context.

        Returns:
            Self for method chaining.

        """
        if IntegrationType.USER_INSTALL not in self.integration_types:
            self.integration_types.append(IntegrationType.USER_INSTALL)
        return self

    def add_interaction_context(
        self,
        context: InteractionContextType,
    ) -> CommandBuilder:
        """Add an interaction context where the command can be used.

        Args:
            context: The interaction context to add

        Returns:
            Self for method chaining.

        Note:
            PRIVATE_CHANNEL context requires USER_INSTALL in integration_types.

        """
        if context not in self.contexts:
            self.contexts.append(context)
        return self

    def set_default_permissions(self, permissions: str) -> CommandBuilder:
        """Set default member permissions required to use this command.

        Args:
            permissions: Bitwise permissions string (use "0" to restrict to admins)

        Returns:
            Self for method chaining.

        """
        self.default_member_permissions = permissions
        return self

    def set_nsfw(self, *, nsfw: bool = True) -> CommandBuilder:
        """Mark the command as age-restricted.

        Args:
            nsfw: Whether the command is age-restricted

        Returns:
            Self for method chaining.

        """
        self.nsfw = nsfw
        return self

    def add_option(
        self,
        name: str,
        description: str,
        option_type: ApplicationCommandOptionType,
        choices: list[ApplicationCommandOptionChoice] | None = None,
        *,
        required: bool = False,
        **kwargs: Unpack[OptionKwargs],
    ) -> CommandBuilder:
        """Add an option to the command.

        Args:
            name: Option name (1-32 characters)
            description: Option description (1-100 characters)
            option_type: Type of option
            required: Whether the option is required
            choices: List of choices for the option
            **kwargs: Additional option parameters (min_value, max_value, autocomplete, etc.)

        Returns:
            Self for method chaining.

        """
        option: ApplicationCommandOption = {
            "type": option_type,
            "name": name,
            "description": description,
        }

        if required:
            option["required"] = required

        if choices:
            option["choices"] = choices

        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                option[key] = value  # type: ignore[literal-required]

        self.options.append(option)
        return self

    def add_localization(
        self,
        locale: str,
        name: str | None = None,
        description: str | None = None,
    ) -> CommandBuilder:
        """Add localized names and descriptions.

        Args:
            locale: Locale code (e.g., "es-ES", "zh-CN")
            name: Localized name (if None, keeps existing)
            description: Localized description (if None, keeps existing)

        Returns:
            Self for method chaining.

        """
        if name:
            if self.name_localizations is None:
                self.name_localizations = {}
            self.name_localizations[locale] = name

        if description:
            if self.description_localizations is None:
                self.description_localizations = {}
            self.description_localizations[locale] = description

        return self

    def build(self) -> CreateApplicationCommand:
        """Build the command structure.

        Returns:
            A dictionary containing the command structure ready for API submission.

        """
        command: CreateApplicationCommand = {
            "name": self.name,
            "description": self.description,
        }

        if self.command_type != ApplicationCommandType.CHAT_INPUT:
            command["type"] = self.command_type

        if self.options:
            command["options"] = self.options

        if self.integration_types:
            command["integration_types"] = self.integration_types

        if self.contexts:
            command["contexts"] = self.contexts

        if self.default_member_permissions is not None:
            command["default_member_permissions"] = self.default_member_permissions

        if self.nsfw:
            command["nsfw"] = self.nsfw

        if self.name_localizations:
            command["name_localizations"] = self.name_localizations

        if self.description_localizations:
            command["description_localizations"] = self.description_localizations

        return command


class CommandRegistrar:
    """Helper for registering commands with Discord API.

    Provides methods to register, update, and delete application commands
    for both global and guild-specific scopes.
    """

    def __init__(self, client: DiscordClient | AsyncDiscordClient) -> None:
        """Initialize the command registrar.

        Args:
            client: Discord client instance to use for API calls

        """
        self.client = client

    def register_global_command(
        self,
        application_id: str,
        command: CreateApplicationCommand | ApplicationCommand,
    ) -> httpx.Response:
        """Register a global application command.

        Global commands are available on all guilds where the app is installed
        and may be available in DMs depending on contexts.

        Args:
            application_id: Your application's ID
            command: Command structure to register

        Returns:
            Response from Discord API containing the created command object.

        References:
            https://docs.discord.com/developers/interactions/application-commands#create-global-application-command

        """
        if isinstance(self.client, AsyncDiscordClient):
            msg = "Use register_global_command_async for async client"
            raise TypeError(msg)

        endpoint = f"/applications/{application_id}/commands"
        return self.client.post(endpoint, json=dict(command))

    async def register_global_command_async(
        self,
        application_id: str,
        command: CreateApplicationCommand | ApplicationCommand,
    ) -> httpx.Response:
        """Register a global application command (async).

        Args:
            application_id: Your application's ID
            command: Command structure to register

        Returns:
            Response from Discord API containing the created command object.

        """
        if not isinstance(self.client, AsyncDiscordClient):
            msg = "Use register_global_command for sync client"
            raise TypeError(msg)

        endpoint = f"/applications/{application_id}/commands"
        return await self.client.post(endpoint, json=dict(command))  # ty:ignore[no-matching-overload]

    def register_guild_command(
        self,
        application_id: str,
        guild_id: str,
        command: CreateApplicationCommand | ApplicationCommand,
    ) -> httpx.Response:
        """Register a guild-specific application command.

        Guild commands are only available in the specified guild and update instantly.
        Useful for testing before making commands global.

        Args:
            application_id: Your application's ID
            guild_id: Guild ID where the command should be available
            command: Command structure to register

        Returns:
            Response from Discord API containing the created command object.

        References:
            https://docs.discord.com/developers/interactions/application-commands#create-guild-application-command

        """
        if isinstance(self.client, AsyncDiscordClient):
            msg = "Use register_guild_command_async for async client"
            raise TypeError(msg)

        endpoint = f"/applications/{application_id}/guilds/{guild_id}/commands"
        return self.client.post(endpoint, json=dict(command))

    async def register_guild_command_async(
        self,
        application_id: str,
        guild_id: str,
        command: CreateApplicationCommand | ApplicationCommand,
    ) -> httpx.Response:
        """Register a guild-specific application command (async).

        Args:
            application_id: Your application's ID
            guild_id: Guild ID where the command should be available
            command: Command structure to register

        Returns:
            Response from Discord API containing the created command object.

        """
        if not isinstance(self.client, AsyncDiscordClient):
            msg = "Use register_guild_command for sync client"
            raise TypeError(msg)

        endpoint = f"/applications/{application_id}/guilds/{guild_id}/commands"
        return await self.client.post(endpoint, json=dict(command))  # ty:ignore[no-matching-overload]

    def get_global_commands(
        self,
        application_id: str,
        *,
        with_localizations: bool = False,
    ) -> httpx.Response:
        """Fetch all global commands for the application.

        Args:
            application_id: Your application's ID
            with_localizations: Include full localization dictionaries

        Returns:
            Response containing array of application command objects.

        """
        if isinstance(self.client, AsyncDiscordClient):
            msg = "Use get_global_commands_async for async client"
            raise TypeError(msg)

        endpoint = f"/applications/{application_id}/commands"
        params = {"with_localizations": str(with_localizations).lower()}
        return self.client.get(endpoint, params=params)

    async def get_global_commands_async(
        self,
        application_id: str,
        *,
        with_localizations: bool = False,
    ) -> httpx.Response:
        """Fetch all global commands for the application (async).

        Args:
            application_id: Your application's ID
            with_localizations: Include full localization dictionaries

        Returns:
            Response containing array of application command objects.

        """
        if not isinstance(self.client, AsyncDiscordClient):
            msg = "Use get_global_commands for sync client"
            raise TypeError(msg)

        endpoint = f"/applications/{application_id}/commands"
        params = {"with_localizations": str(with_localizations).lower()}
        return await self.client.get(endpoint, params=params)

    def delete_global_command(
        self,
        application_id: str,
        command_id: str,
    ) -> httpx.Response:
        """Delete a global command.

        Args:
            application_id: Your application's ID
            command_id: ID of the command to delete

        Returns:
            Response with 204 No Content on success.

        """
        if isinstance(self.client, AsyncDiscordClient):
            msg = "Use delete_global_command_async for async client"
            raise TypeError(msg)

        endpoint = f"/applications/{application_id}/commands/{command_id}"
        return self.client.delete(endpoint)

    async def delete_global_command_async(
        self,
        application_id: str,
        command_id: str,
    ) -> httpx.Response:
        """Delete a global command (async).

        Args:
            application_id: Your application's ID
            command_id: ID of the command to delete

        Returns:
            Response with 204 No Content on success.

        """
        if not isinstance(self.client, AsyncDiscordClient):
            msg = "Use delete_global_command for sync client"
            raise TypeError(msg)

        endpoint = f"/applications/{application_id}/commands/{command_id}"
        return await self.client.delete(endpoint)
