"""Tests for the Purchase Categories resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.purchase_categories import PurchaseCategories
from moco_py.types.purchase_categories import PurchaseCategory

BASE = "https://test.mocoapp.com/api/v1"

CATEGORY_JSON = {
    "id": 123,
    "name": "Travel expenses",
    "credit_account": "6640",
    "active": True,
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def purchase_categories(client: Moco) -> PurchaseCategories:
    return PurchaseCategories(client._transport)


class TestPurchaseCategoriesList:
    @respx.mock
    def test_list_categories(self, purchase_categories: PurchaseCategories) -> None:
        respx.get(f"{BASE}/purchases/categories").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([CATEGORY_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = purchase_categories.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], PurchaseCategory)
        assert page.items[0].name == "Travel expenses"


class TestPurchaseCategoriesGet:
    @respx.mock
    def test_get_category(self, purchase_categories: PurchaseCategories) -> None:
        respx.get(f"{BASE}/purchases/categories/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(CATEGORY_JSON).encode()
            )
        )
        resp = purchase_categories.get(123)
        assert resp.parsed.id == 123
        assert resp.parsed.active is True
