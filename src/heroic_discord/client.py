"""HTTP client for Discord API."""

from typing import TYPE_CHECKING, Any, Self

import httpx

from heroic_discord.constants import API, AUTH, USER_AGENT

from .log import base_logger

if TYPE_CHECKING:
    from types import TracebackType

logger = base_logger.getChild(__name__)


class DiscordClient:
    """HTTP client for interacting with Discord API.

    Handles authentication, user agent headers, and rate limiting
    as specified in Discord's HTTP API documentation.
    """

    def __init__(
        self,
        token: str,
        token_type: str = "Bot",  # noqa: S107
        url: str = "https://github.com/HEROgold/heroic-discord",
        version: str = "0.0.1",
    ) -> None:
        """Initialize the Discord HTTP client.

        Args:
            token: Discord bot or bearer token
            token_type: Type of token authentication ("Bot" or "Bearer")
            url: URL to your bot's repository or website
            version: Version number of your bot

        """
        self.token = token
        self.token_type = token_type
        self.base_url = API

        # Format the user agent according to Discord's requirements
        user_agent = USER_AGENT.format(url=url, versionNumber=version)

        # Set up authentication header
        auth_header = AUTH.format(token_type=token_type, token=token)

        # Initialize httpx client with default headers
        self.client = httpx.Client(
            base_url=self.base_url,
            headers={
                "Authorization": auth_header,
                "User-Agent": user_agent,
            },
            timeout=30.0,
        )

    def __enter__(self) -> Self:
        """Context manager entry."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Context manager exit - closes the client."""
        if exc_type is not None and exc_val is not None:
            logger.error(
                "Exception occurred in DiscordClient context: %s: %s",
                exc_type.__name__,
                exc_val,
                exc_info=(exc_type, exc_val, exc_tb),
            )
        self.close()

    def close(self) -> None:
        """Close the HTTP client connection."""
        self.client.close()

    def get(
        self,
        endpoint: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make a GET request to the Discord API.

        Args:
            endpoint: API endpoint (e.g., "/users/@me")
            params: Query parameters
            headers: Additional headers to include

        Returns:
            httpx.Response object

        """
        return self.client.get(endpoint, params=params, headers=headers)

    def post(
        self,
        endpoint: str,
        *,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make a POST request to the Discord API.

        Args:
            endpoint: API endpoint
            json: JSON data to send (sets Content-Type: application/json)
            data: Form data to send
            headers: Additional headers to include

        Returns:
            httpx.Response object

        """
        request_headers = headers or {}

        # Ensure Content-Type is set appropriately
        if json is not None and "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/json"
        elif data is not None and "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/x-www-form-urlencoded"

        return self.client.post(
            endpoint,
            json=json,
            data=data,
            headers=request_headers,
        )

    def put(
        self,
        endpoint: str,
        *,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make a PUT request to the Discord API.

        Args:
            endpoint: API endpoint
            json: JSON data to send
            data: Form data to send
            headers: Additional headers to include

        Returns:
            httpx.Response object

        """
        request_headers = headers or {}

        if json is not None and "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/json"
        elif data is not None and "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/x-www-form-urlencoded"

        return self.client.put(
            endpoint,
            json=json,
            data=data,
            headers=request_headers,
        )

    def patch(
        self,
        endpoint: str,
        *,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make a PATCH request to the Discord API.

        Args:
            endpoint: API endpoint
            json: JSON data to send
            data: Form data to send
            headers: Additional headers to include

        Returns:
            httpx.Response object

        """
        request_headers = headers or {}

        if json is not None and "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/json"
        elif data is not None and "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/x-www-form-urlencoded"

        return self.client.patch(
            endpoint,
            json=json,
            data=data,
            headers=request_headers,
        )

    def delete(
        self,
        endpoint: str,
        *,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make a DELETE request to the Discord API.

        Args:
            endpoint: API endpoint
            headers: Additional headers to include

        Returns:
            httpx.Response object

        """
        return self.client.delete(endpoint, headers=headers)


class AsyncDiscordClient:
    """Asynchronous HTTP client for interacting with Discord API.

    Handles authentication, user agent headers, and rate limiting
    as specified in Discord's HTTP API documentation.
    """

    def __init__(
        self,
        token: str,
        token_type: str = "Bot",  # noqa: S107
        url: str = "https://github.com/HEROgold/heroic-discord",
        version: str = "0.0.1",
    ) -> None:
        """Initialize the Discord async HTTP client.

        Args:
            token: Discord bot or bearer token
            token_type: Type of token authentication ("Bot" or "Bearer")
            url: URL to your bot's repository or website
            version: Version number of your bot

        """
        self.token = token
        self.token_type = token_type
        self.base_url = API

        # Format the user agent according to Discord's requirements
        user_agent = USER_AGENT.format(url=url, versionNumber=version)

        # Set up authentication header
        auth_header = AUTH.format(token_type=token_type, token=token)

        # Initialize httpx async client with default headers
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={
                "Authorization": auth_header,
                "User-Agent": user_agent,
            },
            timeout=30.0,
        )

    async def __aenter__(self) -> Self:
        """Async context manager entry."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Async context manager exit - closes the client."""
        if exc_type is not None and exc_val is not None:
            logger.error(
                "Exception occurred in AsyncDiscordClient context: %s: %s",
                exc_type.__name__,
                exc_val,
                exc_info=(exc_type, exc_val, exc_tb),
            )
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client connection."""
        await self.client.aclose()

    async def get(
        self,
        endpoint: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make a GET request to the Discord API.

        Args:
            endpoint: API endpoint (e.g., "/users/@me")
            params: Query parameters
            headers: Additional headers to include

        Returns:
            httpx.Response object

        """
        return await self.client.get(endpoint, params=params, headers=headers)

    async def post(
        self,
        endpoint: str,
        *,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make a POST request to the Discord API.

        Args:
            endpoint: API endpoint
            json: JSON data to send (sets Content-Type: application/json)
            data: Form data to send
            headers: Additional headers to include

        Returns:
            httpx.Response object

        """
        request_headers = headers or {}

        # Ensure Content-Type is set appropriately
        if json is not None and "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/json"
        elif data is not None and "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/x-www-form-urlencoded"

        return await self.client.post(
            endpoint,
            json=json,
            data=data,
            headers=request_headers,
        )

    async def put(
        self,
        endpoint: str,
        *,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make a PUT request to the Discord API.

        Args:
            endpoint: API endpoint
            json: JSON data to send
            data: Form data to send
            headers: Additional headers to include

        Returns:
            httpx.Response object

        """
        request_headers = headers or {}

        if json is not None and "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/json"
        elif data is not None and "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/x-www-form-urlencoded"

        return await self.client.put(
            endpoint,
            json=json,
            data=data,
            headers=request_headers,
        )

    async def patch(
        self,
        endpoint: str,
        *,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make a PATCH request to the Discord API.

        Args:
            endpoint: API endpoint
            json: JSON data to send
            data: Form data to send
            headers: Additional headers to include

        Returns:
            httpx.Response object

        """
        request_headers = headers or {}

        if json is not None and "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/json"
        elif data is not None and "Content-Type" not in request_headers:
            request_headers["Content-Type"] = "application/x-www-form-urlencoded"

        return await self.client.patch(
            endpoint,
            json=json,
            data=data,
            headers=request_headers,
        )

    async def delete(
        self,
        endpoint: str,
        *,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Make a DELETE request to the Discord API.

        Args:
            endpoint: API endpoint
            headers: Additional headers to include

        Returns:
            httpx.Response object

        """
        return await self.client.delete(endpoint, headers=headers)
