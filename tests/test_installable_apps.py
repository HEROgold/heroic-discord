"""Tests for user-installable apps functionality."""


from heroic_discord.installable_apps import (
    ApplicationCommandOptionType,
    ApplicationCommandType,
    CommandBuilder,
    IntegrationType,
    InteractionContextType,
)


def test_command_builder_basic() -> None:
    """Test basic command creation."""
    builder = CommandBuilder("test", "Test command")
    command = builder.build()

    assert command["name"] == "test"
    assert command["description"] == "Test command"


def test_command_builder_with_guild_install() -> None:
    """Test command with guild install context."""
    builder = CommandBuilder("leaderboard", "View leaderboard")
    builder.add_guild_install_context()
    command = builder.build()

    assert "integration_types" in command
    assert IntegrationType.GUILD_INSTALL in command["integration_types"]


def test_command_builder_with_user_install() -> None:
    """Test command with user install context."""
    builder = CommandBuilder("profile", "View profile")
    builder.add_user_install_context()
    command = builder.build()

    assert "integration_types" in command
    assert IntegrationType.USER_INSTALL in command["integration_types"]


def test_command_builder_with_both_install_contexts() -> None:
    """Test command with both guild and user install contexts."""
    builder = CommandBuilder("wiki", "Search wiki")
    builder.add_guild_install_context()
    builder.add_user_install_context()
    command = builder.build()

    assert "integration_types" in command
    assert IntegrationType.GUILD_INSTALL in command["integration_types"]
    assert IntegrationType.USER_INSTALL in command["integration_types"]


def test_command_builder_with_interaction_contexts() -> None:
    """Test command with multiple interaction contexts."""
    builder = CommandBuilder("help", "Get help")
    builder.add_interaction_context(InteractionContextType.GUILD)
    builder.add_interaction_context(InteractionContextType.BOT_DM)
    builder.add_interaction_context(InteractionContextType.PRIVATE_CHANNEL)
    command = builder.build()

    assert "contexts" in command
    assert InteractionContextType.GUILD in command["contexts"]
    assert InteractionContextType.BOT_DM in command["contexts"]
    assert InteractionContextType.PRIVATE_CHANNEL in command["contexts"]


def test_command_builder_with_options() -> None:
    """Test command with options."""
    builder = CommandBuilder("search", "Search for something")
    builder.add_option(
        name="query",
        description="Search query",
        option_type=ApplicationCommandOptionType.STRING,
        required=True,
        min_length=1,
        max_length=100,
    )
    command = builder.build()

    assert "options" in command
    assert len(command["options"]) == 1
    assert command["options"][0]["name"] == "query"
    assert command["options"][0]["type"] == ApplicationCommandOptionType.STRING
    assert command["options"][0]["required"] is True # pyright: ignore[reportTypedDictNotRequiredAccess]


def test_command_builder_with_choices() -> None:
    """Test command option with choices."""
    builder = CommandBuilder("animal", "Get animal photo")
    builder.add_option(
        name="type",
        description="Animal type",
        option_type=ApplicationCommandOptionType.STRING,
        required=True,
        choices=[
            {"name": "Dog", "value": "dog"},
            {"name": "Cat", "value": "cat"},
        ],
    )
    command = builder.build()

    assert "options" in command
    assert "choices" in command["options"][0]
    assert len(command["options"][0]["choices"]) == 2


def test_command_builder_with_permissions() -> None:
    """Test command with default permissions."""
    builder = CommandBuilder("admin", "Admin command")
    builder.set_default_permissions("0")
    command = builder.build()

    assert "default_member_permissions" in command
    assert command["default_member_permissions"] == "0"


def test_command_builder_with_nsfw() -> None:
    """Test command marked as NSFW."""
    builder = CommandBuilder("nsfw", "NSFW command")
    builder.set_nsfw(nsfw=True)
    command = builder.build()

    assert "nsfw" in command
    assert command["nsfw"] is True


def test_command_builder_with_localization() -> None:
    """Test command with localization."""
    builder = CommandBuilder("test", "Test command")
    builder.add_localization("es-ES", name="prueba", description="Comando de prueba")
    builder.add_localization("zh-CN", name="测试", description="测试命令")
    command = builder.build()

    assert "name_localizations" in command
    assert "description_localizations" in command
    assert command["name_localizations"]["es-ES"] == "prueba"  # pyright: ignore[reportOptionalSubscript] # ty:ignore[not-subscriptable]
    assert command["description_localizations"]["zh-CN"] == "测试命令"  # pyright: ignore[reportOptionalSubscript] # ty:ignore[not-subscriptable]


def test_command_builder_user_command_type() -> None:
    """Test creating a USER command type."""
    builder = CommandBuilder(
        "High Five",
        "",
        command_type=ApplicationCommandType.USER,
    )
    command = builder.build()

    assert "type" in command
    assert command["type"] == ApplicationCommandType.USER
    assert command["description"] == ""


def test_command_builder_message_command_type() -> None:
    """Test creating a MESSAGE command type."""
    builder = CommandBuilder(
        "Bookmark",
        "",
        command_type=ApplicationCommandType.MESSAGE,
    )
    command = builder.build()

    assert "type" in command
    assert command["type"] == ApplicationCommandType.MESSAGE


def test_command_builder_fluent_interface() -> None:
    """Test fluent interface returns self."""
    builder = CommandBuilder("test", "Test")

    result = builder.add_guild_install_context()
    assert result is builder

    result = builder.add_user_install_context()
    assert result is builder

    result = builder.add_interaction_context(InteractionContextType.GUILD)
    assert result is builder

    result = builder.set_default_permissions("0")
    assert result is builder

    result = builder.set_nsfw(nsfw=True)
    assert result is builder


def test_integration_type_values() -> None:
    """Test IntegrationType enum values."""
    assert IntegrationType.GUILD_INSTALL == 0
    assert IntegrationType.USER_INSTALL == 1


def test_interaction_context_type_values() -> None:
    """Test InteractionContextType enum values."""
    assert InteractionContextType.GUILD == 0
    assert InteractionContextType.BOT_DM == 1
    assert InteractionContextType.PRIVATE_CHANNEL == 2


def test_application_command_type_values() -> None:
    """Test ApplicationCommandType enum values."""
    assert ApplicationCommandType.CHAT_INPUT == 1
    assert ApplicationCommandType.USER == 2
    assert ApplicationCommandType.MESSAGE == 3
    assert ApplicationCommandType.PRIMARY_ENTRY_POINT == 4


def test_duplicate_integration_types_not_added() -> None:
    """Test that duplicate integration types are not added."""
    builder = CommandBuilder("test", "Test")
    builder.add_guild_install_context()
    builder.add_guild_install_context()
    command = builder.build()

    assert len(command["integration_types"]) == 1 # pyright: ignore[reportTypedDictNotRequiredAccess]


def test_duplicate_interaction_contexts_not_added() -> None:
    """Test that duplicate interaction contexts are not added."""
    builder = CommandBuilder("test", "Test")
    builder.add_interaction_context(InteractionContextType.GUILD)
    builder.add_interaction_context(InteractionContextType.GUILD)
    command = builder.build()

    assert len(command["contexts"]) == 1 # pyright: ignore[reportTypedDictNotRequiredAccess]


def test_empty_command_minimal_structure() -> None:
    """Test that minimal command has only required fields."""
    builder = CommandBuilder("minimal", "Minimal command")
    command = builder.build()

    # Should only have name and description
    assert "name" in command
    assert "description" in command
    # These should not be present if not set
    assert "integration_types" not in command
    assert "contexts" not in command
    assert "options" not in command
    assert "nsfw" not in command
