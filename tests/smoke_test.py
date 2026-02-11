#!/usr/bin/env python
"""Smoke test to verify the package was built correctly and can be imported."""

import sys


def main() -> int:
    """Run basic smoke tests on the heroic-discord package."""
    try:
        # Test that the package can be imported
        import heroic_discord  # noqa: PLC0415

        # Test that basic functionality works
        result = heroic_discord.hello()
        assert isinstance(result, str), "hello() should return a string"
        assert len(result) > 0, "hello() should return a non-empty string"

        print("✓ Package import successful")
        print(f"✓ Basic functionality verified: {result}")
        print("✓ All smoke tests passed")

    except ImportError as e:
        print(f"✗ Failed to import package: {e}")
        return 1
    except AssertionError as e:
        print(f"✗ Assertion failed: {e}")
        return 1
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return 1
    else:
        return 0


if __name__ == "__main__":
    sys.exit(main())
