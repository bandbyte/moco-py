"""Tests for the Receipts resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from moco_py import Moco
from moco_py.resources.receipts import Receipts
from moco_py.types.receipts import Receipt

BASE = "https://test.mocoapp.com/api/v1"

RECEIPT_JSON = {
    "id": 123,
    "title": "Team-Lunch",
    "date": "2021-12-13",
    "billable": False,
    "pending": False,
    "gross_total": 56.5,
    "currency": "CHF",
    "items": [
        {
            "gross_total": 56.5,
            "vat": {
                "id": 186,
                "tax": 7.7,
                "reverse_charge": False,
                "intra_eu": False,
            },
            "purchase_category": {
                "id": 2684,
                "name": "Bewirtungsaufwände",
            },
        }
    ],
    "project": {
        "id": 567,
        "name": "Intern/Admin",
        "billable": False,
        "company": {"id": 789, "name": "Acme Inc."},
    },
    "refund_request": {"id": 266, "status": "paid"},
    "info": "Teamlunch mit Peter, Sandra und Till",
    "user": {"id": 933, "firstname": "Sabine", "lastname": "Schäuble"},
    "attachment_url": "/system/documents/account/123/document/123/d8fef77df35c5753.pdf",
}


@pytest.fixture()
def client() -> Moco:
    return Moco(api_key="test-key", base_url=BASE)


@pytest.fixture()
def receipts(client: Moco) -> Receipts:
    return Receipts(client._transport)


class TestReceiptsList:
    @respx.mock
    def test_list_receipts(self, receipts: Receipts) -> None:
        respx.get(f"{BASE}/receipts").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps([RECEIPT_JSON]).encode(),
                headers={
                    "X-Page": "1",
                    "X-Per-Page": "100",
                    "X-Total": "1",
                },
            )
        )
        page = receipts.list()
        assert len(page.items) == 1
        assert isinstance(page.items[0], Receipt)
        assert page.items[0].title == "Team-Lunch"
        assert page.items[0].gross_total == 56.5

    @respx.mock
    def test_list_receipts_with_filters(self, receipts: Receipts) -> None:
        respx.get(f"{BASE}/receipts").mock(
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
        page = receipts.list(
            from_date="2021-12-01", to_date="2021-12-31"
        )
        assert len(page.items) == 0


class TestReceiptsGet:
    @respx.mock
    def test_get_receipt(self, receipts: Receipts) -> None:
        respx.get(f"{BASE}/receipts/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(RECEIPT_JSON).encode()
            )
        )
        resp = receipts.get(123)
        assert resp.parsed.id == 123
        assert resp.parsed.items is not None
        assert resp.parsed.items[0].gross_total == 56.5


class TestReceiptsCreate:
    @respx.mock
    def test_create_receipt(self, receipts: Receipts) -> None:
        respx.post(f"{BASE}/receipts").mock(
            return_value=httpx.Response(
                200, content=json.dumps(RECEIPT_JSON).encode()
            )
        )
        resp = receipts.create(
            date="2021-12-13",
            title="Team-Lunch",
            currency="CHF",
            items=[{"vat_code_id": 186, "gross_total": 56.5}],
        )
        assert resp.parsed.title == "Team-Lunch"


class TestReceiptsUpdate:
    @respx.mock
    def test_update_receipt(self, receipts: Receipts) -> None:
        updated = {**RECEIPT_JSON, "title": "Lunch with customer"}
        respx.patch(f"{BASE}/receipts/123").mock(
            return_value=httpx.Response(
                200, content=json.dumps(updated).encode()
            )
        )
        resp = receipts.update(123, title="Lunch with customer")
        assert resp.parsed.title == "Lunch with customer"


class TestReceiptsDelete:
    @respx.mock
    def test_delete_receipt(self, receipts: Receipts) -> None:
        respx.delete(f"{BASE}/receipts/123").mock(
            return_value=httpx.Response(200, content=b"")
        )
        resp = receipts.delete(123)
        assert resp.parsed is None
