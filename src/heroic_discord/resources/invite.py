"""Discord Invite Resource Structures.

This module contains TypedDict definitions for Discord Invite objects.
Reference: https://docs.discord.com/developers/resources/invite
"""

from enum import IntEnum
from typing import TypedDict


class InviteType(IntEnum):
    """Types of invites.

    https://docs.discord.com/developers/resources/invite#invite-object-invite-types
    """

    GUILD = 0
    GROUP_DM = 1
    FRIEND = 2


class InviteTargetType(IntEnum):
    """Target types for voice channel invites.

    https://docs.discord.com/developers/resources/invite#invite-object-invite-target-types
    """

    STREAM = 1
    EMBEDDED_APPLICATION = 2


class InviteFlags(IntEnum):
    """Guild invite flags as powers of 2.

    https://docs.discord.com/developers/resources/invite#invite-object-guild-invite-flags
    """

    IS_GUEST_INVITE = 1 << 0


class InviteMetadata(TypedDict, total=False):
    """Extra metadata about an invite.

    https://docs.discord.com/developers/resources/invite#invite-metadata-object
    """

    uses: int  # Number of times invite has been used
    max_uses: int  # Max times invite can be used
    max_age: int  # Duration (seconds) after which invite expires
    temporary: bool  # Whether invite only grants temporary membership
    created_at: str  # ISO8601 timestamp when invite was created


class Invite(TypedDict, total=False):
    """Represents a code that adds a user to a guild or group DM.

    https://docs.discord.com/developers/resources/invite#invite-object
    """

    type: int  # Invite type (InviteType)
    code: str  # Invite code (unique ID)
    guild: dict  # Partial guild object
    channel: dict | None  # Partial channel object
    inviter: dict  # User who created the invite
    target_type: int  # Target type for voice channel invite
    target_user: dict  # User whose stream to display
    target_application: dict  # Partial application object for embedded application
    approximate_presence_count: int  # Approximate online member count
    approximate_member_count: int  # Approximate total member count
    expires_at: str | None  # ISO8601 expiration date
    guild_scheduled_event: dict  # Guild scheduled event data
    flags: int  # Guild invite flags bitfield
    roles: list[dict]  # Partial role objects for roles assigned upon accepting


__all__ = [
    "Invite",
    "InviteFlags",
    "InviteMetadata",
    "InviteTargetType",
    "InviteType",
]
