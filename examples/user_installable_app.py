"""Example implementations demonstrating user-installable Discord apps.

This module provides practical examples of how to create and register
user-installable commands with various contexts and configurations.

Based on the Discord tutorial:
https://docs.discord.com/developers/tutorials/developing-a-user-installable-app
"""

from heroic_discord.client import DiscordClient
from heroic_discord.installable_apps.builder import CommandBuilder, CommandRegistrar
from heroic_discord.installable_apps.enums import (
    ApplicationCommandOptionType,
    ApplicationCommandType,
    InteractionContextType,
)


def create_profile_command() -> CommandBuilder:
    """Create a /profile command for user-installed apps.

    This command displays a user's game profile and is only available
    when the app is installed to a user. It can be used in guilds,
    bot DMs, and private channels.

    Example from tutorial:
        Command available everywhere for user-installed apps.
        Responds ephemerally in guilds, normally in DMs.

    Returns:
        CommandBuilder configured for profile command.

    """
    return (
        CommandBuilder("profile", "Get information about your game inventory and progress")
        .add_user_install_context()
        .add_interaction_context(InteractionContextType.GUILD)
        .add_interaction_context(InteractionContextType.BOT_DM)
        .add_interaction_context(InteractionContextType.PRIVATE_CHANNEL)
    )


def create_leaderboard_command() -> CommandBuilder:
    """Create a /leaderboard command for guild-installed apps.

    This command shows a game leaderboard for the current server.
    Only available in guild contexts with guild installation.

    Example from tutorial:
        Guild-only command that displays server-specific data.

    Returns:
        CommandBuilder configured for leaderboard command.

    """
    return (
        CommandBuilder("leaderboard", "View game leaderboard for the current server")
        .add_guild_install_context()
        .add_interaction_context(InteractionContextType.GUILD)
    )


def create_wiki_command() -> CommandBuilder:
    """Create a /wiki command available in multiple contexts.

    This command looks up game items and characters. Available for both
    guild and user installations, and can be used in multiple contexts.

    Example from tutorial:
        Multi-context command that works in many places.

    Returns:
        CommandBuilder configured for wiki command.

    """
    return (
        CommandBuilder("wiki", "Find information about game items and characters")
        .add_guild_install_context()
        .add_user_install_context()
        .add_interaction_context(InteractionContextType.GUILD)
        .add_interaction_context(InteractionContextType.BOT_DM)
        .add_interaction_context(InteractionContextType.PRIVATE_CHANNEL)
        .add_option(
            name="query",
            description="What to search for",
            option_type=ApplicationCommandOptionType.STRING,
            required=True,
            min_length=1,
            max_length=100,
        )
    )


def create_link_command() -> CommandBuilder:
    """Create a /link command for linking game accounts.

    This command links a user's game account to Discord. Only available
    in the bot's DM for user-installed apps (private account linking).

    Example from tutorial:
        DM-only command for sensitive operations.

    Returns:
        CommandBuilder configured for link command.

    """
    return (
        CommandBuilder("link", "Link your game account to Discord")
        .add_user_install_context()
        .add_interaction_context(InteractionContextType.BOT_DM)
    )


def create_user_context_menu_command() -> CommandBuilder:
    """Create a user context menu command.

    This creates a "High Five" command that appears when right-clicking
    a user. Available for both guild and user installations.

    Returns:
        CommandBuilder configured for user context menu.

    """
    return (
        CommandBuilder(
            "High Five",
            "",  # Description is empty for USER commands
            command_type=ApplicationCommandType.USER,
        )
        .add_guild_install_context()
        .add_user_install_context()
        .add_interaction_context(InteractionContextType.GUILD)
        .add_interaction_context(InteractionContextType.PRIVATE_CHANNEL)
    )


def create_message_context_menu_command() -> CommandBuilder:
    """Create a message context menu command.

    This creates a "Bookmark" command that appears when right-clicking
    a message. Available for user installations in multiple contexts.

    Returns:
        CommandBuilder configured for message context menu.

    """
    return (
        CommandBuilder(
            "Bookmark",
            "",  # Description is empty for MESSAGE commands
            command_type=ApplicationCommandType.MESSAGE,
        )
        .add_user_install_context()
        .add_interaction_context(InteractionContextType.GUILD)
        .add_interaction_context(InteractionContextType.BOT_DM)
        .add_interaction_context(InteractionContextType.PRIVATE_CHANNEL)
    )


def register_example_commands(
    token: str,
    application_id: str,
) -> None:
    """Register all example commands globally.

    This function demonstrates how to register multiple commands
    with different installation and interaction contexts.

    Args:
        token: Your Discord bot token
        application_id: Your application's ID

    Example:
        >>> register_example_commands("YOUR_BOT_TOKEN", "YOUR_APP_ID")

    """
    with DiscordClient(token) as client:
        registrar = CommandRegistrar(client)

        # Register all example commands
        commands = [
            create_profile_command(),
            create_leaderboard_command(),
            create_wiki_command(),
            create_link_command(),
            create_user_context_menu_command(),
            create_message_context_menu_command(),
        ]

        for cmd_builder in commands:
            command = cmd_builder.build()
            response = registrar.register_global_command(application_id, command)

            if response.status_code in (200, 201):
                print(f"✓ Registered command: {command['name']}")
            else:
                print(f"✗ Failed to register {command['name']}: {response.text}")


def interaction_context_example(interaction: dict) -> dict:
    """Handle interaction context metadata.

    This demonstrates how to use the interaction metadata to customize
    responses based on where the command was invoked.

    Args:
        interaction: The interaction payload from Discord

    Returns:
        Dictionary with response data customized for the context.

    Example from tutorial:
        The /profile command responds ephemerally in guilds but
        normally in bot DMs.

    """
    context = interaction.get("context")
    authorizing_owners = interaction.get("authorizing_integration_owners", {})

    # Determine if we should respond ephemerally
    # BOT_DM = 1, others should be ephemeral
    is_ephemeral = context != 1

    response = {
        "type": 4,  # CHANNEL_MESSAGE_WITH_SOURCE
        "data": {
            "content": "Here's your profile!",
        },
    }

    if is_ephemeral:
        # Respond ephemerally in guilds and private channels
        response["data"]["flags"] = 64  # EPHEMERAL flag

    # Check who authorized the app
    if "1" in authorizing_owners:  # USER_INSTALL
        user_id = authorizing_owners["1"]
        print(f"App was authorized by user: {user_id}")

    if "0" in authorizing_owners:  # GUILD_INSTALL
        guild_id = authorizing_owners["0"]
        print(f"App was installed in guild: {guild_id}")

    return response


if __name__ == "__main__":
    # Example usage - replace with your actual credentials
    # Never hardcode tokens in production!
    import os

    bot_token = os.getenv("DISCORD_BOT_TOKEN", "")
    app_id = os.getenv("DISCORD_APPLICATION_ID", "")

    if bot_token and app_id:
        register_example_commands(bot_token, app_id)
    else:
        print("Please set DISCORD_BOT_TOKEN and DISCORD_APPLICATION_ID environment variables")
