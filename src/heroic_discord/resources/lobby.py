"""Discord Lobby Resource Structures.

This module contains TypedDict definitions for Discord Lobby objects.
Reference: https://docs.discord.com/developers/resources/lobby
"""

from enum import IntEnum
from typing import TypedDict


class LobbyMemberFlags(IntEnum):
    """Lobby member flags as powers of 2.

    https://docs.discord.com/developers/resources/lobby#lobby-member-object-lobby-member-flags
    """

    CAN_LINK_LOBBY = 1 << 0


class LobbyMember(TypedDict, total=False):
    """Represents a member of a lobby.

    https://docs.discord.com/developers/resources/lobby#lobby-member-object
    """

    id: str  # User ID (snowflake)
    metadata: dict[str, str] | None  # String key/value pairs (max total 1000 chars)
    flags: int  # Lobby member flags bitfield


class Lobby(TypedDict, total=False):
    """Represents a lobby for matchmaking.

    https://docs.discord.com/developers/resources/lobby#lobby-object
    """

    id: str  # Lobby ID (snowflake)
    application_id: str  # Application that created the lobby (snowflake)
    metadata: dict[str, str] | None  # String key/value pairs (max total 1000 chars)
    members: list[LobbyMember]  # Members of the lobby
    linked_channel: dict  # Guild channel linked to the lobby


__all__ = [
    "Lobby",
    "LobbyMember",
    "LobbyMemberFlags",
]
