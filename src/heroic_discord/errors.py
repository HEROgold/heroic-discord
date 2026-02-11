"""Defines error response structures for Discord API validation errors."""

from typing import NotRequired, Required, TypedDict


class ErrorDetail(TypedDict):
    """Represents a single error detail from Discord API."""

    code: Required[str]
    message: Required[str]


class ErrorField(TypedDict):
    """Represents a field with errors."""

    _errors: Required[list[ErrorDetail]]


class ActivityIndexErrors(TypedDict):
    """Represents errors for a specific activity index."""

    platform: NotRequired[ErrorField]
    type: NotRequired[ErrorField]


class ActivityErrors(TypedDict):
    """Represents errors for activities array."""

    activities: Required[dict[str, ActivityIndexErrors]]


class ObjectErrors(TypedDict):
    """Represents errors for object fields."""

    access_token: NotRequired[ErrorField]


class RequestErrors(TypedDict):
    """Represents errors at the request level."""

    _errors: Required[list[ErrorDetail]]


class ArrayErrorResponse(TypedDict):
    """Discord API error response for array validation errors."""

    code: Required[int]
    errors: Required[ActivityErrors]
    message: Required[str]


class ObjectErrorResponse(TypedDict):
    """Discord API error response for object validation errors."""

    code: Required[int]
    errors: Required[ObjectErrors]
    message: Required[str]


class RequestErrorResponse(TypedDict):
    """Discord API error response for request-level errors."""

    code: Required[int]
    message: Required[str]
    errors: Required[RequestErrors]
