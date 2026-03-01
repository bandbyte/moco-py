"""Exception hierarchy for the MOCO API client."""

from __future__ import annotations

from typing import Any

import httpx


class MocoError(Exception):
    """Base exception for all MOCO API errors."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        body: Any | None = None,
        response: httpx.Response | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.body = body
        self.response = response


class AuthenticationError(MocoError):
    """401 — Invalid or missing API key."""


class PermissionError(MocoError):
    """403 — Insufficient permissions."""


class NotFoundError(MocoError):
    """404 — Resource does not exist."""


class ValidationError(MocoError):
    """422 — Invalid request parameters."""


class RateLimitError(MocoError):
    """429 — Too many requests."""

    def __init__(
        self,
        message: str,
        *,
        retry_after: float | None = None,
        status_code: int | None = None,
        body: Any | None = None,
        response: httpx.Response | None = None,
    ) -> None:
        super().__init__(message, status_code=status_code, body=body, response=response)
        self.retry_after = retry_after


class ServerError(MocoError):
    """5xx — Server-side error."""


class APIConnectionError(MocoError):
    """Network-level connection error."""

    def __init__(self, message: str) -> None:
        super().__init__(message, status_code=None, body=None, response=None)


class APITimeoutError(APIConnectionError):
    """Request timed out."""


_STATUS_CODE_MAP: dict[int, type[MocoError]] = {
    401: AuthenticationError,
    403: PermissionError,
    404: NotFoundError,
    422: ValidationError,
    429: RateLimitError,
}


def _raise_for_status(response: httpx.Response) -> None:
    """Raise an appropriate exception for error HTTP status codes."""
    if response.status_code < 400:
        return

    body: Any = None
    message = f"HTTP {response.status_code}"
    try:
        body = response.json()
        if isinstance(body, dict):
            msg = body.get("message") or body.get("error")
            if msg is not None:
                message = str(msg)
    except Exception:
        body = response.text or None

    exc_class = _STATUS_CODE_MAP.get(response.status_code)
    if exc_class is None:
        exc_class = ServerError if response.status_code >= 500 else MocoError

    if exc_class is RateLimitError:
        retry_after_raw = response.headers.get("Retry-After")
        retry_after: float | None = None
        if retry_after_raw is not None:
            try:
                retry_after = float(retry_after_raw)
            except ValueError:
                pass
        raise RateLimitError(
            message,
            retry_after=retry_after,
            status_code=response.status_code,
            body=body,
            response=response,
        )

    raise exc_class(
        message,
        status_code=response.status_code,
        body=body,
        response=response,
    )
