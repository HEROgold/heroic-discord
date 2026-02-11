"""Example usage of the Discord HTTP client."""

from http.client import OK

from heroic_discord import DiscordClient


def main() -> None:
    """Use the Discord client."""
    # Initialize the client with your bot token
    with DiscordClient(
        token="YOUR_BOT_TOKEN_HERE",
        token_type="Bot",
        url="https://github.com/HEROgold/heroic-discord",
        version="0.0.1",
    ) as client:
        # Example: Get current user information
        response = client.get("/users/@me")

        if response.status_code == OK:
            user_data = response.json()
            print(f"Logged in as: {user_data['username']}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

        # Example: Send a message to a channel
        # channel_id = "YOUR_CHANNEL_ID"
        # response = client.post(
        #     f"/channels/{channel_id}/messages",
        #     json={"content": "Hello from heroic-discord!"}
        # )


if __name__ == "__main__":
    main()
