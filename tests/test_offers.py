"""Tests for the Offers resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.offers import Offers
from moco_py.types.offers import Offer

BASE = "https://test.mocoapp.com/api/v1"

OFFER_JSON = {
    "id": 273,
    "identifier": "A1704-042",
    "invoice_id": 1873491,
    "date": "2017-04-12",
    "due_date": "2017-04-26",
    "title": "Offer - User Management",
    "recipient_address": "Beispiel GmbH\nPeter Muster\nBeispielstrasse 123\n12345 Berlin",
    "currency": "EUR",
    "net_total": 12750,
    "tax": 19,
    "gross_total": 15172.5,
    "discount": 10,
    "status": "created",
    "tags": ["Print", "Digital"],
    "company": {"id": 1234, "name": "Acme Corp."},
    "project": {"id": 1234, "identifier": "P123", "name": "A Project"},
    "deal": {"id": 1234, "name": "A Lead"},
    "user": {"id": 1234, "firstname": "Jane", "lastname": "Doe"},
    "items": [
        {
            "id": 29,
            "type": "item",
            "title": "Project Setup",
            "description": None,
            "quantity": 1,
            "unit": "d",
            "unit_price": 1500,
            "unit_cost": 1200,
            "net_total": 1500,
            "optional": False,
            "service_type": "service",
        }
    ],
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
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
def offers(client: Moco) -> Offers:
    return Offers(client._transport)


class TestOffersList:
    @respx.mock
    def test_list_offers(self, offers: Offers) -> None:
        respx.get(f"{BASE}/offers").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([OFFER_JSON]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        page = offers.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Offer)
        assert page.items[0].identifier == "A1704-042"

    @respx.mock
    def test_list_offers_with_filters(self, offers: Offers) -> None:
        route = respx.get(f"{BASE}/offers").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([]).encode(),
                headers=PAGINATION_HEADERS,
            )
        )
        offers.list(status="created", company_id="1234")
        assert route.called


class TestOffersGet:
    @respx.mock
    def test_get_offer(self, offers: Offers) -> None:
        respx.get(f"{BASE}/offers/273").mock(
            return_value=httpx.Response(
                200, content=json.dumps(OFFER_JSON).encode()
            )
        )
        resp = offers.get(273)
        assert resp.parsed.id == 273
        assert resp.parsed.title == "Offer - User Management"
        assert resp.parsed.company is not None
        assert resp.parsed.company.name == "Acme Corp."


class TestOffersCreate:
    @respx.mock
    def test_create_offer(self, offers: Offers) -> None:
        respx.post(f"{BASE}/offers").mock(
            return_value=httpx.Response(
                200, content=json.dumps(OFFER_JSON).encode()
            )
        )
        resp = offers.create(
            recipient_address="Beispiel GmbH",
            date="2017-04-12",
            due_date="2017-04-26",
            title="Offer - User Management",
            tax=19.0,
            items=[{"type": "item", "title": "Setup", "quantity": 1, "unit": "d", "unit_price": 1500}],
            company_id=1234,
        )
        assert resp.parsed.id == 273


class TestOffersAssign:
    @respx.mock
    def test_assign_offer(self, offers: Offers) -> None:
        respx.put(f"{BASE}/offers/273/assign").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = offers.assign(273, company_id=1234, project_id=2345)
        assert resp.parsed is None


class TestOffersUpdateStatus:
    @respx.mock
    def test_update_status(self, offers: Offers) -> None:
        respx.put(f"{BASE}/offers/273/update_status").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = offers.update_status(273, status="sent")
        assert resp.parsed is None


class TestOffersSendEmail:
    @respx.mock
    def test_send_email(self, offers: Offers) -> None:
        respx.post(f"{BASE}/offers/273/send_email").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = offers.send_email(
            273, subject="Offer", text="Kind regards"
        )
        assert resp.parsed is None
