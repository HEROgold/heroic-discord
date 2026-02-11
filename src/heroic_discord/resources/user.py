"""Discord User Resource Structures.

This module contains TypedDict definitions for Discord User objects.
Reference: https://docs.discord.com/developers/resources/user
"""

from enum import IntEnum
from typing import TypedDict


class UserFlags(IntEnum):
    """User flags as powers of 2.

    https://docs.discord.com/developers/resources/user#user-object-user-flags
    """

    STAFF = 1 << 0
    PARTNER = 1 << 1
    HYPESQUAD = 1 << 2
    BUG_HUNTER_LEVEL_1 = 1 << 3
    HYPESQUAD_ONLINE_HOUSE_1 = 1 << 6
    HYPESQUAD_ONLINE_HOUSE_2 = 1 << 7
    HYPESQUAD_ONLINE_HOUSE_3 = 1 << 8
    PREMIUM_EARLY_SUPPORTER = 1 << 9
    TEAM_PSEUDO_USER = 1 << 10
    BUG_HUNTER_LEVEL_2 = 1 << 14
    VERIFIED_BOT = 1 << 16
    VERIFIED_DEVELOPER = 1 << 17
    CERTIFIED_MODERATOR = 1 << 18
    BOT_HTTP_INTERACTIONS = 1 << 19
    ACTIVE_DEVELOPER = 1 << 22


class PremiumType(IntEnum):
    """Premium types (Nitro levels).

    https://docs.discord.com/developers/resources/user#user-object-premium-types
    """

    NONE = 0
    NITRO_CLASSIC = 1
    NITRO = 2
    NITRO_BASIC = 3


class AvatarDecorationData(TypedDict, total=False):
    """Avatar decoration data.

    https://docs.discord.com/developers/resources/user#avatar-decoration-data-object
    """

    asset: str  # Avatar decoration hash
    sku_id: str  # SKU ID of decoration (snowflake)


class Nameplate(TypedDict, total=False):
    """User nameplate data.

    https://docs.discord.com/developers/resources/user#nameplate
    """

    sku_id: str  # Nameplate SKU ID (snowflake)
    asset: str  # Path to nameplate asset
    label: str  # Label (currently unused)
    palette: str  # Background color


class Collectibles(TypedDict, total=False):
    """User collectibles (excluding avatar decorations).

    https://docs.discord.com/developers/resources/user#collectibles
    """

    nameplate: Nameplate  # User nameplate


class UserPrimaryGuild(TypedDict, total=False):
    """Primary guild information for a user.

    https://docs.discord.com/developers/resources/user#user-object-user-primary-guild
    """

    identity_guild_id: str | None  # Primary guild ID (snowflake)
    identity_enabled: bool | None  # Whether displaying server tag
    tag: str | None  # Server tag text (max 4 chars)
    badge: str | None  # Server tag badge hash


class User(TypedDict, total=False):
    """Represents a Discord user.

    https://docs.discord.com/developers/resources/user#user-object
    """

    id: str  # User ID (snowflake)
    username: str  # Username (not unique across platform)
    discriminator: str  # User's Discord-tag
    global_name: str | None  # Display name, if set
    avatar: str | None  # Avatar hash
    bot: bool  # Whether user is an OAuth2 application
    system: bool  # Whether user is Official Discord System user
    mfa_enabled: bool  # Whether user has two factor enabled
    banner: str | None  # Banner hash
    accent_color: int | None  # Banner color as integer
    locale: str  # User's chosen language option
    verified: bool  # Whether email is verified
    email: str | None  # User's email
    flags: int  # User flags bitfield
    premium_type: int  # Type of Nitro subscription
    public_flags: int  # Public flags on account
    avatar_decoration_data: AvatarDecorationData | None  # Avatar decoration data
    collectibles: Collectibles | None  # User collectibles
    primary_guild: UserPrimaryGuild | None  # Primary guild


class Connection(TypedDict, total=False):
    """User account connection.

    https://docs.discord.com/developers/resources/user#connection-object
    """

    id: str  # Connection account ID
    name: str  # Connection account username
    type: str  # Service of this connection
    revoked: bool  # Whether connection is revoked
    integrations: list[dict]  # Array of partial server integrations
    verified: bool  # Whether connection is verified
    friend_sync: bool  # Whether friend sync is enabled
    show_activity: bool  # Whether activities will be shown in presence
    two_way_link: bool  # Whether has corresponding third party OAuth2 token
    visibility: int  # Connection visibility (0=None, 1=Everyone)


class ApplicationRoleConnection(TypedDict, total=False):
    """Role connection attached by an application.

    https://docs.discord.com/developers/resources/user#application-role-connection-object
    """

    platform_name: str | None  # Vanity name of platform (max 50 chars)
    metadata: dict[str, str]  # Metadata mapping (max 100 chars per value)


__all__ = [
    "ApplicationRoleConnection",
    "AvatarDecorationData",
    "Collectibles",
    "Connection",
    "Nameplate",
    "PremiumType",
    "User",
    "UserFlags",
    "UserPrimaryGuild",
]
