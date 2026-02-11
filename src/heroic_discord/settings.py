""""Settings for the Heroic Discord client."""
from pathlib import Path

from confkit import Config as BaseConfig
from confkit import ConfigContainerMeta
from confkit.ext.parsers import EnvParser


class Config(BaseConfig):
    """Configuration for the Discord client."""

Config.set_file(Path(".env"))
Config.set_parser(EnvParser())

class Settings(metaclass=ConfigContainerMeta):
    """Container for all configuration settings."""

    bot_token = Config("DISCORD_BOT_TOKEN")
    """The bot token to authenticate with the Discord API."""
    app_id = Config("DISCORD_APP_ID")
    """The application ID of the discord application."""
    public_key = Config("DISCORD_PUBLIC_KEY")
    """The public key of the discord application."""
