"""Internal HTTP transport with auth, retries, and error handling."""

from __future__ import annotations

import random
import time
from typing import Any, TypeVar, overload

import httpx
from pydantic import TypeAdapter

from ._constants import RETRY_STATUS_CODES
from ._response import MocoResponse
from .exceptions import (
    APIConnectionError,
    APITimeoutError,
    _raise_for_status,
)

T = TypeVar("T")

_INITIAL_RETRY_DELAY = 0.5


def _parse_response(
    cast_to: type[T],
    response: httpx.Response,
    *,
    is_list: bool,
) -> MocoResponse[Any]:
    """Parse an httpx.Response into a MocoResponse with Pydantic."""
    if is_list:
        adapter = TypeAdapter(list[cast_to])  # type: ignore[valid-type]
        parsed = adapter.validate_json(response.content)
    else:
        parsed = cast_to.model_validate_json(response.content)  # type: ignore[attr-defined]
    return MocoResponse(parsed=parsed, http_response=response)


class SyncTransport:
    """Synchronous HTTP transport for the MOCO API."""

    def __init__(
        self,
        *,
        base_url: str,
        api_key: str,
        timeout: float,
        max_retries: int,
        default_headers: dict[str, str] | None = None,
        http_client: httpx.Client | None = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._max_retries = max_retries
        self._owns_client = http_client is None

        headers = {
            "Authorization": f"Token token={api_key}",
            "Content-Type": "application/json",
            **(default_headers or {}),
        }

        self._default_headers: dict[str, str]
        if http_client is not None:
            self._client = http_client
            self._default_headers = headers
        else:
            self._client = httpx.Client(
                timeout=timeout,
                headers=headers,
            )
            self._default_headers = {}

    @overload
    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = ...,
        json_data: Any | None = ...,
        cast_to: type[T],
        is_list: bool = ...,
    ) -> MocoResponse[T]: ...

    @overload
    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = ...,
        json_data: Any | None = ...,
        cast_to: None = ...,
        is_list: bool = ...,
    ) -> MocoResponse[None]: ...

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_data: Any | None = None,
        cast_to: type[T] | None = None,
        is_list: bool = False,
    ) -> MocoResponse[Any]:
        url = f"{self._base_url}/{path.lstrip('/')}"
        hdrs = self._default_headers or None

        last_exc: Exception | None = None
        for attempt in range(self._max_retries + 1):
            try:
                response = self._client.request(
                    method,
                    url,
                    params=params,
                    json=json_data,
                    headers=hdrs,
                )
            except httpx.TimeoutException as exc:
                last_exc = exc
                if attempt < self._max_retries:
                    self._sleep_for_retry(attempt)
                    continue
                raise APITimeoutError(f"Request timed out: {exc}") from exc
            except httpx.TransportError as exc:
                last_exc = exc
                if attempt < self._max_retries:
                    self._sleep_for_retry(attempt)
                    continue
                raise APIConnectionError(f"Connection error: {exc}") from exc

            if (
                response.status_code in RETRY_STATUS_CODES
                and attempt < self._max_retries
            ):
                delay = self._retry_delay(attempt, response)
                time.sleep(delay)
                last_exc = None
                continue

            _raise_for_status(response)

            if cast_to is None:
                return MocoResponse(parsed=None, http_response=response)

            return _parse_response(cast_to, response, is_list=is_list)

        if last_exc is not None:
            if isinstance(last_exc, httpx.TimeoutException):
                raise APITimeoutError(f"Request timed out: {last_exc}") from last_exc
            raise APIConnectionError(f"Connection error: {last_exc}") from last_exc
        raise APIConnectionError("Request failed after retries")

    def request_raw(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_data: Any | None = None,
    ) -> httpx.Response:
        """Make a request returning raw httpx.Response."""
        url = f"{self._base_url}/{path.lstrip('/')}"
        hdrs = self._default_headers or None

        last_exc: Exception | None = None
        for attempt in range(self._max_retries + 1):
            try:
                response = self._client.request(
                    method,
                    url,
                    params=params,
                    json=json_data,
                    headers=hdrs,
                )
            except httpx.TimeoutException as exc:
                last_exc = exc
                if attempt < self._max_retries:
                    self._sleep_for_retry(attempt)
                    continue
                raise APITimeoutError(f"Request timed out: {exc}") from exc
            except httpx.TransportError as exc:
                last_exc = exc
                if attempt < self._max_retries:
                    self._sleep_for_retry(attempt)
                    continue
                raise APIConnectionError(f"Connection error: {exc}") from exc

            if (
                response.status_code in RETRY_STATUS_CODES
                and attempt < self._max_retries
            ):
                delay = self._retry_delay(attempt, response)
                time.sleep(delay)
                continue

            _raise_for_status(response)
            return response

        if last_exc is not None:
            if isinstance(last_exc, httpx.TimeoutException):
                raise APITimeoutError(f"Request timed out: {last_exc}") from last_exc
            raise APIConnectionError(f"Connection error: {last_exc}") from last_exc
        raise APIConnectionError("Request failed after retries")

    def _retry_delay(
        self,
        attempt: int,
        response: httpx.Response | None = None,
    ) -> float:
        if response is not None and response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            if retry_after is not None:
                try:
                    return float(retry_after)
                except ValueError:
                    pass
        return float(_compute_backoff(attempt))

    def _sleep_for_retry(self, attempt: int) -> None:
        time.sleep(_compute_backoff(attempt))

    def close(self) -> None:
        if self._owns_client:
            self._client.close()


class AsyncTransport:
    """Asynchronous HTTP transport for the MOCO API."""

    def __init__(
        self,
        *,
        base_url: str,
        api_key: str,
        timeout: float,
        max_retries: int,
        default_headers: dict[str, str] | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._max_retries = max_retries
        self._owns_client = http_client is None

        headers = {
            "Authorization": f"Token token={api_key}",
            "Content-Type": "application/json",
            **(default_headers or {}),
        }

        self._default_headers: dict[str, str]
        if http_client is not None:
            self._client = http_client
            self._default_headers = headers
        else:
            self._client = httpx.AsyncClient(
                timeout=timeout,
                headers=headers,
            )
            self._default_headers = {}

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_data: Any | None = None,
        cast_to: type[T] | None = None,
        is_list: bool = False,
    ) -> MocoResponse[Any]:
        import asyncio

        url = f"{self._base_url}/{path.lstrip('/')}"
        hdrs = self._default_headers or None

        last_exc: Exception | None = None
        for attempt in range(self._max_retries + 1):
            try:
                response = await self._client.request(
                    method,
                    url,
                    params=params,
                    json=json_data,
                    headers=hdrs,
                )
            except httpx.TimeoutException as exc:
                last_exc = exc
                if attempt < self._max_retries:
                    await asyncio.sleep(_compute_backoff(attempt))
                    continue
                raise APITimeoutError(f"Request timed out: {exc}") from exc
            except httpx.TransportError as exc:
                last_exc = exc
                if attempt < self._max_retries:
                    await asyncio.sleep(_compute_backoff(attempt))
                    continue
                raise APIConnectionError(f"Connection error: {exc}") from exc

            if (
                response.status_code in RETRY_STATUS_CODES
                and attempt < self._max_retries
            ):
                delay = self._retry_delay(attempt, response)
                await asyncio.sleep(delay)
                continue

            _raise_for_status(response)

            if cast_to is None:
                return MocoResponse(parsed=None, http_response=response)

            return _parse_response(cast_to, response, is_list=is_list)

        if last_exc is not None:
            if isinstance(last_exc, httpx.TimeoutException):
                raise APITimeoutError(f"Request timed out: {last_exc}") from last_exc
            raise APIConnectionError(f"Connection error: {last_exc}") from last_exc
        raise APIConnectionError("Request failed after retries")

    async def request_raw(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_data: Any | None = None,
    ) -> httpx.Response:
        import asyncio

        url = f"{self._base_url}/{path.lstrip('/')}"
        hdrs = self._default_headers or None

        last_exc: Exception | None = None
        for attempt in range(self._max_retries + 1):
            try:
                response = await self._client.request(
                    method,
                    url,
                    params=params,
                    json=json_data,
                    headers=hdrs,
                )
            except httpx.TimeoutException as exc:
                last_exc = exc
                if attempt < self._max_retries:
                    await asyncio.sleep(_compute_backoff(attempt))
                    continue
                raise APITimeoutError(f"Request timed out: {exc}") from exc
            except httpx.TransportError as exc:
                last_exc = exc
                if attempt < self._max_retries:
                    await asyncio.sleep(_compute_backoff(attempt))
                    continue
                raise APIConnectionError(f"Connection error: {exc}") from exc

            if (
                response.status_code in RETRY_STATUS_CODES
                and attempt < self._max_retries
            ):
                delay = self._retry_delay(attempt, response)
                await asyncio.sleep(delay)
                continue

            _raise_for_status(response)
            return response

        if last_exc is not None:
            if isinstance(last_exc, httpx.TimeoutException):
                raise APITimeoutError(f"Request timed out: {last_exc}") from last_exc
            raise APIConnectionError(f"Connection error: {last_exc}") from last_exc
        raise APIConnectionError("Request failed after retries")

    def _retry_delay(
        self,
        attempt: int,
        response: httpx.Response | None = None,
    ) -> float:
        if response is not None and response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            if retry_after is not None:
                try:
                    return float(retry_after)
                except ValueError:
                    pass
        return float(_compute_backoff(attempt))

    async def close(self) -> None:
        if self._owns_client:
            await self._client.aclose()


def _compute_backoff(attempt: int) -> float:
    """Compute retry delay with exponential backoff and jitter."""
    delay: float = _INITIAL_RETRY_DELAY * (2**attempt)
    jitter: float = delay * 0.25 * (2 * random.random() - 1)
    return delay + jitter
