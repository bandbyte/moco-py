"""Response wrapper providing typed access alongside raw httpx.Response."""

from __future__ import annotations

from typing import Generic, TypeVar

import httpx

T = TypeVar("T")


class MocoResponse(Generic[T]):
    """Wraps a parsed Pydantic model with access to the raw HTTP response."""

    __slots__ = ("parsed", "http_response")

    def __init__(self, *, parsed: T, http_response: httpx.Response) -> None:
        self.parsed = parsed
        self.http_response = http_response

    @property
    def status_code(self) -> int:
        return self.http_response.status_code

    @property
    def headers(self) -> httpx.Headers:
        return self.http_response.headers
