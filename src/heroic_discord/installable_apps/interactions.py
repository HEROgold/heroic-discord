"""TypedDict structures for Discord interaction metadata."""

from typing import TYPE_CHECKING, NotRequired, Required, TypedDict

if TYPE_CHECKING:
    from heroic_discord.installable_apps.enums import InteractionContextType


class AuthorizingIntegrationOwners(TypedDict, total=False):
    """Provides data about IDs relevant to the installation context(s).

    The keys are IntegrationType values (as strings "0" or "1").
    The values depend on the key:
    - For GUILD_INSTALL ("0"): the guild ID
    - For USER_INSTALL ("1"): the user ID who authorized the app

    References:
        https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-object-authorizing-integration-owners-object

    """

    # Prefixed with _ to avoid syntax errors!.
    _0: NotRequired[str]  # GUILD_INSTALL - guild_id
    _1: NotRequired[str]  # USER_INSTALL - user_id

class InteractionMetadata(TypedDict):
    """Metadata for an interaction message.

    Messages created in response to an interaction include this metadata
    which provides context about the original interaction.

    References:
        https://docs.discord.com/developers/resources/message#message-interaction-metadata-object

    """

    id: Required[str]
    """ID of the interaction."""

    type: Required[int]
    """Type of interaction."""

    user_id: Required[str]
    """ID of the user who triggered the interaction."""

    authorizing_integration_owners: Required[AuthorizingIntegrationOwners]
    """IDs relevant to the installation context(s)."""

    original_response_message_id: NotRequired[str]
    """ID of the original response message (for components/modals)."""

    interacted_message_id: NotRequired[str]
    """ID of the message that contained interactive component."""

    triggering_interaction_metadata: NotRequired[InteractionMetadata]
    """Metadata for the interaction that triggered this component/modal."""


class InteractionData(TypedDict):
    """Base structure for interaction payload data.

    This contains common fields present in most interaction types.
    """

    id: NotRequired[str]
    """ID of the invoked command."""

    name: NotRequired[str]
    """Name of the invoked command."""

    type: NotRequired[int]
    """Type of the invoked command."""


class PartialUser(TypedDict):
    """Simplified user object in interaction payloads."""

    id: Required[str]
    """User's ID."""

    username: Required[str]
    """User's username."""

    discriminator: Required[str]
    """User's 4-digit discriminator."""

    avatar: NotRequired[str | None]
    """User's avatar hash."""

    bot: NotRequired[bool]
    """Whether the user is a bot."""


class PartialChannel(TypedDict):
    """Simplified channel object in interaction payloads."""

    id: Required[str]
    """Channel's ID."""

    type: Required[int]
    """Channel's type."""

    name: NotRequired[str]
    """Channel's name."""


class Interaction(TypedDict):
    """Structure for an interaction received from Discord.

    This represents the full interaction payload sent to your app when
    a user invokes a command or interacts with a component.

    References:
        https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-object

    """

    id: Required[str]
    """ID of the interaction."""

    application_id: Required[str]
    """ID of the application this interaction is for."""

    type: Required[int]
    """Type of interaction."""

    data: NotRequired[InteractionData]
    """Interaction data payload."""

    guild_id: NotRequired[str]
    """Guild ID where the interaction was triggered (if in a guild)."""

    channel_id: NotRequired[str]
    """Channel ID where the interaction was triggered."""

    channel: NotRequired[PartialChannel]
    """Partial channel object."""

    member: NotRequired[dict]
    """Guild member object (if interaction is in a guild)."""

    user: NotRequired[PartialUser]
    """User object (if interaction is in a DM or when member is not present)."""

    token: Required[str]
    """Continuation token for responding to the interaction."""

    version: Required[int]
    """Read-only property, always 1."""

    message: NotRequired[dict]
    """For components, the message the component was attached to."""

    app_permissions: NotRequired[str]
    """Bitwise set of permissions your app has in the context."""

    locale: NotRequired[str]
    """Selected language of the invoking user."""

    guild_locale: NotRequired[str]
    """Guild's preferred locale (if invoked in a guild)."""

    entitlements: NotRequired[list[dict]]
    """Entitlements for the invoking user/guild."""

    authorizing_integration_owners: Required[AuthorizingIntegrationOwners]
    """Installation context owners for this interaction."""

    context: NotRequired[InteractionContextType]
    """Context where the interaction was triggered.

    Note:
        This is an integer value matching InteractionContextType enum.
        0 = GUILD, 1 = BOT_DM, 2 = PRIVATE_CHANNEL
    """
