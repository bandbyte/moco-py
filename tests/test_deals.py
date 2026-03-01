"""Tests for the Deals (Leads) resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.deals import Deals
from moco_py.types.deals import Deal

BASE = "https://test.mocoapp.com/api/v1"

DEAL_JSON = {
    "id": 123,
    "name": "Website V2",
    "status": "pending",
    "reminder_date": "2022-09-19",
    "closed_on": None,
    "money": 61000.0,
    "currency": "CHF",
    "info": "Interesting Lead!",
    "custom_properties": {"Type": "Website"},
    "user": {
        "id": 933593033,
        "firstname": "Nicola",
        "lastname": "Piccinini",
    },
    "company": {
        "id": 760260535,
        "name": "Beispiel AG",
        "type": "customer",
    },
    "person": {"id": 123311, "name": "Max Muster"},
    "category": {"id": 12, "name": "Angebot", "probability": 30},
    "service_period_from": "2022-09-01",
    "service_period_to": "2023-01-31",
    "inbox_email_address": "lead-website-v2-jh72nuqrkfcndwkj@inbox.mocoapp.com",
    "created_at": "2021-10-17T09:33:46Z",
    "updated_at": "2012-10-17T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def deals(client: Moco) -> Deals:
    return Deals(client._transport)


class TestDealsList:
    @respx.mock
    def test_list_deals(self, deals: Deals) -> None:
        respx.get(f"{BASE}/deals").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([DEAL_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = deals.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Deal)
        assert page.items[0].name == "Website V2"
        assert page.items[0].money == 61000.0

    @respx.mock
    def test_list_deals_with_filters(self, deals: Deals) -> None:
        respx.get(f"{BASE}/deals").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "0",
                },
            )
        )
        page = deals.list(status="won", company_id=123)
        assert len(page.items) == 0


class TestDealsGet:
    @respx.mock
    def test_get_deal(self, deals: Deals) -> None:
        respx.get(f"{BASE}/deals/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(DEAL_JSON).encode()
            )
        )
        resp = deals.get(123)
        assert resp.parsed.id == 123
        assert resp.parsed.status == "pending"


class TestDealsCreate:
    @respx.mock
    def test_create_deal(self, deals: Deals) -> None:
        respx.post(f"{BASE}/deals").mock(
            return_value=httpx.Response(
                200, content=json.dumps(DEAL_JSON).encode()
            )
        )
        resp = deals.create(
            name="Website V2",
            currency="CHF",
            money=61000.0,
            reminder_date="2022-09-19",
            user_id=933593033,
            deal_category_id=12,
        )
        assert resp.parsed.name == "Website V2"


class TestDealsUpdate:
    @respx.mock
    def test_update_deal(self, deals: Deals) -> None:
        updated = {**DEAL_JSON, "status": "lost"}
        respx.put(f"{BASE}/deals/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = deals.update(123, status="lost")
        assert resp.parsed.status == "lost"


class TestDealsDelete:
    @respx.mock
    def test_delete_deal(self, deals: Deals) -> None:
        respx.delete(f"{BASE}/deals/123").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = deals.delete(123)
        assert resp.parsed is None
