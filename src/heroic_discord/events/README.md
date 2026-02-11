# Discord Events Module

This module provides comprehensive type definitions and structures for Discord's event system, including both Gateway (WebSocket) and Webhook (HTTP) events.

## Overview

Discord events allow your app to receive real-time updates about actions happening in servers, channels, and user interactions. There are two primary methods to receive events:

### Gateway Events (WebSocket)
Gateway events are sent over persistent WebSocket connections and provide real-time updates. They are the primary way apps receive events from Discord.

**Key Features:**
- Real-time bidirectional communication
- Requires maintaining a persistent connection
- Supports heartbeating, resuming, and sharding
- Controlled by Gateway Intents

**Use Cases:**
- Real-time message monitoring
- User presence tracking
- Voice state changes
- Most Discord resource updates

### Webhook Events (HTTP)
Webhook events are sent to your app's configured URL over HTTP when specific lifecycle events occur.

**Key Features:**
- One-way communication from Discord to your app
- No persistent connection required
- Not real-time or guaranteed order
- Limited event types

**Use Cases:**
- App authorization/deauthorization
- Entitlement lifecycle (purchases, updates)
- Social SDK messages (lobbies, direct messages)

## Module Structure

```
events/
├── __init__.py           # Main exports and base types
├── base.py              # Common enums and base structures
├── gateway/             # Gateway (WebSocket) events
│   ├── __init__.py      # Gateway exports
│   ├── send_events.py   # Events sent from app to Discord
│   └── receive_events.py # Events received from Discord
└── webhook/             # Webhook (HTTP) events
    ├── __init__.py      # Webhook exports
    └── events.py        # Webhook event structures
```

## Usage Examples

### Gateway Events

#### Identifying with Gateway
```python
from heroic_discord.events.gateway import IdentifyStructure, IdentifyConnectionProperties
from heroic_discord.events.base import GatewayIntent

identify_payload: IdentifyStructure = {
    "token": "your_bot_token",
    "intents": GatewayIntent.GUILDS | GatewayIntent.GUILD_MESSAGES,
    "properties": {
        "os": "linux",
        "browser": "heroic_discord",
        "device": "heroic_discord"
    }
}
```

#### Handling Gateway Events
```python
from heroic_discord.events.gateway import ReadyEventFields, MessageCreateExtraFields

# Ready event - initial connection
def handle_ready(event_data: ReadyEventFields):
    session_id = event_data["session_id"]
    resume_url = event_data["resume_gateway_url"]
    # Store for resuming connection

# Message create event
def handle_message_create(event_data: MessageCreateExtraFields):
    guild_id = event_data.get("guild_id")
    member = event_data.get("member")
    # Process message
```

#### Updating Presence
```python
from heroic_discord.events.gateway import UpdatePresenceStructure, ActivityObject

presence: UpdatePresenceStructure = {
    "since": None,
    "activities": [{
        "name": "with Discord API",
        "type": 0  # Playing
    }],
    "status": "online",
    "afk": False
}
```

### Webhook Events

#### Handling Application Authorization
```python
from heroic_discord.events.webhook import ApplicationAuthorizedStructure

def handle_app_authorized(event_data: ApplicationAuthorizedStructure):
    integration_type = event_data["integration_type"]
    user = event_data["user"]
    scopes = event_data["scopes"]
    
    if integration_type == 0:  # Guild installation
        guild = event_data.get("guild")
        print(f"Installed to guild: {guild}")
    else:  # User installation
        print(f"Installed to user: {user}")
```

#### Handling Entitlements
```python
from heroic_discord.events.webhook import EntitlementCreateStructure

def handle_entitlement_create(event_data: EntitlementCreateStructure):
    user_id = event_data["user_id"]
    sku_id = event_data["sku_id"]
    # Grant user access to premium features
```

## Gateway Intents

Gateway Intents control which events your app receives over the Gateway connection. Some intents are privileged and require approval for verified apps.

### Standard Intents
```python
from heroic_discord.events.base import GatewayIntent

# Combine intents using bitwise OR
intents = (
    GatewayIntent.GUILDS |
    GatewayIntent.GUILD_MESSAGES |
    GatewayIntent.GUILD_MESSAGE_REACTIONS
)
```

### Privileged Intents
These require explicit approval:
- `GUILD_MEMBERS` - Guild member events
- `GUILD_PRESENCES` - User presence updates
- `MESSAGE_CONTENT` - Message content access

### Intent Coverage

#### GUILDS (1 << 0)
- GUILD_CREATE, GUILD_UPDATE, GUILD_DELETE
- GUILD_ROLE_CREATE, GUILD_ROLE_UPDATE, GUILD_ROLE_DELETE
- CHANNEL_CREATE, CHANNEL_UPDATE, CHANNEL_DELETE
- CHANNEL_PINS_UPDATE
- THREAD_CREATE, THREAD_UPDATE, THREAD_DELETE
- STAGE_INSTANCE_CREATE, STAGE_INSTANCE_UPDATE, STAGE_INSTANCE_DELETE

#### GUILD_MEMBERS (1 << 1) - Privileged
- GUILD_MEMBER_ADD, GUILD_MEMBER_UPDATE, GUILD_MEMBER_REMOVE

#### GUILD_MESSAGES (1 << 9)
- MESSAGE_CREATE, MESSAGE_UPDATE, MESSAGE_DELETE, MESSAGE_DELETE_BULK

#### GUILD_MESSAGE_REACTIONS (1 << 10)
- MESSAGE_REACTION_ADD, MESSAGE_REACTION_REMOVE
- MESSAGE_REACTION_REMOVE_ALL, MESSAGE_REACTION_REMOVE_EMOJI

## Gateway Opcodes

Gateway opcodes define the type of payload being sent/received:

```python
from heroic_discord.events.base import GatewayOpcode

# Receive opcodes
GatewayOpcode.DISPATCH         # 0 - Event dispatched
GatewayOpcode.HELLO           # 10 - Connection start
GatewayOpcode.HEARTBEAT_ACK   # 11 - Heartbeat acknowledged

# Send opcodes
GatewayOpcode.HEARTBEAT        # 1 - Keep-alive ping
GatewayOpcode.IDENTIFY         # 2 - Start session
GatewayOpcode.RESUME           # 6 - Resume session
GatewayOpcode.REQUEST_GUILD_MEMBERS  # 8 - Request members
```

## Event Categories

### Connection Events
- `HELLO` - Initial connection, contains heartbeat interval
- `READY` - Successful handshake, contains session info
- `RESUMED` - Session resumed after disconnect

### Channel Events
- `CHANNEL_CREATE`, `CHANNEL_UPDATE`, `CHANNEL_DELETE`
- `THREAD_CREATE`, `THREAD_UPDATE`, `THREAD_DELETE`
- `CHANNEL_PINS_UPDATE`

### Guild Events
- `GUILD_CREATE`, `GUILD_UPDATE`, `GUILD_DELETE`
- `GUILD_MEMBER_ADD`, `GUILD_MEMBER_UPDATE`, `GUILD_MEMBER_REMOVE`
- `GUILD_ROLE_CREATE`, `GUILD_ROLE_UPDATE`, `GUILD_ROLE_DELETE`
- `GUILD_BAN_ADD`, `GUILD_BAN_REMOVE`

### Message Events
- `MESSAGE_CREATE`, `MESSAGE_UPDATE`, `MESSAGE_DELETE`
- `MESSAGE_REACTION_ADD`, `MESSAGE_REACTION_REMOVE`

### Voice Events
- `VOICE_STATE_UPDATE` - User voice state changes
- `VOICE_SERVER_UPDATE` - Voice server updates

### Presence Events
- `PRESENCE_UPDATE` - User presence/status changes
- `TYPING_START` - User starts typing

## Best Practices

### Gateway Connection Management
1. **Cache the Gateway URL** - Store and reuse the URL from `Get Gateway Bot`
2. **Handle Disconnects** - Implement proper resume logic using `resume_gateway_url`
3. **Heartbeat Timing** - Use jitter on first heartbeat: `heartbeat_interval * random(0, 1)`
4. **Rate Limits** - Respect 120 events per 60 seconds limit
5. **Sharding** - Shard connections for bots in 2500+ guilds

### Intent Selection
1. **Minimize Intents** - Only request intents your app needs
2. **Privileged Intents** - Apply for approval if required
3. **Message Content** - Only request if absolutely necessary

### Event Handling
1. **Sequence Numbers** - Track sequence numbers for resuming
2. **State Caching** - Cache relevant data to minimize API calls
3. **Error Handling** - Gracefully handle malformed or unexpected events

## References

- [Discord Events Overview](https://docs.discord.com/developers/events/overview)
- [Gateway Documentation](https://docs.discord.com/developers/events/gateway)
- [Gateway Events](https://docs.discord.com/developers/events/gateway-events)
- [Webhook Events](https://docs.discord.com/developers/events/webhook-events)
- [Gateway Intents](https://docs.discord.com/developers/events/gateway#gateway-intents)
- [Opcodes and Status Codes](https://docs.discord.com/developers/topics/opcodes-and-status-codes)

## Type Safety

All structures use `TypedDict` for type safety and IDE autocompletion:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from heroic_discord.events.gateway import IdentifyStructure
    
def create_identify(token: str, intents: int) -> IdentifyStructure:
    return {
        "token": token,
        "intents": intents,
        "properties": {
            "os": "linux",
            "browser": "heroic_discord",
            "device": "heroic_discord"
        }
    }
```

## Contributing

When adding new event types:
1. Follow the existing naming conventions
2. Include full documentation with Discord API references
3. Mark optional fields with `total=False` in TypedDict
4. Add appropriate exports to `__init__.py` files
5. Update this README with usage examples
