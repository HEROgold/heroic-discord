"""Discord Poll Resource Structures.

This module contains TypedDict definitions for Discord Poll objects.
Reference: https://docs.discord.com/developers/resources/poll
"""

from enum import IntEnum
from typing import TypedDict


class LayoutType(IntEnum):
    """Poll layout types.

    https://docs.discord.com/developers/resources/poll#layout-type
    """

    DEFAULT = 1


class PollMedia(TypedDict, total=False):
    """Media object for poll questions and answers.

    https://docs.discord.com/developers/resources/poll#poll-media-object
    """

    text: str  # Text content (max 300 for question, 55 for answer)
    emoji: dict  # Partial emoji object


class PollAnswer(TypedDict, total=False):
    """Represents a poll answer.

    https://docs.discord.com/developers/resources/poll#poll-answer-object
    """

    answer_id: int  # Answer ID
    poll_media: PollMedia  # Answer media data


class PollAnswerCount(TypedDict, total=False):
    """Vote count for a poll answer.

    https://docs.discord.com/developers/resources/poll#poll-results-object-poll-answer-count-object
    """

    id: int  # Answer ID
    count: int  # Number of votes
    me_voted: bool  # Whether current user voted for this answer


class PollResults(TypedDict, total=False):
    """Results of a poll.

    https://docs.discord.com/developers/resources/poll#poll-results-object
    """

    is_finalized: bool  # Whether votes have been precisely counted
    answer_counts: list[PollAnswerCount]  # Counts for each answer


class Poll(TypedDict, total=False):
    """Represents a poll.

    https://docs.discord.com/developers/resources/poll#poll-object
    """

    question: PollMedia  # Poll question
    answers: list[PollAnswer]  # Poll answers
    expiry: str | None  # ISO8601 timestamp when poll ends
    allow_multiselect: bool  # Whether users can select multiple answers
    layout_type: int  # Layout type (LayoutType)
    results: PollResults  # Poll results


class PollCreateRequest(TypedDict, total=False):
    """Request object for creating a poll.

    https://docs.discord.com/developers/resources/poll#poll-create-request-object
    """

    question: PollMedia  # Poll question
    answers: list[PollAnswer]  # Poll answers (up to 10)
    duration: int  # Hours poll should be open (up to 768 = 32 days), defaults to 24
    allow_multiselect: bool  # Whether users can select multiple answers, defaults to false
    layout_type: int  # Layout type, defaults to DEFAULT


__all__ = [
    "LayoutType",
    "Poll",
    "PollAnswer",
    "PollAnswerCount",
    "PollCreateRequest",
    "PollMedia",
    "PollResults",
]
