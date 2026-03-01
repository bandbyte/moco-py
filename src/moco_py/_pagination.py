"""Header-based pagination for the MOCO API."""

from __future__ import annotations

import re
from collections.abc import AsyncIterator, Iterator
from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, TypeVar

import httpx
from pydantic import TypeAdapter

if TYPE_CHECKING:
    from ._transport import AsyncTransport, SyncTransport

T = TypeVar("T")

_LINK_NEXT_RE = re.compile(r'<[^>]*[?&]page=(\d+)[^>]*>;\s*rel="next"')


def _parse_link_next(link: str | None) -> int | None:
    """Extract the next page number from a Link header with rel="next"."""
    if link is None:
        return None
    match = _LINK_NEXT_RE.search(link)
    if match is None:
        return None
    return int(match.group(1))


@dataclass(frozen=True)
class PageInfo:
    """Metadata from pagination response headers."""

    page: int
    per_page: int
    total: int


class SyncPage(Generic[T]):
    """A single page of results from a paginated MOCO API endpoint."""

    def __init__(
        self,
        *,
        items: list[T],
        http_response: httpx.Response,
        transport: SyncTransport,
        path: str,
        params: dict[str, object],
        cast_to: type[T],
    ) -> None:
        self.items = items
        self.http_response = http_response
        self._transport = transport
        self._path = path
        self._params = params
        self._cast_to = cast_to

        headers = http_response.headers
        self.page_info = PageInfo(
            page=int(headers.get("X-Page", "1")),
            per_page=int(headers.get("X-Per-Page", "100")),
            total=int(headers.get("X-Total", str(len(items)))),
        )
        self._next_page = _parse_link_next(headers.get("Link"))

    @property
    def has_next(self) -> bool:
        return self._next_page is not None

    def next_page(self) -> SyncPage[T]:
        """Fetch the next page of results."""
        if self._next_page is None:
            raise StopIteration("No more pages")
        params = {**self._params, "page": self._next_page}
        response = self._transport.request_raw("GET", self._path, params=params)
        adapter = TypeAdapter(list[self._cast_to])  # type: ignore[name-defined]
        items = adapter.validate_json(response.content)
        return SyncPage(
            items=items,
            http_response=response,
            transport=self._transport,
            path=self._path,
            params=self._params,
            cast_to=self._cast_to,
        )

    def __iter__(self) -> Iterator[T]:
        yield from self.items

    def auto_paging_iter(self) -> Iterator[T]:
        """Iterate over all items across all pages."""
        page: SyncPage[T] = self
        while True:
            yield from page.items
            if not page.has_next:
                break
            page = page.next_page()


class AsyncPage(Generic[T]):
    """A single page of results from a paginated MOCO API endpoint (async)."""

    def __init__(
        self,
        *,
        items: list[T],
        http_response: httpx.Response,
        transport: AsyncTransport,
        path: str,
        params: dict[str, object],
        cast_to: type[T],
    ) -> None:
        self.items = items
        self.http_response = http_response
        self._transport = transport
        self._path = path
        self._params = params
        self._cast_to = cast_to

        headers = http_response.headers
        self.page_info = PageInfo(
            page=int(headers.get("X-Page", "1")),
            per_page=int(headers.get("X-Per-Page", "100")),
            total=int(headers.get("X-Total", str(len(items)))),
        )
        self._next_page = _parse_link_next(headers.get("Link"))

    @property
    def has_next(self) -> bool:
        return self._next_page is not None

    async def next_page(self) -> AsyncPage[T]:
        if self._next_page is None:
            raise StopAsyncIteration("No more pages")
        params = {**self._params, "page": self._next_page}
        response = await self._transport.request_raw("GET", self._path, params=params)
        adapter = TypeAdapter(list[self._cast_to])  # type: ignore[name-defined]
        items = adapter.validate_json(response.content)
        return AsyncPage(
            items=items,
            http_response=response,
            transport=self._transport,
            path=self._path,
            params=self._params,
            cast_to=self._cast_to,
        )

    def __iter__(self) -> Iterator[T]:
        yield from self.items

    async def auto_paging_iter(self) -> AsyncIterator[T]:
        page: AsyncPage[T] = self
        while True:
            for item in page.items:
                yield item
            if not page.has_next:
                break
            page = await page.next_page()
