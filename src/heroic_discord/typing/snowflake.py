"""Discord Snowflake ID implementation.

Discord utilizes Twitter's snowflake format for uniquely identifiable descriptors (IDs).
These IDs are guaranteed to be unique across all of Discord, except in some unique
scenarios in which child objects share their parent's ID. Because Snowflake IDs are
up to 64 bits in size (e.g. a uint64), they are always returned as strings in the
HTTP API to prevent integer overflows in some languages.
"""

from datetime import UTC, datetime
from typing import Self


class Snowflake:
    """Discord Snowflake ID.

    A 64-bit unique identifier used throughout Discord's API.

    Structure (left to right):
    - Timestamp: bits 63-22 (42 bits) - Milliseconds since Discord Epoch (2015-01-01)
    - Internal worker ID: bits 21-17 (5 bits)
    - Internal process ID: bits 16-12 (5 bits)
    - Increment: bits 11-0 (12 bits) - Incremented for every ID generated on that process
    """

    DISCORD_EPOCH = 1420070400000  # First second of 2015 in milliseconds (1420070400000)

    def __init__(self, value: int) -> None:
        """Initialize a Snowflake from an integer."""
        if value < 0:
            msg = "Snowflake ID cannot be negative"
            raise ValueError(msg)
        if value >= 2**64:
            msg = "Snowflake ID cannot exceed 64 bits"
            raise ValueError(msg)

        self._value = value

    @property
    def value(self) -> int:
        """Get the raw integer value of the snowflake."""
        return self._value

    @property
    def timestamp(self) -> int:
        """Extract the timestamp component (bits 63-22).

        Returns:
            Milliseconds since Discord Epoch (2015-01-01).

        """
        return (self._value >> 22) + self.DISCORD_EPOCH

    @property
    def worker_id(self) -> int:
        """Extract the internal worker ID (bits 21-17).

        Returns:
            The internal worker ID (0-31).

        """
        return (self._value & 0x3E0000) >> 17

    @property
    def process_id(self) -> int:
        """Extract the internal process ID (bits 16-12).

        Returns:
            The internal process ID (0-31).

        """
        return (self._value & 0x1F000) >> 12

    @property
    def increment(self) -> int:
        """Extract the increment component (bits 11-0).

        Returns:
            The increment value (0-4095).

        """
        return self._value & 0xFFF

    @property
    def datetime(self) -> datetime:  # ty:ignore[invalid-type-form]
        """Convert the timestamp to a datetime object.

        Returns:
            A timezone-aware datetime in UTC.

        """
        return datetime.fromtimestamp(self.timestamp / 1000, tz=UTC)

    @classmethod
    def from_datetime(
        cls,
        dt: datetime,  # ty:ignore[invalid-type-form]
        worker_id: int = 0,
        process_id: int = 0,
        increment: int = 0,
    ) -> Self:
        """Create a Snowflake from a datetime and optional components.

        Raises:
            ValueError: If any component is out of range.

        """
        if not 0 <= worker_id < 32:  # noqa: PLR2004
            msg = "worker_id must be between 0 and 31"
            raise ValueError(msg)
        if not 0 <= process_id < 32:  # noqa: PLR2004
            msg = "process_id must be between 0 and 31"
            raise ValueError(msg)
        if not 0 <= increment < 4096:  # noqa: PLR2004
            msg = "increment must be between 0 and 4095"
            raise ValueError(msg)

        timestamp_ms = int(dt.timestamp() * 1000) - cls.DISCORD_EPOCH

        value = (timestamp_ms << 22) | (worker_id << 17) | (process_id << 12) | increment
        return cls(value)

    @classmethod
    def from_timestamp_ms(cls, timestamp_ms: int) -> Self:
        """Create a Snowflake from a timestamp in milliseconds.

        Useful for pagination where you want results from the beginning of time
        (Discord Epoch, but 0 works here too) or before/after a specific time.

        Args:
            timestamp_ms: Milliseconds since Discord Epoch (2015-01-01).
                Use 0 to get a snowflake representing Discord Epoch.

        Returns:
            A new Snowflake instance with the given timestamp and all other fields set to 0.

        """
        # Shift timestamp to proper position (bits 63-22)
        value = (timestamp_ms << 22)
        return cls(value)

    def __int__(self) -> int:
        """Convert to integer."""
        return self._value

    def __str__(self) -> str:
        """Convert to string (as returned by Discord API)."""
        return str(self._value)

    def __repr__(self) -> str:
        """Return a detailed representation."""
        return f"Snowflake({self._value})"

    def __eq__(self, other: object) -> bool:
        """Check equality with another Snowflake or integer."""
        if isinstance(other, Snowflake):
            return self._value == other._value
        if isinstance(other, int):
            return self._value == other
        return NotImplemented

    def __lt__(self, other: Snowflake) -> bool:
        """Compare Snowflakes (chronologically)."""
        return self._value < other._value

    def __le__(self, other: Snowflake) -> bool:
        """Compare Snowflakes (chronologically)."""
        return self._value <= other._value

    def __gt__(self, other: Snowflake) -> bool:
        """Compare Snowflakes (chronologically)."""
        return self._value > other._value

    def __ge__(self, other: Snowflake) -> bool:
        """Compare Snowflakes (chronologically)."""
        return self._value >= other._value

    def __hash__(self) -> int:
        """Make Snowflake hashable."""
        return hash(self._value)
