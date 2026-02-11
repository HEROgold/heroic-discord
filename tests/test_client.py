"""Tests for the Discord HTTP client."""

from heroic_discord.client import DiscordClient
from heroic_discord.constants import API, AUTH, USER_AGENT


def test_client_initialization() -> None:
    """Test that the client initializes with correct headers."""
    token = "test_token_123"
    token_type = "Bot"
    url = "https://github.com/test/repo"
    version = "1.0.0"

    client = DiscordClient(
        token=token,
        token_type=token_type,
        url=url,
        version=version,
    )

    # Check base URL
    assert client.base_url == API

    # Check headers are set correctly
    assert "Authorization" in client.client.headers
    assert "User-Agent" in client.client.headers

    # Verify Authorization header format
    expected_auth = AUTH.format(token_type=token_type, token=token)
    assert client.client.headers["Authorization"] == expected_auth

    # Verify User-Agent format
    expected_ua = USER_AGENT.format(url=url, versionNumber=version)
    assert client.client.headers["User-Agent"] == expected_ua
    assert "DiscordBot" in client.client.headers["User-Agent"]
    assert url in client.client.headers["User-Agent"]
    assert version in client.client.headers["User-Agent"]

    client.close()


def test_client_context_manager() -> None:
    """Test that the client works as a context manager."""
    token = "test_token_456"

    with DiscordClient(token=token) as client:
        assert client is not None
        assert client.token == token
        # Client should be open within context
        assert not client.client.is_closed


def test_client_default_token_type() -> None:
    """Test that default token type is 'Bot'."""
    client = DiscordClient(token="test_token")

    assert "Bot test_token" in client.client.headers["Authorization"]

    client.close()


def test_client_bearer_token() -> None:
    """Test that Bearer token type works correctly."""
    token = "bearer_token_789"
    client = DiscordClient(token=token, token_type="Bearer")

    assert "Bearer bearer_token_789" in client.client.headers["Authorization"]

    client.close()


def test_client_user_agent_format() -> None:
    """Test that user agent follows Discord's required format."""
    url = "https://github.com/HEROgold/heroic-discord"
    version = "0.0.1"

    client = DiscordClient(
        token="test",
        url=url,
        version=version,
    )

    user_agent = client.client.headers["User-Agent"]

    # Should follow format: DiscordBot ($url, $versionNumber)
    assert user_agent.startswith("DiscordBot (")
    assert url in user_agent
    assert version in user_agent
    assert user_agent.endswith(")")

    client.close()
