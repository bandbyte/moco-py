"""Base resource classes for sync and async API access."""

from __future__ import annotations

from typing import Any, TypeVar

from pydantic import TypeAdapter

from ._pagination import AsyncPage, SyncPage
from ._response import MocoResponse
from ._transport import AsyncTransport, SyncTransport

T = TypeVar("T")


class SyncResource:
    """Base class for synchronous API resource namespaces."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def _get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        cast_to: type[T],
    ) -> MocoResponse[T]:
        return self._transport.request("GET", path, params=params, cast_to=cast_to)

    def _get_list(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        cast_to: type[T],
    ) -> SyncPage[T]:
        response = self._transport.request_raw("GET", path, params=params)
        adapter = TypeAdapter(list[cast_to])  # type: ignore[valid-type]
        items = adapter.validate_json(response.content)
        return SyncPage(
            items=items,
            http_response=response,
            transport=self._transport,
            path=path,
            params=params or {},
            cast_to=cast_to,
        )

    def _post(
        self,
        path: str,
        *,
        json_data: Any = None,
        cast_to: type[T],
    ) -> MocoResponse[T]:
        return self._transport.request(
            "POST", path, json_data=json_data, cast_to=cast_to
        )

    def _put(
        self,
        path: str,
        *,
        json_data: Any = None,
        cast_to: type[T],
    ) -> MocoResponse[T]:
        return self._transport.request(
            "PUT", path, json_data=json_data, cast_to=cast_to
        )

    def _patch(
        self,
        path: str,
        *,
        json_data: Any = None,
        cast_to: type[T],
    ) -> MocoResponse[T]:
        return self._transport.request(
            "PATCH", path, json_data=json_data, cast_to=cast_to
        )

    def _delete(self, path: str) -> MocoResponse[None]:
        return self._transport.request("DELETE", path, cast_to=None)


class AsyncResource:
    """Base class for asynchronous API resource namespaces."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def _get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        cast_to: type[T],
    ) -> MocoResponse[Any]:
        return await self._transport.request(
            "GET", path, params=params, cast_to=cast_to
        )

    async def _get_list(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        cast_to: type[T],
    ) -> AsyncPage[T]:
        response = await self._transport.request_raw("GET", path, params=params)
        adapter = TypeAdapter(list[cast_to])  # type: ignore[valid-type]
        items = adapter.validate_json(response.content)
        return AsyncPage(
            items=items,
            http_response=response,
            transport=self._transport,
            path=path,
            params=params or {},
            cast_to=cast_to,
        )

    async def _post(
        self,
        path: str,
        *,
        json_data: Any = None,
        cast_to: type[T],
    ) -> MocoResponse[Any]:
        return await self._transport.request(
            "POST", path, json_data=json_data, cast_to=cast_to
        )

    async def _put(
        self,
        path: str,
        *,
        json_data: Any = None,
        cast_to: type[T],
    ) -> MocoResponse[Any]:
        return await self._transport.request(
            "PUT", path, json_data=json_data, cast_to=cast_to
        )

    async def _patch(
        self,
        path: str,
        *,
        json_data: Any = None,
        cast_to: type[T],
    ) -> MocoResponse[Any]:
        return await self._transport.request(
            "PATCH", path, json_data=json_data, cast_to=cast_to
        )

    async def _delete(self, path: str) -> MocoResponse[Any]:
        return await self._transport.request("DELETE", path, cast_to=None)
