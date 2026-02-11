"""Heroic Discord - A Discord API wrapper."""

from heroic_discord.client import DiscordClient

__all__ = ["DiscordClient"]


def hello() -> str:
    """Test function to verify package is working."""
    return "Hello from heroic-discord!"
