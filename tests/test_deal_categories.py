"""Tests for the Deal Categories resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.types.deal_categories import DealCategory

BASE = "https://test.mocoapp.com/api/v1"

DEAL_CATEGORY_JSON = {
    "id": 123,
    "name": "Contact",
    "probability": 1,
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


class TestDealCategoriesList:
    @respx.mock
    def test_list_deal_categories(self, client: Moco) -> None:
        respx.get(f"{BASE}/deal_categories").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([DEAL_CATEGORY_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = client.deal_categories.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], DealCategory)
        assert page.items[0].name == "Contact"
        assert page.items[0].probability == 1


class TestDealCategoriesGet:
    @respx.mock
    def test_get_deal_category(self, client: Moco) -> None:
        respx.get(f"{BASE}/deal_categories/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(DEAL_CATEGORY_JSON).encode()
            )
        )
        resp = client.deal_categories.get(123)
        assert resp.parsed.id == 123
        assert resp.parsed.name == "Contact"


class TestDealCategoriesCreate:
    @respx.mock
    def test_create_deal_category(self, client: Moco) -> None:
        respx.post(f"{BASE}/deal_categories").mock(
            return_value=httpx.Response(
                200, content=json.dumps(DEAL_CATEGORY_JSON).encode()
            )
        )
        resp = client.deal_categories.create(name="Contact", probability=1)
        assert resp.parsed.name == "Contact"
        assert resp.parsed.probability == 1


class TestDealCategoriesUpdate:
    @respx.mock
    def test_update_deal_category(self, client: Moco) -> None:
        updated = {**DEAL_CATEGORY_JSON, "name": "Qualified"}
        respx.put(f"{BASE}/deal_categories/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = client.deal_categories.update(123, name="Qualified")
        assert resp.parsed.name == "Qualified"


class TestDealCategoriesDelete:
    @respx.mock
    def test_delete_deal_category(self, client: Moco) -> None:
        respx.delete(f"{BASE}/deal_categories/123").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = client.deal_categories.delete(123)
        assert resp.parsed is None
