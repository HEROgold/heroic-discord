"""Utility functions for working with user-installable apps."""

from typing import TYPE_CHECKING, TypedDict

from heroic_discord.installable_apps.enums import IntegrationType, InteractionContextType

if TYPE_CHECKING:
    from heroic_discord.installable_apps.interactions import (
        AuthorizingIntegrationOwners,
        Interaction,
    )


class InteractionResponseData(TypedDict, total=False):
    """Data payload for an interaction response."""

    content: str
    flags: int


class InteractionResponse(TypedDict):
    """Structure for an interaction response."""

    type: int
    data: InteractionResponseData


def is_guild_interaction(interaction: Interaction) -> bool:
    """Check if interaction occurred in a guild.

    Args:
        interaction: The interaction payload

    Returns:
        True if the interaction was in a guild, False otherwise.

    """
    return interaction.get("context") == InteractionContextType.GUILD


def is_bot_dm_interaction(interaction: Interaction) -> bool:
    """Check if interaction occurred in bot DM.

    Args:
        interaction: The interaction payload

    Returns:
        True if the interaction was in a DM with the bot, False otherwise.

    """
    return interaction.get("context") == InteractionContextType.BOT_DM


def is_private_channel_interaction(interaction: Interaction) -> bool:
    """Check if interaction occurred in a private channel.

    Args:
        interaction: The interaction payload

    Returns:
        True if the interaction was in a private channel (DM/group DM), False otherwise.

    """
    return interaction.get("context") == InteractionContextType.PRIVATE_CHANNEL


def get_authorizing_user_id(owners: AuthorizingIntegrationOwners) -> str | None:
    """Get the user ID who authorized the app (USER_INSTALL).

    Args:
        owners: The authorizing_integration_owners from an interaction

    Returns:
        User ID if app was user-installed, None otherwise.

    """
    return owners.get("1")


def get_authorizing_guild_id(owners: AuthorizingIntegrationOwners) -> str | None:
    """Get the guild ID where the app was installed (GUILD_INSTALL).

    Args:
        owners: The authorizing_integration_owners from an interaction

    Returns:
        Guild ID if app was guild-installed, None otherwise.

    """
    return owners.get("0")


def is_user_installed(owners: AuthorizingIntegrationOwners) -> bool:
    """Check if the app was installed to a user account.

    Args:
        owners: The authorizing_integration_owners from an interaction

    Returns:
        True if app was installed to a user, False otherwise.

    """
    return "1" in owners


def is_guild_installed(owners: AuthorizingIntegrationOwners) -> bool:
    """Check if the app was installed to a guild.

    Args:
        owners: The authorizing_integration_owners from an interaction

    Returns:
        True if app was installed to a guild, False otherwise.

    """
    return "0" in owners


def should_respond_ephemeral(interaction: Interaction) -> bool:
    """Determine if response should be ephemeral based on context.

    This is a common pattern: respond ephemerally in guilds and private
    channels, but normally in bot DMs.

    Args:
        interaction: The interaction payload

    Returns:
        True if response should be ephemeral, False otherwise.

    """
    context = interaction.get("context")
    return context != InteractionContextType.BOT_DM


def get_interaction_context_name(context: int) -> str:
    """Get human-readable name for an interaction context.

    Args:
        context: The context value (0, 1, or 2)

    Returns:
        String name of the context.

    """
    context_names = {
        InteractionContextType.GUILD: "Guild",
        InteractionContextType.BOT_DM: "Bot DM",
        InteractionContextType.PRIVATE_CHANNEL: "Private Channel",
    }
    return context_names.get(InteractionContextType(context), f"Unknown ({context})")


def get_integration_type_name(integration_type: int) -> str:
    """Get human-readable name for an integration type.

    Args:
        integration_type: The integration type value (0 or 1)

    Returns:
        String name of the integration type.

    """
    integration_names = {
        IntegrationType.GUILD_INSTALL: "Guild Install",
        IntegrationType.USER_INSTALL: "User Install",
    }
    return integration_names.get(IntegrationType(integration_type), f"Unknown ({integration_type})")


def format_permissions_bitset(permissions: list[int]) -> str:
    """Convert a list of permission bit positions to a bitset string.

    Args:
        permissions: List of bit positions (e.g., [5, 6] for bits 5 and 6)

    Returns:
        String representation of the bitset for use in commands.

    Example:
        >>> format_permissions_bitset([5, 6])  # MANAGE_GUILD and BAN_MEMBERS
        '96'

    """
    result = 0
    for bit in permissions:
        result |= 1 << bit
    return str(result)


def parse_permissions_bitset(bitset: str) -> list[int]:
    """Parse a permissions bitset string into bit positions.

    Args:
        bitset: String representation of the bitset

    Returns:
        List of bit positions that are set.

    Example:
        >>> parse_permissions_bitset('96')
        [5, 6]

    """
    value = int(bitset)
    positions = []
    bit = 0
    while value > 0:
        if value & 1:
            positions.append(bit)
        value >>= 1
        bit += 1
    return positions


def create_ephemeral_response(content: str) -> InteractionResponse:
    """Create an ephemeral interaction response.

    Args:
        content: The message content

    Returns:
        Interaction response dictionary with ephemeral flag.

    """
    return {
        "type": 4,  # CHANNEL_MESSAGE_WITH_SOURCE
        "data": {
            "content": content,
            "flags": 64,  # EPHEMERAL
        },
    }


def create_response(content: str, *, ephemeral: bool = False) -> InteractionResponse:
    """Create an interaction response.

    Args:
        content: The message content
        ephemeral: Whether the response should be ephemeral

    Returns:
        Interaction response dictionary.

    """
    response: InteractionResponse = {
        "type": 4,  # CHANNEL_MESSAGE_WITH_SOURCE
        "data": {
            "content": content,
        },
    }

    if ephemeral:
        response["data"]["flags"] = 64  # EPHEMERAL

    return response
