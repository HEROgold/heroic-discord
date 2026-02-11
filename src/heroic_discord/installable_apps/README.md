# User-Installable Apps

This module provides comprehensive support for Discord's user-installable applications, allowing you to create apps that can be installed to user accounts, guilds (servers), or both.

## Overview

Discord apps can be installed in two contexts:

- **Guild Install**: Traditional server-based installation
- **User Install**: New capability allowing apps to be installed to individual user accounts

Commands can then be configured to work in different interaction contexts:

- **Guild**: Regular server channels
- **Bot DM**: Direct messages with your bot
- **Private Channel**: DMs and group DMs (requires USER_INSTALL)

## Quick Start

```python
from heroic_discord.installable_apps import (
    CommandBuilder,
    CommandRegistrar,
    IntegrationType,
    InteractionContextType,
)
from heroic_discord.client import DiscordClient

# Create a command builder
builder = CommandBuilder("profile", "View your game profile")

# Configure installation contexts
builder.add_user_install_context()  # Can be installed to users

# Configure where it can be used
builder.add_interaction_context(InteractionContextType.GUILD)
builder.add_interaction_context(InteractionContextType.BOT_DM)
builder.add_interaction_context(InteractionContextType.PRIVATE_CHANNEL)

# Build the command
command = builder.build()

# Register it
with DiscordClient(token="YOUR_BOT_TOKEN") as client:
    registrar = CommandRegistrar(client)
    response = registrar.register_global_command("YOUR_APP_ID", command)
```

## Tutorial Examples

Based on the [official Discord tutorial](https://docs.discord.com/developers/tutorials/developing-a-user-installable-app), here are common command patterns:

### User Profile Command

Available everywhere for user-installed apps:

```python
builder = CommandBuilder("profile", "Get information about your game inventory and progress")
builder.add_user_install_context()
builder.add_interaction_context(InteractionContextType.GUILD)
builder.add_interaction_context(InteractionContextType.BOT_DM)
builder.add_interaction_context(InteractionContextType.PRIVATE_CHANNEL)
```

### Guild Leaderboard Command

Only available in servers:

```python
builder = CommandBuilder("leaderboard", "View game leaderboard for the current server")
builder.add_guild_install_context()
builder.add_interaction_context(InteractionContextType.GUILD)
```

### Wiki Search Command

Available in both contexts:

```python
from heroic_discord.installable_apps import ApplicationCommandOptionType

builder = CommandBuilder("wiki", "Find information about game items and characters")
builder.add_guild_install_context()
builder.add_user_install_context()
builder.add_interaction_context(InteractionContextType.GUILD)
builder.add_interaction_context(InteractionContextType.BOT_DM)
builder.add_interaction_context(InteractionContextType.PRIVATE_CHANNEL)

# Add a search parameter
builder.add_option(
    name="query",
    description="What to search for",
    option_type=ApplicationCommandOptionType.STRING,
    required=True,
    min_length=1,
    max_length=100,
)
```

### Account Linking Command

DM-only for privacy:

```python
builder = CommandBuilder("link", "Link your game account to Discord")
builder.add_user_install_context()
builder.add_interaction_context(InteractionContextType.BOT_DM)
```

## Context Menu Commands

### User Context Menu

Right-click on a user:

```python
from heroic_discord.installable_apps import ApplicationCommandType

builder = CommandBuilder(
    "High Five",
    "",  # Empty description for USER commands
    command_type=ApplicationCommandType.USER,
)
builder.add_user_install_context()
builder.add_interaction_context(InteractionContextType.GUILD)
```

### Message Context Menu

Right-click on a message:

```python
builder = CommandBuilder(
    "Bookmark",
    "",  # Empty description for MESSAGE commands
    command_type=ApplicationCommandType.MESSAGE,
)
builder.add_user_install_context()
builder.add_interaction_context(InteractionContextType.GUILD)
builder.add_interaction_context(InteractionContextType.BOT_DM)
builder.add_interaction_context(InteractionContextType.PRIVATE_CHANNEL)
```

## Handling Interactions

When your app receives an interaction, use the metadata to customize responses:

```python
from heroic_discord.installable_apps import Interaction, InteractionContextType

def handle_profile_command(interaction: Interaction) -> dict:
    """Respond based on where the command was invoked."""
    context = interaction.get("context")
    
    # Respond ephemerally in guilds, normally in DMs
    is_ephemeral = context != InteractionContextType.BOT_DM
    
    response = {
        "type": 4,  # CHANNEL_MESSAGE_WITH_SOURCE
        "data": {
            "content": "Here's your profile!",
        },
    }
    
    if is_ephemeral:
        response["data"]["flags"] = 64  # EPHEMERAL flag
    
    return response
```

### Understanding Authorizing Integration Owners

The `authorizing_integration_owners` field tells you who authorized the app:

```python
def check_authorization(interaction: Interaction) -> None:
    """Check who authorized the app."""
    owners = interaction.get("authorizing_integration_owners", {})
    
    # Check for user installation
    if "1" in owners:  # USER_INSTALL
        user_id = owners["1"]
        print(f"App authorized by user: {user_id}")
    
    # Check for guild installation
    if "0" in owners:  # GUILD_INSTALL
        guild_id = owners["0"]
        print(f"App installed in guild: {guild_id}")
```

## Advanced Features

### Permissions

Restrict commands to users with specific permissions:

```python
# Only administrators can use this command
builder.set_default_permissions("0")

# Require MANAGE_GUILD permission (bit 5)
permissions = str(1 << 5)
builder.set_default_permissions(permissions)
```

### Age-Restricted Commands

Mark commands as NSFW:

```python
builder.set_nsfw(True)
```

### Localization

Add translations for your commands:

```python
builder.add_localization(
    locale="es-ES",
    name="perfil",
    description="Ver tu perfil de juego"
)

builder.add_localization(
    locale="zh-CN",
    name="个人资料",
    description="查看你的游戏资料"
)
```

### Command Options with Choices

Create commands with predefined choices:

```python
from heroic_discord.installable_apps import ApplicationCommandOptionType

builder = CommandBuilder("animal", "Get a random animal photo")

builder.add_option(
    name="type",
    description="Type of animal",
    option_type=ApplicationCommandOptionType.STRING,
    required=True,
    choices=[
        {"name": "Dog", "value": "dog"},
        {"name": "Cat", "value": "cat"},
        {"name": "Penguin", "value": "penguin"},
    ],
)
```

## API Reference

### Enums

- `IntegrationType`: GUILD_INSTALL (0), USER_INSTALL (1)
- `InteractionContextType`: GUILD (0), BOT_DM (1), PRIVATE_CHANNEL (2)
- `ApplicationCommandType`: CHAT_INPUT (1), USER (2), MESSAGE (3), PRIMARY_ENTRY_POINT (4)
- `ApplicationCommandOptionType`: SUB_COMMAND (1), SUB_COMMAND_GROUP (2), STRING (3), INTEGER (4), BOOLEAN (5), USER (6), CHANNEL (7), ROLE (8), MENTIONABLE (9), NUMBER (10), ATTACHMENT (11)

### Classes

- `CommandBuilder`: Fluent interface for building commands
- `CommandRegistrar`: Helper for registering commands with Discord API

### TypedDicts

- `ApplicationCommand`: Full command structure
- `CreateApplicationCommand`: Simplified structure for command creation
- `ApplicationCommandOption`: Command option structure
- `Interaction`: Full interaction payload
- `InteractionMetadata`: Metadata for interaction messages

## Complete Example

See `examples/user_installable_app.py` for a complete working example with multiple command types.

## References

- [Developing a User-Installable App (Tutorial)](https://docs.discord.com/developers/tutorials/developing-a-user-installable-app)
- [Application Commands](https://docs.discord.com/developers/interactions/application-commands)
- [Command Contexts](https://docs.discord.com/developers/interactions/application-commands#contexts)
- [Receiving and Responding to Interactions](https://docs.discord.com/developers/interactions/receiving-and-responding)
