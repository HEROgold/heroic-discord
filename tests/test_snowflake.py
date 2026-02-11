"""Tests for the Snowflake class."""

from datetime import UTC, datetime

import pytest

from heroic_discord.typing.snowflake import Snowflake


def test_snowflake_from_int() -> None:
    """Test creating a Snowflake from an integer."""
    snowflake = Snowflake(175928847299117063)
    assert snowflake.value == 175928847299117063
    assert int(snowflake) == 175928847299117063


def test_snowflake_from_string() -> None:
    """Test creating a Snowflake from a string."""
    snowflake = Snowflake(175928847299117063)
    assert snowflake.value == 175928847299117063
    assert str(snowflake) == "175928847299117063"


def test_snowflake_timestamp_extraction() -> None:
    """Test extracting timestamp from the example in the documentation."""
    # Example from Discord docs: 175928847299117063
    # Binary: 00000000 00001001 11000011 01111011 11110011 11100010 00000001 11000111
    # Timestamp bits (63-22): 41944705796 + 1420070400000 = 1462015105796
    snowflake = Snowflake(175928847299117063)
    assert snowflake.timestamp == 1462015105796


def test_snowflake_worker_id_extraction() -> None:
    """Test extracting worker ID."""
    # From example: bits 21-17 should give worker ID
    snowflake = Snowflake(175928847299117063)
    # Binary has 00000 in positions 21-17, which is 0
    assert 0 <= snowflake.worker_id < 32


def test_snowflake_process_id_extraction() -> None:
    """Test extracting process ID."""
    snowflake = Snowflake(175928847299117063)
    assert 0 <= snowflake.process_id < 32


def test_snowflake_increment_extraction() -> None:
    """Test extracting increment."""
    snowflake = Snowflake(175928847299117063)
    # Last 12 bits: 000111000111 = 455
    expected_increment = 175928847299117063 & 0xFFF
    assert snowflake.increment == expected_increment


def test_snowflake_datetime_conversion() -> None:
    """Test converting timestamp to datetime."""
    snowflake = Snowflake(175928847299117063)
    dt = snowflake.datetime
    assert isinstance(dt, datetime)
    assert dt.tzinfo == UTC
    # Should be around April 30, 2016
    assert dt.year == 2016
    assert dt.month == 4
    assert dt.day == 30


def test_snowflake_from_datetime() -> None:
    """Test creating a Snowflake from datetime."""
    dt = datetime(2016, 4, 30, 11, 18, 25, 796000, tzinfo=UTC)
    snowflake = Snowflake.from_datetime(dt, worker_id=1, process_id=0, increment=7)

    assert snowflake.worker_id == 1
    assert snowflake.process_id == 0
    assert snowflake.increment == 7
    assert snowflake.datetime.year == 2016


def test_snowflake_equality() -> None:
    """Test Snowflake equality comparisons."""
    sf1 = Snowflake(175928847299117063)
    sf2 = Snowflake(175928847299117063)
    sf3 = Snowflake(175928847299117064)

    assert sf1 == sf2
    assert sf1 != sf3
    assert sf1 == 175928847299117063


def test_snowflake_comparison() -> None:
    """Test Snowflake ordering."""
    sf1 = Snowflake(100)
    sf2 = Snowflake(200)

    assert sf1 < sf2
    assert sf1 <= sf2
    assert sf2 > sf1
    assert sf2 >= sf1


def test_snowflake_hashable() -> None:
    """Test that Snowflakes can be used in sets and dicts."""
    sf1 = Snowflake(175928847299117063)
    sf2 = Snowflake(175928847299117063)
    sf3 = Snowflake(175928847299117064)

    snowflake_set = {sf1, sf2, sf3}
    assert len(snowflake_set) == 2  # sf1 and sf2 are equal


def test_snowflake_negative_value() -> None:
    """Test that negative values raise ValueError."""
    with pytest.raises(ValueError, match="cannot be negative"):
        Snowflake(-1)


def test_snowflake_too_large() -> None:
    """Test that values exceeding 64 bits raise ValueError."""
    with pytest.raises(ValueError, match="cannot exceed 64 bits"):
        Snowflake(2**64)


def test_snowflake_from_datetime_invalid_worker_id() -> None:
    """Test that invalid worker_id raises ValueError."""
    dt = datetime.now(UTC)
    with pytest.raises(ValueError, match="worker_id must be between 0 and 31"):
        Snowflake.from_datetime(dt, worker_id=32)


def test_snowflake_from_datetime_invalid_process_id() -> None:
    """Test that invalid process_id raises ValueError."""
    dt = datetime.now(UTC)
    with pytest.raises(ValueError, match="process_id must be between 0 and 31"):
        Snowflake.from_datetime(dt, process_id=-1)


def test_snowflake_from_datetime_invalid_increment() -> None:
    """Test that invalid increment raises ValueError."""
    dt = datetime.now(UTC)
    with pytest.raises(ValueError, match="increment must be between 0 and 4095"):
        Snowflake.from_datetime(dt, increment=4096)


def test_snowflake_repr() -> None:
    """Test Snowflake representation."""
    snowflake = Snowflake(175928847299117063)
    assert repr(snowflake) == "Snowflake(175928847299117063)"


def test_snowflake_from_timestamp_ms() -> None:
    """Test creating a Snowflake from milliseconds timestamp for pagination."""
    # Create a snowflake from timestamp (e.g., for pagination)
    timestamp_ms = 41944705796  # milliseconds since Discord Epoch
    snowflake = Snowflake.from_timestamp_ms(timestamp_ms)

    # The timestamp should be preserved
    assert snowflake.timestamp == timestamp_ms + Snowflake.DISCORD_EPOCH
    # Other fields should be 0
    assert snowflake.worker_id == 0
    assert snowflake.process_id == 0
    assert snowflake.increment == 0


def test_snowflake_from_timestamp_ms_zero() -> None:
    """Test creating a Snowflake from timestamp 0 (Discord Epoch)."""
    # Using 0 represents the Discord Epoch, useful for pagination from the beginning
    snowflake = Snowflake.from_timestamp_ms(0)

    assert snowflake.timestamp == Snowflake.DISCORD_EPOCH
    assert snowflake.value == 0
    assert snowflake.worker_id == 0
    assert snowflake.process_id == 0
    assert snowflake.increment == 0

