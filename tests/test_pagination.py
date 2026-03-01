"""Tests for pagination."""

from __future__ import annotations

import httpx
import pytest
import respx
from pydantic import BaseModel

from moco_py._pagination import SyncPage, _parse_link_next
from moco_py._transport import SyncTransport

BASE_URL = "https://test.mocoapp.com/api/v1"


class Item(BaseModel):
    id: int
    name: str


def _make_transport(max_retries: int = 0) -> SyncTransport:
    return SyncTransport(
        base_url=BASE_URL,
        api_key="test-key",
        timeout=5.0,
        max_retries=max_retries,
    )


class TestParseLinkNext:
    def test_with_next(self) -> None:
        link = '<https://test.mocoapp.com/api/v1/things.json?page=3>; rel="next"'
        assert _parse_link_next(link) == 3

    def test_without_next(self) -> None:
        link = '<https://test.mocoapp.com/api/v1/things.json?page=2>; rel="prev"'
        assert _parse_link_next(link) is None

    def test_none(self) -> None:
        assert _parse_link_next(None) is None

    def test_multiple_links(self) -> None:
        link = (
            '<https://test.mocoapp.com/api/v1/things.json?page=1>; rel="prev", '
            '<https://test.mocoapp.com/api/v1/things.json?page=3>; rel="next"'
        )
        assert _parse_link_next(link) == 3


class TestSyncPage:
    def _make_page(
        self,
        items: list[Item],
        headers: dict[str, str],
        transport: SyncTransport | None = None,
    ) -> SyncPage[Item]:
        resp = httpx.Response(
            200,
            json=[i.model_dump() for i in items],
            headers=headers,
            request=httpx.Request("GET", f"{BASE_URL}/things"),
        )
        return SyncPage(
            items=items,
            http_response=resp,
            transport=transport or _make_transport(),
            path="/things",
            params={},
            cast_to=Item,
        )

    def test_page_info(self) -> None:
        page = self._make_page(
            [Item(id=1, name="A")],
            {"X-Page": "2", "X-Per-Page": "50", "X-Total": "120"},
        )
        assert page.page_info.page == 2
        assert page.page_info.per_page == 50
        assert page.page_info.total == 120

    def test_has_next_true(self) -> None:
        page = self._make_page(
            [Item(id=1, name="A")],
            {
                "X-Page": "1",
                "X-Per-Page": "1",
                "X-Total": "2",
                "Link": '<https://test.mocoapp.com/api/v1/things.json?page=2>; rel="next"',
            },
        )
        assert page.has_next is True

    def test_has_next_false(self) -> None:
        page = self._make_page(
            [Item(id=1, name="A")],
            {"X-Page": "1", "X-Per-Page": "100", "X-Total": "1"},
        )
        assert page.has_next is False

    def test_iter_current_page(self) -> None:
        items = [Item(id=1, name="A"), Item(id=2, name="B")]
        page = self._make_page(
            items,
            {"X-Page": "1", "X-Per-Page": "100", "X-Total": "2"},
        )
        assert list(page) == items

    @respx.mock
    def test_auto_paging_iter(self) -> None:
        transport = _make_transport()

        # Page 2 response
        respx.get(f"{BASE_URL}/things", params={"page": 2}).mock(
            return_value=httpx.Response(
                200,
                json=[{"id": 3, "name": "C"}],
                headers={"X-Page": "2", "X-Per-Page": "2", "X-Total": "3"},
            )
        )

        # Build page 1 manually
        page1 = self._make_page(
            [Item(id=1, name="A"), Item(id=2, name="B")],
            {
                "X-Page": "1",
                "X-Per-Page": "2",
                "X-Total": "3",
                "Link": f'<{BASE_URL}/things.json?page=2>; rel="next"',
            },
            transport=transport,
        )

        all_items = list(page1.auto_paging_iter())
        assert len(all_items) == 3
        assert all_items[0].id == 1
        assert all_items[2].id == 3

    def test_next_page_raises_when_no_next(self) -> None:
        page = self._make_page(
            [Item(id=1, name="A")],
            {"X-Page": "1", "X-Per-Page": "100", "X-Total": "1"},
        )
        with pytest.raises(StopIteration):
            page.next_page()
