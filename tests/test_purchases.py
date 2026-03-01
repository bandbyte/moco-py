"""Tests for the Purchases resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.purchases import Purchases
from moco_py.types.purchases import Purchase

BASE = "https://test.mocoapp.com/api/v1"

PURCHASE_JSON = {
    "id": 987,
    "identifier": "E2016-0001",
    "receipt_identifier": "KK121",
    "title": "SBB Ticket",
    "info": None,
    "iban": "CH3908704016075473007",
    "reference": None,
    "date": "2020-02-28",
    "due_date": None,
    "service_period_from": "2020-02-28",
    "service_period_to": "2020-02-28",
    "status": "pending",
    "payment_method": "bank_transfer",
    "net_total": 44.88,
    "gross_total": 46.0,
    "currency": "CHF",
    "file_url": None,
    "custom_properties": {"Various": "some stuff"},
    "tags": ["Transportation"],
    "approval_status": "approved",
    "company": {
        "id": 5552,
        "name": "Schweizerische Bundesbahnen SBB",
        "iban": "CH3908704016075473007",
    },
    "payments": [],
    "user": {"id": 433109936, "firstname": "Mario", "name": "Rossi"},
    "refund_request": None,
    "credit_card_transaction": None,
    "items": [
        {
            "id": 311936153,
            "title": "SBB Ticket",
            "net_total": 44.88,
            "tax_total": 1.12,
            "tax": 2.5,
            "vat": {
                "tax": 2.5,
                "reverse_charge": False,
                "intra_eu": False,
                "active": True,
                "code": "9",
            },
            "tax_included": True,
            "gross_total": 46.0,
            "category": {
                "id": 671034328,
                "name": "Spesen und Reisekosten",
                "credit_account": "6640",
            },
            "supplier_credit_number": 70001,
            "expense": None,
            "receipt": None,
        }
    ],
    "created_at": "2018-10-17T09:33:46Z",
    "updated_at": "2018-10-17T09:33:46Z",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def purchases(client: Moco) -> Purchases:
    return Purchases(client._transport)


class TestPurchasesList:
    @respx.mock
    def test_list_purchases(self, purchases: Purchases) -> None:
        respx.get(f"{BASE}/purchases").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([PURCHASE_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = purchases.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Purchase)
        assert page.items[0].title == "SBB Ticket"

    @respx.mock
    def test_list_purchases_with_filters(self, purchases: Purchases) -> None:
        respx.get(f"{BASE}/purchases").mock(
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
        page = purchases.list(status="pending", payment_method="cash")
        assert len(page.items) == 0


class TestPurchasesGet:
    @respx.mock
    def test_get_purchase(self, purchases: Purchases) -> None:
        respx.get(f"{BASE}/purchases/987").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PURCHASE_JSON).encode()
            )
        )
        resp = purchases.get(987)
        assert resp.parsed.id == 987
        assert resp.parsed.currency == "CHF"


class TestPurchasesCreate:
    @respx.mock
    def test_create_purchase(self, purchases: Purchases) -> None:
        respx.post(f"{BASE}/purchases").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PURCHASE_JSON).encode()
            )
        )
        resp = purchases.create(
            date="2020-02-28",
            currency="CHF",
            payment_method="bank_transfer",
            items=[{"title": "SBB Ticket", "total": 46.0, "tax": 2.5, "tax_included": True}],
        )
        assert resp.parsed.id == 987


class TestPurchasesUpdate:
    @respx.mock
    def test_update_purchase(self, purchases: Purchases) -> None:
        updated = {**PURCHASE_JSON, "status": "archived"}
        respx.put(f"{BASE}/purchases/987").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = purchases.update(987, status="archived")
        assert resp.parsed.status == "archived"


class TestPurchasesUpdateStatus:
    @respx.mock
    def test_update_status(self, purchases: Purchases) -> None:
        updated = {**PURCHASE_JSON, "status": "archived"}
        respx.patch(f"{BASE}/purchases/987/update_status").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = purchases.update_status(987, status="archived")
        assert resp.parsed.status == "archived"


class TestPurchasesDelete:
    @respx.mock
    def test_delete_purchase(self, purchases: Purchases) -> None:
        respx.delete(f"{BASE}/purchases/987").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = purchases.delete(987)
        assert resp.parsed is None


class TestPurchasesAssignToProject:
    @respx.mock
    def test_assign_to_project(self, purchases: Purchases) -> None:
        respx.post(f"{BASE}/purchases/987/assign_to_project").mock(
            return_value=httpx.Response(
                200, content=json.dumps(PURCHASE_JSON).encode()
            )
        )
        resp = purchases.assign_to_project(
            987, item_id=311936153, project_id=23345545
        )
        assert resp.parsed.id == 987
