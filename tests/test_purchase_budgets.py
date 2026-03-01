"""Tests for the Purchase Budgets resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.purchase_budgets import PurchaseBudgets
from moco_py.types.purchase_budgets import PurchaseBudget

BASE = "https://test.mocoapp.com/api/v1"

BUDGET_JSON = {
    "id": "2",
    "year": 2024,
    "title": "Betrieb – Hosting",
    "active": True,
    "target": 84000,
    "exhaused": 66483,
    "planned": 4494,
    "remaining": 13023,
}

PAGINATION_HEADERS = {
    "X-Page": "1",
    "X-Per-Page": "100",
    "X-Total": "1",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def budgets(client: Moco) -> PurchaseBudgets:
    return PurchaseBudgets(client._transport)


class TestPurchaseBudgetsList:
    @respx.mock
    def test_list_budgets(self, budgets: PurchaseBudgets) -> None:
        respx.get(f"{BASE}/purchases/budgets").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([BUDGET_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = budgets.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], PurchaseBudget)
        assert page.items[0].title == "Betrieb – Hosting"

    @respx.mock
    def test_list_budgets_with_year(self, budgets: PurchaseBudgets) -> None:
        route = respx.get(f"{BASE}/purchases/budgets").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([BUDGET_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = budgets.list(year=2024)
        assert len(page.items) == 1
        assert "year" in str(route.calls[0].request.url)
